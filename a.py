import pandas as pd

# Dữ liệu nhân viên
data = {
    'STT': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'tennv': ['Nguyễn Văn A', 'Trần Thị B', 'Lê Văn Cường', 'Phạm Thị Dung', 'Hoàng Văn E',
              'Nguyễn Thị Hương', 'Võ Văn G', 'Lý Thị Kim Anh', 'Đặng Văn Long', 'Mai Thị Thu'],
    'gioitinh': ['Nam', 'Nữ', 'Nam', 'Nữ', 'Nam', 'Nữ', 'Nam', 'Nữ', 'Nam', 'Nữ'],
    'ngaysinh': ['1990-05-15', '1985-09-20', '1988-11-10', '1992-07-25', '1987-03-18',
                 '1995-12-30', '1989-08-05', '1993-04-12', '1986-06-28', '1990-02-14'],
    'diachi': ['Số 10, Đường A, Quận 1, TP HCM', 'Số 5, Đường B, Quận 2, TP HCM', 'Số 15, Đường C, Quận 3, TP HCM',
               'Số 20, Đường D, Quận 4, TP HCM', 'Số 25, Đường E, Quận 5, TP HCM', 'Số 30, Đường F, Quận 6, TP HCM',
               'Số 35, Đường G, Quận 7, TP HCM', 'Số 40, Đường H, Quận 8, TP HCM', 'Số 45, Đường I, Quận 9, TP HCM',
               'Số 50, Đường K, Quận 10, TP HCM'],
    'sdt': ['0901234567', '0912345678', '0987654321', '0978123456', '0965432109',
            '0943216789', '0934567890', '0923456789', '0981234567', '0918765432'],
    'tendangnhap': ['nvana', 'ttbtran', 'lvcuong', 'ptdung', 'hvehoang',
                    'nthuong', 'vvgvo', 'ltkhanh', 'dvl', 'mtthu'],
    'matkhau': ['123456', 'abcdef', 'lvcuong123', 'dungpham@123', 'matkhau123',
                'huong123', 'vanvo@123', 'kimanh!@#', 'longdang@2023', 'thu!@#'],
    'chucvu': ['Quản lý', 'Thủ thư', 'Quản lý', 'Thủ thư', 'Quản lý',
               'Thủ thư', 'Quản lý', 'Thủ thư', 'Quản lý', 'Thủ thư']
}

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data)

# Xuất DataFrame ra file Excel
excel_filename = 'nhanvien.xlsx'
df.to_excel(excel_filename, index=False)

print(f'File Excel đã được xuất thành công: {excel_filename}')