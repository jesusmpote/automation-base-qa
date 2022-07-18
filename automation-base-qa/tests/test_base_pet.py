import pytest
from models.datos import payload_put
import requests
import logging
from config import BASE_URL, HEADERS, BASE_URL_DELETE, HEADERS_DELETE
import logging as logger


class TestPet:

    @pytest.mark.pet
    def test_post(self, generate_petstore):
        logger.info("TEST: Create new pet")
        assert generate_petstore[0]['id'] == generate_petstore[0]['id'], "No se pudo crear la mascota"
        print(generate_petstore)

    def test_put(self):
        logging.info("Generando pet")
        response = requests.put(url=BASE_URL, headers=HEADERS, data=payload_put)
        assert response.status_code == 200, "No se pudo updatear la mascota"
        assert response.encoding == 'utf-8'
        print("Headers: ", response.headers)
        print(response.encoding)

    def test_delete(self, generate_petstore):
        logger.info("TEST: Create new pet")
        payload = str(generate_petstore[0]['id'])
        response = requests.delete(url=BASE_URL_DELETE + payload, headers=HEADERS_DELETE)
        assert response.status_code == 200
        print(response.text)
        print("El Status code es: ", response.status_code)
        print("Content: ", response.content)





