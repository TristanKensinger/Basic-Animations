import pygame

class Player:

    #Bool variables
    right = False
    left = False
    facingRight = True
    dead = False
    revive = False
    isJump = False

    #Integer variables
    vel = 5
    jumpCount = 22
    deadCount = 0
    runCount = 0
    idleCount = 0
    jumpPicCount = 0

    #Lists of pictures for animation
    idle = [pygame.image.load("sprites/idle (1).png"),pygame.image.load("sprites/idle (2).png"),pygame.image.load("sprites/idle (3).png"),
        pygame.image.load("sprites/idle (4).png"),pygame.image.load("sprites/idle (5).png"),pygame.image.load("sprites/idle (6).png"),
        pygame.image.load("sprites/idle (7).png"),pygame.image.load("sprites/idle (8).png"),pygame.image.load("sprites/idle (9).png"),
        pygame.image.load("sprites/idle (10).png")]
    running = [pygame.image.load("sprites/run (1).png"),pygame.image.load("sprites/run (2).png"),pygame.image.load("sprites/run (3).png"),
        pygame.image.load("sprites/run (4).png"),pygame.image.load("sprites/run (5).png"),pygame.image.load("sprites/run (6).png"),
        pygame.image.load("sprites/run (7).png"),pygame.image.load("sprites/run (8).png")]
    jumping = [pygame.image.load("sprites/jump (1).png"),pygame.image.load("sprites/jump (2).png"),pygame.image.load("sprites/jump (3).png"),
        pygame.image.load("sprites/jump (4).png"),pygame.image.load("sprites/jump (5).png"),pygame.image.load("sprites/jump (6).png"),
        pygame.image.load("sprites/jump (7).png"),pygame.image.load("sprites/jump (8).png"),pygame.image.load("sprites/jump (9).png"),
        pygame.image.load("sprites/jump (10).png")]
    deadPics = [pygame.image.load("sprites/dead (1).png"),pygame.image.load("sprites/dead (2).png"),pygame.image.load("sprites/dead (3).png"),
        pygame.image.load("sprites/dead (4).png"),pygame.image.load("sprites/dead (5).png"),pygame.image.load("sprites/dead (6).png"),
        pygame.image.load("sprites/dead (7).png"),pygame.image.load("sprites/dead (8).png"),pygame.image.load("sprites/dead (9).png"),
        pygame.image.load("sprites/dead (10).png")]

    #Player init
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    #Draws the player to the window
    def draw(self, win):
        if self.dead or self.revive:
            if not self.facingRight:
                win.blit(pygame.transform.flip(pygame.transform.scale(self.deadPics[self.deadCount//5], (self.w, self.h)), True, False), (self.x, self.y))
            else:
                win.blit(pygame.transform.scale(self.deadPics[self.deadCount//5], (self.w, self.h)), (self.x, self.y))
        elif not self.right and not self.left and not self.isJump:
            if not self.facingRight:
                win.blit(pygame.transform.flip(pygame.transform.scale(self.idle[self.idleCount//3], (self.w, self.h)), True, False), (self.x, self.y))
            else:
                win.blit(pygame.transform.scale(self.idle[self.idleCount//3], (self.w, self.h)), (self.x, self.y))
        elif not self.isJump:
            if not self.facingRight:
                win.blit(pygame.transform.flip(pygame.transform.scale(self.running[self.runCount//5], (self.w, self.h)), True, False), (self.x, self.y))
            else:
                win.blit(pygame.transform.scale(self.running[self.runCount//5], (self.w, self.h)), (self.x, self.y))
        else:
            if not self.facingRight:
                win.blit(pygame.transform.flip(pygame.transform.scale(self.jumping[self.jumpPicCount//5], (self.w, self.h)), True, False), (self.x, self.y))
            else:
                win.blit(pygame.transform.scale(self.jumping[self.jumpPicCount//5], (self.w, self.h)), (self.x, self.y))
    
    #Updates the player with key inputs
    def update(self, win, keys):
        #Player is alive code
        if not self.dead:
            if keys[pygame.K_d]:
                self.dead = True
            if keys[pygame.K_LEFT] and self.x > 0:
                self.facingRight = False
                self.left = True
                self.right = False
                self.x -= self.vel
                if self.runCount < 35:
                    self.runCount += 1
                else:
                    self.runCount = 0
            elif keys[pygame.K_RIGHT] and self.x < win.get_width()-self.w:
                self.facingRight = True
                self.right = True
                self.left = False
                self.x += self.vel
                if self.runCount < 35:
                    self.runCount += 1
                else:
                    self.runCount = 0
            else:
                self.left = False
                self.right = False
                if self.idleCount < 27:
                    self.idleCount += 1
                else:
                    self.idleCount = 0
            
            if self.isJump == False:
                self.jumpPicCount = 0
                if keys[pygame.K_SPACE]:
                    self.isJump = True
        else: #player is dead
            if self.deadCount < 45 and not self.revive:
                self.deadCount += 1
            elif keys[pygame.K_r]:
                self.revive = True

        #Revive code   
        if self.revive:
            if self.deadCount > 0:
                self.deadCount -= 1
            else:
                self.dead = False
                self.revive = False
            
        #Falling code
        if self.isJump:
            if self.jumpPicCount < 45:
                self.jumpPicCount += 1
            else:
                self.jumpPicCount = 0
            if self.jumpCount>= -22:
                self.y -= self.jumpCount
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 22
    


    