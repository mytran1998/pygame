import pygame
from ship import Ship
from bullet import Bullet
from alien import Alien
from explosions import Explosion
from game import Game
from ship_mini import ShipMini
from power import Power
import random
from os import path
import sys
from pygame.locals import *


BLACK = (0, 0, 0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

bg_start_image = pygame.image.load("images/background-start.png")
bg_end_image = pygame.image.load("images/background-end.png")
music_dir = path.join(path.dirname(__file__), 'music')
font_name = pygame.font.match_font('arial')
#Music
pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)
shoot_sound = pygame.mixer.Sound(path.join(music_dir, 'pew.wav'))
coll_sound = []
for s in ['expl1.wav', 'expl2.wav']:
	coll_sound.append(pygame.mixer.Sound(path.join(music_dir, s)))

LV_1 = 50
LV_2 = 100 

def event_keydown(event, game ,ship, screen, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    # Move the ship to the left by activating 'direction' flag
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
    	create_bullet(screen, game, ship, bullets)

def event_keyup(event, ship):
    # Stop the ship by activating 'direction' flag
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    # Stop the ship by activating 'direction' flag
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def create_bullet(screen, game, ship, bullets):
	# Tạo mới viên đạn và thêm vào group bullets 
    bullet = Bullet(screen, ship, 0)
    if game.score >= LV_1 and game.score <= LV_2:
        bullet = Bullet(screen, ship, 1)
    elif game.score > LV_2:
        bullet = Bullet(screen, ship, 2)
    bullets.add(bullet)
    shoot_sound.play()

def update_and_delete_bullet(game, bullets):
	bullets.update(game)
	# Xóa đạn nếu qua khỏi viền top
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def draw_bullet(bullets):
    for bullet in bullets:
        bullet.draw_bullet() 

def create_alien(screen, aliens, n):
	# Tạo mới n bullet
	for i in range(n):
		alien = Alien(screen)
		aliens.add(alien)

def draw_aline(aliens):
	# Vẽ alien
	for alien in aliens:
		alien.blitme()

def draw_expl(explosions):
	for expl in explosions:
		expl.blitme()
		explosions.remove(expl)

def draw_power(powers):
	for pow in powers:
		pow.blitme()

# Kiểm tra va chạm giữa alien và bullet
def check_coll_bullet_alien(game, aliens, bullets, screen, explosions, powers):
    collisions = pygame.sprite.groupcollide(aliens, bullets, True, True)
    for collision in collisions:
        # Tăng điểm
        game.score += 1
		# Mỗi lần bắn trúng thì tạo thêm 1 alien
        create_alien(screen, aliens, 1)
		# Hiệu ứng nổ
        expl = Explosion(collision.rect.center, screen, random.randint(0,2))
        explosions.add(expl)
		# Power
        if random.random() > 0.9:
            pow = Power(collision.rect.center, screen)
            powers.add(pow)
		# Nhạc
        else:
            random.choice(coll_sound).play()

# Kiểm tra va chạm giữa alien và ship
def check_coll_alien_ship(ship, aliens, screen, explosions):
	colls = pygame.sprite.spritecollide(ship, aliens, True)
	for coll in colls:
		ship.shield -= 20
		create_alien(screen, aliens, 1)
		expl = Explosion(coll.rect.center, screen, 0)
		explosions.add(expl)
		coll_sound[1].play()
		if ship.shield <= 0:
			ship.hide()
			ship.lives -= 1
			ship.shield = 100
			
	if ship.lives == 0:
		return True
	else:
		return False

# Kiểm tra va chạm giữa ship và power
def check_coll_ship_power(ship, powers):
	colls = pygame.sprite.spritecollide(ship, powers, True)
	for coll in colls:
		# Thêm 20 máu
		ship.shield += 20 
		if ship.shield >= 100:
			ship.shield = 100


# Phần hiển thị điểm 
def draw_score(screen, text, size, x, y, color):
	font = pygame.font.Font(font_name, size)
	text_surface = font.render(text, True, color)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	screen.blit(text_surface, text_rect)

# Hiển thị màn hình kết thúc
def draw_game_over(screen, game):
	screen.blit(bg_end_image, [0,0])
	pygame.display.flip()

#Hiển thị start menu
def draw_menu_start(screen, game):
	screen.blit(bg_start_image, [0,0])
	pygame.display.flip()

	
# Hiển thị % mạng
def draw_shield(x, y, screen ,shield):
	if shield < 0:
		shield = 0
	fill = (shield / 100) * 100
	outline_rect = pygame.Rect(x, y, 100, 10)
	fill_rect = pygame.Rect(x, y, fill, 10)
	if shield > 40:
		pygame.draw.rect(screen, GREEN, fill_rect)
	else:
		pygame.draw.rect(screen, RED, fill_rect)
	pygame.draw.rect(screen, WHITE, outline_rect, 2) 


def draw_ship_mini(screen, x, y, lives):
	for i in range(lives):
		ship_mini = ShipMini(screen, x, y, i)
		ship_mini.blitme() 