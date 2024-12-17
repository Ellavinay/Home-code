# import calendar
# y=int(input("enter year of calender :  "))
# m=int(input("enter month of calender :  "))
#
# print(calendar.month(y,m))

data=input("enter data : ")
vowel="aeiou"

if data in vowel:
    print(f"The given data {data} is a vowel :")

else:
    print(f"The given data  {data} is not a vowel")