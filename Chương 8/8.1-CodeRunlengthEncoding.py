def run_length_encoding(s):
    s = s.strip()
    if not s:
        return ""
    indx = 0
    result = []
    # Bắt đầu từ chỉ mục 1, vì phải so sánh với ký tự trước đó
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:  # Nếu ký tự hiện tại khác ký tự trước đó
            result.append(f"{s[i - 1]}{i - indx}")  # Thêm ký tự và số lần lặp
            indx = i  # Cập nhật chỉ mục
    # Thêm ký tự cuối cùng và số lần lặp của nó
    result.append(f"{s[-1]}{len(s) - indx}")
    return ''.join(result)
# Nhập chuỗi đầu vào
# Thêm input để AC
s=input().strip()
s = input().strip() 
encoded_string = run_length_encoding(s)
print(encoded_string) 