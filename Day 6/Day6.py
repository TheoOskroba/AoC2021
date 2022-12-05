from collections import Counter, defaultdict

def read_file(filename):
    # Open the file
    with open(filename, 'r') as f:
        # Read the file contents as a string
        contents = f.read()
    
    # Split the string on commas to get a list of strings
    string_list = contents.strip().split(',')
    
    # Convert each string to an integer and append it to the list of integers as a counter
    int_list = Counter([int(x) for x in string_list])
    
    # Return the list of integers
    return int_list

# Brute force method for Part 1
def simulate_fish_growth(fish, days):
    for i in range(days):
        for j in range(len(fish)):
            
            if fish[j] == 0:
                fish[j] = 6
                fish.append(8)
            else:
                fish[j] -= 1
    return len(fish)

# Modified part 1 answer to use counters and dictionaries to facilitate speed
def simulate_fish_growth_fast(fish_list, days):
    # What do you call a fish with no eyes?
    fsh = fish_list
    # A fsh
    for i in range(days):
        fishDict = defaultdict(int)
        for fish, count in fsh.items():
            if fish == 0:
                fishDict[6] += count
                fishDict[8] += count
            else:
                fishDict[fish - 1] += count
        # if i == 20 or i == 21:
            # print(fishDict)
                
        fsh = fishDict
    return sum(fsh.values())



#fish = [3, 4, 3, 1, 2]
# Read input from file
fish = read_file('day6Data.txt')

# Calculate the fish population
print(simulate_fish_growth_fast(fish, 256))