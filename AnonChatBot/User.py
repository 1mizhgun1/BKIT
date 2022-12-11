from config import *

# класс для хранения информации об одном пользователе
class User:
    def __init__(self):
        self.sex = 'n'                  # пол
        self.want = 'n'                 # предпочтения поиска (по полу)
        self.age = DEFAULT_USER_AGE     # возраст
        self.state = 0                  # состояние использования бота
        self.companion = 0              # id собеседника
