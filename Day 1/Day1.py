def read_ints(filepath):
    # Create an empty list to store the ints
    ints = []
    
    # Open the file in read mode
    with open(filepath, 'r') as file:
        # Loop through each line in the file
        for line in file:
            # Convert the line to an int and append it to the list
            ints.append(int(line))
    
    # Return the list of ints
    return ints

def num_times_greater(nums):
    # Set initial values
    prev_sum = 0
    count = 0
    
    # Loop through the values in the list using a sliding window of size 3
    for i in range(len(nums) - 2):
        # Get the current, previous, and next values
        curr = nums[i]
        prev = nums[i + 1]
        next = nums[i + 2]
        
        # Calculate the sum of the values in the window
        curr_sum = curr + prev + next
        
        #print(curr_sum)
        
        # Check if the current sum is greater than the previous sum
        if i != 0 and curr_sum > prev_sum:
            count += 1
        
        # Update the previous sum
        prev_sum = curr_sum
    
    # Return the count
    return count
    
    # Define a list of ints
nums = [199,200,208,210,200,207,240,269,260,263]

data = read_ints('day1Data.txt')

# Get the number of times where the current value is greater than the previous value
count = num_times_greater(data)

# Print the count
print(count)