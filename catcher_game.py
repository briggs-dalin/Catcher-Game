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
        self.score = 0
        self.lives = 5
        self.game_over = False

        # Level system
        self.level = 1
        self.points_per_level = 10  # Level up every 10 points
        self.fall_speed = -5.5  # Base falling speed

    def setup(self):
        """Set up the game and initialize variables."""
        self.score = 0
        self.lives = 5
        self.game_over = False
        self.level = 1
        self.fall_speed = -5.5

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.falling_objects_list = arcade.SpriteList()

        # Player sprite
        self.player = arcade.SpriteSolidColor(
            80, 30, SCREEN_WIDTH // 2, 50, (0, 255, 255, 255)
        )
        self.player_list.append(self.player)

        # Schedule falling objects
        arcade.unschedule(self.spawn_falling_object)
        arcade.schedule(self.spawn_falling_object, 1.33)

    def on_draw(self):
        """Render the screen."""
        self.clear()
        self.player_list.draw()
        self.falling_objects_list.draw()

        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 16)
        arcade.draw_text(f"Lives: {self.lives}", SCREEN_WIDTH - 120, SCREEN_HEIGHT - 30, arcade.color.RED, 16)
        arcade.draw_text(f"Level: {self.level}", SCREEN_WIDTH//2 - 40, SCREEN_HEIGHT - 30, arcade.color.YELLOW, 16)

    def on_update(self, delta_time):
        """Logic that updates every frame."""
        if self.game_over:
            return

        self.player_list.update()
        self.falling_objects_list.update()

        # Keep player on screen
        if self.player.left < 0:
            self.player.left = 0
        if self.player.right > SCREEN_WIDTH:
            self.player.right = SCREEN_WIDTH

        # Check collisions
        collisions = arcade.check_for_collision_with_list(self.player, self.falling_objects_list)
        for obj in collisions:
            obj.remove_from_sprite_lists()
            if getattr(obj, "is_bad", False):
                self.lives -= 1
            else:
                self.score += 1

        # Remove objects that fall off the bottom
        for obj in self.falling_objects_list:
            if obj.bottom < 0:
                obj.remove_from_sprite_lists()
                if not getattr(obj, "is_bad", False):
                    self.lives -= 1

        # Level up based on score
        new_level = self.score // self.points_per_level + 1
        if new_level > self.level:
            self.level = new_level
            self.fall_speed = -5.5 - (self.level - 1)  # Increase fall speed per level
            print(f"Level Up! Now at level {self.level}, fall speed: {self.fall_speed}")

        # End game if no lives
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
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0

    def spawn_falling_object(self, delta_time: float):
        """Create a new falling object with a type (good or bad)."""
        width = random.randint(15, 30)
        height = random.randint(15, 30)

        # Chance of bad object increases slightly with level (max 60%)
        is_bad = random.random() < min(0.25 + 0.05*(self.level - 1), 0.6)

        if is_bad:
            color = (255, 60, 60, 255)  # Red = bad
        else:
            color = (
                random.randint(50, 255),
                random.randint(50, 255),
                random.randint(50, 255),
                255
            )

        x = random.randint(width // 2, SCREEN_WIDTH - width // 2)
        y = SCREEN_HEIGHT + height // 2

        obj = arcade.SpriteSolidColor(width, height, x, y, color)
        obj.change_y = self.fall_speed * (1.3 if is_bad else 1)
        obj.is_bad = is_bad

        self.falling_objects_list.append(obj)


def main():
    window = CatcherGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()