import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Catcher Game - Step 1: Game Window"

class CatcherGame(arcade.Window):
    """Main application class."""

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        """Render the screen."""
        self.clear()  # Clears the window (replaces start_render)
        arcade.draw_text("Welcome to Catcher Game!", 200, 300,
                     arcade.color.BLACK, font_size=24, bold=True)

def main():
    """Main function"""
    window = CatcherGame()
    arcade.run()

if __name__ == "__main__":
    main()
