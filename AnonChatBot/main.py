from Application import *

# создание приложения ( бот + работа с файлом + словарь { user_id : User } )
app = Application(TOKEN)

# старт
@app.bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    app.users[user_id] = User()
    app.to_state_1(user_id, 'Привет!\nДля улучшения подбора собеседников советую ответить на пару вопросов. Для начала определимся с твоим полом.')

# поиск собеседника
@app.bot.message_handler(commands=['search'])
def search(message):
    user_id = message.from_user.id
    if app.users[user_id].companion != 0:
        app.to_state_5(user_id, 'В данный момент пообщаться не с кем :(')
    else:
        app.bot.send_message(user_id, 'У тебя уже есть собеседник.')

# завершение диалога
@app.bot.message_handler(commands=['stop'])
def stop(message):
    user_id = message.from_user.id
    if app.users[user_id].companion != 0:
        app.stop_command(user_id, 'Диалог завершён.', 'Собеседник завершил диалог.')
    else:
        app.bot.send_message(user_id, 'У тебя ещё нет собеседника.\nНажми /search.')

# следующий собеседник
@app.bot.message_handler(commands=['next'])
def next(message):
    user_id = message.from_user.id
    if app.users[user_id].companion != 0:
        app.next_command(user_id)
    else:
        app.bot.send_message(user_id, 'У тебя ещё нет собеседника.\nНажми /search.')

# отправить собеседнику ссылку на свой аккаунт
@app.bot.message_handler(commands=['link'])
def next(message):
    user_id = message.from_user.id
    if app.users[user_id].companion != 0:
        app.bot.send_message(user_id, 'Ссылка на мой аккаунт:\nhttps://t.me/{}'.format(message.from_user.username))
    else:
        app.bot.send_message(user_id, 'У тебя ещё нет собеседника.\nНажми /search.')

# изменение настроек поиска
@app.bot.message_handler(commands=['reset'])
def reset(message):
    user_id = message.from_user.id
    if app.users[user_id].companion == 0:
        app.to_state_1(user_id, 'Выбери свой пол.')
    else:
        app.bot.send_message(user_id, 'Опция недоступна во время диалога.')

# помощь по боту
@app.bot.message_handler(commands=['help'])
def help(message):
    user_id = message.from_user.id
    app.bot.send_message(user_id, 'Здесь будет информация о боте.')

# правила общения в чате
@app.bot.message_handler(commands=['rules'])
def rules(message):
    user_id = message.from_user.id
    app.bot.send_message(user_id, 'Здесь будут правила общения в чате.')

# взаимодействие с пользователем в зависимости от его состояния (state)
@app.bot.message_handler(content_types=CONTENT_TYPES)
def text_processing(message):
    user_id = message.from_user.id

    # state 1 - выбор пола
    if app.users[user_id].state == 1:
        correct = app.choose_sex(user_id, message)
        if correct:
            app.to_state_2(user_id, 'Отлично!\nТеперь отправь мне свой возраст.')
        else:
            app.bot.send_message(user_id, 'Просто нажми на одну из кнопок.')

    # state 2 - выбор возраста
    elif app.users[user_id].state == 2:
        correct = app.choose_age(user_id, message)
        if message.text == 'Назад':
            app.to_state_1(user_id, 'Выбери свой пол.')
        elif correct:
            app.to_state_3(user_id, 'Запомнил! Наконец, последний вопрос: собеседники какого пола для тебя предпочтительнее?')
        else:
            app.bot.send_message(user_id, 'Введи одно число, либо нажми "Неважно".')

    # state 3 - выбор предпочтений поиска
    elif app.users[user_id].state == 3:
        correct = app.choose_want(user_id, message)
        if message.text == 'Назад':
            app.to_state_2(user_id, 'Отправь свой возраст.')
        elif correct:
            app.to_state_4(user_id, 'Готово! Теперь ты можешь общаться, для этого нажми\n🔎 Поиск собеседника".')
        else:
            app.bot.send_message(user_id, 'Просто нажми на одну из кнопок.')

    # state 4 - готовность искать собеседника
    elif app.users[user_id].state == 4:
        if message.text == '🔎 Поиск собеседника':
            app.process_state_5(user_id)
        elif message.text == 'Назад':
            app.to_state_3(user_id, 'Cобеседники какого пола для тебя предпочтительнее?')
        else:
            app.bot.send_message(user_id, 'Нажми "🔎 Поиск собеседника".')

    # state 5 - поиск собеседника
    elif app.users[user_id].state == 5:
        if message.text == 'Остановить поиск':
            app.to_state_4(user_id, 'Вы завершили поиск.', back=False)
        else:
            app.bot.send_message(user_id, 'Собеседник ещё не найден.')

    # state 6 - диалог
    elif app.users[user_id].state == 6 and app.users[user_id].companion != 0:
        if message.content_type == 'text':
            if message.text == 'Завершить диалог':
                app.stop_command(user_id, 'Диалог завершён.', 'Собеседник завершил диалог.')
            elif message.text == 'Следующий собеседник':
                app.next_command(user_id)
        app.send_content(message)

if __name__ == '__main__':
    app.bot.polling(none_stop=True, interval=0)
