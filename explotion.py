import pygame as pg

explosion_anim = [pg.image.load(f'explosion/regularExplosion0{i}.png') for i in range(0, 7)]
print(explosion_anim)


class Explosion(pg.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = explosion_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        current_time = pg.time.get_ticks()
        frame_duration = 150
        frame_index = (current_time // frame_duration) % len(explosion_anim)
        self.image = explosion_anim[frame_index]

        if frame_index == len(explosion_anim) - 1:
            self.kill()