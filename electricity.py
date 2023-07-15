#program for calculating electricity bill in Python
units=int(input("please enter the number of units you consumed in a month"))


if(units<=100):
    payAmount=units*1.5
    fixedcharge = 0.00
elif units<=200:
    payAmount=(100*1.5)+(units-100)*2.5
    fixedcharge=0.0


Total=payAmount+fixedcharge
print("Electicity bill=%.2f" %Total)