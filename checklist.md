# Checklist khôi phục ptdl.com.vn

Cập nhật: 2026-11-03. `[x]` là đã xong, `[ ]` là chưa làm hoặc đang chờ chủ site / NhanHoa.

## Trạng thái nhanh
- Đã có: nội dung thật (3 bài + 1 bài khôi phục, chữ các trang, bố cục Elementor), 174 tệp media, thông tin công ty từ nguồn công khai, site tĩnh dự phòng `site/` (bản 2), báo cáo kiểm tra `wp-admin`.
- Đang chờ: NhanHoa (SSL, dung lượng, bản sao lưu, log lỗi, PHP) và các câu trả lời của chủ site về nội dung.
- Xem `docs/plan.md`, `docs/content-inventory.md`, `docs/nhanhoa-request.md`.

## Giai đoạn 1: Bảo vệ và lấy quyền
- [ ] Đổi mật khẩu WordPress admin (đã lộ trong chat).
- [ ] Đổi mật khẩu tài khoản quản lý domain trên access.dotvndns.vn. Bật 2FA nếu có.
- [ ] Kiểm tra DNS trong trang quản lý domain: nameserver, A record, MX, TXT.
- [ ] Gửi tin nhắn cho NhanHoa qua kênh chính thức (đã soạn ở `docs/nhanhoa-request.md`): báo sự cố, yêu cầu cấp lại quyền control panel, xin sao lưu toàn bộ (file + database), log lỗi PHP.
- [ ] Nhờ NhanHoa kiểm tra dung lượng tài khoản `nhxuoq3c` (thư mục lớn nhất, `/tmp`, hộp thư, backup cũ).
- [ ] Đổi mật khẩu hosting, FTP, database sau khi có quyền.
- [ ] Kiểm tra file hosts trên máy (`C:\Windows\System32\drivers\etc\hosts`).

## Giai đoạn 2: Sao lưu
- [ ] Tải bản sao đầy đủ từ NhanHoa về `backup/`.
- [ ] Xuất database (file .sql) và lưu vào `backup/`.
- [ ] Kiểm tra bản sao: mở được không, có đủ thư mục `wp-content`, `wp-admin`, `wp-includes`.
- [x] Xuất nội dung qua REST API (bài viết, trang, media) vào `backup/live/`.
- [x] Xuất WordPress (WXR) từ `wp-admin`, tách Elementor và cấu hình vào `docs/elementor/`, `docs/config/`.
- [x] Tải đủ 174 tệp media (video 67 MB chỉ lưu trên máy).
- [x] Lưu thông tin Site Health và kiểm tra `wp-admin` vào `docs/audit-wp-admin.md`, `docs/findings.md`.

## Giai đoạn 3: Điều tra
- [x] Liệt kê user admin trong WordPress (phát hiện `acadtapi`, ID 11, đăng ký 27/07/2026).
- [ ] Chủ site xác nhận tài khoản `acadtapi`, rồi hạ quyền hoặc xóa nếu là của kẻ tấn công.
- [ ] So sánh WordPress core với bản gốc.
- [ ] Tìm file `.php` lạ trong `wp-content/uploads`, file ẩn, file có tên ngẫu nhiên (cần quyền file từ NhanHoa).
- [ ] Kiểm tra `wp-config.php`, `.htaccess`, `index.php`, `maintenance.php` xem có mã lạ không (cần quyền file).
- [x] Ghi kết quả vào `docs/findings.md`.

## Giai đoạn 4: Khôi phục WordPress
- [x] Đổi lại tên site "Hacked by ..." thành "PTDL – Vận Chuyển Bắc Nam" (cần xác nhận khẩu hiệu).
- [x] Chuyển 139 trang và 19 bài spam vào thùng rác (khôi phục được).
- [ ] Đánh dấu 176 bình luận spam (chờ chủ site đồng ý).
- [ ] Dọn dung lượng: xóa backup cũ, cache, log lớn (sau khi đã sao lưu).
- [ ] Tìm nguyên nhân lỗi 500 (cần log lỗi PHP).
- [ ] Nâng PHP từ 7.4.33 lên phiên bản được hỗ trợ (qua control panel hosting).
- [ ] Gia hạn chứng chỉ SSL.
- [ ] Cập nhật WordPress, plugin (6 plugin có bản mới), gỡ theme không dùng.
- [ ] Sửa `post_max_size` ≥ `upload_max_filesize`, cài extension PHP `fileinfo`.

## Giai đoạn 5: Gia cố và kiểm tra
- [ ] Bật bảo vệ (Wordfence hoặc Sucuri) và quét toàn bộ site.
- [ ] Bật xác thực 2 lớp cho WordPress admin.
- [ ] Chặn lộ danh sách người dùng trong sitemap.
- [ ] Thiết lập sao lưu tự động định kỳ.
- [ ] Kiểm tra lại trang chủ, form liên hệ, trang dịch vụ.

## Phương án dự phòng: site mới (`site/`)
- [x] Dựng site tĩnh 10 trang (trang chủ, giới thiệu, dịch vụ, tin tức + 4 bài, liên hệ, tracking, 404).
- [x] Nén ảnh, thêm `sitemap.xml`, `robots.txt`, kiểm tra bố cục máy tính và điện thoại.
- [x] Khôi phục bài "Bảo hiểm hàng hóa là gì?" từ bản sửa đổi cũ.
- [x] Tạo `preview/` với đường dẫn giống WordPress cũ (trang không có dấu `/` cuối, bài viết `.htm`), chạy local bằng `serve.py`, có `.htaccess` cho LiteSpeed. Dựng lại bằng `python scripts/build_preview.py` sau khi sửa `site/`.
- [ ] Chủ site xác nhận địa chỉ, email, giờ làm việc, "10 năm kinh nghiệm" (xem `docs/content-inventory.md`).
- [ ] Bổ sung nội dung các tuyến miền Bắc, Nam, Trung và Bắc Nam, bảng giá, số liệu năng lực.
- [ ] Chép video Thaco vào `site/assets/video/` hoặc nhúng từ YouTube.
- [ ] Thay form liên hệ `mailto:` bằng dịch vụ gửi form thật.
- [ ] Chọn hosting và triển khai site mới lên `ptdl.com.vn` sau khi SSL được gia hạn.
