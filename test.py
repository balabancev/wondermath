import json
import requests

def main(question):
    print(question)

def test():
    with open("response.json", "r") as f:
        main(json.loads(f.read()))

test()