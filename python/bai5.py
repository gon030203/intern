def ten_ban_cao_hon(tenBanThuNhat, chieuCaoBanThuNhat, tenBanThuHai, chieuCaoBanThuHai):
   #So sanh chieu cao cua hai ban
   if chieuCaoBanThuNhat > chieuCaoBanThuHai:
       #Tra ve ten cua ban thu nhat
       return tenBanThuNhat
   #Tra ve ten cua ban thu hai
   return tenBanThuHai


try:
    print("Nhap ten ban thu nhat")
    tenBanThuNhat = input()
    print("Nhap chieu cao thu nhat")
    chieuCaoBanThuNhat = int(input())

    print("Nhap ten ban thu hai")
    tenBanThuHai = input()
    print("Nhap chieu cao thu hai")
    chieuCaoBanThuHai = int(input())


    #Su dung cau truc re nhanh xu ly truong hop chieu cao nho hon 1 va chieu cao bang nhau
    if chieuCaoBanThuNhat < 1 or chieuCaoBanThuHai < 1:
        print("Chieu cao phai lon hon 0!")
    elif chieuCaoBanThuNhat == chieuCaoBanThuHai:
        print("{} cao bang {}".format(tenBanThuNhat, tenBanThuHai))
    else:   
        #Goi thuc thi ham va truyen cac tham so cho ham
        tenBanCaoHon = ten_ban_cao_hon(tenBanThuNhat, chieuCaoBanThuNhat, tenBanThuHai, chieuCaoBanThuHai)
        print("{} cao hon.".format(tenBanCaoHon))
except:
    print("Gia tri nhap vao khong hop le")
