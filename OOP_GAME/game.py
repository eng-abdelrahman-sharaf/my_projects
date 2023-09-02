from gru import Gru
from vector import Vector
from villain import Villain
import time # time sleep
import random #randint

class Game:
    """this is the whole game that manupulates characters, animations, ..etc
    
    to run the game you must use Game_obj.game_loop()
    """
    def __init__(self) -> None:
        self.round = 1
        self.players = []
        self.current_player:Villain
        self.other_player:Villain
    
    def get_player(self, villain : Villain) -> None:
        villain.game_world = self   
        self.players.append(villain)
    
    def ask_for_shield(self,player :Villain):
        
        # the defense player
        self.changing_current_player()
        while True:
            player_shields : dict = player.shields
            key = self.dict_to_table( player_shields, True , "computer says : please choose a shield\n" ,  True)

            if key :
                save_value = player.shield(key)[0]
                
                # there is an lack in resources or energy 
                if  not save_value:
                    # to print the error message 
                    self.print_data()
                    print (f"\033[31mcomputer says : {player.shield(key)[1]}\n\033[0m")
                    continue
                # this means that the player  has no errors
                else:
                    return save_value
            # that means that the user chose None
            else :
                return 0
    
    def ask_for_attacks(self, player : Villain):
            
        while True :
            player_weapons : dict = player.weapons
            key = self.dict_to_table( player_weapons, True , "computer says : please choose a weapon\n" , True )

            # here the key is none
            if not key : return 
            

            # there is an lack in resources or energy
            if  not player.attack(key ,  self.other_player ) [0] : 
                # printing error message
                self.print_data()
                print (f"\033[31mcomputer says : {player.attack(key , self.other_player) [1]}\033[0m")
            
            else :
                break

        
            
    def dict_to_table(self , dict_ :dict , return_the_key:bool = False , prompt:str = None , add_none:bool=False):
        """
        Description
        --------------
        convert a dictionary to a table with the ability of taking a input of the key you want to choose

        cautions
        --------------
        the user must input an int value and

        Parameter
        --------------
            * `dict_` : the dictionary to convert 
            * `return_the_key` : if you want to get the key and make the user select it  
            * `add_none` : to add none to the elements of the table
            * `prompt` : the string you want to write when taking the input


        Return
        --------------
        none if `return_the_key` =  False

        the key if `return_the_key` =  True
        """
        
        counter = 1 
        for i in dict_:
            print(f"{counter}. {i}")
            counter+=1
        if add_none:
            print(f"{counter}. None")
        # to make additional space
        print()
        if return_the_key == True:
            while True:
                try :
                    option = int(input(prompt))

                    if (option >= 1 and option < counter) or (option == counter and add_none):
                        break
                    else:
                        raise ValueError(f"print a number from 1 to {counter - 1 + add_none * 1}")
                except ValueError as vr:
                    print(vr)
                    continue
                except:
                    continue
            try:
                return list(dict_.keys())[option-1]
            # this means that the user chose none 
            except:
                return None

    def check_no_victims(self):
        """ checks there are no players with 0 health or 0 energy in both cases he is dead :P """
        return all([i.is_alive for i in self.players]) 

    # waiting animation
    def wait(self , duration , text = "waiting :")-> None:
        """ 
        Description
        --------------
        making a simple waiting animation 

        Parameter
        --------------
            * `duration` : number of seconds to wait
            * `text` : string you want to be printed in waiting 

        Return
        --------------
        None
        """
        start = time.time()
        duration = duration
        
        print(text  , end='')
        
        while True:
            for i in "-\|/":
                print(f"\b{i}" , end = "" , flush=True)
                if time.time() >= (duration + start):
                    print("")
                    return
                time.sleep(.15)

    def changing_current_player(self , with_animation :bool= True) -> None:
        """ 
        Description
        --------------
        switches between current and other player and add animation if required

        it also increment the round variable after the two players take their turns

        Parameter
        --------------
            * `with_animation` 

        Return
        --------------
        None
        """
        # as to current player state
        self.other_player = self.current_player
        self.current_player = self.players[1 - self.players.index(self.current_player)]
        if with_animation :
            self.wait(1 , f"changing to player {self.current_player.name} :")
            self.print_data()
        # round increase by only when the two players play their turns 
        # so in print_data we print int(round) 
        self.round+=0.5 

    def choose_attack_or_shield(self):
        while True:
            try:
                option = int(input(f"\ncomputer to {self.current_player.name} : choose to \n\n1. attack\n2. shield\n"))
                assert option in [1,2]
                return option
            except:
                continue
        

    def print_data(self):
        """ 
        gives you information like health energy and current player and round number
        on top of the screen
        """
        print("\033[2J\033[H", end='')
        print("\033[31mGRU vs VECTOR\033[0m".center(60))
        print(f"round {int(self.round)}".center(54))
        print("\033[32m> current player {} \"{}\" heal : {} energy : {}\033[0m".format( self.current_player._type, self.current_player.name , self.current_player.health, self.current_player.energy))
        print("the other player {} \"{}\" heal : {} energy : {}\n".format(self.other_player._type , self.other_player.name , self.other_player.health, self.other_player.energy))

    def game_loop(self) -> None:

        """main game loop that runs the hole game"""
        
        self.players.append(Gru(input("enter GRU player name\n") , self))
        self.players.append(Vector(input("enter VECTOR player name\n") , self))
        self.wait(2)

        # make random first player
        self.current_player = self.players[random.randint(0 , 1)]
        self.changing_current_player(with_animation=False)

        
        # printing data
        self.print_data()
        while True:
            if self.check_no_victims():
                pass
            else:
                print("Game Over")
                if self.current_player.is_alive:
                    print(f"{self.current_player.name} wins")
                else:
                    print(f"{self.other_player.name} wins")
                break
            self.ask_for_attacks(self.current_player)

            # switching current player
            self.changing_current_player()
        print("thanks for playing :)")


            
