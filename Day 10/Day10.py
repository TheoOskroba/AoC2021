def read_file_to_2d_list(file_name):
    # Create an empty list to store the lines
    lines = []

    # Open the file for reading
    with open(file_name, 'r') as file:
        # Read each line from the file
        for line in file:
            # Split the line into a list of words
            words = [*line.strip()]
            # Add the list of words to the list of lines
            lines.append(words)

    # Return the list of lines
    return lines

# Calculate the score of part 2 by completeing the pattern
def complete_pattern(stack):
    # Keep track of the score
    score = 0
    
    # Pop elements remaining on stack and calculate their scores
    while stack:
        c = stack.pop()
        score *= 5
        if c == '(':
            score += 1
        elif c == '[':
            score += 2
        elif c == '{':
            score += 3
        elif c == '<':
            score += 4

    # Return the score for the current string
    return score

# Find the syntax errors and return the illegal character
def find_syntax_error(line):
    # Create a stack to store the opening characters
    stack = []
    # Iterate over the characters in the line
    for c in line:
    # If the character is an opening character, push it onto the stack
        if c in '([{<':
            stack.append(c)
        # If the character is a closing character, pop the top item from the stack and check if it matches
        elif c in ')]}>':
            # If the stack is empty or the top item does not match the closing character, the line is corrupted
            if not stack or c != {'(': ')', '[': ']', '{': '}', '<': '>'}[stack.pop()]:
                return c

    # If the stack is not empty, the line is incomplete
    if stack:
        # Return the score calculated by passing the remaining
        # stack to the complete_pattern function
        return complete_pattern(stack)
        # return 'incomplete'

    # If the line is not corrupted or incomplete, it is valid
    return 0

# Calculate the score for both part 1 and part 2
def find_errors(lines):
    # Keep track of illegal character score
    score = 0
    
    # Keep track of autocomplete string scores
    score_list = []
    
    # Iterate over the data and calculate the scores
    for line in lines:
        # If the returned value is an illegal character
        # we update the score appropriately
        c = find_syntax_error(line)
        if c == ')':
            score += 3
        elif c == ']':
            score += 57
        elif c == '}':
            score += 1197
        elif c == '>':
            score += 25137
        # Otherwise the output will be a score value for the autocomplete string
        # so we append it to the list of autocomplete scores
        else:
            score_list.append(c)
    
    # Return both scores
    return score, score_list



# Read the lines of the file into a 2D list
lines = read_file_to_2d_list('day10Data.txt')

# Find the illegal character score and the list of autocomplete scores
score, score_list = find_errors(lines)

# Print illegal character score
print(score)

# Print the middle score after first sorting the list and finding the middle index
print(sorted(score_list)[int((len(score_list)- 1)/2)])