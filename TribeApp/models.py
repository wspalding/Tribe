from TribeApp.Models.TribeModel import Tribe
from TribeApp.Models.UserModel import User
from TribeApp import login




@login.user_loader
def load_user(id):
    return User.query.get(id)


