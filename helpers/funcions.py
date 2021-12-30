from website.models import User



def define_user(email):
    user = User.query.filter_by(email=email).first()
    return user