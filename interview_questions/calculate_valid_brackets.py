input_brackets = ")((())"

def calculate_brackets(input_string):
    open_count = 0
    valid_pairs = 0
    for i in input_string:
        if i == "(":
            open_count += 1

        elif i == ")":
            if open_count > 0:
                open_count -= 1
            
                valid_pairs += 1

    return valid_pairs

counter = calculate_brackets(input_brackets)
print(counter)

# Question asked in Persistent