from .game import SHIPS, Battleship, Runnable


class BattleshipConsole(Runnable):
    def run(self):
        game = Battleship()

        print("Welcome to Battleship 🛥️")
        print("You can use the HELP command to obtain help")

        while True:
            if game.finished:
                print(game.repr(emoji=True))
                print("You just won the game, congratulations 🎉")
                break

            command = input(">> ")
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
                print(game.repr(emoji=True))

            else:
                try:
                    result, position = game.shoot(command)
                except Exception as exception:
                    print(exception)
                else:
                    if position.kind in SHIPS:
                        print(f"{position.kind.emoji} You {result} a {position.kind}")
                    else:
                        print(f"{position.kind.emoji} You {result} ({position.kind})")
