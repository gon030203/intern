#Dinh nghia ham

#tuyChon == 0: tinh tong cac chu so chan
#tuyChon == 1: tinh tong cac chu so le
def tong_chu_so(soTuNhien, tuyChon):
    tong = 0
    while soTuNhien > 0:
        #Kiem tra chu so cuoi la chan hay le
        if soTuNhien % 2 == tuyChon:
            tong += soTuNhien % 10
        soTuNhien = soTuNhien // 10
    return tong

def tich_chan_le(soTuNhien):
   return tong_chu_so(soTuNhien, 0) * tong_chu_so(soTuNhien, 1)
  

try:
    print("Nhap n: ")
    n = int(input())
    
    if n < 0:
        print("Vui long nhap so tu nhien!")
    else:
        print(tich_chan_le(n))

except:
   print("Gia tri nhap vao khong hop le")
