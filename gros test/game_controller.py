import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from game import Game 
from game_service import GameService

app = FastAPI()
game_service = GameService()

class CreateGameData(BaseModel):
    player_name: str
    min_x: int
    max_x: int
    min_y: int
    max_y: int
    min_z: int
    max_z: int

class JoinGameData(BaseModel):
    game_data : int

class AddVesselData(BaseModel):
    game_data : int

class ShootAtData(BaseModel):
    game_data : int

@app.post("/create-game")
async def create_game(game_data: CreateGameData):
    return game_service.create_game(game_data.player_name, game_data.min_x,
                                    game_data.max_x, game_data.min_y,
                                    game_data.max_y, game_data.min_z,
                                    game_data.max_z)

@app.get("/get-game")
async def get_game(game_id: int) -> Game:
    return game_service.get_game(game_id)


@app.post("/join-game")
async def join_game(game_data: JoinGameData) -> bool:
    return game_service.join_game(game_data)
     
@app.post("/add-vessel")
async def add_vessel(game_data: AddVesselData) -> bool:
    return game_service.add_vessel(game_data)

@app.post("/shoot-at")
async def shoot_at(game_data: ShootAtData) -> bool:
    return game_service.shoot_at(game_data)

@app.get("/game-status")
async def get_game_status(game_id: int, player_name: str) -> str:
    return game_service.get_game_status(game_id)

@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
 return JSONResponse(
 status_code=500,
 content={"message": f"{exc}"}
 )
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)