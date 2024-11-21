import json.decoder
from datetime import datetime

from requests import Response


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Нет cookie с именем {cookie_name} в ответе"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, header_name):
        assert header_name in response.headers, f"Нет заголовка с именем {header_name} в ответе"
        return response.headers[header_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Ответ не в формате JSON. Текст ответа - '{response.text}'"

        assert name in response_as_dict, f"В ответе нет ключа '{name}'"
        return response_as_dict[name]

    def prepare_registration_data(self, email=None):
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%d%m%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
        return {
            'username': 'Dima',
            'firstName': 'Dima',
            'lastName': 'Dima',
            'email': email,
            'password': '123'
        }