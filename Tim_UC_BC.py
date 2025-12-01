import Ham_UC_BC
while(True):
    try:
        A = int(input('Nhap A: '))
        B = int(input('Nhap B: '))
        if A > 0 and B > 0:
            break
    except ValueError:
        print("Loi nhap lieu!")
        
print (f"USCLN cua {A} va {B} la {Ham_UC_BC.USCLN(A,B)}")