# program that convert random generated base two numbers to base ten 
import random
random_list = []
random_num = ""
num_list = [0,1]
for _ in range(4):
    number = random.choice(num_list)
    random_num += str(number)
    random_list.append(number)

Base_Ten_Result = (random_list[0] * 2**3) + (random_list[1] * 2**2) + (random_list[2] * 2**1) + (random_list[3] * 2**0)
print(random_num)
print(f"The BASE TEN equivalent is {Base_Ten_Result}")