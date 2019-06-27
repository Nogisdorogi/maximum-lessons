import random
import vk_api

def get_desert(id):
    TOKEN = "a86d6faca86d6faca86d6facc5a8063a26aa86da86d6facf57e5bc5af969d1c3660e87e"
    vk_session = vk_api.VkApi(token = TOKEN)
    vk = vk_session.get_api()
    posts = vk.wall.get(owner_id=id,count=10,offset=random.randint(1,500))
    desert = []
    for post in posts["items"]:
        attachment = post.get("attachments")
        if attachment and attachment[0]["type"] == "photo":
           desert.append( attachment[0]["photo"]["id"])
    return "photo{}_{}".format(id,random.choice(desert))
    
