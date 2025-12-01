def nhapN():
    while True:
        try:
            N = int(input())
            if(N > 0):
                break
        except ValueError:
            print("Loi nhap lieu!")
    return N

def xuatTG(N):
    for i in range(1, N+1):
        print("*"*i)

def xuatTG1(N):
    for i in range(1, N+1):
        for j in range(1, i+1):
            print("*", end="")
        print() #Xuong hang

def soHH(N):
    tong = 0
    for i in range(1,N):
        if N%i == 0:
            tong += 1
    if tong == N:
        return True
    return False