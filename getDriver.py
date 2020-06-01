import requests
import zipfile
import os

def updateDriver():
    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    url_file = 'https://chromedriver.storage.googleapis.com/'
    file_name = 'chromedriver_win32.zip'


    version = requests.get(url)

    if version.text:
        file = requests.get(url_file + version.text + '/' + file_name)
        with open('./chromedriver/'+file_name, "wb") as code:
            code.write(file.content)

    #절대경로 구하기
    file_path = os.path.abspath('./chromedriver/'+file_name)
    folder_path = os.path.abspath('./chromedriver/')

    unzip = zipfile.ZipFile(file_path)
    unzip.extractall(folder_path)
    unzip.close()
    os.remove(file_path)

