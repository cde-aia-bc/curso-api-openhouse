from fastapi import FastAPI
from api.views import GetCliente, rest_get_cliente

def create_app():
	app = FastAPI()

	@app.get("/")
	async def hola():
		return "Hola mundo"

	@app.post("/get_cliente")
	async def get_cliente(request: GetCliente):
		return rest_get_cliente(request)

	return app