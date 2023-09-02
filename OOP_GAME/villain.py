class Villain:
    """
    Description
    --------------------
    a villain class that can attack defend and get damage  
    

    Parameters
    --------------------
        * `name` : the name of the villain Gru :<
        * `game_world` : and obj of Game
    """
    def __init__(self , name , game_world):
        self.health , self.energy , self.is_alive , self.weapons , self.shields , self._type= 100 , 500 , True , {} , {} , "villain"
        self.name = name
        self.game_world = game_world

        
    def attack(self , weapon_name: str, enemy) -> tuple:
        """ 
        Description
        --------------
        attacking the enemy 

        Parameter
        --------------
            * `weapon_name` : should be a name of weapons  in self.weapons
            * `enemy` : should be an object of Villain class or inherits from it

        Return
        --------------
        True if the attack was successful

        False if the attack was unsuccessful and a `message` of the error
        """

        # check if you can attack (energy - resources)
        if  self.weapons[weapon_name] ["energy"] <= self.energy:
            if self.weapons[weapon_name] ["resources"]: 
                # decreasing resources
                self.weapons[weapon_name] ["resources"]-=1
                self.energy -= self.weapons[weapon_name] ["energy"]  
                if self.energy == 0 : self.is_alive = False

                # damage the enemy
                if self._type == "Gru":
                    is_avoidable = self.weapons[weapon_name]["is_avoidable"]
                # as Vector doesn't have is_avoidable in its features
                else:
                    is_avoidable = True
                enemy.damage(self.weapons[weapon_name]["damage"]  , is_avoidable)

                
                return True , None
                
            else:
                return False , f"No enough resources for {weapon_name} attack"
        else:
                return False , f"No enough energy for {weapon_name} attack"
                

    def damage(self , damage_value:int , is_avoidable : bool ) -> None:
        """
        Description
        --------------
        makes damage to the enemy 
        and change its state from alive to dead if the attack >= health

        Parameter
        --------------
            * `damage_value` 

        Return
        --------------
        None
        """
            

        shielding = 0
        if is_avoidable and self.game_world.choose_attack_or_shield() == 2: shielding = self.game_world.ask_for_shield(self)
        damage_value  -= shielding*damage_value
        if damage_value >= self.health :
            self.health = 0
            self.is_alive = False
        else:
            self.health -= damage_value




    def shield(self , shield_name:str) -> tuple:
        """
        Description
        --------------
        protect the villain from the enemy attack

        Parameter
        --------------
            * `shield_name` : string 

        Return
        --------------
        shield save value if shielding was successful

        0 if the shield was not successful and a message
        """
        if self.shields [shield_name] ["energy"] <= self.energy :
            if self.shields [shield_name] ["resources"] :
                self.shields [shield_name] ["resources"] -= 1
                self.energy -= self.shields[shield_name] ["energy"]  
                if self.energy == 0 : self.is_alive = False
                return self.shields [shield_name]["save"] , None
            else:
                return 0 , f"No enough resources for {shield_name} attack"
        else:
                return 0 , f"No enough energy for {shield_name} attack"