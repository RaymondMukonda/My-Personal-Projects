import json

person = {"name": "John", "age": 25, "city": "New York", "haschildren": False, "title": ["engineer", "programmer"] }

# to turn tis into json formate
personJSON = json.dumps(person)
print(personJSON)