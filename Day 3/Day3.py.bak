def read_bin(filepath):
    # Open the file in read-only mode
  with open(filepath, 'r') as file:
    # Read the lines from the file
    lines = file.readlines()
    
    # Strip the newline character from each line
    lines = [line.strip() for line in lines]
    
    # Return the list of binary strings
    return lines
    
def generate_gamma_epsilon_rates(binary_numbers):
  # Find the length of the longest binary number
  max_length = len(binary_numbers[0])
  
  # Initialize the gamma rate as a string of zeros with the same length as the binary numbers
  gamma_rate = '0' * max_length
  
  
  # For each position in the binary numbers
  for i in range(max_length):
    # Count the number of zeros and ones at this position
    zero_count = sum(binary_number[i] == '0' for binary_number in binary_numbers)
    one_count = sum(binary_number[i] == '1' for binary_number in binary_numbers)
    
    # Set the corresponding bit in the gamma rate to be the most common bit at this position
    if zero_count > one_count:
      #gamma_rate[i] = '0'
      gamma_rate = gamma_rate[:i] + '0' + gamma_rate[i+1:]
    else:
      #gamma_rate[i] = '1'
      gamma_rate = gamma_rate[:i] + '1' + gamma_rate[i+1:]
    
  # The epsilon rate is simply the inverse of the gamma rate
  epsilon_rate = ''.join(str(int(bit) ^ 1) for bit in gamma_rate)

  
  # Return the gamma rate and epsilon rate as integers
  #print(gamma_rate)
  #print(epsilon_rate)
  return int(gamma_rate, 2), int(epsilon_rate, 2)
  
  
def calculate_oxygen_rating(binary_strings):
  # Keep track of the current list of binary strings
  current_strings = binary_strings
  
  # Keep track of current index
  index = 0
  
  # Repeat until only one binary string remains
  while len(current_strings) > 1:
    # Count the number of zeros and ones at the current index
    zero_count = sum(binary_string[index] == '0' for binary_string in current_strings)
    one_count = sum(binary_string[index] == '1' for binary_string in current_strings)
    
    # If more zeros appear at this index, add a 1 to the index counter and select all binary strings that start with 0
    if zero_count > one_count:
      index += 1
      current_strings = [binary_string for binary_string in current_strings if binary_string[index - 1] == '0']
      
    # If more ones appear at this index, add a 1 to the index counter and select all binary strings that start with 1
    else:
      index += 1
      current_strings = [binary_string for binary_string in current_strings if binary_string[index - 1] == '1']
      
  # Return the oxygen rating as an integer
  oxygen_rating = current_strings[0]
  return int(''.join(str(bit) for bit in oxygen_rating), 2)  


def calculate_co2_rating(binary_strings):
  # Keep track of the current list of binary strings
  current_strings = binary_strings
  
  # Keep track of current index
  index = 0
  
  # Repeat until only one binary string remains
  while len(current_strings) > 1:
    # Count the number of zeros and ones at the current index
    zero_count = sum(binary_string[index] == '0' for binary_string in current_strings)
    one_count = sum(binary_string[index] == '1' for binary_string in current_strings)
    
    # If fewer zeros appear at this index, add a 1 to the index counter and select all binary strings that start with 0
    if zero_count <= one_count:
      index += 1
      current_strings = [binary_string for binary_string in current_strings if binary_string[index - 1] == '0']
      
    # If fewer ones appear at this index, add a 1 to the index counter and select all binary strings that start with 1
    else:
      index += 1
      current_strings = [binary_string for binary_string in current_strings if binary_string[index - 1] == '1']
      
  # Return the co2 rating as an integer
  co2_rating = current_strings[0]
  return int(''.join(str(bit) for bit in co2_rating), 2)
    
binNums = read_bin('day3Data.txt')

gamma_rate, epsilon_rate = generate_gamma_epsilon_rates(binNums)

oxygen_rating = calculate_oxygen_rating(binNums)
co2_rating = calculate_co2_rating(binNums)


# Print the gamma and epsilon rates
print(f'Gamma rate: {gamma_rate}')
print(f'Epsilon rate: {epsilon_rate}')
print(f'Power Consumption: {gamma_rate*epsilon_rate}')

print(f'Oxygen rating: {oxygen_rating}')
print(f'CO2 rating: {co2_rating}')
print(f'Life support rating: {oxygen_rating*co2_rating}')
