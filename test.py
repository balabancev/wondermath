import json

with open("response.json", "r") as f:
    question = json.loads(f.read())
    print(question)
    
