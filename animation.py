import math, pygame, sprites

def Player_animation(self):

    self.down_animation = [
        self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
        self.game.character_spritesheet.get_sprite(32, 0, self.width, self.height),
        self.game.character_spritesheet.get_sprite(64, 0, self.width, self.height),
    ]

    self.up_animation = [
        self.game.character_spritesheet.get_sprite(0, 32, self.width, self.height),
        self.game.character_spritesheet.get_sprite(32, 32, self.width, self.height),
        self.game.character_spritesheet.get_sprite(64, 32, self.width, self.height),
    ]

    self.left_animation = [
        self.game.character_spritesheet.get_sprite(0, 96, self.width, self.height),
        self.game.character_spritesheet.get_sprite(32, 96, self.width, self.height),
        self.game.character_spritesheet.get_sprite(64, 96, self.width, self.height),
    ]

    self.right_animation = [
        self.game.character_spritesheet.get_sprite(0, 64, self.width, self.height),
        self.game.character_spritesheet.get_sprite(32, 64, self.width, self.height),
        self.game.character_spritesheet.get_sprite(64, 64, self.width, self.height),
    ]

def Player_animation_animate(self):

    if self.facing == 'down':
        if self.y_change == 0:
            self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
        else:
            self.image = self.down_animation[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 3:
                self.animation_loop = 1

    if self.facing == 'up':
        if self.y_change == 0:
            self.image = self.game.character_spritesheet.get_sprite(0, 32, self.width, self.height)
        else:
            self.image = self.up_animation[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 3:
                self.animation_loop = 1

    if self.facing == 'left':
        if self.x_change == 0:
            self.image = self.game.character_spritesheet.get_sprite(0, 96, self.width, self.height)
        else:
            self.image = self.left_animation[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 3:
                self.animation_loop = 1

    if self.facing == 'right':
        if self.x_change == 0:
            self.image = self.game.character_spritesheet.get_sprite(0, 64, self.width, self.height)
        else:
            self.image = self.right_animation[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 3:
                self.animation_loop = 1

def enemy_animation(self):
    self.left_animation = [
        self.game.enemy_spritesheet.get_sprite(3, 98, self.width, self.height),
        self.game.enemy_spritesheet.get_sprite(35, 98, self.width, self.height),
        self.game.enemy_spritesheet.get_sprite(68, 98, self.width, self.height)
    ]

    self.right_animation = [
        self.game.enemy_spritesheet.get_sprite(3, 66, self.width, self.height),
        self.game.enemy_spritesheet.get_sprite(35, 66, self.width, self.height),
        self.game.enemy_spritesheet.get_sprite(68, 66, self.width, self.height)
    ]

def enemy_animation_animate(self):
    if self.facing == "left":
        if self.x_change == 0:
            self.image = self.game.enemy_spritesheet.get_sprite(3, 98, self.width, self.height)
        else:
            self.image = self.left_animation[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 3:
                self.animation_loop = 1

    if self.facing == "right":
        if self.x_change == 0:
            self.image = self.game.enemy_spritesheet.get_sprite(3, 66, self.width, self.height)
        else:
            self.image = self.right_animation[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 3:
                self.animation_loop = 1