import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from mem import get_memes
from soup import get_soup
from desert import get_desert
from valute import get_course
from pogoda import get_weather
from random import get_random

def main():
    TOKEN = "81a26da808d895c9a773536de66dc0fa22f2e36239132647ee26ed2e750c1f7a10a7b64b27b773180c0f1"

    vk_session = vk_api.VkApi(token = TOKEN)
    vk = vk_session.get_api()
    hello = """
    Привет,я бот и могу следующее:
    хочу суп - бот кидает суп 
    хочу сладенького - бот кидает десерт
    мем - бот кидает мем
    курс - бот кидает курс
    погода - бот кидает температуру
    """

    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            msg_text = event.text.lower()
            if msg_text == "мем":
               vk.messages.send(user_id=event.user_id,random_id= get_random_id(),message=event.text,attachment=get_soup("-75214966"))
            elif msg_text == "хочу суп":
               vk.messages.send(user_id=event.user_id,random_id= get_random_id(),message=event.text,attachment=get_soup("-49715849"))
            elif msg_text == "хочу сладенького":
               vk.messages.send(user_id=event.user_id,random_id= get_random_id(),message=event.text,attachment=get_desert("-44705173"))
            elif msg_text == "курс":
                valutes_id = [(get_courseid) for id in valutes_id]
                vk.messages.send(user_id=event.user_id,random_id= get_random_id(),message="\n".join(valutes))
            elif msg_text == "погода ":
                city_id = ["rostov-na-donu","moscow","saint-petersburg"]
                town = [muin(city) for city in city_id]
                vk.messages.send(user_id=event.user_id,random_id= get_random_id(),message="\n".join(town))
            elif  msg_text == "я загадал число от 1 до 10":
                  vk.messages.send(user_id=event.user_id,random_id= get_random_id(),message=get_random() + " " + "Это оно?")
            else:
                vk.messages.send(user_id=event.user_id,random_id= get_random_id(),message=hello)


main()