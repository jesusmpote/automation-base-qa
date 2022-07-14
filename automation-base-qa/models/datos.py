import json
import random


payload_post = json.dumps({
      "id": random.randint(1, 100),
      "category": {
        "id": random.randint(1, 100),
        "name": "big dog"
      },
      "name": "Perrito test",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": random.randint(1, 100),
          "name": "string"
        }
      ],
      "status": "available"
})

payload_put = json.dumps({
      "id": 66,
      "category": {
        "id": random.randint(1, 100),
        "name": "Little dog"
      },
      "name": "Perrito test PUT",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 68,
          "name": "string"
        }
      ],
      "status": "available"
})
