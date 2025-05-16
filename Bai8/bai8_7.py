print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
import tkinter
import random
# Nhập thư viện tkinter để tạo GUI và random để trộn màu.

colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
# Danh sách màu sẽ xuất hiện trong trò chơi.

score = 0
timeleft = 120  # thời gian chơi tính bằng giây (120 giây = 2 phút)

def startGame(event):
    # Hàm bắt đầu trò chơi khi nhấn Enter.
    if timeleft == 120:
        countdown()
        nextColour()
    # Nếu là lần đầu (thời gian chưa chạy), bắt đầu đếm ngược và gọi hiển thị màu kế tiếp.

def nextColour():
    global score
    global timeleft

    if timeleft > 0:
        e.focus_set()
        # Đặt con trỏ vào ô nhập liệu để người chơi gõ tiếp.

        # Kiểm tra đáp án:
        # Nếu chữ người chơi gõ (in thường) trùng màu của chữ hiển thị (colours[1]):
        if e.get().lower() == colours[1].lower():
            score += 2  # đúng cộng 2 điểm
        elif e.get() != "":
            score -= 1  # sai trừ 1 điểm

        e.delete(0, tkinter.END)
        # Xóa ô nhập liệu để chuẩn bị nhận câu tiếp theo.

        random.shuffle(colours)
        # Xáo trộn danh sách màu ngẫu nhiên.

        label.config(fg=colours[1], text=colours[0])
        # Hiển thị chữ: text là colours[0], màu chữ là colours[1]
        # Mục tiêu là người chơi phải gõ tên màu (màu chữ) chứ không phải từ hiện ra.

        scoreLabel.config(text="Score: " + str(score))
        # Cập nhật điểm trên màn hình.

def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)
    # Đếm ngược thời gian: mỗi giây trừ 1, cập nhật nhãn thời gian, gọi lại chính nó sau 1000ms.

# === Tạo giao diện ===
root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("375x200")
# Tạo cửa sổ chính, đặt tên và kích thước.

instructions = tkinter.Label(root, text="Type in the colour of the words, not the word text!", font=('Helvetica', 12))
instructions.pack()
# Hiển thị hướng dẫn chơi.

scoreLabel = tkinter.Label(root, text="Press Enter to start", font=('Helvetica', 12))
scoreLabel.pack()
# Hiển thị điểm số hoặc trạng thái bắt đầu.

timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()
# Hiển thị thời gian còn lại.

label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()
# Nhãn lớn để hiển thị từ (màu sắc và chữ).

e = tkinter.Entry(root)
e.pack()
e.focus_set()
# Ô nhập liệu, người chơi sẽ nhập tên màu.

root.bind('<Return>', startGame)
# Gán sự kiện nhấn phím Enter để gọi hàm startGame.

root.mainloop()
# Bắt đầu vòng lặp GUI.