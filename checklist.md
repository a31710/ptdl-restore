# Checklist khôi phục ptdl.com.vn

## Giai đoạn 1: Bảo vệ và lấy quyền
- [ ] Đổi mật khẩu WordPress admin (đã lộ trong chat).
- [ ] Đổi mật khẩu tài khoản quản lý domain trên access.dotvndns.vn. Bật 2FA nếu có.
- [ ] Kiểm tra DNS trong trang quản lý domain: nameserver, A record, MX, TXT.
- [ ] Liên hệ NhanHoa qua kênh chính thức: báo sự cố, yêu cầu cấp lại quyền control panel, xin sao lưu toàn bộ (file + database).
- [ ] Nhờ NhanHoa kiểm tra dung lượng tài khoản `nhxuoq3c` (thư mục lớn nhất, `/tmp`, hộp thư, backup cũ).
- [ ] Đổi mật khẩu hosting, FTP, database sau khi có quyền.
- [ ] Kiểm tra file hosts trên máy (`C:\Windows\System32\drivers\etc\hosts`).

## Giai đoạn 2: Sao lưu
- [ ] Tải bản sao đầy đủ từ NhanHoa về `backup/`.
- [ ] Xuất database (file .sql) và lưu vào `backup/`.
- [ ] Kiểm tra bản sao: mở được không, có đủ thư mục `wp-content`, `wp-admin`, `wp-includes`.
- [ ] Lưu Site Health (Công cụ → Tình trạng website → Thông tin) vào `docs/`.

## Giai đoạn 3: Điều tra
- [ ] Liệt kê user admin trong WordPress, xóa hoặc hạ quyền user lạ.
- [ ] So sánh WordPress core với bản 7.1.4 gốc.
- [ ] Tìm file `.php` lạ trong `wp-content/uploads`, file ẩn, file có tên ngẫu nhiên.
- [ ] Kiểm tra `wp-config.php`, `.htaccess`, `index.php` xem có mã lạ không.
- [ ] Ghi kết quả vào `docs/findings.md`.

## Giai đoạn 4: Khôi phục
- [ ] Dọn dung lượng: xóa backup cũ, cache, log lớn (sau khi đã sao lưu).
- [ ] Nâng PHP từ 7.4.33 lên phiên bản được hỗ trợ (qua control panel hosting).
- [ ] Cập nhật WordPress lên 7.1.4 (thử "Thử lại" trước, nếu lỗi thì cập nhật thủ công).
- [ ] Gỡ plugin không kích hoạt và theme không dùng.
- [ ] Cập nhật các plugin còn lại.
- [ ] Sửa `post_max_size` ≥ `upload_max_filesize`.

## Giai đoạn 5: Gia cố và kiểm tra
- [ ] Bật bảo vệ (Wordfence hoặc Sucuri) và quét toàn bộ site.
- [ ] Bật xác thực 2 lớp cho WordPress admin.
- [ ] Thiết lập sao lưu tự động định kỳ.
- [ ] Kiểm tra lại trang chủ, form liên hệ, trang dịch vụ.

## Phương án dự phòng (nếu không lấy được bản sao đầy đủ)
- [ ] Dựng lại site bằng code mới, dựa trên nội dung trong `docs/archive-homepage-text.txt` và các trang khác lấy từ Wayback (nếu có).
- [ ] Thu thập lại nội dung từ khách hàng, nhân viên, hoặc trang mạng xã hội của công ty.
