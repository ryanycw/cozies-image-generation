import utils
import env
import os
import json

def genJson():
    utils.logs.mkdir(os.path.join(env.jsonResultPath, "ticket"))
    recordJson = {}
    for idx in range(9547):
        recordJson["tokenId"] = idx
        recordJson["name"] = f"{env.ticketName} #{str(idx)}"
        recordJson["description"] = env.ticketDesc
        recordJson["image"] = f"{env.ticketImg}"
        recordJson["animation_url"] = f"{env.ticketAni}"
        recordJson["external_url"] = "https://cozies.io/"
        json.dump(recordJson,open(f"{os.path.join(env.jsonResultPath, 'ticket')}/{str(idx)}.json",'w',encoding='utf-8'), ensure_ascii=False, indent=4)