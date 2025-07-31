import random

class Battleship:
    # ship sizes can be adjusted here
    SHIP_SIZES = [1, 2, 3]

    @staticmethod
    def main():
        # opening message
        print("Welcome to Battleship. Wanna play a game?")
        print("You’ll be guessing positions on a straight line board.")
        print("Each ship takes up 1 to 3 spaces. Try to sink all of them before you run out of attempts.")
        print("~ = untouched, X = hit, - = miss\n")

        # main game loop – gives the user the option to replay
        while True:
            Battleship.play_game()
            again = input("\nDo you want to play again? (yes/no): ").lower()
            if again != 'yes':
                print("Cool, thanks for playing.")
                break

    @staticmethod
    def play_game():
        # get board size and number of allowed attempts from the user
        try:
            board_size = int(input("Enter the size of the board (e.g., 20): "))
            max_attempts = int(input("Enter the number of allowed attempts (e.g., 10): "))
        except ValueError:
            print("You gotta enter a number for both. Restart the game.")
            return

        # create the board using ~ to show untouched positions
        board = ['~'] * board_size

        # set up the ships (original stays intact, remaining gets updated as hits happen)
        ships_original = Battleship.place_ships(board_size)
        ships_remaining = [list(ship) for ship in ships_original]

        # tracking guesses, hits, and attempts
        guesses = set()
        hits = 0
        attempts = 0
        total_targets = sum(len(ship) for ship in ships_remaining)

        print("Board: " + " ".join(board))

        # main guessing loop
        while hits < total_targets and attempts < max_attempts:
            try:
                guess = int(input(f"Enter a position to guess (0 to {board_size - 1}): "))
            except ValueError:
                print("That wasn't a number. Try again.")
                continue

            if guess < 0 or guess >= board_size:
                print("Out of range. Pick a number that’s on the board.")
                continue

            if guess in guesses:
                print("You already guessed that spot.")
                continue

            guesses.add(guess)
            attempts += 1

            if Battleship.check_hit(guess, ships_remaining):
                hits += 1
                board[guess] = 'X'
                print("Hit!")

                if Battleship.just_sank_ship(ships_remaining):
                    print("You've sunk a ship!")
            else:
                board[guess] = '-'
                print("Miss!")

            print("Board: " + " ".join(board))

        # end of game messages
        if hits == total_targets:
            print("Congratulations! You've sunk all ships!")
        else:
            print("You’re out of attempts. Game over.")

        # show where the ships actually were
        print(f"Original ship positions: {ships_original}")

    @staticmethod
    def place_ships(board_size):
        ships = []
        taken = set()

        for size in Battleship.SHIP_SIZES:
            placed = False
            while not placed:
                start = random.randint(0, board_size - size)
                ship = list(range(start, start + size))

                # add buffer zone around each ship so they don’t touch
                buffer = set(range(start - 1, start + size + 1))
                if buffer & taken:
                    continue

                ships.append(ship)
                taken.update(ship)
                placed = True

        return ships

    @staticmethod
    def check_hit(guess, ships_remaining):
        # check if guess is in any of the ships
        for ship in ships_remaining:
            if guess in ship:
                ship.remove(guess)  # mark that hit by removing it from the ship
                return True
        return False

    @staticmethod
    def just_sank_ship(ships_remaining):
        # check if any ship was just fully hit
        for ship in ships_remaining:
            if len(ship) == 0:
                ships_remaining.remove(ship)
                return True
        return False


# entry point to run the game
if __name__ == "__main__":
    Battleship.main()
