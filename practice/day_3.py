not 5 == 5

False or True or False

a = 5
b = 7
 
if a >= b and a != b:
    print("A")
elif not a >= b and a != b:
    print("B")
else:
    print("C")

weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5:
    if bmi < 25:
        print("normal weight")
else: 
    print("overweight")