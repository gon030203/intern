# Hàm thêm học sinh vào danh sách
def them_hoc_sinh(hoc_sinh_list):
    ten = input("Nhập tên học sinh: ")
    if not ten.isalpha():
        print("Tên học sinh không hợp lệ!")
        return
    tuoi = input("Nhập tuổi học sinh: ")
    while not tuoi.isdigit() or int(tuoi) <= 0:
        print("Tuổi không hợp lệ. Vui lòng nhập lại.")
        tuoi = input("Nhập tuổi học sinh: ")
    tuoi = int(tuoi)
    
    diem = input("Nhập điểm thi học sinh: ")
    while not diem.replace('.', '', 1).isdigit():
        print("Điểm không hợp lệ. Vui lòng nhập lại.")
        diem = input("Nhập điểm thi học sinh: ")
    diem = float(diem)
    
    lop_hoc = input("Nhập lớp học của học sinh: ")
    hoc_sinh_list.append({'Tên': ten, 'Tuổi': tuoi, 'Điểm': diem, 'Lớp': lop_hoc})
    print(f"Đã thêm học sinh {ten} vào hệ thống.")

# Hàm tìm kiếm học sinh theo tên hoặc lớp học
def tim_kiem_hoc_sinh(hoc_sinh_list):
    tim_kiem = input("Nhập tên hoặc lớp học cần tìm: ").lower()
    ket_qua = [hs for hs in hoc_sinh_list if tim_kiem in hs['Tên'].lower() or tim_kiem in hs['Lớp'].lower()]
    
    if ket_qua:
        for hs in ket_qua:
            print(f"Tên: {hs['Tên']}, Tuổi: {hs['Tuổi']}, Điểm: {hs['Điểm']}, Lớp: {hs['Lớp']}")
    else:
        print("Không tìm thấy học sinh nào.")

# Hàm hiển thị danh sách học sinh
def hien_thi_danh_sach(hoc_sinh_list):
    if not hoc_sinh_list:
        print("Chưa có học sinh nào trong hệ thống.")
        return
    for hs in hoc_sinh_list:
        print(f"Tên: {hs['Tên']}, Tuổi: {hs['Tuổi']}, Điểm: {hs['Điểm']}, Lớp: {hs['Lớp']}")

# Hàm tính điểm trung bình lớp học
def tinh_diem_trung_binh(hoc_sinh_list):
    lop_hoc = input("Nhập lớp học cần tính điểm trung bình: ")
    diem_tong = 0
    so_hoc_sinh = 0
    for hs in hoc_sinh_list:
        if hs['Lớp'].lower() == lop_hoc.lower():
            diem_tong += hs['Điểm']
            so_hoc_sinh += 1
    if so_hoc_sinh > 0:
        diem_trung_binh = diem_tong / so_hoc_sinh
        print(f"Điểm trung bình lớp {lop_hoc} là: {diem_trung_binh:.2f}")
    else:
        print(f"Lớp {lop_hoc} không có học sinh nào.")


def quan_ly_hoc_sinh():
    hoc_sinh_list = []
    while True:
        print("\nChọn chức năng:")
        print("1. Thêm học sinh")
        print("2. Tìm kiếm học sinh")
        print("3. Hiển thị danh sách học sinh")
        print("4. Tính điểm trung bình lớp học")
        print("5. Thoát")

        lua_chon = input("Nhập lựa chọn của bạn (1/2/3/4/5): ")

        if lua_chon == '1':
            them_hoc_sinh(hoc_sinh_list)
        elif lua_chon == '2':
            tim_kiem_hoc_sinh(hoc_sinh_list)
        elif lua_chon == '3':
            hien_thi_danh_sach(hoc_sinh_list)
        elif lua_chon == '4':
            tinh_diem_trung_binh(hoc_sinh_list)
        elif lua_chon == '5':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

# Chạy chương trình quản lý học sinh
quan_ly_hoc_sinh()
