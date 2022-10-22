import math

def devide_list_for_n(array: list, number: int) -> list[list]:
    div_number: int = math.ceil(len(array) / number)
    result: list[list] = []
    start_index = 0

    for index in range(1, div_number+1):
        result.append(array[start_index:index*number])

        start_index = index * number
    
    return result

def from_string(string: str) -> int:
    return int(''.join([str(ord(symbol)) for symbol in string]))

def from_code(code: int) -> str:
    return ''.join([chr(int(symbol)) for symbol in devide_list_for_n(str(code), 2)])

# task 1
n, e = 4123265921, 16561

message = from_string("GAPONUKEUGENE")
print(f"encoded message: %d" % pow(message, e, n))

# task 2
d = 1052472841
p = 58477
q = 59651

encoded_message1 = 2883179429
encoded_message2 = 1390467723

print(f"decoded message1: %s" % from_code(pow(encoded_message1, d, p * q)))
print(f"decoded message2: %s" % from_code(pow(encoded_message2, d, p * q)))