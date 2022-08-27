#import modules
import pygame as pg
import sys

pg.mixer.init()

#load all sprites
csprite = pg.image.load(r"C:\Beniam\CS Excercises\Projects\Virtual Piano\C sprite.png")
c_sprite = pg.image.load(r"C:\Beniam\CS Excercises\Projects\Virtual Piano\C # sprite.png")
dsprite = pg.image.load(r"C:\Beniam\CS Excercises\Projects\Virtual Piano\D sprite.png")
esprite = pg.image.load(r"C:\Beniam\CS Excercises\Projects\Virtual Piano\E sprite.png")
fsprite = pg.image.load(r"C:\Beniam\CS Excercises\Projects\Virtual Piano\F sprite.png")

#load in sound
middleC = pg.mixer.Sound("MiddleC.wav")
middleC_ = pg.mixer.Sound("MiddleC#.wav")
middleD = pg.mixer.Sound("MiddleD.wav")
middleE = pg.mixer.Sound("MiddleE.wav")
middleE_ = pg.mixer.Sound("MiddleEflat.wav")
middleF = pg.mixer.Sound("MiddleF.wav")
middleF_ = pg.mixer.Sound("MiddleF#.wav")
middleG = pg.mixer.Sound("MiddleG.wav")
middleA = pg.mixer.Sound("MiddleA.wav")
middleA_ = pg.mixer.Sound("MiddleAflat.wav")
middleB = pg.mixer.Sound("MiddleB.wav")
middleB_ = pg.mixer.Sound("MiddleBflat.wav")

#color parameters
white = (255, 255, 255)
black = (0, 0, 0)
teal = (205, 209, 228)

#define main function
def main():
    running = True
    
    screen = pg.display.set_mode([750, 500])
    screen.fill(teal)
    
    #set initial positions for piano keys
    initial_x = int(screen.get_height())/3
    initial_y = int(screen.get_width())/10
    key_factor = (14*3)
    
    while running:
        
        #load in piano keys
        c = screen.blit(csprite, (initial_x, initial_y))
        c_ = screen.blit(c_sprite, (initial_x + key_factor - 2, initial_y - key_factor))
        d = screen.blit(dsprite, (initial_x + key_factor * (3/2) - 8, initial_y - 3))
        e_ = screen.blit(c_sprite, (initial_x + key_factor * (5/2) - 10 , initial_y - key_factor - 2))
        e = screen.blit(esprite, (initial_x + (3*key_factor) - 1, initial_y - 3))
        f = screen.blit(fsprite, (initial_x + ((9/2)*key_factor) - 10, initial_y - 2.5))
        f_ = screen.blit(c_sprite, (initial_x + (5*key_factor) - 4, initial_y - key_factor - 2))
        g = screen.blit(dsprite, (initial_x + ((11/2)*key_factor) - 9, initial_y - 4))
        a_ = screen.blit(c_sprite, (initial_x + ((13/2)*key_factor) - 11, initial_y - key_factor - 2))
        a = screen.blit(dsprite, (initial_x + (7*key_factor) - 16, initial_y - 4))
        b_ = screen.blit(c_sprite, (initial_x + ((15/2)*key_factor) + 3, initial_y - key_factor - 2))
        b = screen.blit(esprite, (initial_x + ((17/2)*key_factor) - 10, initial_y - 4))
        
        #pygame exit button
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        #collision detection
        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            
            #playing notes in the event of collision detection
            if c.collidepoint(x, y):
                for i in range(1):
                    pg.mixer.Sound.play(middleC)
            if c_. collidepoint(x, y):
                for i in range(1):
                    pg.mixer.Sound.play(middleC_)
            if d.collidepoint(x, y):
                for i in range(1):
                    pg.mixer.Sound.play(middleD)
            if e.collidepoint(x, y):
                for i in range(1):
                    pg.mixer.Sound.play(middleE)
            if e_.collidepoint(x, y):
                for i in range(1):
                    pg.mixer.Sound.play(middleE_)
            if f.collidepoint(x, y):
                for i in range(1):
                    pg.mixer.Sound.play(middleF)
            if f_.collidepoint(x, y):
                for i in range(1):
                    pg.mixer.Sound.play(middleF_)
            if g.collidepoint(x, y):
                for i in range(1):
                    pg.mixer.Sound.play(middleG)
            if a_.collidepoint(x, y):
                for i in range(1):
                    pg.mixer.Sound.play(middleA_)
            if a.collidepoint(x, y):
                for i in range(1):
                    pg.mixer.Sound.play(middleA)
            if b_.collidepoint(x, y):
                for i in range(1):
                    pg.mixer.Sound.play(middleB_)
            if b.collidepoint(x, y):
                for i in range(1):
                    pg.mixer.Sound.play(middleB)
        
        pg.time.wait(70)        
        pg.display.flip()

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()