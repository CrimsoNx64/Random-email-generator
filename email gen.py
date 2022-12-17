import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    numbers=string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    result_str2 = ''.join(random.choice(numbers) for i in range(length))
    result_str3=result_str+result_str2
    result_str3=result_str3+"@gmail.com"
    print(result_str3)



get_random_string(8)
get_random_string(8)
get_random_string(8)
get_random_string(8)
get_random_string(8)


repeat=int(input("Repeat? 1 = yes, 2 = no: "))
print("")
get_random_string(8)
get_random_string(8)
get_random_string(8)
get_random_string(8)
get_random_string(8)
print("")

while  repeat == 1:
    repeat=int(input("Repeat? 1 = yes, 2 = no: "))
    print("")
    get_random_string(8)
    get_random_string(8)
    get_random_string(8)
    get_random_string(8)
    get_random_string(8)
    print("")

else:
    print("end")
    
    
