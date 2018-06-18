import pygame
from alien_invasion.game_sprite import GameSprite

_alien_image = "alien_invasion/images/alien.png"


class Alien(GameSprite):
    """ A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """ Initialize the alien and set it's starting position. """
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set it's rect attribute.
        self.image = pygame.image.load(_alien_image)
        self.rect = self.image.get_rect()

        # Starting each new alien at the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's exact position.
        self.rect.x = float(self.rect.x)

    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self):
        """ Draw the alien at it's current location. """
        self.screen.blit(self.image, self.rect)
