from pymongo.mongo_client import MongoClient

#You Need To Add Your Password Here To Make A Secure Connection With The MongoDB Server
uri = "mongodb+srv://DivyamTalwar:<EnterYourPasswordHere>@cluster0.rozxq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)