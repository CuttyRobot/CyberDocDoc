import datetime
import json

import requests

# MorgenWald
if __name__ == "__main__":
    # alpha = requests.post('https://test1.western-gate.online/message/led')
    # print(alpha.text)
    tabl_1 = {
        "message_id": 1,
        "date-time": str(datetime.datetime.now())
    }
    lost = requests.post('http://localhost:9012/message', json=tabl_1)
    print(lost.text)