from models.datos import payload_post, payload_put
import pytest
import requests
from config import BASE_URL, HEADERS
import logging as logger



@pytest.mark.pet
@pytest.fixture(scope='class')
def generate_petstore():
    logger.info("TEST: Create new pet")
    response = requests.post(url=BASE_URL, headers=HEADERS, data=payload_post)
    response_json = response.json()
    assert response.status_code == 200
    print(response.content)
    print(response.headers)
    print(response.encoding)
    print(response.content)
    yield response_json, response
