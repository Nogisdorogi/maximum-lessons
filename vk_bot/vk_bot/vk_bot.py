import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from memes import get_memes
from valute import get_course
from story import get_story
import weather
import random
def main():
    TOKEN = "81a26da808d895c9a773536de66dc0fa22f2e36239132647ee26ed2e750c1f7a10a7b64b27b773180c0f1"
    vk_session = vk_api.VkApi(token = TOKEN)
    vk = vk_session.get_api()
    hello = """
    Привет,я бот и могу следующее:
    1.)мем - бот кидает мем
    2.)курс - бот кидает курс
    3.)погода - бот кидает температуру воздуха в Ростове
    4.)страшилка - бот кидает тебе леденящую душу историю
    5.)я загадал число от 1 до 10 - бот пытается угадать задуманное число
    """
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            msg_text = event.text.lower()
            if msg_text == "мем":
               vk.messages.send(user_id=event.user_id,random_id= get_random_id(),message=event.text,attachment=get_memes("-75214966"))
            elif msg_text == "страшилка":
               vk.messages.send(user_id=event.user_id,random_id= get_random_id(),message=get_story("-40529013"))
            elif msg_text == "курс":
                valutes_id = ["R01235","R01239","R01375"]
                valutes = [get_course(id) for id in valutes_id]
                vk.messages.send(user_id=event.user_id,random_id= get_random_id(),message="\n".join(valutes))

            elif msg_text == "погода":              
                vk.messages.send(user_id=event.user_id,random_id= get_random_id(),message=weather.muin("rostov-na-donu"))

            elif  msg_text == "я загадал число от 1 до 10":
                  result = random.randint(1,10)
                  vk.messages.send(user_id=event.user_id,random_id= get_random_id(),message="{} Это оно?".format(result))
            elif msg_text == "да":
                       vk.messages.send(user_id=event.user_id,random_id= get_random_id(),message="я выиграл)")
            elif msg_text == "нет":
                       vk.messages.send(user_id=event.user_id,random_id= get_random_id(),message="О ужас(")        
            else:
                vk.messages.send(user_id=event.user_id,random_id= get_random_id(),message=hello)

main()