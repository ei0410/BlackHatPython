def sum(number_one, number_two):
    number_one_int = convert_interger(number_one)
    number_two_int = convert_interger(number_two)
    
    result = number_one_int + number_two_int
    
    return result

def convert_interger(number_string):
    converted_interger = int(number_string)
    
    return converted_interger

answer = sum("1", "2")