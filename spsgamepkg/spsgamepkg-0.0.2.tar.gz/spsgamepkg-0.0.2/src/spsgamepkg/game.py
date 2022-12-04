import random
import time
__version__ = '0.0.1'
__author__ = 'Aswin Venkat'

def rules():
        """
        Prints the rules for the game
        """
        
        print("""

    Rules and winner decision for stone, paper, scissors

            stone vs paper       : Paper wins
            stone vs scisors     : Stone wins
            paper vs scissors    : Scissor wins

        """)

class Game:
    def __init__(self,player_name:str):
        """
        Rock Paper Scissors - a basic program to play rock,paper,scissors with PC
        ==========================================================================
        This is a fun Python package to play rock paper scissors with PC.   
        """
        self.player_name=player_name
        self.list_=['stone','paper','scissors']
        self.my_score=0
        self.pc_score=0
        
    def condition(self,pc:str,player:str):
        """
        PARAMETERS:
        ===========
        pc      : str type ['stone' or 'paper' or 'scissors']
        player  : str type ['stone' or 'paper' or 'scissors']
        """
        assert player=='stone' or player=='paper' or player=='scissors', "player should be 'stone' or 'paper' or 'scissors'"
        assert pc=='stone' or pc=='paper' or pc=='scissors', "pc should be 'stone' or 'paper' or 'scissors'"
        if(pc==player):
                print("DRAW")

        else:
            if(player=="stone"):
                if(pc=="paper"):
                    print("PC wins this round")
                    self.pc_score+=1
                else:
                    print("You win this round")
                    self.my_score+=1

            if(player=="paper"):
                if(pc=="scissors"):
                    print("PC wins this round")
                    self.pc_score+=1
                else:
                    print("You win this round")
                    self.my_score+=1

            if(player=="scissors"):
                if(pc=="stone"):
                    print("PC wins this round")
                    self.pc_score+=1
                else:
                    print("You win this round")
                    self.my_score+=1
        
    def display_result(self):

        """
        To display the RESULT of the game
        """

        print(' SCOREBOARD '.center(25, ':'))
        print("YOU: \t",self.my_score,"\nPC: \t",self.pc_score)
        print(":"*25)

        if(self.my_score>self.pc_score):
            print(
                """

{} WINS THE GAME!!!
                
                """.format(self.player_name)
            )

        elif(self.my_score<self.pc_score):
            print(
                """

Sorry {}, PC WINS THE GAME!!!

                """.format(self.player_name)
            )

        else:
            print("{}!! Scores Level, its a DRAW".format(self.player_name))
            choice=input("Do you want the tie-breaker? y/n : ")
            assert choice=='y' or choice=='n',"Choice should be either 'y' or 'n'"
            if(choice=='y'):
                self.game(1)
                self.display_result()
            else:
                pass

    def game(self,count:int):
        """
        Parameters:
        ===========
        count : int type
            Enter how many times you want to compete with PC
        """
        print("""
        """)
        if(self.my_score==0 and self.pc_score==0):
            print("\nHELLO {},".format(self.player_name))
            time.sleep(1)
            print("You are about to start the game")
            time.sleep(1)
            print("Good luck!")
            time.sleep(1)
            print("Remember the list below to enter your input")

        self.n=count
        print("""
            1. stone
            2. paper
            3. scissors
            """)

        for _ in range(self.n):
            player_choice=int(input("\nEnter your choice : "))
            assert 0 < player_choice < 4,"Choice should be 1 or 2 or 3"
            
            player=self.list_[player_choice-1]
            pc=random.choice(self.list_)

            print("\nYour input is :",player)
            time.sleep(0.5)
            print("pc input is :",pc)
            time.sleep(0.5)
            print()
            self.condition(pc,player)
                
        print(' GAME OVER '.center(25,':'))
        print('To know you results, use display_results() method')
        print('To reset the score, use clear_score() method')
            
    def clear_score(self):
        """
        Used to clear the score
        """
        self.my_score=0
        self.pc_score=0