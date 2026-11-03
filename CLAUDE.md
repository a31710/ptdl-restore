# Dự án khôi phục ptdl.com.vn

## Bối cảnh
- Site: https://ptdl.com.vn — công ty vận chuyển PTDL (vận tải Bắc Nam, nội thành, xe tải/container).
- Site WordPress (theme transpi, Elementor, WPCargo, Contact Form 7, MC4WP). WordPress 7.1.4 đang có sẵn, PHP 7.4.33 (đã hết hỗ trợ).
- Sự cố: site bị defacement ("Hacked by Trenggalek6etar") và lỗi `Disk quota exceeded` khi cập nhật WordPress.
- Hosting: NhanHoa Software (AS131353, IP 103.124.95.33, host gir02.nhanhoa.com). Tài khoản hosting: nhxuoq3c. Thư mục site: /home/nhxuoq3c/ptdl.com.vn
- Nhà đăng ký domain: dotvndns.vn (nameserver ns1/ns2/ns3.dotvndns.vn). Trang quản lý thật: access.dotvndns.vn (một chữ n).
- Email lừa đảo đáng ngờ đã nhận: "Gui lai thong tin dang ky domain" — không dùng link trong đó.

## Mục tiêu
1. Lấy được bản sao đầy đủ của site (file + database) từ NhanHoa.
2. Điều tra và dọn mã độc, file lạ, tài khoản admin lạ.
3. Khôi phục site: cập nhật WordPress/PHP/plugin, xử lý lỗi dung lượng.
4. Phương án dự phòng: nếu không khôi phục được WordPress, dựng lại site bằng code mới dựa trên nội dung đã lưu (xem docs/findings.md).

## Quy tắc làm việc
- KHÔNG ghi mật khẩu, token, hay thông tin đăng nhập vào bất kỳ file nào trong dự án, kể cả CLAUDE.md. Dùng trình quản lý mật khẩu.
- Trước mọi thay đổi trên file, hãy commit git để có thể quay lại.
- Không xóa file trên server hoặc trong `backup/` khi chưa liệt kê và được xác nhận. Ưu tiên ghi lại đường dẫn và danh sách trước.
- Không tin link trong email hay tin nhắn. Liên hệ NhanHoa và nhà đăng ký qua kênh chính thức do tự tìm.
- Thư mục `backup/` không đưa lên git (xem .gitignore).

## Cấu trúc
- `docs/timeline.md` — mốc thời gian sự cố và việc đã làm.
- `docs/findings.md` — kết quả kiểm tra, bao gồm khả năng khôi phục từ Wayback Machine.
- `docs/archive-homepage-text.txt` — văn bản trang chủ lấy từ Wayback (snapshot 2025-03-20).
- `checklist.md` — việc cần làm theo thứ tự.
- `scripts/archive_crawl.py` — tải các trang từ Wayback Machine.
- `backup/` — bản sao site và database (không đưa lên git).
