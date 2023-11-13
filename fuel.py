str=input("Дробь: ")
s=str.rsplit(sep="/" )
x=int(s[0])
y=int (s[1])
try:
    f=x/y*100
    if f>=99:
        print('F')
        exit()
    elif f<=1:
        print('E')
        exit()
    else :
        f=int(f)

    print(repr(f) + "%" )
except (ValueError, ZeroDivisionError):
    pass
