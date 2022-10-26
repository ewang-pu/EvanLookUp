import flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import auth

app = flask.Flask(
    __name__, template_folder="src", static_folder="static_files"
)
app.secret_key = "234rfvbnjkiytfcdertgbn"
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql+psycopg2://stwiezab:eN4T8unVzyIE49TzhKCbf1m5lKkGhjWU@peanut.db.elephantsql.com/stwiezab"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models import UsersModel, ClubsModel


## Index Route
@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
    # Setup data model
    netid = auth.authenticate()
    user = db.session.get(UsersModel, netid)
    # If no data is associated with the user, they are redirected
    # to create a profile
    if user is None:
        return flask.redirect(flask.url_for("profilecreation"))
    # Otherwise index is loaded with their clubs
    else:
        print(user.netid)
        print(user.first_name)
        print(user.last_name)
        print(user.instagram)
        print(user.phone)
        html_code = flask.render_template("index.html", netid=netid)
        response = flask.make_response(html_code)
        return response


## Profile Creation Route
@app.route("/profilecreation", methods=["GET"])
def profilecreation():
    netid = auth.authenticate()
    user = db.session.get(UsersModel, netid)
    if user is not None:
        return flask.redirect("/")
    # Only needs to render the form
    return flask.render_template("profilecreation.html")


## Profile Update Route
@app.route("/profileupdate", methods=["GET"])
def profileupdate():
    # Only needs to render the update form
    return flask.render_template("profileupdate.html")


## Profile Posting Route
@app.route("/profilepost", methods=["POST"])
def profilepost():
    # Get all important pieces of the form and turn them into
    # a data set
    ## ADD MORE AS NEEDED
    netid = flask.request.form["netid"]
    first_name = flask.request.form["first_name"]
    last_name = flask.request.form["last_name"]
    phone = flask.request.form["phone"]
    instagram = flask.request.form["instagram"]
    snapchat = flask.request.form["snapchat"]
    is_admin = False
    photo = ""
    new_user = UsersModel(
        netid,
        first_name,
        last_name,
        phone,
        instagram,
        snapchat,
        is_admin,
        photo,
    )
    # Input the user into the DB
    db.session.add(new_user)
    db.session.commit()
    # Redirect to index for loading the user's new page
    return flask.redirect("/")


## Group Creation Route
@app.route("/groupcreation", methods=["GET"])
def groupcreation():
    # Only needs to render the creation form
    return flask.render_template("groupcreation.html")


@app.route("/grouppost", methods=["POST"])
def grouppost():
    clubid = db.session.query(ClubsModel).count() + 1
    name = flask.request.form["name"]
    description = flask.request.form["description"]
    info_shared = ""
    try:
        share_socials = flask.request.form["share_socials"]
        info_shared = "1"
    except:
        info_shared = "0"
    try:
        share_phone = flask.request.form["share_phone"]
        info_shared = info_shared + "1"
    except:
        info_shared = info_shared + "0"
    new_club = ClubsModel(clubid, name, description, info_shared)
    db.session.add(new_club)
    db.session.commit()
    # Redirect to index for loading the user's new page
    return flask.redirect("/")
