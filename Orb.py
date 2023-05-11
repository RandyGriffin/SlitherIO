import pygame


class Orb:
    def __init__(self, x, y, r,filePath):
        self.rect = pygame.Rect(x, y, r, r)  # hitbox
        image = pygame.image.load(filePath)
        self.texture = pygame.transform.scale(image, (r, r))
        self.velocity = [-1,1]    #moves the vectors


    def update(self,player):
        self.rect.x += self.velocity[0]  #allows the player to move
        self.rect.y += self.velocity[1]

        if self.rect.colliderect(player.rect): #if orb is touching player orb, orb will disappear
            player.score += 5
            return True
        return False

    def render(self, window):
        window.blit(self.texture, (self.rect.x, self.rect.y))