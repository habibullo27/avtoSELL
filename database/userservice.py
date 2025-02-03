from database.models import *
from database import get_db
from database import get_db
from database.models import User

def check_user_name(user_name):
    db = next(get_db())
    checker = db.query(User).filter_by(username=user_name).first()
    if checker:
        return False
    return True
def check_phone_number(phone_number):
    db = next(get_db())
    checker = db.query(User).filter_by(phone_number=phone_number).first()
    if checker:
        return False
    return True
def check_email(email):
    db = next(get_db())
    checker = db.query(User).filter_by(email=email).first()
    if checker:
        return False
    return True

def registration_db(user_name, phone_number, email, password, birthday=None, city=None):
    db = next(get_db())
    if not check_user_name(user_name):
        return "Пользователь с таким именем уже существует"
    if not check_phone_number(phone_number):
        return "Пользователь с таким телефоном уже существует"
    if not check_email(email):
        return "Пользователь с таким Email уже существует"
    new_user = User(username=user_name, phone_number=phone_number,
                    email=email, city=city, password=password, birthday=birthday)
    db.add(new_user)
    db.commit()
    return new_user.id
def login_db(identificator, password):
    with next(get_db()) as db:
        user = db.query(User).filter_by(
            username = identificator).first()
        if not user:
            user = db.query(User).filter_by(
                email=identificator).first()
            if not user:
                user = db.query(User).filter_by(
                    phone_number=identificator).first()
        if user and user.password == password:
            return {'status':1, 'message': user.id}
        return {'status':0, 'message': 'Неверный логин или пароль'}
