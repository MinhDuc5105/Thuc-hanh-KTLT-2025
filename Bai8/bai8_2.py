print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
import turtle, random

# Nhập thư viện turtle để vẽ đồ họa và random để chọn ngẫu nhiên màu sắc.

colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
# Tạo danh sách các màu sắc để sử dụng cho bút vẽ.

painter = turtle.Turtle()
# Tạo một đối tượng turtle (con rùa) để vẽ, đặt tên là painter.

painter.pensize(3)
# Đặt độ dày bút vẽ là 3.

for i in range(10):
    # Lặp 10 lần để vẽ 10 hình tròn.

    color = random.choice(colors)
    # Chọn ngẫu nhiên một màu trong danh sách colors.

    painter.pencolor(color)
    # Đặt màu bút vẽ hiện tại thành màu được chọn.

    painter.circle(100)
    # Vẽ một hình tròn bán kính 100 đơn vị, bắt đầu từ vị trí hiện tại.

    painter.right(30)
    # Quay con rùa sang phải 30 độ (xoay góc nhỏ để thay đổi hướng vẽ).

    painter.left(60)
    # Quay con rùa sang trái 60 độ.

    painter.setposition(0, 0)
    # Đưa con rùa về lại vị trí gốc (tọa độ 0,0).