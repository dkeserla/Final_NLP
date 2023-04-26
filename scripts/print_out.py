# Created using ChatGPT

import json

with open("./eval_output/incorrect.jsonl", "r") as input_file, open("./eval_output/output.jsonl", "w") as output_file:
    for line in input_file:
        data = json.loads(line)
        premise = data["premise"]
        hypothesis = data["hypothesis"]
        output_data = {"premise": premise, "hypothesis": hypothesis}
        output_file.write(json.dumps(output_data) + "\n")
