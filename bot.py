import telebot
import wikipedia
wikipedia.set_lang('ru')
bot = telebot.TeleBot('6491424040:AAFhih5ZjUoxg4JHMvL9F7wX6YyJkCwtQSA')
@bot.message_handler(content_types=['text'])
def echo(message:telebot.types.Message):
    text = message.text
    print(text)
    id = message.chat.id
    if text == '/start':
        bot.send_message(id, 'Привет! Напиши любое слово/термин')
    else:
        try:
            bot.send_message(id, wikipedia.summary(text))
        except:
            bot.send_message(id, 'Ничего не найдено')
    
    
    
bot.polling(none_stop=True)
