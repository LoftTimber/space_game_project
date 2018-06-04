# Imports
import pygame, os
os.environ['SDL_VIDEO_CENTERED'] = '1'
import math




# Initialize game engine
pygame.init()


# Window
##WIDTH = 1350
##HEIGHT = 730
##WIDTH = 2550
##HEIGHT = 1565
WIDTH = 704
HEIGHT = 704
SIZE = (WIDTH, HEIGHT)
TITLE = "Space War"
screen = pygame.display.set_mode(SIZE)      ########################### work on stair case to funnel trap evode
pygame.display.set_caption(TITLE)




# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
##R = (255, 0, 0)     #RED
##O = (255, 165, 0)   #ORANGE
##Y = (255, 255, 0)   #YELLOW
##G = (0, 128, 0)     #GREEN
##S = (0,0,255)       #BLUE
##I = (75,0,130)      #INDIGO
##V = (238,130,238)   #VIOLET
##
##
##
##
##
##
##
##f = (34, 139, 34)
##W = (255, 255, 255) #WHITE
##b = (75, 200, 255)  #SKYBLUE
##l = (176, 196, 222) #LIGHTSTEELBLUE
##DARKERWHITE = (235, 245, 255) #DARKERWHITE
##B = (0, 0, 0)       #BLACK
##o = (255,80,0)      #DARKERORANGE
##g = (34, 139, 34)   #FORESTGREEN

# Images
pix1_img = pygame.image.load('space_game_stuff/images/pixel.png')
B_pix = pygame.image.load('space_game_stuff/images/pixel_1.png')
O_pix = pygame.image.load('space_game_stuff/images/gray_pixel.png')
f_pix = pygame.image.load('space_game_stuff/images/pixel_1.png')
o_pix = pygame.image.load('space_game_stuff/images/pixel_1.png')
ship_img = pygame.image.load('space_game_stuff/images/pixel.png')
fire_img = pygame.image.load('space_game_stuff/images/pixel.png')
thunder_img = pygame.image.load('space_game_stuff/images/pixel.png')
left_arrow = pygame.image.load('space_game_stuff/images/pixel.png')
right_arrow = pygame.image.load('space_game_stuff/images/pixel.png')
up_arrow = pygame.image.load('space_game_stuff/images/pixel.png')
down_arrow = pygame.image.load('space_game_stuff/images/pixel.png')
B_pix = pygame.transform.scale(B_pix, (64, 64))
O_pix = pygame.transform.scale(O_pix, (64, 64))
f_pix = pygame.transform.scale(f_pix, (64, 64))
o_pix = pygame.transform.scale(o_pix, (64, 64))
left_arrow = pygame.transform.scale(left_arrow, (64, 64))
right_arrow = pygame.transform.scale(right_arrow, (64, 64))
up_arrow = pygame.transform.scale(up_arrow, (64, 64))
down_arrow = pygame.transform.scale(down_arrow, (64, 64))
##player_facing_left
##player_jump_left
##player_jump_right

