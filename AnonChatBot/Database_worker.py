from User import *

# класс для хранения состояний пользователей
class Database_worker:
    def __init__(self, path_users):
        self.path_users = path_users

    # чтение из файла
    def get_users(self):
        users = {}
        with open(self.path_users) as file:
            n = int(next(file))
            for i in range(n):
                line = file.readline()
                user = User()
                user_id, user.sex, user.want, user.age, user.state, user.companion = map(str, line.split())
                user.age = int(user.age)
                user.state = int(user.state)
                user.companion = int(user.companion)
                users[int(user_id)] = user
        return users

    # запись в файл
    def write_users(self, users):
        with open(self.path_users, 'w') as file:
            file.write(str(len(users)) + '\n')
            for user_id, user in users.items():
                file.write('{} {} {} {} {} {}\n'.format(user_id, user.sex, user.want, user.age, user.state, user.companion))
