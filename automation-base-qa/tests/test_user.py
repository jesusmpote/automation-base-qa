from models.datos import payload_post, payload_put
from models.datos_user import payload_user
import pytest
import requests
from config import BASE_URL_USER, HEADER_USER
import logging as logger


class TestUser:

    def test_generate_user(self):
        logger.info("TEST: Create new user")
        response = requests.post(url=BASE_URL_USER, headers=HEADER_USER, data=payload_user)
        response_json = response.json()
        assert response.status_code == 200, "Status Code is not 200"
        assert response_json['message'] is not None, "Message is empty"
        assert response_json['code'] == 200
        print(response.content)
        print(response.headers)
        print(response.encoding)
        print(response.content)
        # yield response_json, response
