import string
import random

s1=list(string.ascii_lowercase)
s2=list(string.ascii_uppercase)
s3=list(string.digits)
s4=list(string.punctuation)

character_number=input("How many characters for the password?: ")

while True:
  try:
    character_number= int(character_number)
    if character_number < 6:
      print("Plese enter a number greater than 6")
      character_number= input("How many characters for the password?: ")

    else:
      break
  except:
    print("Plese enter numbers only")
    character_number= input("How many characters for the password?: ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1=round(character_number*(30/100))
part2=round(character_number*(20/100))

password= []

for i in range(part1):
  password.append(s1[i])
  password.append(s2[i]) 

for i in range(part2):
  password.append(s3[i])
  password.append(s4[i])

random.shuffle(password)

password="".join(password[0:])

print(password)