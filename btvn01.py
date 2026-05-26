student_name = "nguYEn vAn a"
student_code = "rk-001-python"
email = "Student01@GMAIL.COM"

student_name.strip()
student_name.title()

student_code.strip()
student_code.upper()

email.strip()
email.lower()

print("Họ và tên:", student_name)
print("Mã học viện:", student_code)
print("email:", email)

# student_name.strip() không làm thay đổi trực tiếp biến student_name vì không được gán lại
# student_name.title() không tạo ra kết quả "Nguyen Van A" trong chương trình hiện tại vì không được gán lại
# student_code.upper() không làm mã học viên chuyển thành chữ hoa vì không được gán lại
# email.lower() không làm email chuyển thành chữ thường vì không được gán lại
# Sửa code

student_name = "nguYEn vAn a"
student_code = "rk-001-python"
email = "Student01@GMAIL.COM"

student_name = student_name.strip().title()
student_code = student_code.strip().upper()
email = email.strip().lower()

print("Họ và tên:", student_name)
print("Mã học viện:", student_code)
print("email:", email)