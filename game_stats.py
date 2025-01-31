class GameStats():
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialise statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion in an active state
        self.game_active = True

    def reset_stats(self):
        """Initialise statistics that can chnageduring the game."""
        self.ships_left = self.ai_settings.ship_limit