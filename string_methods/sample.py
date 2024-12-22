def create_string_methods_sample():
    # 1. upper(), lower() - Chuyển đổi chữ hoa/thường
    # Use case: Chuẩn hóa input từ người dùng
    text = "Hello World"
    print("upper():", text.upper())  # HELLO WORLD
    print("lower():", text.lower())  # hello world

    # 2. strip(), lstrip(), rstrip() - Xóa khoảng trắng
    # Use case: Làm sạch dữ liệu input
    text_with_spaces = "   hello   "
    print("strip():", text_with_spaces.strip())  # "hello"

    # 3. split() - Tách chuỗi thành list
    # Use case: Xử lý dữ liệu CSV hoặc text
    sentence = "Python is awesome"
    print("split():", sentence.split())  # ['Python', 'is', 'awesome']

    # 4. join() - Nối list thành chuỗi
    # Use case: Tạo chuỗi từ danh sách
    words = ["Python", "is", "awesome"]
    print("join():", " ".join(words))  # "Python is awesome"

    # 5. replace() - Thay thế chuỗi
    # Use case: Thay thế nội dung trong text
    text = "Hello World"
    print("replace():", text.replace("World", "Python"))  # "Hello Python"

    # 6. find(), index() - Tìm vị trí chuỗi con
    # Use case: Tìm kiếm trong text
    text = "Python Programming"
    print("find():", text.find("Program"))  # 7
    # find() trả về -1 nếu không tìm thấy, index() raise ValueError

    # 7. startswith(), endswith() - Kiểm tra tiền tố/hậu tố
    # Use case: Kiểm tra định dạng file, URL
    filename = "document.pdf"
    print("endswith():", filename.endswith(".pdf"))  # True

    # 8. count() - Đếm số lần xuất hiện
    # Use case: Phân tích text
    text = "hello hello world"
    print("count():", text.count("hello"))  # 2

    # 9. format() - Định dạng chuỗi
    # Use case: Tạo chuỗi động
    name = "Alice"
    age = 25
    print("format():", "I am {0} and I'm {1} years old".format(name, age))
    # Hoặc f-string trong Python 3.6+
    print("f-string:", f"I am {name} and I'm {age} years old")
