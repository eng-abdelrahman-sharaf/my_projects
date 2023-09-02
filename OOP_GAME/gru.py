from villain import Villain

class Gru(Villain):
    def __init__(self , name , game_world):
        super().__init__(name , game_world)
        """
        Description
        --------------------
        Gru is a villain class that can attack defend and get damage  
        

        Parameters
        --------------------
            * `name` : the name of the villain Gru :<
            * `game_world` : and obj of Game
        """
        self._type = "Gru"

        # weapons features 
        self.weapons = {
                "freeze_gun":{"energy": 50 , "damage": 11 , "resources": float("inf")},
                "electric_prod":{"energy": 88 , "damage": 18 , "resources":5 },
                "mega_magnet":{"energy": 92 , "damage": 10 , "resources": 3 , "is_reducing": True},
                "kalman_missile":{"energy": 120 , "damage": 20 , "resources": 1 , "is_avoidable": False},
        }

        # shield features
        self.shields = {
            "energy-projected_barrier_gun": {"energy":20 , "save":0.4 , "resources" : float("inf")},
            "selective_permeability": {"energy":50 , "save":0.9 , "resources" : 2},
                        }

        # adding is_avoidable and is_reducing features for each weapon
        for i in self.weapons.keys():
            if "is_avoidable" not in self.weapons[i]:
                self.weapons[i] ["is_avoidable"] = True
            if "is_reducing" not in self.weapons[i]:
                self.weapons[i] ["is_reducing"] = False

  