import pygame as pg
from sprite.space_ship import SpaceShip
from sprite.meteor import Meteor
from sprite.bullet import Bullet
from explotion import Explosion
from helth_bar import HelthBar
import random

pg.init()
pg.font.init()

font = pg.font.SysFont('None', 100)

W, H = 900, 900

screen = pg.display.set_mode((W, H))

score = 0
run = True

pg.time.set_timer(pg.USEREVENT, 500)  # Ивент спавна метеоритов

clock = pg.time.Clock()

player = SpaceShip(300, 300)
helth_bar = HelthBar(W // 2, 50)

all_sprite = pg.sprite.Group(player, helth_bar)
meteors = pg.sprite.Group()
bullets = pg.sprite.Group()

pg.mouse.set_visible(False)

while run:
    screen.blit(pg.image.load('bg.jpg'), (0, 0))
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if event.type == pg.USEREVENT:
            meteor = Meteor(random.randint(0, W), -10, random.randint(-3, 3), random.randint(1, 6))
            all_sprite.add(meteor)
            meteors.add(meteor)

        if event.type == pg.MOUSEBUTTONUP:
            bullet = Bullet(player.rect.centerx, player.rect.y)
            all_sprite.add(bullet)
            bullets.add(bullet)

    hits = pg.sprite.groupcollide(bullets, meteors, True, True, pg.sprite.collide_circle)
    for hit in hits:
        if hit:
            score += 1
            exp = Explosion(hit.rect.center)
            all_sprite.add(exp)

    if pg.sprite.groupcollide([player], meteors, False, True, pg.sprite.collide_circle):
        helth_bar.width -= 30

    for m in meteors:
        if 0 < m.rect.x < W and m.rect.y > H:
            helth_bar.width -= 30
            m.kill()

    if helth_bar.width <= 0:
        for sprite in all_sprite:
            sprite.kill()
        game_over_text = font.render(f"Game Over", False, 'white')
        screen.blit(game_over_text, (W // 2 - game_over_text.get_width() // 2, 500))
        pg.mouse.set_visible(True)

    score_text = font.render(f"{score}", False, 'white')
    screen.blit(score_text, (W // 2 - 25, 100))

    all_sprite.draw(screen)
    all_sprite.update()

    pg.display.update()

pg.quit()
