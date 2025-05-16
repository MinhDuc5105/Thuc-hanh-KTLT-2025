print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
import turtle

# Nhập thư viện turtle để vẽ đồ họa.

colors = ['red', 'blue', 'green']
# Tạo danh sách 3 màu đỏ, xanh dương, xanh lá để sử dụng lần lượt.

window = turtle.Screen()
# Tạo cửa sổ vẽ mới và gán tên là window.

window.bgcolor("white")
# Đặt màu nền cửa sổ vẽ thành màu trắng.

painter = turtle.Turtle()
# Tạo đối tượng con rùa để vẽ, đặt tên là painter.

painter.pensize(2)
# Đặt độ dày nét bút vẽ là 2.

for i in range(12):
    # Lặp 12 lần để vẽ 12 hình tròn (vì 360°/30°=12 vòng).

    painter.pencolor(colors[i % 3])
    # Chọn màu bút vẽ theo thứ tự: i%3 = 0,1,2 → màu đỏ, xanh dương, xanh lá → lặp lại.

    painter.circle(100)
    # Vẽ hình tròn có bán kính 100 tại vị trí hiện tại.

    painter.left(30)
    # Quay con rùa sang trái 30 độ để chuẩn bị vẽ hình tròn tiếp theo xoay quanh tâm.

painter.hideturtle()
# Ẩn con rùa sau khi vẽ xong để không che khuất hình vẽ.

window.mainloop()
# Giữ cửa sổ vẽ mở, chờ người dùng đóng cửa sổ.