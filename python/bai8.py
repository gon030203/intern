def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def liet_ke_so_nguyen_to(a, b):
    for i in range(a, b + 1):
        if kiem_tra_so_nguyen_to(i):
            print(i, end=' ')

try:
    a = int(input("Nhap so a: "))
    b = int(input("Nhap so b: "))

    if a < 0 or b < 0:
        print("Vui long nhap so tu nhien!")
    elif a > b:
        print("So thu nhat lon hon so thu hai!")
    else:
        liet_ke_so_nguyen_to(a, b)

except:
    print("Gia tri nhap vao khong hop le")
