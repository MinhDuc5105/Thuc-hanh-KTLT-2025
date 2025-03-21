print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
import math

pos = [0, 0]

while True:
    s = input().strip()  # Xóa khoảng trắng đầu/cuối
    if not s:  # Nếu không nhập gì, thoát vòng lặp
        break

    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])

    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps

# Tính khoảng cách Euclid từ vị trí (0,0) đến pos
print(int(round(math.sqrt(pos[0]**2 + pos[1]**2))))


