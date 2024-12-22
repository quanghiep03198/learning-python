import array


def create_array_sample():
    # Tạo một mảng số nguyên
    my_array = array.array("I", [1, 2, 3, 4, 5])

    # Truy cập phần tử
    print(my_array[0])  # Output: 1

    # Thêm phần tử
    my_array.append(6)

    # Xóa phần tử
    my_array.remove(3)

    # Duyệt qua các phần tử
    for item in my_array:
        print(item)
