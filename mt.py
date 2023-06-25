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
# load_connections
import os
import random

HELLO_MILVUS = 'hello_milvus'

load_dotenv()

def listDatabases():
  dbs = db.list_database()
  print('  ', dbs)

def listCollections():
  collects = utility.list_collections()
  print('  ', collects)

def checkCollection(name):
  if utility.has_collection(HELLO_MILVUS):
    print(f"   ===> check: {HELLO_MILVUS} exists.")
  else:
    print(f"   ===> check: {HELLO_MILVUS} not exist.")

def checkCollectionInfo(collect):
  print('   schema:', collect.schema)
  print('   description:', collect.description)
  print('   name:', collect.name)
  print('   is_empty:', collect.is_empty)
  print('   num_entities:', collect.num_entities)
  print('   primary_field:', collect.primary_field)
  print('   indexes:', collect.indexes)
  print('   properties:', collect.properties if hasattr(collect, 'properties') else '(none)')

# 0. Connect
print("0. Connect")
conn = connections.connect(
  host=os.getenv('MILVUS_HOST'), 
  port=os.getenv('MILVUS_PORT')
)
print('   connected')
print()

# 1. List databases
print("1. List databases")
listDatabases()
print()

# 2. List collections
print("2. List collections")
listCollections()
print()

# 3. Drop hello_milvus collection if exists.
print('3. Drop hello_milvus if exists')
checkCollection(HELLO_MILVUS)
if utility.has_collection(HELLO_MILVUS):
  print(f'   drop it.')
  utility.drop_collection(HELLO_MILVUS)  
if utility.has_collection('Book'):
  utility.drop_collection('Book')
  print('dropped Book')
if utility.has_collection('book'):
  utility.drop_collection('book')
  print('dropped book')
print()

# 4. List collections
print('4. List collections')
listCollections()
print()

# 5. Create collection
print('5. Create collection')
fields = [
    FieldSchema(name="pk", dtype=DataType.INT64, is_primary=True, auto_id=False),
    FieldSchema(name="random", dtype=DataType.DOUBLE),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=8)
]
schema = CollectionSchema(fields=fields, description=F"{HELLO_MILVUS} is the simplest demo to introduce the APIs")
hello_milvus = Collection(HELLO_MILVUS, data=None, schema=schema, consistency_level="Strong", properties={"collection.ttl.seconds": 15})
print('   created.')
print('   checking ...')
print('    ', hello_milvus) #checkCollectionInfo(hello_milvus)
print()

# 6. Get collection info
print('6. Get collection info')
checkCollectionInfo(hello_milvus)
print()

# 7. List collections
print('7. List collections')
listCollections()
print()

# 8. Check having index "embedding"
print('8. Check index "embedding"')
hello_milvus = Collection(HELLO_MILVUS, schema)
hasIndex = hello_milvus.has_index(index_name="embedding")
print('   With index "embedding"', hasIndex)
print('   indices:', hello_milvus.indexes)
print()

# 9. Add index
print('9. Create index')
print('   creating index')
indexParams = {
  "index_type": "IVF_FLAT",
  "metric_type": "L2",
  "params": {"nlist": 128},
}
hello_milvus.create_index("embedding", indexParams, index_name="idx_embedding")
hasIndex = hello_milvus.has_index(index_name="idx_embedding")
print('   hasIndex:', hasIndex)
print()

# 10. Check having index "embedding"
print('10. Check index "embedding"')
hello_milvus = Collection(HELLO_MILVUS, schema)
hasIndex = hello_milvus.has_index(index_name="embedding")
print('   With index "embedding"', hasIndex)
print('   indices:', hello_milvus.indexes)
print()

# 11. Add entities
print('11. Add entities')
NUM = 5
data  = [
 [i for i in range(NUM)],
 [0.1, 0.2, 0.3, 0.4, 0.5],
#  [float(random.randrange(-20, -10)) for _ in range(NUM)],  # field random
 [[random.random() for _ in range(8)] for _ in range(NUM)],  # field embedding
]
print('  data[0]', data[0])
print('  data[1]', data[1])
print('  data[2]', data[2])
# result = hello_milvus.insert((1, 1.1, [1000]))
try:
  hello_milvus = Collection(HELLO_MILVUS)
  print(f"   Before insert: {hello_milvus.num_entities}")  # check the num_entites
  insert_result  = hello_milvus.insert(data)
  vectors = data[2]
  # print('data[2]', vectors)
  hello_milvus.flush()
  hello_milvus.load()
except:
  print('Something went wrong.')

print(f"    After insert: {hello_milvus.num_entities}")  # check the num_entites
print()
# print(insert_result )

# 12. Check collection info
# print('12. Check collection info')
# checkCollectionInfo(hello_milvus)
# print()


# 13. Search records  # search(collection, _VECTOR_FIELD_NAME, _ID_FIELD_NAME, vectors[:3])
print("13. Search")
print("vectors[:1]", vectors[:1])
search_params = {
  "data":  vectors[:2],
  "anns_field": "embedding",
  "param": {
    "metric_type": "L2",
    "params": {
      "nprobe": 16
    }
  },
  "limit": 10,
  "expr": "pk < 5"
}
search_result = hello_milvus.search(**search_params)
for i, item in enumerate(search_result):
  print(f"  Search result item for {i}th vector:")
  for j, res in enumerate(item):
    print(f"  Top {j}: {res}")
print('')      


# 14. Query (for pk == 3)
print('14. Query Records')
query_result = hello_milvus.query(expr="random>0.3", output_fields=["pk", "random", "embedding"])
print('query result', query_result)
result_ids = [row['pk'] for row in query_result]
print('result ids', result_ids)
print()

# 15. Delete
print('15. Delete entity by id')
delete_result = hello_milvus.delete(f"pk in [{result_ids[0]}]")
print('  result', delete_result)
hello_milvus.flush()
checkCollectionInfo(hello_milvus)
print()

# 16. Query (for pk == 3)
print('16. Query Records')
query_result = hello_milvus.query(expr="pk==3", output_fields=["pk", "random"])
result_ids = [row['pk'] for row in query_result]
print('result ids', result_ids)
checkCollectionInfo(hello_milvus)
print()

# 17. Drop Collection
print('17. Drop collection')
print('   dropping collection')
utility.drop_collection(HELLO_MILVUS)  
checkCollection(HELLO_MILVUS)
listCollections()
print()

# collection = Collection('Book')
# collection.index(index_name="vec_index")
# collection.load()
# data = [
#   [i for i in range(2000)],
#   [i for i in range(10000, 12000)],
#   [[random.random() for _ in range(2)] for _ in range(2000)],
# ]
# result = collection.insert(data)
# print(result)
#conns = utility.list_collections()
#print(conns)                   

# print()
# print("*** Query")

# res = collection.query(
#     expr="book_id in [2,4,6,8]",
#     output_fields=["book_id", "book_intro"],
#     consistency_level="Strong"
# )
# sorted_res = sorted(res, key=lambda k: k['book_id'])
# print(sorted_res)
