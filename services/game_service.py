from dao.game_dao import GameDao
from model.battlefield import Battlefield
from model.game import Game
from model.player import Player
from model.cruiser import Cruiser
from model.destroyer import Destroyer
from model.frigate import Frigate
from model.submarine import Submarine


class GameService:
    def __init__(self):
        self.game_dao = GameDao()


    def create_game(self, player_name: str, min_x: int, max_x: int, min_y: int,
        max_y: int, min_z: int, max_z: int) -> int:
        game = Game()
        battle_field = Battlefield(min_x, max_x, min_y, max_y, min_z, max_z)
        game.add_player(Player(player_name, battle_field))
        return self.game_dao.create_game(game)
    
    def join_game(self, game_id: int, player_name: str) -> bool :
        self.game = self.game_dao.find_game(game_id)
        try    :
            self.findgame(game_id)
            return True
        except :
            return False

    def get_game(self, game_id: int) -> Game:
        self.game = Game()
        #liste_des_joueurs = self.game.get_players()
        #print(liste_des_joueurs)
        #nombre_de_vaisseaux =
        return self.game_dao.find_game(game_id)
        
    def add_vessel(self, game_id: int, player_name: str, vessel_type: str,
    x: int, y: int, z: int) -> bool:

        jeu=self.game_dao.find_game(game_id)
        terrain = jeu.get_players()[0].get_battlefield()
       
        if vessel_type == "Cruiser":
            vessel = Cruiser(x,y,z)
        elif vessel_type == "Destroyer":
            vessel = Destroyer(x,y,z)
        elif vessel_type == "Frigate":    
            vessel = Frigate(x,y,z)
        else:
            vessel = Submarine(x,y,z)

        terrain.add_vessel(vessel)
        return True

    def shoot_at(self, game_id: int, shooter_name: str, vessel_id: int, x: int,
    y: int, z: int) -> bool:
        jeu=self.game_dao.find_game(game_id)

        for player in jeu.get_players():
            if player.get_name==shooter_name:
                for vessel in player.get_battlefield().get_vessels():
                    if vessel.id == vessel_id:
                        vessel.fire_at(x,y,z)
        return True
       
    def get_game_status(self, game_id: int, shooter_name: str) -> str:
        jeu = self.game_dao.find_game(game_id)
        for player in jeu.get_players():
            if player.get_name() == shooter_name:
                if player.get_battlefield().get_vessels() is None:
                    return "PERDU"
            elif player.get_battlefield().get_vessels() is None:
                return "GAGNE"
        return "ENCOURS"

    
        
   
  
