import json

track_x = []
track_y = []

# Read the entire file content
with open("circuit_data.txt") as f:
    content = f.read()

# Parse the entire content as a single JSON array
data = json.loads(content)

# Iterate through the list of objects
for item in data:
    x_val = item.get("x")
    y_val = item.get("y")
    
    # Only add if the pair coordinates is not already tracked
    if x_val is not None and x_val not in track_x:
        track_x.append(x_val)
        track_y.append(y_val)

# Create list of dictionaries
coordinates = [{"x": x, "y": y} for x, y in zip(track_x, track_y)]

# Write to file using json.dump (handles commas and brackets automatically)
with open("track.json", "w") as f:
    json.dump(coordinates, f, indent=2)
