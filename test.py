import json

with open("response.json", "r") as f:
    question = json.loads(f.read())
    print(question)
    factor = question["factor"]
    starting_multiplier = question["starting_multiplier"]
    multiplier_inc = question["multiplier_inc"]
    starting_base = question["starting_base"]
    base_inc = question["base_inc"]
    print("Let me see:")

    for i in range(0, 10):
        multiplier = starting_multiplier + multiplier_inc * i
        base = starting_base +  base_inc * i
        res = factor * multiplier
        s = ""        
        while res:
            s = str(res % base) + s
            res //= base
        assert int(s) == 12 + i, "Oh dear! I shall never get to twenty at that rate!"

        print(f"{factor} times {multiplier} is {s}")
