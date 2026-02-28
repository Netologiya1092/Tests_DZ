import requests
import pytest

TOKEN = 'ВАШ_ТОКЕН_ЗДЕСЬ'
URL = 'https://cloud-api.yandex.net/v1/disk/resources'
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'OAuth {TOKEN}'
}

class TestYandexDisk:
    
    def setup_method(self):
        self.folder_name = "TestFolder_Pytest"

    # Положительный тест
    def test_create_folder_success(self):
        params = {'path': self.folder_name}
        response = requests.put(URL, headers=HEADERS, params=params)
        
        # 201 - Создано (успех)
        assert response.status_code == 201
        
        # Проверяем наличие папки в списке
        check_response = requests.get(URL, headers=HEADERS, params={'path': '/'})
        items = check_response.json().get('_embedded', {}).get('items', [])
        names = [item['name'] for item in items]
        assert self.folder_name in names

    # Отрицательный тест: создание уже существующей папки
    def test_create_folder_already_exists(self):
        params = {'path': self.folder_name}
        # Пытаемся создать второй раз
        response = requests.put(URL, headers=HEADERS, params=params)
        assert response.status_code == 409 # Conflict

    # Отрицательный тест: неверный токен
    def test_create_folder_unauthorized(self):
        bad_headers = {'Authorization': 'OAuth bad_token'}
        params = {'path': "some_folder"}
        response = requests.put(URL, headers=bad_headers, params=params)
        assert response.status_code == 401 # Unauthorized

    def teardown_method(self):
        # Удаляем созданную папку после тестов, чтобы не мусорить
        requests.delete(URL, headers=HEADERS, params={'path': self.folder_name})

