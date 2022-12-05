from .game import Battleship, Runnable


class BattleshipConsole(Runnable):
    def run(self):
        game = Battleship()

        print("Welcome to Battleship 🛥️")

        while True:
            if game.finished:
                print("You just won the game 🎉")
                break

            command = input("Coordinates to shoot (eg: A5) >> ")
            command = command.strip()
            command = command.upper()

            if command == "":
                continue

            elif command == "HELP":
                print(f"{'HELP'.rjust(10, ' ')} - Prints the current message")
                print(f"{'EXIT'.rjust(10, ' ')} - Quits the current game")
                print(
                    f"{'DESTROY'.rjust(10, ' ')} - Destroys the current game by shooting all the vessels"
                )
                print(
                    f"{'PRINT'.rjust(10, ' ')} - Prints the current state of the game to console"
                )
                print(
                    f"{'EMOJI'.rjust(10, ' ')} - Prints the emoji version of the state"
                )
                print(
                    f"{'[X][Y]'.rjust(10, ' ')} - Shoots the target coordinate (eg: A5)"
                )

            elif command == "EXIT":
                print("Bye, bye 👋")
                break

            elif command == "DESTROY":
                print("Armageddon is here 💣")
                game.destroy()

            elif command == "PRINT":
                print(game)

            elif command == "EMOJI":
                print(game._buffer(emoji=True))

            else:
                try:
                    position = game.shoot(command)
                except Exception as exception:
                    print(exception)
                else:
                    print(f"You shot '{position}' {position.emoji}")
