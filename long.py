import json

with open("./eval_output/correct.jsonl", "r") as input_file, open("./eval_output/long_correct.jsonl", "w") as output_file:
    for line in input_file:
        data = json.loads(line)
        premise = data["premise"]
        if len(premise) >= 100:
            output_file.write(line)
