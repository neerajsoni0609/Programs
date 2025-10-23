def number_to_words(num):
    if num == 0:
        return "zero"
    
    # Define word representations for numbers
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
             "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", 
            "eighty", "ninety"]
    scales = ["", "thousand", "million", "billion", "trillion"]
    
    words = []
    scale_pos = 0
    num = int(num)  # Ensure we're working with an integer
    
    while num > 0:
        chunk = num % 1000
        num = num // 1000
        
        if chunk != 0:
            chunk_words = []
            hundred = chunk // 100
            remainder = chunk % 100
            
            if hundred > 0:
                chunk_words.append(units[hundred] + " hundred")
            
            if remainder > 0:
                if remainder < 10:
                    chunk_words.append(units[remainder])
                elif 10 <= remainder < 20:
                    chunk_words.append(teens[remainder - 10])
                else:
                    ten_part = tens[remainder // 10]
                    unit_part = units[remainder % 10]
                    if unit_part:
                        chunk_words.append(ten_part + "-" + unit_part)
                    else:
                        chunk_words.append(ten_part)
            
            if scale_pos > 0:
                chunk_words.append(scales[scale_pos])
            
            words.insert(0, ' '.join(chunk_words))
        
        scale_pos += 1
    
    return ' '.join(words)

# Example usage
while True:
    try:
        number = input("Enter a number (or 'q' to quit): ")
        if number.lower() == 'q':
            break
        print(number_to_words(int(number)))
    except ValueError:
        print("Please enter a valid integer.")