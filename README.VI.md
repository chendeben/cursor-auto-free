# Công Cụ Tự Động Hóa Cursor Pro

## Lời Nhắc
Gần đây có người mang phần mềm này bán trên các trang thương mại, việc này nên hạn chế. Không phải cái gì cũng cần kiếm tiền.

## Tuyên Bố Giấy Phép
Dự án này sử dụng giấy phép [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).  
Điều đó có nghĩa là bạn có thể:  
- **Chia sẻ** — Sao chép và phân phối tác phẩm này trên mọi phương tiện hoặc định dạng.  
Nhưng phải tuân thủ các điều kiện sau:
- **Phi thương mại** — Không được sử dụng tác phẩm này cho mục đích thương mại.

## Giới Thiệu Tính Năng
Tự động đăng ký tài khoản, tự động làm mới token, giải phóng đôi tay.

## Địa Chỉ Tải Về
[https://github.com/chendeben/cursor-auto-free/releases](https://github.com/chendeben/cursor-auto-free/releases)

## Lưu Ý Quan Trọng
1. **Hãy đảm bảo bạn đã cài đặt trình duyệt Chrome. Nếu chưa, [tải về tại đây](https://www.google.com/intl/en_pk/chrome/).**  
2. **Bạn cần đăng nhập vào tài khoản, dù tài khoản có hiệu lực hay không, đăng nhập là bắt buộc.**  
3. **Cần có kết nối mạng ổn định, ưu tiên sử dụng máy chủ nước ngoài. Không bật proxy toàn cầu.**

## Hướng Dẫn Cấu Hình
Không cần cấu hình để sử dụng trực tiếp.
Tải tệp `.env.example` về thư mục gốc của chương trình và đổi tên thành `.env`.

## Hướng Dẫn Chạy
### Hướng Dẫn Theo Nền Tảng
#### Cấu Hình Biến Môi Trường

Bạn có thể cấu hình các tùy chọn sau trong tệp `.env`:

```bash
# Cấu Hình Tùy Chọn
HEADLESS=true       # Bật chế độ không giao diện (mặc định: false)
PROXY='http://127.0.0.1:7890'  # Địa chỉ máy chủ proxy (tùy chọn)
```

Dự án này được sửa đổi từ [gpt-cursor-auto](https://github.com/chengazhen/cursor-auto-free), với những thay đổi về phần nhận email. Hiện nay đã có API hệ thống email tích hợp sẵn, không cần cấu hình email nữa, và tự động sử dụng email tạm thời để nhận mã xác thực.

## Nhật Ký Cập Nhật
- **2025-01-09**: Thêm log, chức năng tự xây dựng.  
- **2025-01-10**: Tối ưu hóa cấu hình email. 
- **2025-01-11**: Thêm chế độ không giao diện và cấu hình proxy thông qua tệp .env.
- **2025-01-12**: Loại bỏ yêu cầu cấu hình email.

Lấy cảm hứng từ [gpt-cursor-auto](https://github.com/hmhm2022/gpt-cursor-auto).
