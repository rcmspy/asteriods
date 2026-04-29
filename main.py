import pygame
import sys
from player import Player
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state, log_event
from asteroidfield import AsteroidField
from asteroid import Asteroid
from circleshape import CircleShape 
from shot import Shot


       
def main():
    pygame.init()
    clock = pygame.time.Clock()
  
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")  

       
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField() 
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
  


    while True:
        
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        for obj in asteroids:
             if obj.collides_with(player):
                print("Game over!")
                log_event("player_hit")
                sys.exit()
             for shot in shots:
                if shot.collides_with(obj):        
                   log_event("asteroid_shot")
                   shot.kill() 
                   obj.split()
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
      
        pygame.display.flip()

        dt = clock.tick(60)/(1000)
    
       
if __name__ == "__main__":
        main()
