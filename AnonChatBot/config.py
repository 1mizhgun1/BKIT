# токен бота
TOKEN = 'здесь должен быть токен бота'

# путь к файлу с данными о состояниях пользователей (при первом запуске бота в файле записано одно число: 0 - количество пользователей
PATH_USERS = 'database\\users.txt'

# возраст пользователя по умолчанию (нужен для поиска собеседников)
DEFAULT_USER_AGE = 14

# типы контента, которыми могут обмениваться пользователи в диалоге
CONTENT_TYPES = ['text', 'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location', 'contact', 'animation']

# эхо-режим для отладки (меняется только Application.find_companion --> условие в цикле for и условие перед return)
# MODE = 'SELF_TO_SELF'

# обычный режим
MODE = 'WORK'
