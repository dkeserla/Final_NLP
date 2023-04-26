import json

while True:
    user_input = input("Enter a JSON string containing 'premise', 'hypothesis', and 'label' keys (or 'no' to exit): ")
    
    if user_input.lower() == "no":
        break
    
    try:
        # Parse the JSON input
        input_dict = json.loads(user_input)
        
        # Extract the required attributes
        premise = input_dict["premise"]
        hypothesis = input_dict["hypothesis"]
        label = input_dict["label"]
        
        # Print the attributes
        print(f"Premise: {premise}")
        print(f"Hypothesis: {hypothesis}")
        print(f"Label: {label}")
    except (json.JSONDecodeError, KeyError) as e:
        print("Error: Invalid input format or missing keys. Please provide a valid JSON string with 'premise', 'hypothesis', and 'label' keys.")
