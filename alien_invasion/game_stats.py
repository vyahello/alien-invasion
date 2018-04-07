from abc import ABC, ABCMeta, abstractmethod

_score_path = 'alien_invasion/stats/high_score.txt'


class Stats(ABC):
    """Represent abstraction for stats."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def reset_stats(self):
        pass


class GameStats(Stats):
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start Alien Invasion in an inactive state.
        self.game_active = False

        with open(_score_path) as high_score_file:
            self.high_score = int(high_score_file.read())

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
