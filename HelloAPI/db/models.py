from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute

class Cliente(Model):
	class Meta:
		region = "us-east-1"
		table_name = "cliente"

	num_doc = UnicodeAttribute(hash_key=True)
	nombre = UnicodeAttribute()
	saldo = NumberAttribute()
	moroso = NumberAttribute(null=True)

def get_cliente(num_doc):
	return list(Cliente.query(hash_key=num_doc))
