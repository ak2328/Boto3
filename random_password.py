from random import choice

len_pass= 8

vali_car = "lffdjdikdofvovndmwlwpdpe9292887@$$#%#^&@*&*(@()@))VVFVSBBSSNWJHJEJAKMSBFMDKOUBDBBD@#$%^&**()?"

'''
# Method 1
for each in range(len_pass):
    print(choice(vali_car),end='')
'''

password = []

''' 
#Method 2
for each in range(len_pass):
    password.append(choice(vali_car))

random_pass = "".join(password)

print(random_pass)

'''
# Method 3
random_pass = "".join(choice(vali_car) for each in range(len_pass))
print(random_pass)
