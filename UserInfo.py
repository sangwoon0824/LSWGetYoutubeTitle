import json

class userInfo(object):

    file_path = "./config/USERINFO.json"
    data = dict()
    userData = dict()
    soundData = dict()

    def setID(self,_id):
        self.userData["id"] = _id

    def setPW(self,_pw):
        self.userData["pw"] = _pw

    def setURL(self,url):
        self.userData["url"] = url

    def dataSet(self):
        self.data["userData"] = self.userData

        with open('./USERINFO.json', 'w', encoding="utf-8") as outfile:
            json.dump(self.data, outfile, ensure_ascii=False, indent="\t")

    def getID(self):
        with open('./USERINFO.json','r') as f:
            json_file = json.load(f)
            savedID = json_file["userData"]["id"]
        return savedID

    def getPW(self):
        with open('./USERINFO.json','r') as f:
            json_file = json.load(f)
            savedPW = json_file["userData"]["pw"]  
        return savedPW

    def getURL(self):
        with open('./USERINFO.json','r') as f:
            json_file = json.load(f)
            savedURL = json_file["userData"]["url"]  
        return savedURL