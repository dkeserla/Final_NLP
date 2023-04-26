import json

jsonl_file = "./eval_output/sample_long_correct.jsonl"
tsv_file = "./eval_output/sample_long_correct.tsv"

with open(jsonl_file, "r") as f1, open(tsv_file, "w") as f2:
    for line in f1:
        data = json.loads(line)
        premise = data["premise"]
        hypothesis = data["hypothesis"]
        label = data["label"]
        f2.write(f"{premise}\t{hypothesis}\t{label}\n")