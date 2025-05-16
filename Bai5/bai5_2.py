print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
import datetime as dt  # Nhập module datetime, đặt tên rút gọn là dt để dùng cho tiện

format = '%Y-%m-%dT%H:%M:%S'
# Định nghĩa định dạng chuỗi ngày giờ: năm-tháng-ngàyTgiờ:phút:giây (ISO format)

t1 = dt.datetime.strptime('2008-10-12T14:45:52', format)
# Chuyển chuỗi thời gian '2008-10-12T14:45:52' thành đối tượng datetime theo định dạng đã định nghĩa

print('Year ' + str(t1.year))    # In ra năm của thời điểm t1: 2008
print('Day ' + str(t1.day))      # In ra ngày (trong tháng) của thời điểm t1: 12
print('Month ' + str(t1.month))  # In ra tháng của thời điểm t1: 10
print('Minute ' + str(t1.minute))# In ra phút của thời điểm t1: 45
print('Second ' + str(t1.second))# In ra giây của thời điểm t1: 52

t2 = dt.datetime.now()
# Lấy thời gian hiện tại của máy tính và gán cho biến t2

diff = t2 - t1
# Tính khoảng thời gian (kiểu timedelta) giữa thời điểm hiện tại và thời điểm t1

print('Chênh lệch bao nhiêu ngày? ' + str(diff.days))
# In ra số ngày chênh lệch giữa t2 và t1 (tức là t2 cách t1 bao nhiêu ngày)