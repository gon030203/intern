#Dinh nghia ham
def tinh_tong(n):
   if n:
       return n + tinh_tong(n-1)
   return 0

try:
   n = int(input())
   if n < 0:
       print("Vui long nhap so tu nhien!")
   else:   
       print(tinh_tong(n))
except:
   print("Gia tri nhap vao khong hop le")
