def create_list_methods_sample():
    # Khởi tạo mảng
    numbers = [1, 2, 3, 4, 5]
    fruits = ["apple", "banana", "orange"]

    # 1. Thêm phần tử
    numbers.append(6)  # Thêm vào cuối: [1, 2, 3, 4, 5, 6]
    # print(numbers)
    numbers.insert(0, 0)  # Chèn vào vị trí: [0, 1, 2, 3, 4, 5, 6]

    # 2. Xóa phần tử
    numbers.pop()  # Xóa phần tử cuối
    numbers.pop(0)  # Xóa theo index
    numbers.remove(2)  # Xóa theo giá trị

    # 3. Tìm kiếm
    index = numbers.index(3)  # Tìm vị trí của giá trị
    count = numbers.count(1)  # Đếm số lần xuất hiện

    # 4. Sắp xếp
    numbers.sort()  # Tăng dần
    numbers.sort(reverse=True)  # Giảm dần
    numbers.reverse()  # Đảo ngược mảng

    # 5. Các phương thức khác
    length = len(numbers)  # Độ dài mảng
    numbers.extend(fruits)  # Nối mảng
    numbers.clear()  # Xóa tất cả phần tử

    # 6. Cắt mảng (slicing)
    numbers = [1, 2, 3, 4, 5]
    sub_array = numbers[1:3]  # Lấy từ index 1 đến 2
    first_three = numbers[:3]  # Lấy 3 phần tử đầu
    last_three = numbers[-3:]  # Lấy 3 phần tử cuối
    print(numbers)

    # Tìm kiếm phần tử mảng
