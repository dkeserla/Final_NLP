# Created using ChatGPT

import json

with open("./contrast_sets/fine_tuned_eval_output/eval_predictions.jsonl", "r") as input_file, open("./contrast_sets/fine_tuned_eval_output/correct.jsonl", "w") as output_file:
    for line in input_file:
        data = json.loads(line)
        label = data["label"]
        predicted_label = data["predicted_label"]
        if label == predicted_label:
            output_file.write(line)