# Game classes
class Pixel(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        
        
        
        
        self.type = 0
        

    def move_left(self, ship):
        self.rect.x -= ship.speed
        
    def move_right(self, ship):
        self.rect.x += ship.speed

    def move_up(self, ship):
        self.rect.y -= ship.speed
        
    def move_down(self, ship):
        self.rect.y += ship.speed

    def move_left_half(self, ship):
        self.rect.x -= ship.speed/2
        
        
    def move_right_half(self, ship):
        self.rect.x += ship.speed/2

    def move_up_half(self, ship):
        self.rect.y -= ship.speed/2
        
    def move_down_half(self, ship):
        self.rect.y += ship.speed/2

    def update(self, spells1, mobs):
        

        hit_list = pygame.sprite.spritecollide(self, spells1, False)
        for s in spells1:
            s.hp = s.hp
        for hit in hit_list:
            if self.type == "black":
                s.hp -= 1

            
##        go_left = False
##        go_right = False
##
##        num = 5
##        for i in range(9):
##            if pixel_items[num].filled == True:
##                go_right = True
##
##            num += 12
##            
##        num = 6
##        for i in range(9):
##            if pixel_items[num].filled == True:
##                if go_right == True:
##                    go_left = go_right
##                go_right = False
##
##            num += 12
##
##            
##        num = 4
##        for i in range(9):
##            if pixel_items[num].filled == True:
##                if go_left == True:
##                    go_right = go_right
##                go_left = False
##
##            num += 12
##            
##
##        if go_left == True:
##            self.rect.x -= 15
##
##        elif go_right == True:
##            self.rect.x += 15

        

            
        








          

    
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.top = x
        self.rect.centerx = x+32
        self.rect.centery = y+32
        self.rect.bottom = y+64
        

        self.speed = 4
        self.shield = 10
        self.shot_range = 500
        
        

    def move_left(self, ship):
        self.rect.x -= ship.speed
        
    def move_right(self, ship):
        self.rect.x += ship.speed

    def move_up(self, ship):
        self.rect.y -= ship.speed
        
    def move_down(self, ship):
        self.rect.y += ship.speed

    def move_left_half(self, ship):
        self.rect.x -= ship.speed/2
        
    def move_right_half(self, ship):
        self.rect.x += ship.speed/2

    def move_up_half(self, ship):
        self.rect.y -= ship.speed/2
        
    def move_down_half(self, ship):
        self.rect.y += ship.speed/2
    
    def make_arrow(self, mouse_pos):
        arrow = Fire(fire_img)

        
        if self.rect.centerx-mouse_pos[0] == 0:
            arrow.angle = 90
        elif (self.rect.centerx-mouse_pos[0]) == (self.rect.centery-mouse_pos[1]) and (mouse_pos[0] < self.rect.centerx)\
             and mouse_pos[1] <= self.rect.centery:
            arrow.angle = 45
        elif (self.rect.centerx-mouse_pos[0]) == (self.rect.centery-mouse_pos[1]) and (mouse_pos[0] > self.rect.centerx)\
             and mouse_pos[1] <= self.rect.centery:
            arrow.angle = -45
        elif (self.rect.centerx-mouse_pos[0]) == (self.rect.centery-mouse_pos[1]) and (mouse_pos[0] < self.rect.centerx)\
             and mouse_pos[1] >= self.rect.centery:
            arrow.angle = 45
        elif (self.rect.centerx-mouse_pos[0]) == (self.rect.centery-mouse_pos[1]) and (mouse_pos[0] > self.rect.centerx)\
             and mouse_pos[1] >= self.rect.centery:
            arrow.angle = -45
        elif (self.rect.centerx-mouse_pos[0]) > (self.rect.centery-mouse_pos[1]):
            arrow.angle = math.degrees(math.atan((self.rect.centery-mouse_pos[1])/(self.rect.centerx-mouse_pos[0])))
        elif (self.rect.centerx-mouse_pos[0]) < (self.rect.centery-mouse_pos[1]):
            arrow.angle = (math.degrees(math.atan((self.rect.centery-mouse_pos[1])/(self.rect.centerx-mouse_pos[0]))))
        else:
            arrow.angle = 90
        
        
        
        
        if (arrow.angle >= 67 or arrow.angle <= -67) and mouse_pos[1] <= self.rect.centery:
            arrow.rect.centerx = self.rect.centerx
            arrow.rect.bottom = self.rect.top
            arrow.real_angle = 0
        elif arrow.angle >= 23 and mouse_pos[1] <= self.rect.centery:
            arrow.rect.centerx = self.rect.centerx-64
            arrow.rect.bottom = self.rect.top
            arrow.real_angle = 315
        elif arrow.angle <= -23 and mouse_pos[1] <= self.rect.centery:
            arrow.rect.centerx = self.rect.centerx+64
            arrow.rect.bottom = self.rect.top
            arrow.real_angle = 45
        elif arrow.angle > -23 and mouse_pos[0] <= self.rect.centerx and mouse_pos[1] <= self.rect.centery:
            arrow.rect.centerx = self.rect.centerx-64
            arrow.rect.bottom = self.rect.bottom
            arrow.real_angle = 270
        elif arrow.angle > -23 and mouse_pos[0] >= self.rect.centerx and mouse_pos[1] <= self.rect.centery:
            arrow.rect.centerx = self.rect.centerx+64
            arrow.rect.bottom = self.rect.bottom
            arrow.real_angle = 90
        elif (arrow.angle >= 67 or arrow.angle <= -67) and mouse_pos[1] >= self.rect.centery:
            arrow.rect.centerx = self.rect.centerx
            arrow.rect.top = self.rect.bottom
            arrow.real_angle = 180
        elif arrow.angle >= 23 and mouse_pos[1] >= self.rect.centery:
            arrow.rect.centerx = self.rect.centerx+64
            arrow.rect.top = self.rect.bottom
            arrow.real_angle = 135
        elif arrow.angle <= -23 and mouse_pos[1] >= self.rect.centery:
            arrow.rect.centerx = self.rect.centerx-64
            arrow.rect.top = self.rect.bottom
            arrow.real_angle = 225
        elif arrow.angle > -23 and mouse_pos[0] <= self.rect.centerx and mouse_pos[1] >= self.rect.centery:
            arrow.rect.centerx = self.rect.centerx-64
            arrow.rect.bottom = self.rect.bottom
            arrow.real_angle = 270
        elif arrow.angle > -23 and mouse_pos[0] >= self.rect.centerx and mouse_pos[1] >= self.rect.centery:
            arrow.rect.centerx = self.rect.centerx+64
            arrow.rect.bottom = self.rect.bottom
            arrow.real_angle = 90
        
        arrows.add(arrow)
    

    def cast_fire(self, arrow):
        spell = Fire(fire_img)

        spell.rect.centerx = arrow.rect.centerx
        spell.rect.centery = arrow.rect.centery
        spell.angle = arrow.real_angle
        

        
        
        
        
        spells1.add(spell)


        
        
##        spell = Fire(fire_img)
##
##        spell.rect.centerx = self.rect.centerx+100
##        spell.rect.bottom = self.rect.top
##        spell.side = 1
##        spells1.add(spell)
##
##        spell = Fire(fire_img)
##
##        spell.rect.centerx = self.rect.centerx-100
##        spell.rect.bottom= self.rect.top
##        spell.side = 1
##        spells1.add(spell)
##
##        self.shot_range -= 30
        

    def cast_thunder(self):
        spell = Thunder(thunder_img)

        spell.rect.centerx = self.rect.centerx
        spell.rect.centery = self.rect.top
        spell.side = 1
        
        spells2.add(spell)

    def update_vertical(self):
        collide = False
        if vel_down == True:
            hit_list = pygame.sprite.spritecollide(self, pixels, False)
            for hit in hit_list:
                if hit.type == "black":
                    collide = True
                    
            if collide == True:
                mob1.move_down(self)
                enemy1.move_down(self)
                for s in spells1:
                    s.move_down(self)
                for p in pixels:
                    p.move_down(self)


        collide = False
        if vel_up == True:
            hit_list = pygame.sprite.spritecollide(self, pixels, False)
            for hit in hit_list:
                if hit.type == "black":
                    collide = True
                    
            if collide == True:
                mob1.move_up(self)
                enemy1.move_up(self)
                for s in spells1:
                    s.move_up(self)
                for p in pixels:
                    p.move_up(self)
    def update_horizontal(self):
        collide = False
        if vel_left == True:
            hit_list = pygame.sprite.spritecollide(self, pixels, False)
            for hit in hit_list:
                if hit.type == "black":
                    collide = True
                    
            if collide == True:
                mob1.move_left(self)
                enemy1.move_left(self)
                for s in spells1:
                    s.move_left(self)
                for p in pixels:
                    p.move_left(self)


        collide = False
        if vel_right == True:
            hit_list = pygame.sprite.spritecollide(self, pixels, False)
            for hit in hit_list:
                if hit.type == "black":
                    collide = True
                    
            if collide == True:
                mob1.move_right(self)
                enemy1.move_right(self)
                for s in spells1:
                    s.move_right(self)
                for p in pixels:
                    p.move_right(self)

    def update_vertical_half(self):
        collide = False
        if vel_down == True:
            hit_list = pygame.sprite.spritecollide(self, pixels, False)
            for hit in hit_list:
                if hit.type == "black":
                    collide = True
                    
            if collide == True:
                mob1.move_down_half(self)
                enemy1.move_down_half(self)
                for s in spells1:
                    s.move_down_half(self)
                for p in pixels:
                    p.move_down_half(self)


        collide = False
        if vel_up == True:
            hit_list = pygame.sprite.spritecollide(self, pixels, False)
            for hit in hit_list:
                if hit.type == "black":
                    collide = True
                    
            if collide == True:
                mob1.move_up_half(self)
                enemy1.move_up_half(self)
                for s in spells1:
                    s.move_up_half(self)
                for p in pixels:
                    p.move_up_half(self)
    def update_horizontal_half(self):
        collide = False
        if vel_left == True:
            hit_list = pygame.sprite.spritecollide(self, pixels, False)
            for hit in hit_list:
                if hit.type == "black":
                    collide = True
                    
            if collide == True:
                mob1.move_left_half(self)
                enemy1.move_left_half(self)
                for s in spells1:
                    s.move_left_half(self)
                for p in pixels:
                    p.move_left_half(self)


        collide = False
        if vel_right == True:
            hit_list = pygame.sprite.spritecollide(self, pixels, False)
            for hit in hit_list:
                if hit.type == "black":
                    collide = True
                    
            if collide == True:
                mob1.move_right_half(self)
                enemy1.move_right_half(self)
                for s in spells1:
                    s.move_right_half(self)
                for p in pixels:
                    p.move_right_half(self)

    def update(self, enemies):
        
        hit_list = pygame.sprite.spritecollide(self, enemies, False)

        for hit in hit_list:
            self.shield -= hit.damage

        
##        hit_list = pygame.sprite.spritecollide(self, spells2, False)
##
##        for hit in hit_list:
##            self.shield -= 1

        if self.shield <= 0:
            self.kill()
            

        

    
    
class Fire(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()

        self.damage = .1
        self.hp = 5
        self.speed = 8
        

    def move_left(self, ship):
        self.rect.x -= ship.speed
        
    def move_right(self, ship):
        self.rect.x += ship.speed

    def move_up(self, ship):
        self.rect.y -= ship.speed
        
    def move_down(self, ship):
        self.rect.y += ship.speed

    def move_left_half(self, ship):
        self.rect.x -= ship.speed/2
        
    def move_right_half(self, ship):
        self.rect.x += ship.speed/2

    def move_up_half(self, ship):
        self.rect.y -= ship.speed/2
        
    def move_down_half(self, ship):
        self.rect.y += ship.speed/2

    def update(self, beat):
        
##            if beat%(int(2)) == 0:
##                blast = pygame.math.Vector2(self.point)
##                self.gud = blast.normalize()
##                self.rect.x += (self.speed*self.gud[0])                     #######################normalizing a vector
##                self.rect.y -= (self.speed*self.gud[1])
##                magnitude = math.sqrt((self.point[0] - (self.rect.centerx - ship.rect.centerx))**2 + (self.point[1] - (ship.rect.top - self.rect.centery))**2)
##                
##                self.rect.x += ((self.point[0] - (self.rect.centerx - ship.rect.centerx))/magnitude)*self.speed
##                self.rect.y -= ((self.point[1] - (ship.rect.top - self.rect.centery))/magnitude)*self.speed
        if beat%(int(1)) == 0:
            if self.angle == 0:
                self.rect.x -= self.speed*0
                self.rect.y -= self.speed*1
            elif self.angle == 45:
                self.rect.x += self.speed*0.5
                self.rect.y -= self.speed*0.4
            elif self.angle == 90:
                self.rect.x += self.speed*1
                self.rect.y -= self.speed*0
            elif self.angle == 135:
                self.rect.x += self.speed*0.5
                self.rect.y += self.speed*0.5
            elif self.angle == 180:
                self.rect.x -= self.speed*0
                self.rect.y += self.speed*1
            elif self.angle == 225:
                self.rect.x -= self.speed*0.4
                self.rect.y += self.speed*0.5
            elif self.angle == 270:
                self.rect.x -= self.speed*1
                self.rect.y -= self.speed*0
            elif self.angle == 315:
                self.rect.x -= self.speed*0.5
                self.rect.y -= self.speed*0.5
            
        
            

        

##        hit_list = pygame.sprite.spritecollide(self, pixels, False)
##        for spell in spells1:
##            spell.damage = spell.damage
##        for hit in hit_list:
##            if hit.type == "black":
##                self.rect.x -= self.speed*0
##                self.rect.y -= self.speed*0

##        hit_list = pygame.sprite.spritecollide(self, player, False)
##        for spell in spells1:
##            spell.damage = spell.damage
##        for hit in hit_list:
##            if hit != self:
##                self.hp -= spell.damage
##                self.hp -= self.damage

            
        if self.hp <= 0:
            self.kill()
            
        
##        if mob1.rect.centerx > self.rect.centerx:
##            self.rect.x += self.speed
##
##        if mob1.rect.centerx < self.rect.centerx:
##            self.rect.x -= self.speed

        if self.rect.bottom <= 0:
            self.kill()
        if self.rect.top >= HEIGHT:
            self.kill()
        if self.rect.right <= 0:
            self.kill()
        if self.rect.left >= WIDTH:
            self.kill()
            


    

class Thunder(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        
        self.speed = 12

    def update(self):
        if self.side == 1:
            self.rect.y -= self.speed

        if self.side == 2:
            self.rect.y += self.speed


    
class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = 15
        self.shield = 1

        
        
    def move_left(self, ship):
        self.rect.x -= ship.speed
        
    def move_right(self, ship):
        self.rect.x += ship.speed

    def move_up(self, ship):
        self.rect.y -= ship.speed
        
    def move_down(self, ship):
        self.rect.y += ship.speed

    def move_left_half(self, ship):
        self.rect.x -= ship.speed/2
        
    def move_right_half(self, ship):
        self.rect.x += ship.speed/2

    def move_up_half(self, ship):
        self.rect.y -= ship.speed/2
        
    def move_down_half(self, ship):
        self.rect.y += ship.speed/2

    def move(self, spells1, spells2):

        spell_to_left = False
        spell_to_right = False
        spell_to_left_far = False
        spell_to_right_far = False
        spell_to_left_very_far = False
        spell_to_right_very_far = False
        can_not_go_left = False
        can_not_go_right = False
        will_not_go_left = False
        will_not_go_right = False
        would_not_go_left = False
        would_not_go_right = False
        would_not_go_left_far = False
        would_not_go_right_far = False
        would_not_go_left_very_far = False
        would_not_go_right_very_far = False
        spell_to_far_left = False
        spell_to_far_right = False
        for spell in spells1:
            
            if ((spell.rect.right >= self.rect.left) and spell.rect.centerx <= self.rect.centerx) \
                and (spell.rect.top <= self.rect.bottom+(200) and spell.rect.bottom >= self.rect.top):
                spell_to_left = True

            if (spell.rect.centerx > self.rect.centerx and spell.rect.left <= self.rect.right) \
                and (spell.rect.top <= self.rect.bottom+(200) and spell.rect.bottom >= self.rect.top):
                spell_to_right = True

            if ((spell.rect.right >= self.rect.left) and spell.rect.centerx <= self.rect.centerx) \
                and (spell.rect.top <= self.rect.bottom+(400) and spell.rect.bottom >= self.rect.top):
                spell_to_left_far = True

            if (spell.rect.centerx > self.rect.centerx and spell.rect.left <= self.rect.right) \
                and (spell.rect.top <= self.rect.bottom+(400) and spell.rect.bottom >= self.rect.top):
                spell_to_right_far = True

            if ((spell.rect.right >= self.rect.left) and spell.rect.centerx <= self.rect.centerx) \
                and (spell.rect.top <= self.rect.bottom+(1000) and spell.rect.bottom >= self.rect.top+(400)):
                spell_to_left_very_far = True

            if (spell.rect.centerx > self.rect.centerx and spell.rect.left <= self.rect.right) \
                and (spell.rect.top <= self.rect.bottom+(1000) and spell.rect.bottom >= self.rect.top+(400)):
                spell_to_right_very_far = True

            if (spell.rect.right >= (self.rect.left)-(self.speed*2) and spell.rect.centerx < (self.rect.centerx)) \
                and (spell.rect.top <= self.rect.bottom+(200) and spell.rect.bottom >= self.rect.top):
                can_not_go_left = True

            if (spell.rect.centerx > (self.rect.centerx) and spell.rect.left < (self.rect.right)+(self.speed*2)) \
                and (spell.rect.top <= self.rect.bottom+(200) and spell.rect.bottom >= self.rect.top):
                can_not_go_right = True

            if (spell.rect.centerx >= (self.rect.centerx)-120 and spell.rect.right < (self.rect.left)) \
                and (spell.rect.top <= self.rect.bottom+(200) and spell.rect.bottom >= self.rect.top):
                will_not_go_left = True

            if (spell.rect.right > (self.rect.left) and spell.rect.centerx < (self.rect.centerx)+120) \
                and (spell.rect.top <= self.rect.bottom+(200) and spell.rect.bottom >= self.rect.top):
                will_not_go_right = True

            if (spell.rect.centerx >= (self.rect.centerx)-200 and spell.rect.centerx < (self.rect.centerx)) \
                and (spell.rect.top <= self.rect.bottom+(300) and spell.rect.bottom >= self.rect.top):
                would_not_go_left = True

            if (spell.rect.centerx > (self.rect.centerx) and spell.rect.centerx < (self.rect.centerx)+200) \
                and (spell.rect.top <= self.rect.bottom+(300) and spell.rect.bottom >= self.rect.top):
                would_not_go_right = True

            if (spell.rect.centerx >= (self.rect.centerx)-200 and spell.rect.centerx < (self.rect.centerx)) \
                and (spell.rect.top <= self.rect.bottom+(600) and spell.rect.bottom >= self.rect.top+(400)):
                would_not_go_left_far = True  

            if (spell.rect.centerx > (self.rect.centerx) and spell.rect.centerx < (self.rect.centerx)+200) \
                and (spell.rect.top <= self.rect.bottom+(600) and spell.rect.bottom >= self.rect.top+(400)):
                would_not_go_right_far = True

            if (spell.rect.centerx >= (self.rect.centerx)-200 and spell.rect.centerx < (self.rect.centerx)) \
                and (spell.rect.top <= self.rect.bottom+(500) and spell.rect.bottom >= self.rect.top+(400)):
                would_not_go_left_very_far = True
               

            if (spell.rect.centerx > (self.rect.centerx) and spell.rect.centerx < (self.rect.centerx)+200) \
                and (spell.rect.top <= self.rect.bottom+(500) and spell.rect.bottom >= self.rect.top+(400)):
                would_not_go_right_very_far = True
               

            if ((spell.rect.right >= self.rect.left-200) and spell.rect.centerx <= self.rect.centerx) \
                and (spell.rect.top <= self.rect.bottom+(300) and spell.rect.bottom >= self.rect.top):
                spell_to_far_left = True

            if (spell.rect.centerx > self.rect.centerx and spell.rect.left <= self.rect.right+200) \
                and (spell.rect.top <= self.rect.bottom+(300) and spell.rect.bottom >= self.rect.top):
               spell_to_far_right = True

  
            

        if (spell_to_left_far == True or spell_to_right_far == True) and can_not_go_right == True and can_not_go_left == False:
            self.rect.x -= self.speed

        elif (spell_to_left_far == True or spell_to_right_far == True) and can_not_go_left == True and can_not_go_right == False:
            self.rect.x += self.speed        

        

        elif (spell_to_left_far == True or spell_to_right_far == True) and spell_to_far_right == True and will_not_go_right == True \
             and can_not_go_right == True and can_not_go_left == False:
            self.rect.x -= self.speed
            
        elif (spell_to_left_far == True or spell_to_right_far == True) and spell_to_far_left == True and will_not_go_left == True \
             and can_not_go_left == True and can_not_go_right == False:
            self.rect.x += self.speed

        elif (spell_to_left_far == True or spell_to_right_far == True) and will_not_go_right == True and will_not_go_left == False and can_not_go_left == False:
            self.rect.x -= self.speed

        elif (spell_to_left_far == True or spell_to_right_far == True) and will_not_go_left == True and will_not_go_right == False and can_not_go_right == False:
            self.rect.x += self.speed

        elif (spell_to_left_very_far == True or spell_to_right_very_far == True or spell_to_far_left) and would_not_go_right_far == True \
             and would_not_go_left_far == False and can_not_go_left == False:
            self.rect.x -= self.speed

        elif (spell_to_left_very_far == True or spell_to_right_very_far == True or spell_to_far_right) and would_not_go_left_far == True \
             and would_not_go_right_far == False and can_not_go_right == False:
            self.rect.x += self.speed
            #########################################

        

        elif (spell_to_left_far == False or spell_to_right_far == False) and would_not_go_right == True and would_not_go_left == True\
             and would_not_go_right_far == True and would_not_go_left_far == True  \
             and will_not_go_left == False and can_not_go_left == False:
            self.rect.x -= self.speed

        elif (spell_to_left_far == False or spell_to_right_far == False) and would_not_go_right == True and would_not_go_left == True\
             and would_not_go_right_far == True and would_not_go_left_far == True  \
             and will_not_go_right == False and can_not_go_right == False:
            self.rect.x += self.speed

        elif (spell_to_left_very_far == True or spell_to_right_very_far == True) and would_not_go_left == True and would_not_go_right == False\
             and will_not_go_right == False and can_not_go_right == False:
            self.rect.x -= self.speed

        elif (spell_to_left_very_far == True or spell_to_right_very_far == True) and would_not_go_right == True and would_not_go_left == True\
             and will_not_go_left == False and can_not_go_left == False:
            self.rect.x -= self.speed

        elif (spell_to_left_very_far == True or spell_to_right_very_far == True) and would_not_go_right == True and would_not_go_left == True\
             and will_not_go_right == False and can_not_go_right == False:
            self.rect.x += self.speed

        

        
 
        elif spell_to_left == True and can_not_go_right == False:
            self.rect.x += self.speed
        
        elif spell_to_right == True and can_not_go_left == False:
            self.rect.x -= self.speed
            


               
            
            

            

    def cast_fire(self):
        spell = Fire(fire_img)

        spell.rect.centerx = self.rect.centerx
        spell.rect.y = self.rect.bottom
        spell.side = 2
        
        spells1.add(spell)

    def cast_thunder(self):
        spell = Thunder(thunder_img)

        spell.rect.centerx = self.rect.centerx
        spell.rect.centery = self.rect.top
        spell.side = 2
        
        spells2.add(spell)

##    def drop_bomb(self):
##        bomb = Bomb(fire_img)
##
##        bomb.rect.centerx = self.rect.centerx
##        bomb.rect.y = self.rect.bottom
##        
##        bombs.add(bomb)

    def update(self, spells1, spells2):
        hit_list = pygame.sprite.spritecollide(self, spells1, False)
        
        

        for hit in hit_list:
            self.shield -= 1

        
        hit_list = pygame.sprite.spritecollide(self, spells2, False)

        for hit in hit_list:
            self.shield -= 1

        if self.shield <= 0:
            self.kill()

class enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = 4
        self.shield = 10
        self.damage = .2
        self.sight_range = 4

        
        
    def move_left(self, ship):
        self.rect.x -= ship.speed
        
    def move_right(self, ship):
        self.rect.x += ship.speed

    def move_up(self, ship):
        self.rect.y -= ship.speed
        
    def move_down(self, ship):
        self.rect.y += ship.speed

    def move_left_half(self, ship):
        self.rect.x -= ship.speed/2
        
    def move_right_half(self, ship):
        self.rect.x += ship.speed/2

    def move_up_half(self, ship):
        self.rect.y -= ship.speed/2
        
    def move_down_half(self, ship):
        self.rect.y += ship.speed/2

    def move(self, ship):
        if ship.rect.centery <= self.rect.centery+self.sight_range*64 and ship.rect.centery > self.rect.centery \
           and ship.rect.centerx <= self.rect.centerx+self.sight_range*64 and ship.rect.centerx >= self.rect.centerx-self.sight_range*64:
            self.rect.y += self.speed
        elif ship.rect.centery <= self.rect.centery+self.sight_range*64 and ship.rect.centery >= self.rect.centery-self.sight_range*64 and \
             ship.rect.centerx <= self.rect.centerx+self.sight_range*64 \
             and ship.rect.centerx >= self.rect.centerx-self.sight_range*64 \
           and ship.rect.centery <= self.rect.centery+self.sight_range*64 and ship.rect.centery >= self.rect.centery:
            self.rect.x += self.speed
        if ship.rect.centery >= self.rect.centery-self.sight_range*64 and ship.rect.centery < self.rect.centery \
           and ship.rect.centerx <= self.rect.centerx+self.sight_range*64 and ship.rect.centerx >= self.rect.centerx-self.sight_range*64:
            self.rect.y -= self.speed
        elif ship.rect.centery >= self.rect.centery-self.sight_range*64 and ship.rect.centery <= self.rect.centery+self.sight_range*64 and \
             ship.rect.centerx >= self.rect.centerx-self.sight_range*64 \
             and ship.rect.centerx <= self.rect.centerx:
            self.rect.x -= self.speed
        
        

    def update(self, spells1):
        hit_list = pygame.sprite.spritecollide(self, spells1, False)
        for spell in spells1:
            spell.damage = spell.damage
        

        for hit in hit_list:
            self.shield -= spell.damage

        
##        hit_list = pygame.sprite.spritecollide(self, spells2, False)
##
##        for hit in hit_list:
##            self.shield -= 1

        if self.shield <= 0:
            self.kill()
        


##class Bomb(pygame.sprite.Sprite):
##    
##    def __init__(self, image):
##        super().__init__()
##
##        self.image = image
##        self.rect = image.get_rect()
##        
##        self.speed = 6
##
##    def move_left(self, ship):
##        self.rect.x -= ship.speed
##        
##    def move_right(self, ship):
##        self.rect.x += ship.speed
##
##    def update(self):
##        self.rect.y += self.speed
    
    
class Fleet:

    def __init__(self):
        pass

    def update(self):
        pass



def level_1():
    block_line1= [0,0,0,0,0,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]
    block_line2= [0,0,0,0,0,0,0,0,0,0,8]
    block_line3= [0,0,0,0,0,0,0,0,0,0,8]
    block_line4= [0,0,0,0,0,0,0,0,0,0,8]
    block_line5= [0,0,0,0,0,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]
    block_line6= [0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8]
    block_line7= [0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0]
    block_line8= [8,0,0,0,0,0,0,0,0,0,0]
    block_line9= [8,0,0,0,0,0,0,0,0,0,0]
    block_line10=[8,0,0,0,0,0,0,0,0,0,0]
    block_line11=[8]
    block_line12=[8]
    block_line13=[8]
    block_line14=[8]
    block_line15=[8]
    block_line16=[8,0,0,0,0,0,8,8,8,8,8,0,0,0,0,0,0,8]
    block_line17=[8,0,0,0,0,0,8,8,8,8,8,8,8,8,8,8]
    
    
    level_1_layout = [block_line1,block_line2,block_line3,block_line4,block_line5,block_line6,\
                      block_line7,block_line8,block_line9,block_line10,block_line11,block_line12\
                      ,block_line13,block_line14,block_line15,block_line16,block_line17]
    return level_1_layout


level_layout_list = [level_1()]

pixels = pygame.sprite.Group()

def create_level(level_layout_list, level_on):
    global pixel_items
     
    
    level_on_layout = level_layout_list[level_on-1]
    
    line = 0
    
    
    for i in range(len(level_on_layout)):
        pos = 0
        current_line = level_on_layout[line]
        for i in range(len(current_line)):
            pix_type = current_line[pos]
            if pix_type == 0:
                pass
            else:
                if pix_type == 8:
                    pix = Pixel(B_pix)
                    pix.rect.centerx = (pos*64)+32
                    pix.rect.y = (line*64)
                    pix.rect.bottom = (line*64)+64
                    pix.type = "black"
                    pixels.add(pix)
                if pix_type == 1:
                    pix = Pixel(O_pix)
                    pix.rect.centerx = (pos*64)+32
                    pix.rect.y = (line*64)
                    pix.rect.bottom = (line*64)+64
                    pix.type = "orange"
                    pixels.add(pix)
                if pix_type == 3:
                    pix = Pixel(o_pix)
                    pix.rect.centerx = (pos*64)+32
                    pix.rect.y = (line*64)
                    pix.rect.bottom = (line*64)+64
                    pix.type = "dark_orange"
                    pixels.add(pix)

                
                    
                
                
                
                
                
                
            
            
            pos += 1
        line += 1
    
    

            
metronome = 60
beat = 0

sixteenth = int((refresh_rate**2/metronome)/4)
eighth = sixteenth*2
quarter = sixteenth*4
# Make game objects
##pix_num = 0
##pix_line = 0
##pix_type = pix1_img
##pixel_items = []
##for i in range(9):
##    pix_num = 0
##    for i in range(12):
##        pixel_items.append(Pixel(pix_num, pix_line, pix_type))
##        pix_num += 64
##    pix_line += 64

ship = Ship(320, 320, ship_img)
mob1 = Mob(384, 64, ship_img)
enemy1 = enemy(64, -128, ship_img)



level_on = 1
create_level(level_layout_list, level_on)
# Make sprite groups



player = pygame.sprite.Group()
player.add(ship)
arrows = pygame.sprite.Group()
spells1 = pygame.sprite.Group()
spells2 = pygame.sprite.Group()


mobs = pygame.sprite.Group()
mobs.add(mob1)

enemies = pygame.sprite.Group()
enemies.add(enemy1)



bombs = pygame.sprite.Group()
vel_left = False
vel_right = False
vel_up = False
vel_down = False
even_x = False
even_y = False
# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == pygame.K_1:
                pass
##                ship.cast_fire(mouse_pos)

    

    
    

    
    pressed = pygame.key.get_pressed()
    clicked = pygame.mouse.get_pressed()
    
    if not clicked[0]:
        for a in arrows:
            ship.cast_fire(a)
    for a in arrows:
        a.kill()
    if clicked[0]:
        ship.make_arrow(mouse_pos)
    
        
        
    vel_left = False
    vel_right = False
    vel_up = False
    vel_down = False
    even_x = False
    even_y = False
    
    
    if pressed[pygame.K_LEFT]:
        vel_left = True

    if pressed[pygame.K_RIGHT]:
        vel_right = True

    if pressed[pygame.K_UP]:
        vel_up = True

    if pressed[pygame.K_DOWN]:
        vel_down = True


    if vel_left == True and vel_up == vel_down:
        mob1.move_right(ship)
        enemy1.move_right(ship)
        for s in spells1:
            s.move_right(ship)
        for p in pixels:
            p.move_right(ship)
    
    if vel_right == True and vel_up == vel_down:
        mob1.move_left(ship)
        enemy1.move_left(ship)
        for s in spells1:
            s.move_left(ship)
        for p in pixels:
            p.move_left(ship)

    if vel_left == True and vel_up != vel_down:
        mob1.move_right_half(ship)
        enemy1.move_right_half(ship)
        for s in spells1:
            s.move_right_half(ship)
        for p in pixels:
            p.move_right_half(ship)
    
    if vel_right == True and vel_up != vel_down:
        mob1.move_left_half(ship)
        enemy1.move_left_half(ship)
        for s in spells1:
            s.move_left_half(ship)
        for p in pixels:
            p.move_left_half(ship)
    for p in pixels:
        if p.rect.x%(ship.speed) == 0:
            even_x = True
        
    if vel_up != vel_down or even_x == False:
        ship.update_horizontal_half()
    else:
        ship.update_horizontal()       
    
    
        
    if vel_up == True and vel_left ==  vel_right:
        mob1.move_down(ship)
        enemy1.move_down(ship)
        for s in spells1:
            s.move_down(ship)
        for p in pixels:
            p.move_down(ship)
    
    if vel_down == True and vel_left ==  vel_right:
        mob1.move_up(ship)
        enemy1.move_up(ship)
        for s in spells1:
            s.move_up(ship)
        for p in pixels:
            p.move_up(ship)

    if vel_up == True and vel_left !=  vel_right:
        mob1.move_down_half(ship)
        enemy1.move_down_half(ship)
        for s in spells1:
            s.move_down_half(ship)
        for p in pixels:
            p.move_down_half(ship)
    
    if vel_down == True and vel_left !=  vel_right:
        mob1.move_up_half(ship)
        enemy1.move_up_half(ship)
        for s in spells1:
            s.move_up_half(ship)
        for p in pixels:
            p.move_up_half(ship)
    for p in pixels:
        if p.rect.y%(ship.speed) == 0:
            even_y = True


    

    if vel_left != vel_right or even_y == False:
        ship.update_vertical_half()
    else:
        ship.update_vertical()
            
    
    

##    if pressed[pygame.K_LEFT]:
##        ship.move_left()
##    elif pressed[pygame.K_RIGHT]:
##        ship.move_right()

    #wall to player1
        


        
    
    # Game logic (Check for collisions, update points, etc.)
    beat += 1
##    if beat%(int(sixteenth)) == 0:
##        ship.cast_fire()
##    if beat%(int(sixteenth)) == 0:
##        ship.cast_thunder()

##    if beat%(int(quarter*4)) == 0:
##        mobs.add(Mob(500, 64, ship_img))
    ship.update(enemies)
    pixels.update(spells1, mobs)
       
    spells1.update(beat)

    spells2.update()
    mobs.update(spells1, spells2)
    enemies.update(spells1)
    bombs.update()

    for m in mobs:
        m.move(spells1, spells2)
    for enemy in enemies:
        enemy.move(ship)
##        if beat%(int(quarter)) == 0:
##            m.cast_fire()

    

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(GREEN)
    pixels.draw(screen)
    arrows.draw(screen)
    spells1.draw(screen)
    spells2.draw(screen)
    player.draw(screen)
    mobs.draw(screen)
    enemies.draw(screen)
    bombs.draw(screen)
    


    
    # Update screen (Actually draw the picture in the window.)
    mouse_pos = pygame.mouse.get_pos()
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
