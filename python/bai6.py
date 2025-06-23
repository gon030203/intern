def kiem_tra_ds_giam(danhSachSo):

    ketQua = all(danhSachSo[soThuTu] >= danhSachSo[soThuTu+1] for soThuTu in range(len(danhSachSo)-1))
    return ketQua
  
danhSach = input().split()
#Kiem tra xem danh sach co rong hay khong
if len(danhSach) == 0:
   print("Danh sach rong")
else:
   try:
       danhSachSo = list(map(float, danhSach))
       ketQua = kiem_tra_ds_giam(danhSachSo)
       print(ketQua)
   except:
       print("Gia tri nhap vao khong hop le")
