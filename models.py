from app import db

## Model for users in the database
class UsersModel(db.Model):
    __tablename__ = "users"

    netid = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone = db.Column(db.String)
    instagram = db.Column(db.String)
    snapchat = db.Column(db.String)
    is_admin = db.Column(db.Boolean)
    photo = db.Column(db.String)

    def __init__(
        self,
        netid,
        first_name,
        last_name,
        phone,
        instagram,
        snapchat,
        is_admin,
        photo,
    ):
        self.netid = netid
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.instagram = instagram
        self.snapchat = snapchat
        self.is_admin = is_admin
        self.photo = photo


## Models for clubs in the database
class ClubsModel(db.Model):
    __tablename__ = "clubs"

    clubid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    info_shared = db.Column(db.String)

    def __init__(self, clubid, name, description, info_shared):
        self.clubid = clubid
        self.name = name
        self.description = description
        self.info_shared = info_shared


##class ClubMembersModel(db.Model):

##class JoinRequests(db.Model)

##class CreationRequests(db.Model)
