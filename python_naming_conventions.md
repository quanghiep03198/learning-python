# Quy Tắc Đặt Tên Trong Python

## Quy Tắc Đặt Tên Chính:

### 1. Snake Case (cho biến và hàm)
- Dùng cho tên biến và tên hàm
- Sử dụng chữ thường
- Các từ được nối bằng dấu gạch dưới (_)
```python
# Biến
user_name = "John"
total_qty = 100
first_number = 42

# Hàm
def calc_sum():
    pass

def get_user_information():
    pass
```

### 2. Pascal Case (cho lớp)
- Dùng cho tên lớp (class)
- Mỗi từ viết hoa chữ cái đầu
- Không dùng dấu gạch dưới giữa các từ
```python
class UserEntitty:
    pass

class StudentInfo:
    pass

class DataHandler:
    pass
```

### 3. Hằng Số
- Viết hoa toàn bộ
- Các từ cách nhau bằng dấu gạch dưới
```python
MAX_VALUE = 100
PI_NUMBER = 3.14159
```

### 4. Các Thành Phần Được Bảo Vệ (Protected)
- Bắt đầu bằng một dấu gạch dưới
```python
_protected_number = 10
def _phuong_thuc_noi_bo():
    pass
```

### 5. Các Thành Phần Riêng Tư (Private)
- Bắt đầu bằng hai dấu gạch dưới
```python
__private_number = 20
def __phuong_thuc_rieng():
    pass
```

### 6. Tên Module và Package
- Module: tên ngắn gọn, chữ thường, có thể dùng gạch dưới
- Package: tên ngắn gọn, chữ thường, không dùng gạch dưới
```python
# Tên module
ui_component.py
util_func.py

# Tên package
sample_package
sample_lib
```

## Nguyên Tắc Chung
- Đặt tên có ý nghĩa và dễ hiểu
- Tránh đặt tên một chữ cái (trừ biến đếm i, j, k)
- Tránh đặt tên quá dài
- Giữ nhất quán trong toàn bộ dự án
