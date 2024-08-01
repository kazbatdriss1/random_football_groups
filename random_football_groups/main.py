import json
import random

def create_football_groups(names):
    if len(names) != 76:
        raise ValueError("The list must contain exactly 76 names.")

    random.shuffle(names)  # Shuffle the list to ensure randomness
    groups = [names[i:i + 6] for i in range(0, len(names), 6)]
    
    # If the last group has less than 6 names, we need to handle this case
    if len(groups[-1]) <= 6:
        for i in range(6 - len(groups[-1])):
            groups[-1].append(groups[i].pop())
            
    return groups

# Read names from the JSON file
# Change file names.json on random random_name.json for test with real name
with open('names.json', 'r') as file:
    data = json.load(file)
    names_list = data["names"]

# Create the football groups
football_groups = create_football_groups(names_list)

# Print the groups
for i, group in enumerate(football_groups):
    print(f"Group {i + 1}: {group}")
