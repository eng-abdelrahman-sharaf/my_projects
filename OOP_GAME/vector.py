from villain import Villain

class Vector(Villain):
    def __init__(self , name , game_world):
        """
        Description
        --------------------
        Vector is a villain class that can attack defend and get damage  

        Parameters
        --------------------
            * `name` : the name of the villain Vector :<
            * `game_world` : and obj of Game
        """
        super().__init__(name , game_world)

        # # reducing factor reduces your attack damage
        # self.reducing_factor = 0

        self._type = "Vector"

        self.weapons = {
            "laser_blasters" : {"energy" : 40 , "damage" : 8 , "resources" : float("inf")},
            "plasma_grenades" : {"energy" : 56  , "damage" : 13 , "resources" : 8},
            "sonic_resonance_canon" : {"energy" : 100 , "damage" : 22 , "resources" : 3},
        }

        self.shields = {
        "energy_net_trap" : {"energy" : 15 , "save" : 0.32 , "resources" : float("inf")},
        "quantum_deflector" : {"energy" : 40 , "save" : 0.8 , "resources" : 3},
        }