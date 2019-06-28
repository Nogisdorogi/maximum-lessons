import random
import vk_api

def get_story(id):
    TOKEN = "a86d6faca86d6faca86d6facc5a8063a26aa86da86d6facf57e5bc5af969d1c3660e87e"
    vk_session = vk_api.VkApi(token = TOKEN)
    vk = vk_session.get_api()
    posts = vk.wall.get(owner_id=id,count=10,offset=random.randint(1,500))
    story = []
    for post in posts["items"]:
        if post.get("text"):
           story.append( post.get("text"))
    return random.choice(story)