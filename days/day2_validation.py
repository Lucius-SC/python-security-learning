```python
import re

def validate_fullname(fullname):
    errors = []
    
    if not fullname.strip():
        errors.append("Họ tên không được để trống hoặc chỉ chứa khoảng trắng.")
    else:
        if not (3 <= len(fullname.strip()) <= 50):
            errors.append("Họ tên phải có độ dài từ 3 đến 50 ký tự.")
        if not re.fullmatch(r'^[a-zA-Z\s]+$', fullname.strip()):
            errors.append("Họ tên chỉ được chứa chữ cái và khoảng trắng.")
    return not errors, errors

def validate_age(age):
    errors = []
    try:
        age_int = int(age)
    except ValueError:
        errors.append("Tuổi phải là một số nguyên.")
        return False, errors
    if not (1 <= age_int <= 120):
        errors.append("Tuổi phải từ 1 đến 120.")
    return not errors, errors

def main():
    fullname = input("Nhập họ và tên: ")
    age = input("Nhập tuổi: ")
    
    is_fullname_valid, fullname_errors = validate_fullname(fullname)
    is_age_valid, age_errors = validate_age(age)
    
    if is_fullname_valid and is_age_valid:
        print("Đăng ký thành công ✅")
    else:
        print("Đăng ký không thành công. Vui lòng kiểm tra các lỗi sau:")
        
        if fullname_errors:
            print("- Lỗi Họ Tên:")
            for error in fullname_errors:
                print(f"  • {error}")
        
        if age_errors:
            print("- Lỗi Tuổi:")
            for error in age_errors:
                print(f"  • {error}")

if __name__ == "__main__":
    main()