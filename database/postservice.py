
from .models import Post, Photo
from datetime import datetime
from database import get_db
# Добовление поста
def public_post_db(user_id, post_text):
    db = next(get_db())
    new_post = Post(user_id=user_id, post_text=post_text, publish_date=datetime.now())
    db.add(new_post)
    db.commit()
    return 'Успешно добалено'
def add_post_photo_db(post_id, post_photo):
    db = next(get_db())
    new_post_photo = Photo(post_photo=post_photo, post_id=post_id)
    db.add(new_post_photo)
    db.commit()
    return 'Фото добвлено'
def change_text_db(post_id, new_text):
    db = next(get_db())
    exact_text = db.query(Post).filter_by(id=post_id).first()
    if exact_text:
        exact_text.main_text = new_text
        db.add(new_text)
        db.commit()
        db.refresh()
        return 'Успешно измененно'
    else:
        return False
def delete_post_db(post_id):
    db = next(get_db())
    delete_post = db.query(Post).filter_by(id=post_id).first()
    # delete_post_photo = db.query(Photo).filter_by(post_id=post_id).first()
    if delete_post:
        db.delete(delete_post)
        db.commit()
        db.refresh()
        return 'Успешно удалено'
    else:
        return False

def delete_text_db(text_id):
    db = next(get_db())
    delete_text = db.query(Post).filter_by(id=text_id).first()
    if delete_text:
        db.delete(delete_text)
        db.commit()
        db.refresh()
        return 'Успешно удалено'
    else:
        return False