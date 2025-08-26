# 🐍 Python Security Learning Journey

Xin chào! Đây là hành trình 30 ngày tự học **Python + Security** của Lucius.  

## 🎯 Mục tiêu
- Học Python từ cơ bản → nâng cao
- Ứng dụng Python vào bảo mật (web scanner, log analysis, password check…)
- Rèn tư duy hacker mũ trắng (offensive security mindset)

## 📅 Lộ trình
- **Day 01 → 09**: Python cơ bản (biến, toán tử, list, tuple, dict, set, vòng lặp)
- **Day 10 → 20**: Xử lý file, regex, requests, parsing HTML
- **Day 21 → 30**: Dự án mini (Web scanner, log analyzer, simple brute force demo)

## 📂 Cấu trúc
- `days/`: Bài tập từng ngày
- `mini_tools/`: Script nhỏ áp dụng thực tế
- `docs/`: Tài liệu tham khảo
# Python Security Learning Project 🐍🔒

Repo này lưu lại toàn bộ hành trình 30 ngày học Python & bảo mật (theo dạng day-by-day).  
Mỗi **Day** có code riêng kèm commit rõ ràng để dễ theo dõi tiến trình.  

---

## 📅 Progress

### ✅ Day 1: Username & Password Validation
- Viết hàm kiểm tra `username`:
  + Độ dài 5–15 ký tự
  + Không bắt đầu bằng số
  + Chỉ chứa chữ, số và `_`

- Viết hàm kiểm tra `password`:
  + Tối thiểu 8 ký tự
  + Có chữ hoa, chữ thường, số, ký tự đặc biệt

👉 File: `day1_validation.py`

---

### ✅ Day 2: Fullname & Age Validation
- Viết hàm kiểm tra `fullname`:
  + Không để trống hoặc chỉ có khoảng trắng
  + Độ dài từ 3–50 ký tự
  + Chỉ chứa chữ cái và khoảng trắng

- Viết hàm kiểm tra `age`:
  + Là số nguyên
  + Giá trị từ 1–120

👉 File: `day2_validation.py`