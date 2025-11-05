import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Catcher Game"

PLAYER_SPEED = 5


class CatcherGame(arcade.Window):
    """Main game class."""

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player = None
        self.player_list = None
        self.player_texture = None

    def setup(self):
        """Set up the game and initialize variables."""
        # Create a sprite list for the player
        self.player_list = arcade.SpriteList()

        # Create the player sprite
        self.player = arcade.SpriteSolidColor(80, #Width
                                              30, #Height
                                              0, #Center X
                                              0, #Center Y    
                                              (0, 255, 255, 255) ) # Color Teal
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = 50  
        self.player_list.append(self.player)

    def on_draw(self):
        """Render the screen."""
        self.clear()
        self.player_list.draw()
        arcade.draw_text("Move with arrow keys!", 280, 570, arcade.color.BLACK, 16)

    def on_update(self, delta_time):
        """Logic that updates every frame."""
        # Move the player
        self.player_list.update()
        # Keep player on screen
        if self.player.left < 0:
            self.player.left = 0
        if self.player.right > SCREEN_WIDTH:
            self.player.right = SCREEN_WIDTH

    def on_key_press(self, key, modifiers):
        """Called when a key is pressed."""
        if key == arcade.key.LEFT:
            self.player.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        """Called when a key is released."""
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0


def main():
    window = CatcherGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
