from flask import Flask, jsonify, request, session, flash
from flask_cors import CORS
from database import Database
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)
app.secret_key = "sustainabits"
CORS(app)
database = Database(app)

@app.route("/login", methods=["POST"])
def login():
    args = request.get_json()
    return jsonify(database.login(
        args.get("email", ""), 
        args.get("password", "")
    ))

@app.route("/signup", methods=["POST"])
def register():
    args = request.get_json()

    return database.signup(
        args.get("email", ""), args.get("password", ""), 
        args.get("username", "")
    )

@app.route("/co2", methods=["POST"])
def co2():
    args = request.get_json()

    return database.co2usage(
        args.get("userID", ""), args.get("date", "")
    )

@app.route("/co2Change", methods=["POST"])
def co2Change():
    args = request.get_json()

    return database.co2Change(
        args.get("userID", ""), args.get("date", ""), args.get("categoryID", ""), args.get("dol", ""), args.get("remove", "")
    )


@app.route("/friends", methods=["POST"])
def friends():
    args = request.get_json()
    return database.friends(
        args.get("userID", "")
    )

@app.route("/users", methods=["POST"])
def users():
    args = request.get_json()
    return database.usersWithFriends(
        args.get("userID", "")
    )

@app.route("/events", methods=["POST"])
def events():
    args = request.get_json()
    return database.events(
        args.get("userID", "")
    )

@app.route("/activities", methods=["POST"])
def activities():
    args = request.get_json()
    return database.activities(
        args.get("userID", ""), args.get("date", ""), args.get("treeID", ""), args.get("start", "")
    )

@app.route("/competitions", methods=["POST"])
def competitions():
    args = request.get_json()
    return database.competitions(
        args.get("userID", "")
    )

@app.route("/competition", methods=["POST"])
def competition():
    args = request.get_json()
    return database.competition(
        args.get("userID", ""), args.get("competitionID", "")
    )

@app.route("/trees", methods=["POST"])
def trees():
    args = request.get_json()
    return database.treesUntilNow(
        args.get("userID", "")
    )

@app.route("/friendChange", methods=["POST"])
def friendChange():
    args = request.get_json()
    return database.friendChange(
        args.get("userID", ""), args.get("friendID", ""), args.get("add", "")
    )

@app.route("/userU", methods=["POST"])
def userU():
    args = request.get_json()
    return database.user(
        args.get("userID", "")
    )

@app.route("/insertAct", methods=["POST"])
def insertAct():
    args = request.get_json()
    return database.insertActivity(
        args.get("userID", ""), args.get("activityID","")
    )

@app.route("/insertEvent", methods=["POST"])
def insertEvent():
    args = request.get_json()
    return database.insertEvent(
        args.get("userID", ""), args.get("eventID","")
    )

@app.route("/awards", methods=["GET"])
def awards():
    return database.awards()

@app.route("/createComp", methods=["POST"])
def createC():
    args = request.get_json()
    return database.createCompetition(args.get("userID", ""), args.get("name", ""), args.get("description", ""), args.get("private", ""), args.get("award", ""), args.get("friends", ""), args.get("dates", ""))

@app.route("/joinC", methods=["POST"])
def joinC():
    args = request.get_json()
    return database.joinCompetition(
        args.get("userID", ""), args.get("competitionID","")
    )

@app.route("/updateU", methods=["POST"])
def updateU():
    args = request.get_json()

    if (args.get("image","") is None):
        return database.updateUser(
            args.get("userID", ""), args.get("username",""), args.get("email",""), args.get("image",""), args.get("limit","")
        )
    else:
        image = args.get("image","").split(';base64,')[1]
        missing_padding = len(image) % 4
        if missing_padding != 0:
            image += '=' * (4 - missing_padding)
        print(image)
        image_data = base64.b64decode(image)
        image = Image.open(BytesIO(image_data))
        image.save('./images/' + str(args.get("userID", "")) + '.png')
        return database.updateUser(
            args.get("userID", ""), args.get("username",""), args.get("email",""), str(args.get("userID", "")) + '.png', args.get("limit","")
        )

@app.route("/searchC", methods=["POST"])
def searchC():
    args = request.get_json()
    return database.searchCompetitions(
        args.get("userID", ""), args.get("query", "")
    )

@app.route("/searchE", methods=["POST"])
def searchE():
    args = request.get_json()
    return database.searchEvents(
        args.get("userID", ""), args.get("query", "")
    )

@app.route("/searchA", methods=["POST"])
def searchA():
    args = request.get_json()
    return database.searchActivities(
        args.get("userID", ""), args.get("date", ""), args.get("treeID", ""), args.get("start", ""), args.get("query", "")
    )

@app.route("/searchF", methods=["POST"])
def searchF():
    args = request.get_json()
    return database.searchFriends(
        args.get("userID", ""), args.get("query", "")
    )

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)

