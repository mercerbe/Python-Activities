import random

string = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*"
passwordlength = 16
p = ''.join(random.sample(string,passwordlength))
print p
