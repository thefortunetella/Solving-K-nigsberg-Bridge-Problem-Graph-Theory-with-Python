from possiblewalks import get_walks_starting_from

# Ensure that 'ABCD' is treated as a list of characters, not a string
areas = ['A', 'B', 'C', 'D']

# Generate walks starting from each area
walks_starting_from = {area: get_walks_starting_from(area) for area in areas}

# Calculate the total number of walks
num_total_walks = sum(len(walks) for walks in walks_starting_from.values())

print(num_total_walks)
