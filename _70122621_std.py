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

player = Player(0, 0)
treasure = Treasure(5, 5)

while True:
    direction = input("Which direction would you like to move? ")
    player.direct(direction)
    if treasure.hunt(player):
        print("Congratulations, you found the treasure!")
        break