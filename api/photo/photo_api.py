
from fastapi import APIRouter, UploadFile, File
import random
import imghdr

from database.postservice import change_text_db, delete_post_db

photo_router = APIRouter(prefix="/photo_avto",
                         tags=["Фотографии avto"])


@photo_router.post("/add_photoCAR")
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
async def add_text(text_id:int, text: str):
    file_id = random.randint(1, 10000000000000)
    with open(f"all_text.txt", "w") as file:
        file.write("\n"+text)
        return {"status": 1, "message": "описание вашего avto успешно загружено, ждите звонка! "}

@photo_router.put("/change_text_db")
async def change_text(text_id: int, new_text:str):
    result = change_text_db(text_id, new_text)
    if result:
        return {'message': result}

@photo_router.delete('/delete')
async def del_post(post_id):
    reilt = delete_post_db(post_id)

    return reilt



#
# @photo_router.delete("/delete_photoCAR")
# async def delete_photo(post_id: int, file_id: int):
#     file_path = f"database/photos/photo_{file_id}_{post_id}.jpg"

    # if data.db.path.exists(file_path):
    #     database.remove(file_path)
    #     return {"status": 1, "message": "Фото успешно удалено :) "}
    #
    # return {"status": 0, "message": "Фото не найдено :("}

# @photo_router.delete("/photos/", tags=["Photos"])
# async def delete_photo(photo_id: str = Query(..., description="Идентификатор фотографии для удаления")):
#     """
#     Удалить фотографию.
#     """
#     try:
#         if photo_id not in photos_db:
#             raise HTTPException(status_code=404, detail="Фотография не найдена")
#
#         # Получаем информацию о фотографии
#         photo_info = photos_db[photo_id]
#
#         # Удаляем файл с диска
#         os.remove(photo_info["path"])
#
#         # Удаляем метаданные из базы данных
#         del photos_db[photo_id]
#
#         return JSONResponse(
#             status_code=200,
#             content={
#                 "id": photo_id,
#                 "message": "Фотография успешно удалена"
#             }
#         )
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Ошибка при удалении фотографии: {str(e)}")





# первый метод работы с фотографиями
# @photo_router.post("/add_photo1")
# async def add_photo1(post_id: int,
#                      photo_file: UploadFile=File(...)):
#     # создаем айди для фотографии чтобы использовать его в названии файла
#     file_id = random.randint(1, 10000000000000)
#     if photo_file:
#         # создаем пустой файл для сохранения кода фотографии
#         # который получили от пользователя
#         photo_in_project = open(f"database/photos/photo_{file_id}_{post_id}.jpg",
#                                 "wb")
#         try:
#             # читаем код фотографии, которую отправил пользователь
#             photo_to_save = await photo_file.read()
#             # переписываем код фотографии пользователя в наш файл в проекте
#             photo_in_project.write(photo_to_save)
#         except:
#             print("ошибка")
#         finally:
#             # закрываем файл проекта
#             photo_in_project.close()
#         return {"status": 1, "message": "фото успешно загружено"}
#     return {"status": 0, "message": "ошибка загрузки"}
#