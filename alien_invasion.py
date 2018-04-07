import pygame
from pygame.sprite import Group
from alien_invasion import game_functions
from alien_invasion.settings import GameSettings
from alien_invasion.ship import Ship
from alien_invasion.game_stats import GameStats
from alien_invasion.buttons import GameButton
from alien_invasion.scoreboards import GameScoreboard


def _run_game():
    """ Main module to run the game."""

    # Initialize pygame, Settings and screen objects
    pygame.init()
    ai_settings = GameSettings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = GameScoreboard(ai_settings, screen, stats)

    # Make the Play button.
    play_button = GameButton(screen, "Play")

    # Make a ship, group of bullets and group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create a fleet of aliens.
    game_functions.create_fleet(ai_settings, screen, ship, aliens)

    # Starting main loop for the game
    while True:

        game_functions.check_events(ai_settings, screen, stats, sb, play_button, ship,
                                    aliens, bullets)

        if stats.game_active:
            bullets.update()
            game_functions.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                                          bullets)
            game_functions.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                                         bullets)
            ship.update()

        game_functions.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                                     play_button)


if __name__ == '__main__':
    _run_game()
