import itertools
import re
from collections import Counter

# Read in lines from file and return list of strings
def read_file(filename):
	with open(filename, 'r') as f:
		return [line.strip() for line in f]

# Find where points on a grid have overlapping lines
def find_overlaps(lines):
    # Track all points that have a line over them
    allPoints = []
    
    # Iterate over every line
    for line in lines:
        # Extract each coordinate point from the line
        c1, c2 = line.split('->')
        x1, y1 = tuple(map(int, c1.split(',')))
        x2, y2 = tuple(map(int, c2.split(',')))
        
        # If the line is horizontal/vertical, then we note which points the line covers
        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                for y in range(min(y1, y2), max(y1, y2)+1):
                    allPoints.append((x,y))
                    
    # Return how many points have at least 2 lines over them
    overlaps = [point for point in Counter(allPoints).values() if point >= 2]
    return len(overlaps)

# Find where points on a grid have overlapping lines including diagonals
def find_overlaps_diagonal(lines):
    # Track all points that have a line over them
    allPoints = []
    
    # Iterate over every line
    for line in lines:
        c1, c2 = line.split('->')
        x1, y1 = tuple(map(int, c1.split(',')))
        x2, y2 = tuple(map(int, c2.split(',')))
        
        # If the line is horizontal/vertical, then we note which points the line covers
        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                for y in range(min(y1, y2), max(y1, y2)+1):
                    allPoints.append((x,y))
        # If the line is diagonal
        else:
            # Determine the direction the line is headed 
            xdir = ydir = -1;
            if (x1 < x2):
                xdir = 1 
            if (y1 < y2):
                ydir = 1
            # Find which points are covered by the line by iterating in the given x direction
            y = y1
            for x in range(x1, x2 + xdir, xdir):
                allPoints.append((x,y))
                y += ydir
    
    # Return how many points have at least 2 lines over them
    overlaps = [point for point in Counter(allPoints).values() if point >= 2]
    return len(overlaps)


# Parse the input into a list of lines
lines = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]

# Read lines from file
lines = read_file('day5Data.txt')

# Output final results
print(find_overlaps(lines))
print(find_overlaps_diagonal(lines))
