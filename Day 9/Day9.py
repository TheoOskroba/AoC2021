import numpy as np

# Function to read a heightmap from a file
def read_heightmap(filepath):
    # Open the file
    with open(filepath, 'r') as file:
        # Create a list to store the heightmap
        heightmap = []
        # Iterate through each line in the file
        heightmap = [list(line.strip()) for line in file]
        # Return the heightmap
        return heightmap

# Function to find lowpoints and calculate risk
def calculate_risk(heightmap):
    # Risk level sum
    risk_sum = 0
    
    # Track which points are the lowest
    low_points = []
    
    # Iterate through each location in the heightmap
    for row in range(len(heightmap)):
        for col in range(len(heightmap[row])):
            # Skip locations with height 9
            if heightmap[row][col] == 9:
                continue
            # Check if current location is a low point
            is_low_point = True
            # Check up
            if row > 0 and heightmap[row-1][col] < heightmap[row][col]:
                is_low_point = False
            # Check down
            if row < len(heightmap)-1 and heightmap[row+1][col] < heightmap[row][col]:
                is_low_point = False
            # Check left
            if col > 0 and heightmap[row][col-1] < heightmap[row][col]:
                is_low_point = False
            # Check right
            if col < len(heightmap[row])-1 and heightmap[row][col+1] < heightmap[row][col]:
                is_low_point = False
            # If current location is a low point, add its risk level to the sum
            if is_low_point:
                risk_sum += int(heightmap[row][col]) + 1
                # print(heightmap[row][col])
                low_points.append((row, col))
            
    # Print the total risk level sum
    return risk_sum, low_points

# Check to see if the low point is part of a larger basin
# Iterate recursively until the size of the basin is found
def check_low_point(x, y, heightmap):
    # Track the size of the basin
    basin_size = 0
    
    # Precalculate bounds
    rightBound = len(heightmap[0])
    bottomBound = len(heightmap)
        
    # Base case: Check to see if the current point is either 9 or 
    # a '.'
    if heightmap[x][y] == '.' or heightmap[x][y] == '9':
        return basin_size
    
    # Set the current point to '.' to signify that it has already been traversed
    heightmap[x][y] = '.'
    # Increase basin size
    basin_size += 1
    
    # If within bounds, continue recursively checking points
    if y+1 < rightBound:
        basin_size += check_low_point(x, y+1, heightmap)
    if y-1 >= 0:
        basin_size += check_low_point(x, y-1, heightmap)
    if x+1 < bottomBound:
        basin_size += check_low_point(x+1, y, heightmap)
    if x-1 >= 0:
        basin_size += check_low_point(x-1, y, heightmap)
    # Return the final basin size
    return basin_size

# Find the sizes of all basins in a given heightmap
def find_basins(heightmap, low_points):
    # Track the sizes of the basins
    basin_sizes = []
    # Iterate over all low points (the bottom of every basin)
    # and find the size of the basin they belong to
    for row in low_points:
        basin_sizes.append(check_low_point(row[0], row[1], heightmap))
    # Return a list of basin sizes
    return basin_sizes

# Read a heightmap from file
heightmap = read_heightmap('day9Data.txt')

# Calculate the risk
risk = calculate_risk(heightmap)[0]
# Calculate the lowpoints
low_points = calculate_risk(heightmap)[1]

# Find the sizes of all the basins
basins = find_basins(heightmap, low_points)

# Print risk
print(risk)

# Sort the basin list from greatest to least
basin_sort = sorted(basins, reverse=True)

# Print the product of the largest three entries in the basin list
print(np.prod(basin_sort[:3]))

