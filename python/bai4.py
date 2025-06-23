#Nhap dong du lieu chua day gia tri tu ban phim
dayGiaTri = input()

#Su dung ham split() de cat day gia tri thanh cac chuoi con
danhSachGiaTri = dayGiaTri.split()


try:
    #Su dung ham map() de thuc hien viec chuyen cac chuoi con sang kieu so nguyen
    danhSachSo = map(int, danhSachGiaTri)

    #Su dung ham sum() de tinh tong day so
    tongDaySo = sum(danhSachSo)

    #In ket qua ra man hinh
    print(tongDaySo)
except:
    print("Gia tri nhap vao khong hop le")