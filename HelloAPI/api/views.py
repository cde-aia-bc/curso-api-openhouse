from fastapi.responses import JSONResponse
from db.models import get_cliente
from pydantic import BaseModel

class GetCliente(BaseModel):
	num_doc: str

def rest_get_cliente(request: GetCliente):
	payload = request.dict()
	num_doc = payload["num_doc"]
	api_prueba = get_cliente(num_doc)
	if len(api_prueba) > 0:
		ret = [v.attribute_values for v in api_prueba]
		return JSONResponse(status_code=200, content=ret)
	else:
		return JSONResponse(status_code=404, content={"error": "No se encontraron resultados"})
