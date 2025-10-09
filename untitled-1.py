godine=int(input("unesi svoje godine:"))
visina=int(input("unesi svoju visinu:"))
if godine >= 16:
    if 160<=visina<=190:
        print("smijes se voziti u lunaparku.")
else:
    print("nesmijes se voziti u lunaparku.")