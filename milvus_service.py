from dotenv import load_dotenv
from pymilvus import (
    db,
    connections,
    utility,
    # list_collections,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection,
)
import os

load_dotenv()

# collection info
# {
#   schema: {
#     'auto_id': False
#     'description': 
#     'fields': [
#       {
#         'name': 'pk',
#         'description': '',
#         'type': <DataType.INT64: 5>
#         'is_primary': True,
#         'auto_id': False
#       },
#       {
#         'name': 'random',
#         'description': '',
#         'type': <DataType.DOUBLE: 11>,
#       },
#       {
#         'name': 'embeddings',
#         'description': '',
#         'type': <DataType.FLOAT_VECTOR: 101>,
#         'params': {
#           dim': 8
#         }
#       }
#     ]
#   },
#   description: 'slfkjsdlfjkds',
#   name: 'hello_milvus',
#   is_empty: True,
#   num_entities: 0,
#   primary_field: {
#     'name': 'pk',
#     'description': '',
#     'type': <DataType.INT64: 5>,
#     'is_primary': True,
#     'auto_id': False
#   },
#   indexes: []
#   properties: (none)
# }}

def get_collection(collectionName):
  return Collection(collectionName)

def list_collections():
  collections = utility.list_collections()
  return collections

def using_database(dbName):
  db.using_database(dbName)

def list_database():
  dbs = db.list_database()
  return dbs

def connect_milvus(host, port):
  print('host', host)
  print('port', port)
  connections.connect(
    host=host,
    port=port
  )

def config():
  connections.connect(
      host=os.getenv('MILVUS_HOST'),
      port=os.getenv('MILVUS_PORT')
  )
  print('DB connected successfully.')

