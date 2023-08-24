import requests
from keys.token import TOKEN


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = 'https://cloud-api.yandex.net/v1/disk'
        headers = {'Authorization': 'OAuth '+self.token}
        response = requests.get(url, headers=headers)

        return print(response.json())


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    # path_to_file =
    token = TOKEN
    uploader = YaUploader(token)
    uploader.upload()
    # result = uploader.upload(path_to_file)
