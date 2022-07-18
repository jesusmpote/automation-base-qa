from models.datos_user import payload_user
import pytest
import requests
from config import BASE_URL_USER, HEADER_USER, BASE_URL_GET_USER
import logging as logger


@pytest.mark.user
class TestUser:

    def test_generate_user(self):
        logger.info("TEST: Create new user")
        response = requests.post(url=BASE_URL_USER, headers=HEADER_USER, data=payload_user)
        response_json = response.json()
        assert response.status_code == 200, "Status Code is not 200"
        assert response_json['message'] is not None, "Message is empty"
        assert response_json['code'] == 200

    def test_get_user(self):
        response = requests.get(url=BASE_URL_GET_USER + 'yisus')
        response_json = response.json()
        assert response.status_code == 200
        assert response_json['id'] == response_json['id'], 'No coincide el id'
        assert response_json['email'] == response_json['email'], 'Email no encontrado'
        assert response_json['userStatus'] == 1, 'User Status no corresponde'

