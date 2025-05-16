print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
import turtle
# Nhập thư viện turtle để vẽ đồ họa bằng con rùa (turtle graphics).

window = turtle.Screen()
# Tạo một cửa sổ vẽ mới và gán vào biến window.

window.bgcolor("lightgreen")
# Đặt màu nền của cửa sổ là màu xanh nhạt (lightgreen).

painter = turtle.Turtle()
# Tạo một đối tượng turtle mới (con rùa để vẽ) và gán tên là painter.

painter.fillcolor('blue')
# Đặt màu tô bên trong hình vẽ của con rùa là màu xanh dương (blue).

painter.pencolor('blue')
# Đặt màu bút vẽ (viền) của con rùa là màu xanh dương.

painter.pensize(3)
# Đặt độ dày bút vẽ là 3 đơn vị (đậm hơn mặc định).

def drawsq(t, s):
    # Định nghĩa hàm drawsq với 2 tham số: t là turtle (con rùa),
    # s là độ dài cạnh của hình vuông cần vẽ.
    for i in range(4):
        # Lặp 4 lần để vẽ 4 cạnh của hình vuông.
        t.forward(s)
        # Con rùa di chuyển thẳng về phía trước với khoảng cách s.
        t.left(90)
        # Con rùa quay sang trái 90 độ để chuẩn bị vẽ cạnh tiếp theo.

for i in range(1, 180):
    # Lặp từ i = 1 đến i = 179 (tổng 179 lần).
    painter.left(18)
    # Con rùa quay trái 18 độ so với hướng hiện tại.
    drawsq(painter, 200)
    # Gọi hàm drawsq để vẽ một hình vuông cạnh 200 đơn vị tại vị trí hiện tại của con rùa.