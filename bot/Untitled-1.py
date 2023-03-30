try:
    x=int(input("введіть число x>0"))
except ValueError:
    print("ви ввели число менше 0")
    x=0
else:
    print("число більше 0")
finally:
    print("дякую за огляд")