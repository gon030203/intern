#INPUT : Gồm hai dòng chứa hai số nguyên được nhập từ bàn phím
#OUTPUT : Gồm một dòng duy nhất hiển thị như sau: tong hai so la: {P1}

try:
    #Nhap so thu nhat 
    print("Nhap so thu nhat")
    so1 = int(input())
    #Nhap so thu hai
    print("Nhap so thu hai")
    so2 = int(input())


    tong = so1 + so2
    #In ra tong hai so
    print("Tong cua hai so la:",tong)
except:
    print("Gia tri nhap vao khong hop le")