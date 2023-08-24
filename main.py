import requests
from keys.token import TOKEN


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Authorization': 'OAuth '+self.token}
        file_name = path_to_file.split('\\')
        params = {'path': '/' + file_name[-1], 'overwrite': 'false'}
        response = requests.get(url, headers=headers, params=params)
        if 200 <= response.status_code < 300:
            upload_link = (response.json()).get('href')
            with open(path_to_file, 'rb') as f:
                response = requests.post(upload_link, files={'file': f})
                if 200 <= response.status_code < 300:
                    return print('Файл загружен')
                else:
                    return print('Файл не загружен')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = r'C:\Users\Денис\Desktop\Netology\Yandexuploader\upload\photo.jpg'
    token = TOKEN
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

