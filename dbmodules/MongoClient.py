import pymongo

LOCAL_DB_URL = "mongodb://localhost:27017/"

REMOTE_DB_URL = "mongodb+srv://rajancdr:sky123@cluster0.ca1bexo.mongodb.net/?retryWrites=true&w=majority"

mycol = None
def CreateConnection(name,collName):
  myclient = pymongo.MongoClient(REMOTE_DB_URL)
  mydb = myclient[name]
  try:
    if name in myclient.list_database_names():
      try: 
        if collName in mydb.list_collection_names():
          global mycol 
          mycol = mydb[collName]
        else:
          raise Exception("Collection not found....")
      except Exception as e:
        print(e)
    else:
      raise Exception("Given DB name not found....")
  except Exception as e:
    print(e)
  return mycol
  



# dbName = input("enter DB NAME: ")
# collectionName = input("Enter the collection Name: ")

# connectionObj = CreateConnection(REMOTE_DB_URL,dbName,collectionName)

# print(connectionObj)

