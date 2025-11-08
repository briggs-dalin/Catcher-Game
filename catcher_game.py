import arcade
import random

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Catcher Game"

PLAYER_SPEED = 7.33333


class CatcherGame(arcade.Window):
    """Main game class."""

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player = None
        self.player_list = None
        self.falling_objects_list = arcade.SpriteList()
        self.score = 0  # Score variable
        self.lives = 5  # Lives variable

        # Difficulty scaling variables
        self.fall_speed = -5.5  # Starting fall speed
        self.speed_increase_interval = 15  # Every 15 seconds, speed increases

    def setup(self):
        """Set up the game and initialize variables."""
        # Create a sprite list for the player
        self.player_list = arcade.SpriteList()

        # Create the player sprite
        self.player = arcade.SpriteSolidColor(
            80,  # Width
            30,  # Height
            SCREEN_WIDTH // 2,  # Center X
            50,  # Center Y
            (0, 255, 255, 255)  # Teal color
        )
        self.player_list.append(self.player)

        # Schedule falling object spawns
        arcade.schedule(self.spawn_falling_object, 1.33)  # Spawn every 1.33 seconds

        # Schedule difficulty increase every 15 seconds
        arcade.schedule(self.increase_difficulty, self.speed_increase_interval)

    def on_draw(self):
        """Render the screen."""
        self.clear()
        self.player_list.draw()
        self.falling_objects_list.draw()

        # Draw instructions, score, and lives
        arcade.draw_text("Move with arrow keys!", 280, 570, arcade.color.WHITE, 16)
        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 16)
        arcade.draw_text(f"Lives: {self.lives}", SCREEN_WIDTH - 120, SCREEN_HEIGHT - 30, arcade.color.RED, 16)

    def on_update(self, delta_time):
        """Logic that updates every frame."""
        # Move the player
        self.player_list.update()

        # Keep player on screen
        if self.player.left < 0:
            self.player.left = 0
        if self.player.right > SCREEN_WIDTH:
            self.player.right = SCREEN_WIDTH

        # Update falling objects
        self.falling_objects_list.update()

        # Check for collisions
        collisions = arcade.check_for_collision_with_list(self.player, self.falling_objects_list)
        for obj in collisions:
            obj.remove_from_sprite_lists()
            self.score += 1  # Increase score when caught

        # Remove objects that fall off the bottom and decrease lives
        for obj in self.falling_objects_list:
            if obj.bottom < 0:
                obj.remove_from_sprite_lists()
                self.lives -= 1  # Lose 1 life per missed object

                if self.lives <= 0:
                    print(f"Game Over! Final Score: {self.score}")
                    arcade.close_window()

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

    def spawn_falling_object(self, delta_time: float):
        """Create a new falling object at a random x-position at the top of the screen."""
        width = random.randint(15, 30)
        height = random.randint(15, 30)
        color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255),
            255
        )  # Random bright color
        x = random.randint(width // 2, SCREEN_WIDTH - width // 2)
        y = SCREEN_HEIGHT + height // 2  # Start just above the screen

        obj = arcade.SpriteSolidColor(width, height, x, y, color)
        obj.change_y = self.fall_speed  # Use the current falling speed
        self.falling_objects_list.append(obj)

    def increase_difficulty(self, delta_time: float):
        """Make the game slightly harder by increasing fall speed."""
        self.fall_speed -= 0.3  # Increase fall speed (more negative = faster)
        # Prevent speed from becoming too fast
        self.fall_speed = max(self.fall_speed, -12)
        print(f"Difficulty increased! New fall speed: {self.fall_speed}")


def main():
    window = CatcherGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
