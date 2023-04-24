import json

with open("./eval_output/eval_predictions.jsonl", "r") as input_file, open("./eval_output/correct.jsonl", "w") as output_file:
    for line in input_file:
        data = json.loads(line)
        label = data["label"]
        predicted_label = data["predicted_label"]
        if label == predicted_label:
            output_file.write(line)
