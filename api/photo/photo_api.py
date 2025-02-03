from fastapi import APIRouter, UploadFile, File
import random
import imghdr


photo_router = APIRouter(prefix="/photo_avto",
                         tags=["Фотографии avto"])
# первый метод работы с фотографиями
@photo_router.post("/add_photo1")
async def add_photo1(post_id: int,
                     photo_file: UploadFile=File(...)):
    # создаем айди для фотографии чтобы использовать его в названии файла
    file_id = random.randint(1, 10000000000000)
    if photo_file:
        # создаем пустой файл для сохранения кода фотографии
        # который получили от пользователя
        photo_in_project = open(f"database/photos/photo_{file_id}_{post_id}.jpg",
                                "wb")
        try:
            # читаем код фотографии, которую отправил пользователь
            photo_to_save = await photo_file.read()
            # переписываем код фотографии пользователя в наш файл в проекте
            photo_in_project.write(photo_to_save)
        except:
            print("ошибка")
        finally:
            # закрываем файл проекта
            photo_in_project.close()
        return {"status": 1, "message": "фото успешно загружено"}
    return {"status": 0, "message": "ошибка загрузки"}

# второй вариант
@photo_router.post("/add_photo2")
async def add_photo2(post_id: int,
                     photo_file: UploadFile=File(...)):
    file_id = random.randint(1, 10000000000000)
    ALLOWED_EXTENSIONS = ["jpg", "png", "HEIC"]
    ALLOWED_MIME_TYPES = ["photo/jpg", "photo/png", "photo/HEIC"]

    if photo_file:
        with open(f"database/photos/photo_{file_id}_{post_id}.jpg",
                                "wb") as photo_in_project:
            photo_to_save = await photo_file.read()
            photo_type = imghdr.what(None, photo_to_save)
            print(photo_type)
            photo_in_project.write(photo_to_save)
            return {"status": 1, "message": "фото вашего avto успешно загружено:) "}
    return {"status": 0, "message": "ошибка загрузки:( "}

@photo_router.post("/add_text")
async def add_text(text: str):
    file_id = random.randint(1, 10000000000000)
    with open(f"all_text.txt", "w") as file:
        file.write("\n"+text)
        return {"status": 1, "message": "описание вашего avto успешно загружено, ждите звонка! "}
