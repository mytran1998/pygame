import pygame
from ship import Ship
from bullet import Bullet
from alien import Alien
from game import Game
import random

BLACK = (0, 0, 0)

def event_keydown(event, ship, screen, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    # Move the ship to the left by activating 'direction' flag
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
    	create_bullet(screen, ship, bullets)

def event_keyup(event, ship):
    # Stop the ship by activating 'direction' flag
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    # Stop the ship by activating 'direction' flag
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def create_bullet(screen, ship, bullets):
	# Tạo mới viên đạn và thêm vào group bullets 
    bullet = Bullet(screen, ship)
    bullets.add(bullet)

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

# Kiểm tra va chạm giữa alien và bullet
def check_coll_bullet_alien(game, aliens, bullets, screen):
	collisions = pygame.sprite.groupcollide(aliens, bullets, True, True)
	for collision in collisions:
		# Tăng điểm
		game.score += 1
		# Mỗi lần bắn trúng thì tạo thêm 1 alien
		create_alien(screen, aliens, 1)

# Kiểm tra va chạm giữa alien và ship
def check_coll_alien_ship(ship, aliens):
	colls = pygame.sprite.spritecollide(ship, aliens, True)
	if colls:
		return True
	return False

# Phần hiển thị điểm 
font_name = pygame.font.match_font('arial')
def draw_score(screen, text, size, x, y):
	font = pygame.font.Font(font_name, size)
	text_surface = font.render(text, True, BLACK)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	screen.blit(text_surface, text_rect)

# Hiển thị màn hình kết thúc
def draw_game_over(screen):
	draw_score(screen, "Ban da thua!", 20, screen.get_width() / 2, screen.get_height() / 2)
	draw_score(screen, "Nhan phim bat ki de choi lai ...", 20, screen.get_width()/2, screen.get_height()/2 + 40)
	pygame.display.flip()

