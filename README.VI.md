# Công Cụ Tự Động Hóa Cursor Pro

README cũng có sẵn bằng: [中文](./README.md), [English](./README.EN.md)

## Tính Năng
Đăng ký tài khoản tự động, làm mới token tự động, hoạt động không cần can thiệp.

## Tải Về
[https://github.com/chendeben/cursor-auto-free/releases](https://github.com/chendeben/cursor-auto-free/releases)

## Lưu Ý Quan Trọng
1. **Hãy đảm bảo bạn đã cài đặt trình duyệt Chrome. Nếu chưa, [nhấp vào đây để tải về](https://www.google.com/chrome/)**
2. **Bạn cần đăng nhập vào tài khoản, dù tài khoản có hiệu lực hay không, đăng nhập là bắt buộc**
3. **Cần có kết nối mạng ổn định, ưu tiên sử dụng máy chủ nước ngoài. Không bật proxy toàn cầu**

## Cách Chạy

### Phiên Bản Mac
1. Mở terminal và điều hướng đến thư mục ứng dụng
2. Chạy lệnh để cấp quyền thực thi cho tệp:
```bash
chmod +x ./CursorPro
```
3. Chạy chương trình:
   - Trong terminal:
```bash
./CursorPro
```
   - Hoặc nhấp đúp trong Finder


Lưu ý: Nếu bạn gặp vấn đề sau; [Giải pháp](https://sysin.org/blog/macos-if-crashes-when-opening/)


![image](./screen/c29ea438-ee74-4ba1-bbf6-25e622cdfad5.png)


### Phiên Bản Windows
Đơn giản chỉ cần nhấp đúp vào `CursorPro.exe` để chạy


## Cách Xác Minh Hoạt Động
**Sau khi chạy script, khởi động lại trình soạn thảo của bạn. Bạn sẽ biết nó hoạt động khi tài khoản hiển thị trong hình ảnh bên dưới khớp với tài khoản trong nhật ký đầu ra của script của bạn.**
![image](./screen/截屏2025-01-04%2009.44.48.png)


Dự án này được chỉnh sửa từ [gpt-cursor-auto](https://github.com/chengazhen/cursor-auto-free). Phần truy xuất email đã được sửa đổi với API hệ thống email tích hợp, loại bỏ nhu cầu cấu hình email và tự động sử dụng email tạm thời để nhận mã xác minh.

## Nhật Ký Cập Nhật
- **2025-01-21**: Loại bỏ yêu cầu cấu hình 
