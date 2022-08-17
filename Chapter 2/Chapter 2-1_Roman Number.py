# จงเขียนฟังชั่นแปลง เลขอารบิกเป็นเลขโรมัน และ เลขโรมันเป็นอารบิกโดยที่

# M=1000    CM=900    D=500    CD=400,

# C=100    XC=90    L=50    XL=40,

# X=10    IX=9    V=5    IV=4    I=1

# เช่น 197 = 100 + 90 +7 = 100 + 90 + 5 + 1 + 1 = C XC V I I

# (https://roman-numerals.info/)



# class translator:

#     def deciToRoman(self, num):

#         ## Enter Your Code Here ###

#     def romanToDeci(self, s):

#         ## Enter Your Code Here ###

# num = int(input("Enter number to translate : "))

# print(translator().deciToRoman(num))

# print(translator().romanToDeci(translator().deciToRoman(num)))

number = int(input(("Enter number to translate : ")))
staticNum = number
roman = []

while number > 0:
    if number // 1000 >= 1:
        roman.append("M")
        number -= 1000
    elif number // 900 >= 1:
        roman.append("CM")
        number -= 900
    elif number // 500 >= 1:
        roman.append("D")
        number -= 500
    elif number // 400 >= 1:
        roman.append("CD")
        number -= 400
    elif number // 100 >= 1:
        roman.append("C")
        number -= 100
    elif number // 90 >= 1:
        roman.append("XC")
        number -= 90
    elif number // 50 >= 1:
        roman.append("L")
        number -= 50
    elif number // 40 >= 1:
        roman.append("XL")
        number -= 40
    elif number // 10 >= 1:
        roman.append("X")
        number -= 10
    elif number // 9 >= 1:
        roman.append("IX")
        number -= 9
    elif number // 5 >= 1:
        roman.append("V")
        number -= 5
    elif number // 4 >= 1:
        roman.append("IV")
        number -= 4
    elif number // 1 >= 1:
        roman.append("I")
        number -= 1

for i in roman:
    print(i, end="")
print()
print(staticNum)

    