import requests
from config import BASE_URL_GET


class TestPet:

    def test_de_prueba_get(self, generate_petstore):
        url_api = BASE_URL_GET
        id_mascota = str(generate_petstore[0]['id'])
        request_url = url_api + id_mascota
        response = requests.get(url=request_url)
        response_json = response.json()
        assert response_json['id'] == response_json['id']
        print(response.json())
        print("El estado es: ", response.status_code)
        print(response.headers)
        print(response.request.body)

