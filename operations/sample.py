def create_operators_sample():
    # 1. Toán tử số học
    a = 10
    b = 3
    print("a + b =", a + b)  # Cộng
    print("a - b =", a - b)  # Trừ
    print("a * b =", a * b)  # Nhân
    print("a / b =", a / b)  # Chia
    print("a % b =", a % b)  # Chia lấy dư
    print("a ** b =", a**b)  # Lũy thừa
    print("a // b =", a // b)  # Chia lấy nguyên

    # 2. Toán tử so sánh
    print("a == b:", a == b)  # Bằng
    print("a != b:", a != b)  # Không bằng
    print("a > b:", a > b)  # Lớn hơn
    print("a < b:", a < b)  # Nhỏ hơn
    print("a >= b:", a >= b)  # Lớn hơn hoặc bằng
    print("a <= b:", a <= b)  # Nhỏ hơn hoặc bằng

    # 3. Toán tử logic
    x = True
    y = False
    print("x and y:", x and y)  # Và
    print("x or y:", x or y)  # Hoặc
    print("not x:", not x)  # Phủ định

    # 4. Toán tử gán
    c = 5
    c += 2  # Tương đương c = c + 2
    print("c += 2:", c)
    c -= 2  # Tương đương c = c - 2
    print("c -= 2:", c)
    c *= 2  # Tương đương c = c * 2
    print("c *= 2:", c)
    c /= 2  # Tương đương c = c / 2
    print("c /= 2:", c)
    c %= 2  # Tương đương c = c % 2
    print("c %= 2:", c)
    c **= 2  # Tương đương c = c ** 2
    print("c **= 2:", c)
    c //= 2  # Tương đương c = c // 2
    print("c //= 2:", c)

    # 5. Toán tử membership
    list_example = [1, 2, 3, 4, 5]
    print("3 in list_example:", 3 in list_example)  # Kiểm tra phần tử có trong list
    print(
        "6 not in list_example:", 6 not in list_example
    )  # Kiểm tra phần tử không có trong list

    # 6. Toán tử identity
    d1 = [1, 2, 3]
    d2 = d1
    d3 = [1, 2, 3]
    d4 = d1.copy()
    d5 = d1[:]
    print("d1 is d2:", d1 is d2)  # Kiểm tra cùng đối tượng
    print("d1 is d3:", d1 is d3)  # Kiểm tra cùng đối tượng
    print("d1 is d4:", d1 is d4)  # Kiểm tra cùng đối tượng
    print("d1 is d5:", d1 is not d5)  # Kiểm tra không cùng đối tượng


if __name__ == "__main__":
    create_operators_sample()
