def check_leap(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        return False
        
    elif year % 4 == 0:
        return True
    
year = int(input("Enter Year: "))
print(check_leap(year))