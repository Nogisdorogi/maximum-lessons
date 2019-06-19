import telebot

token = "643499760:AAH9i-wfUIX0d-gl2BIBSEN2n1Z523B82zY"

bot = telebot.TeleBot(token)
def get_last_message():
    return bot.get_updates()[-1]

def get_text(last_message):
    return last_message.message.text

def get_id(last_message):
    return last_message.message.chat.id

def get_first_name(last_message):
    return last_message.message.chat.first_name

update_id = 0
while True:
    last_message = get_last_message()
    text_message = get_text(last_message).lower()
    id = get_id(last_message)
    first_name = get_first_name(last_message) 
    new_update_id = last_message.update_id
    if   new_update_id != update_id:
        if  text_message in ["привет","здорова","хай"]:
            response = "Привет!" + " " + first_name
            bot.send_message(chat_id=id,text=response)
        if text_message in ["пока","чао","досвидули"]:
            response = "Пока)" + " " + first_name
            bot.send_message(chat_id=id,text=response)
        update_id = new_update_id

