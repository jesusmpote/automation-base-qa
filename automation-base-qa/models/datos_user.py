import json
import random

payload_user = json.dumps({
  "id": random.randint(1, 100),
  "username": "yisus",
  "firstName": "Jesus",
  "lastName": "Rodriguez",
  "email": f"test_{random.randint(1, 100)}@gmail.com",
  "password": "Pass1234",
  "phone": "1178936987",
  "userStatus": 1
})
