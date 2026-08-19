from hello import getUserData
import json

# getUserData()

def getData():
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        print(f'hi there user: {data}')
    except:
        print('the has been an err found')


getData()
