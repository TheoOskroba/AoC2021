def read_file(filepath):
    # Create an empty list to store the pairs
    pairs = []
    
    # Open the file in read mode
    with open(filepath, 'r') as file:
        # Loop through each line in the file
        for line in file:
            # Split the line by the delimiter
            parts = line.strip().split(' ')
            
            # Convert the parts to the correct data types
            string_part = parts[0]
            int_part = int(parts[1])
            
            # Create a tuple from the parts and append it to the list
            pairs.append((string_part, int_part))
    
    # Return the list of pairs
    return pairs

def final_position(commands):
    # Set initial position
    x = 0
    y = 0
    z = 0
    
    # Loop through each command
    for command in commands:
        direction = command[0]
        distance = command[1]
        
        # Update position based on direction
        if direction == 'forward':
            x += distance
            y += distance * z
        elif direction == 'up':
            z -= distance
        elif direction == 'down':
            z += distance
    
    # Return final position
    return (x, y, z)
    
# Define a list of commands
commands = [('forward', 5), ('down', 5), ('forward', 8), ('up', 3), ('down', 8), ('forward', 2)]

file = 'day2Data.txt'

data = read_file(file)


# Get the final position
final_pos = final_position(data)

# Print the final position
print(final_pos)
print(final_pos[0]*final_pos[1])