try:
    print("fridge is open")
    a = int(input("enter any number u want to divide"))
    b = int(input("enter the no from hich u want to divide"))
    div=a/b
    print("div=",div)


except ValueError :
    print("you have not entered a digit")
except ZeroDivisionError:
    print("B can not be zero")
except Exception:
    print("something went wrong")
finally:
    print("Fridge is closed")