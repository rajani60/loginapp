from  flask import Flask, render_template , request
from dbmodules.MongoClient import CreateConnection
import pymongo
import hashlib


mycol = CreateConnection("PERSON","details")

print("creation of collection is completed....")

app = Flask(__name__)

def fetchRecordUserName(uname):
  return mycol.find_one({"name":uname})

def inputEncrypPasswd(passwd):
  return hashlib.md5(passwd.encode()).hexdigest()

@app.route("/")
def index():
  return "Hello greeting from webapp...."

@app.route("/home")
def home():
  return render_template("/home.html")


@app.route("/login",methods=["GET","POST"])
def login():
  if request.method == "POST":
    name = request.form["uname"]
    password = request.form["psw"]

    #query to mongo
    dbRecord = fetchRecordUserName(name)
    
    if dbRecord:
      if name == dbRecord["name"]:
        if inputEncrypPasswd(password) == dbRecord["passwd"]:
          return render_template("success.html",response="Welcome to login APP")
        else:
          return render_template("error.html",response="password is invalid")
    else:
      return render_template("error.html",response="no username")

if __name__ == '__main__':
  app.run(debug=True)