from numpy import median

def read_file(filename):
	# Open the file in read mode
	with open(filename, "r") as f:
		# Read the integers from the file and split them by the comma character
		numbers = f.read().split(",")

		# Convert the strings to integers and return the list
		return [int(number) for number in numbers]


def least_fuel_position(positions):
	# Calculate the position that requires the least fuel
	# to align the crabs on by finding the median of the positions
	median_position = median(positions)

	# Initialize the total fuel needed to align the crabs on the median position
	total_fuel = 0

	# Iterate over the positions of the crabs and calculate the fuel needed
	# to move each crab to the median position
	for position in positions:
		total_fuel += abs(median_position - position)

	# Return the median position and the total fuel needed
	# to align the crabs on it
	return median_position, total_fuel

def least_fuel_position_updated(positions):
	# Initialize the minimum fuel needed to align the crabs on a position
	min_fuel = float("inf")

	# Initialize the position that requires the least fuel to align the crabs on
	min_position = 0

	# Iterate over all positions from the minimum to the maximum position
	for position in range(min(positions), max(positions) + 1):
		# Initialize the total fuel needed to align the crabs on the current position
		total_fuel = 0

		# Iterate over the positions of the crabs and calculate the fuel needed
		# to move each crab to the current position
		for crab_position in positions:
			# Calculate the distance between the current position and the crab position
			distance = abs(position - crab_position)

			# Calculate the fuel needed to move from the crab position
			# to the current position by summing the first `distance` natural numbers
			fuel = distance * (distance + 1) // 2

			# Add the fuel needed to move from the crab position
			# to the current position to the total fuel
			total_fuel += fuel

		# If the total fuel needed to align the crabs on the current position
		# is less than the minimum fuel needed to align the crabs on any position,
		# update the minimum fuel and the minimum position
		if total_fuel < min_fuel:
			min_fuel = total_fuel
			min_position = position

	# Return the position that requires the least fuel to align the crabs on
	# and the total fuel needed to align the crabs on this position
	return min_position, min_fuel


positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

# Read positions from file
positions = read_file('day7Data.txt')

# Calculate and display the positions
position, fuel = least_fuel_position(positions)
print(f"The position that requires the least fuel to align the crabs is {position}")
print(f"The total fuel needed to align the crabs on this position is {fuel}")

# Calculate and display the positions for Part 2
position, fuel = least_fuel_position_updated(positions)
print(f"The new position that requires the least fuel to align the crabs is {position}")
print(f"The new total fuel needed to align the crabs on this position is {fuel}")
