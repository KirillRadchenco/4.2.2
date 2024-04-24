#Токен бота
BOT_TOKEN = '7056016843:AAH1n9zUU6dV5oUYp9SLH0g_FkDBeCZr0RM'

# Настройка бота
bot = telebot.TeleBot(BOT_TOKEN)

# Словарь с вопросами и действиями
questions = ["Поцеловать руку первому встречному.",
              "Назови что-то, чего ты никогда не делал раньше.",
              "Есть ли у тебя какая-нибудь необычная фобия?"]
actions = ["Станцуй танец",
           "Спой песню",
           "Сделай десять отжиманий"]

# Состояния пользователя
STATE_START = 0
STATE_QUESTION = 1
STATE_ACTION = 2

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Добро пожаловать в игру \"Правда или действие\"!")
    bot.send_message(message.chat.id, "Выберите \"Правда\" или \"Действие\":",
                      reply_markup=telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
                              .add("Правда", "Действие"))
    bot.set_state(message.chat.id, STATE_START)

# Обработчик кнопки "Правда"
@bot.message_handler(func=lambda message: message.text == "Правда" and bot.get_state(message.chat.id) == STATE_START)
def truth(message):
    bot.send_message(message.chat.id, "Вопрос: " + questions[0])
    bot.set_state(message.chat.id, STATE_QUESTION)

# Обработчик команды /true
@bot.message_handler(commands=['true'], state=STATE_START)
def truth_command(message):
    bot.send_message(message.chat.id, "Вопрос: " + questions[0])
    bot.set_state(message.chat.id, STATE_QUESTION)

# Обработчик кнопки "Действие"
@bot.message_handler(func=lambda message: message.text == "Действие" and bot.get_state(message.chat.id) == STATE_START)
def action(message):
    bot.send_message(message.chat.id, "Действие: " + actions[0])
    bot.set_state(message.chat.id, STATE_ACTION)

# Обработчик команды /action
@bot.message_handler(commands=['action'], state=STATE_START)
def action_command(message):
    bot.send_message(message.chat.id, "Действие: " + actions[0])
    bot.set_state(message.chat.id, STATE_ACTION)

# Запуск бота
bot.infinity_polling()
