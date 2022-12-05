from collections import Counter, defaultdict


def read_file(filename):
  # Open the file in read mode
  with open(filename, "r") as f:
    inputs = []
    outputs = []
    for line in f:
        # Read the strings from the file and split them by the '|' character, then by spaces
        
        strings = line.split(" | ")
        input = strings[0].split()
        output = strings[1].split()
        # print(input, output)
        inputs.append(input)
        outputs.append(output)
    # print(inputs[0], outputs[0])
    # Return the lists of strings
    return inputs, outputs


def count_digits(outputs):
    # Counter to track occurrences of each number
    nums = Counter()
    
    # Iterate over all outputs
    for output in outputs:
        # Iterate over all displays in each output
        for display in output:
            # Determine which unique number is being shown on the display
            # and track it in the Counter
            if len(display) == 2:
                nums[1] += 1
            elif len(display) == 4:
                nums[4] += 1
            elif len(display) == 3:
                nums[7] += 1
            elif len(display) == 7:
                nums[8] += 1
                
    # Return the total number of occurences
    return(sum(nums.values()))


def decode(inputs, outputs):
    # Keep track of the total of every decoded output number
    sum = 0;
    
    # Iterate over all inputs/outputs
    for i in range(len(inputs)):
    
        # Dictionary to track each decoded number
        digit = {}
        
        # Iterate over each display in inputs
        for display in inputs[i]:
            # Find each of the unique numbers and their encoding
            if len(display) == 2:
                digit[1] = display
            elif len(display) == 4:
                digit[4] = display
            elif len(display) == 3:
                digit[7] = display
            elif len(display) == 7:
                digit[8] = display
        
        # Iterate over each display in inputs
        for display in inputs[i]:
            # Find each of the number with length 6 and their encodings
            if len(display) == 6:
                # Knowing that each number contains an already decoded number
                # as a subset, we can determine which number we are looking at
                # and its encoding
                if set(digit[4]).issubset(set(display)):
                    digit[9] = display
                elif set(digit[1]).issubset(set(display)):
                    digit[0] = display
                else:
                    digit[6] = display
                    
        # Iterate over each display in inputs
        for display in inputs[i]:
            # Find each of the number with length 5 and their encodings
            if len(display) == 5:
                # Using the exact same strategy as above, except this time we have even more
                # decoded numbers available to check subsets with
                if set(display).issubset(set(digit[6])):
                    digit[5] = display
                elif set(digit[1]).issubset(set(display)):
                    digit[3] = display
                else:
                    digit[2] = display
                
        # Iterate over all the ouputs and decoded them
        # Then convert into an integer and add it to the running total
        result = []
        for display in outputs[i]:
            for key, val in digit.items():
                if set(display) == set(val):
                    result.append(str(key))
        sum += int(''.join(result))
    
    # Return the total of all outputs
    return sum
        
# Read the strings from the input file
inputs, outputs = read_file("day8Data.txt")

# Part 1
print(count_digits(outputs))

# Part 2
print(decode(inputs, outputs))


# 1: cf,      2 segments
# 7: acf,     3 segments
# 4: bcdf,    4 segments
# 2: acdeg,   5 segments
# 3: acdfg,   5 segments
# 5: abdfg,   5 segments
# 0: abcefg,  6 segments
# 6: abdefg,  6 segments
# 9: abcdfg,  6 segments
# 8: abcdefg, 7 segments
