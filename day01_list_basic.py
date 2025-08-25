# Day 1: Làm quen với List trong Python

# Tạo danh sách bạn bè
danh_sach_ban_be = ["Tuấn", "Giang", "Quân", "Mạnh", "Hồ"]
print(danh_sach_ban_be)

# In ra người đầu tiên và cuối cùng
print(danh_sach_ban_be[0], danh_sach_ban_be[-1])

# Thêm người mới
danh_sach_ban_be.append("Lâm")

# Xoá người "Mạnh"
danh_sach_ban_be.remove("Mạnh")

# Thay đổi tên người thứ 2
danh_sach_ban_be[2] = "Lực"

# In ra danh sách cuối cùng
print(danh_sach_ban_be)