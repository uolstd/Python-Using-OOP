class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def direct(self, direction):
        if direction == 'up':
            self.y += 1
        elif direction == 'down':
            self.y -= 1
        elif direction == 'left':
            self.x -= 1
        elif direction == 'right':
            self.x += 1
        else:
            print("Invalid direction!")
        print(f"Player is now at ({self.x}, {self.y})")

class Treasure(Player):
    def __init__(self, x, y):
        super().__init__(x, y)

    def hunt(self, player):
        if self.x == player.x and self.y == player.y:
            return True
        return False

class Game(Treasure):
    def __init__(self, player_x, player_y, treasure_x, treasure_y):
        self.player = Player(player_x, player_y)
        self.treasure = Treasure(treasure_x, treasure_y)

    def start(self):
        while True:
            direction = input("Which direction would you like to move? ")
            self.player.direct(direction)
            if self.treasure.hunt(self.player):
                print("Congratulations, you found the treasure!")
                break

# Initialize game with player and treasure coordinates
game = Game(0, 0, 5, 5)
game.start()
