def create_data_types_sample():
    # 1. Số (Numbers)
    integer_number = 10  # Số nguyên (int)
    float_number = 3.14  # Số thực (float)
    complex_number = 1 + 2j  # Số phức (complex)

    # 2. Chuỗi (String)
    text = "Hello World"  # String có thể dùng dấu nháy đơn hoặc kép

    # 3. Boolean
    is_true = True
    is_false = False

    # 4. List (Danh sách)
    my_list = [1, 2, "three", 4.0]  # List có thể chứa nhiều kiểu dữ liệu khác nhau
    my_list[0] = 100  # List có thể thay đổi được (mutable)

    # 5. Tuple (Bộ)
    my_tuple = (
        1,
        2,
        "three",
    )  # Tuple tương tự list nhưng không thể thay đổi (immutable)

    # 6. Dictionary (Từ điển)
    my_dict = {
        "name": "Python",
        "version": 3.9,
        "is_fun": True,
    }  # Dictionary lưu trữ cặp key-value

    # 7. Set (Tập hợp)
    my_set = {1, 2, 3, 4}  # Set chứa các phần tử duy nhất

    # Kiểm tra kiểu dữ liệu
    print(f"Type of integer_number: {type(integer_number)}")
    print(f"Type of text: {type(text)}")
    print(f"Type of my_list: {type(my_list)}")
    print(f"Type of my_tuple: {type(my_tuple)}")
    print(f"Type of my_dict: {type(my_dict)}")
    print(f"Type of my_set: {type(my_set)}")

    # Một số ví dụ về thao tác với các kiểu dữ liệu
    print(f"\nList slicing: {my_list[1:3]}")  # Lấy phần tử từ index 1 đến 2
    print(f"String length: {len(text)}")  # Độ dài chuỗi
    print(f"Dictionary value: {my_dict['name']}")  # Truy cập giá trị trong dictionary
    print(f"Set operations: {my_set & {2, 3, 5}}")  # Phép giao của hai tập hợp
