import pygame

class Player:
    def __init__(self, x,y,w,h):
        self.rect = pygame.Rect(x,y,w,h) #hitbox
        image = pygame.image.load("red_orb.png")

        self.texture = pygame.transform.scale(image, (w,h))
        self.speed = 10
        self.score = 0


    def update(self):
        print(self.score)
        keys = pygame.key.get_pressed() #returns pygame's dictionary

        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

    def render(self, window):
        window.blit(self.texture, (self.rect.x,self.rect.y))