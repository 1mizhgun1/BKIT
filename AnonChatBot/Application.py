import telebot
from telebot import types
from Database_worker import *

# класс для работы бота
class Application:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)                   # сам бот
        self.database_worker = Database_worker(PATH_USERS)  # ввод-вывод состояний пользователей в файл
        self.users = self.database_worker.get_users()       # словарь пользователей { user_id : User }

    # выбора пола пользователя
    def choose_sex(self, user_id, message):
        correct = True
        if message.text == '🙎‍♂️ Мужской':
            self.users[user_id].sex = 'm'
        elif message.text == '🙎‍♀️ ‍Женский':
            self.users[user_id].sex = 'w'
        elif message.text == 'Неважно':
            self.users[user_id].sex = 'n'
        else:
            correct = False
        self.database_worker.write_users(self.users)
        return correct

    # выбор возраста пользователя
    def choose_age(self, user_id, message):
        correct = True
        if message.text == 'Неважно':
            self.users[user_id].age = 0
        else:
            try:
                self.users[user_id].age = int(message.text)
            except:
                correct = False
        self.database_worker.write_users(self.users)
        return correct

    # выбор предпочтений поиска пользователя
    def choose_want(self, user_id, message):
        correct = True
        if message.text == '🙎‍♂️ Мужского':
            self.users[user_id].want = 'm'
        elif message.text == '🙎‍♀️ Женского':
            self.users[user_id].want = 'w'
        elif message.text == 'Не имеет значения':
            self.users[user_id].want = 'n'
        else:
            correct = False
        self.database_worker.write_users(self.users)
        return correct

    # старт либо изменение настроек пользователя
    def to_state_1(self, user_id, text):
        self.users[user_id].state = 1
        self.database_worker.write_users(self.users)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton('🙎‍♂️ Мужской')
        btn2 = types.InlineKeyboardButton('🙎‍♀️ ‍Женский')
        btn3 = types.InlineKeyboardButton('Неважно')
        markup.add(btn1, btn2, btn3)
        self.bot.send_message(user_id, text, reply_markup=markup)

    # изменение возраста
    def to_state_2(self, user_id, text):
        self.users[user_id].state = 2
        self.database_worker.write_users(self.users)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.InlineKeyboardButton('Неважно')
        back = types.InlineKeyboardButton('Назад')
        markup.add(btn, back)
        self.bot.send_message(user_id, text, reply_markup=markup)

    # изменение предпочтений поиска
    def to_state_3(self, user_id, text):
        self.users[user_id].state = 3
        self.database_worker.write_users(self.users)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton('🙎‍♂️ Мужского')
        btn2 = types.InlineKeyboardButton('🙎‍♀️ Женского')
        btn3 = types.InlineKeyboardButton('Не имеет значения')
        back = types.InlineKeyboardButton('Назад')
        markup.add(btn1, btn2, btn3, back)
        self.bot.send_message(user_id, text, reply_markup=markup)

    # готовность поиска собеседников
    def to_state_4(self, user_id, text, **kwargs):
        # нужно ли создавать кнопку 'Назад'
        add_back = True
        if len(kwargs) != 0:
            add_back = kwargs['back']

        self.users[user_id].state = 4
        self.database_worker.write_users(self.users)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.InlineKeyboardButton('🔎 Поиск собеседника')
        if add_back:
            back = types.InlineKeyboardButton('Назад')
            markup.add(btn, back)
        else:
            markup.add(btn)
        self.bot.send_message(user_id, text, reply_markup=markup)

    # переход в состояние поиска собеседника
    def to_state_5(self, user_id, text):
        self.users[user_id].state = 5
        self.database_worker.write_users(self.users)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.InlineKeyboardButton('Остановить поиск')
        markup.add(btn)
        self.bot.send_message(user_id, text, reply_markup=markup)

    # переход в состояния диалога
    def to_state_6(self, user_id, text):
        self.users[user_id].state = 6
        self.database_worker.write_users(self.users)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton('Завершить диалог')
        btn2 = types.InlineKeyboardButton('Следующий собеседник')
        markup.add(btn1, btn2)
        self.bot.send_message(user_id, text, reply_markup=markup)

    # поиск индекс пользователя из списка prior, у которого |age - prior_age| - минимально
    @staticmethod
    def find_best_age_in_list(prior, prior_age):
        answer = 0
        prev = abs(prior[0][1].age - prior_age)
        for i in range(1, len(prior)):
            curr = abs(prior[i][1].age - prior_age)
            if curr < prev:
                answer = i
                prev = curr
        return answer

    # поиск собеседника
    def find_companion(self, user_id):
        prior_sex = self.users[user_id].want
        prior_want = self.users[user_id].sex
        prior_age = self.users[user_id].age
        prior_1 = []
        prior_2 = []
        prior_3 = []
        for id, user in self.users.items():
            if MODE == 'WORK' and user.state == 5 and user.companion == 0 and user_id != id or MODE == 'SELF_TO_SELF' and user.state == 5 and user.companion == 0:
                if user.sex == prior_sex and user.want == prior_want:
                    prior_1.append((id, user))
                elif (user.sex != prior_sex or user.want != prior_want) and not (
                        user.sex != prior_sex and user.want != prior_want):
                    prior_2.append((id, user))
                else:
                    prior_3.append((id, user))
        if len(prior_1) > 0:
            id = prior_1[self.find_best_age_in_list(prior_1, prior_age)][0]
        elif len(prior_2) > 0:
            id = prior_2[self.find_best_age_in_list(prior_2, prior_age)][0]
        elif len(prior_3) > 0:
            id = prior_3[self.find_best_age_in_list(prior_3, prior_age)][0]
        else:
            return False
        self.users[user_id].companion = id
        if MODE == 'WORK':
            self.users[user_id].n = 1
            self.users[id].companion = user_id
            self.to_state_6(id, 'Собеседник найден!')
        self.database_worker.write_users(self.users)
        return True

    # выполнение поиска собеседника
    def process_state_5(self, user_id):
        self.to_state_5(user_id, '🔎 Ищу тебе собеседника...')
        found = self.find_companion(user_id)
        if found:
            self.to_state_6(user_id, 'Собеседник найден!')

    # завершение диалога
    def stop_command(self, user_id, text_1, text_2):
        companion_id = self.users[user_id].companion
        self.users[user_id].companion = 0
        self.users[companion_id].companion = 0
        self.to_state_4(user_id, text_1, back=False)
        self.to_state_4(companion_id, text_2, back=False)
        self.database_worker.write_users(self.users)

    # следующий собеседник
    def next_command(self, user_id):
        self.stop_command(user_id, 'Диалог завершён.', 'Собеседник завершил диалог.')
        self.process_state_5(user_id)

    # отправка сообщений между собеседниками
    def send_content(self, message):
        user_id = message.from_user.id

        reply_id = 0
        if message.reply_to_message:
            reply_id = message.reply_to_message.message_id

        if message.content_type not in ['text', 'photo', 'location', 'contact']:
            eval('self.bot.send_' + message.content_type + '(self.users[user_id].companion, message.' + message.content_type + '.file_id, reply_to_message_id=reply_id)')
        elif message.content_type == 'text' and message.text not in ['Следующий собеседник', 'Завершить диалог']:
            self.bot.send_message(self.users[user_id].companion, message.text, reply_to_message_id=reply_id)
        elif message.content_type == 'photo':
            self.bot.send_photo(self.users[user_id].companion, message.photo[len(message.photo) - 1].file_id, reply_to_message_id=reply_id)
        elif message.content_type == 'location':
            self.bot.send_location(self.users[user_id].companion, message.location.latitude, message.location.longitude, reply_to_message_id=reply_id)
        elif message.content_type == 'contact':
            self.bot.send_contact(self.users[user_id].companion, message.contact.phone_number, message.contact.first_name, message.contact.last_name, reply_to_message_id=reply_id)
