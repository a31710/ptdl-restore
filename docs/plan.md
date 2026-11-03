# Kế hoạch khôi phục ptdl.com.vn

Cập nhật: 2026-11-03. Chủ site đã cho phép làm các việc hữu ích để khôi phục site. Kế hoạch dưới đây chia việc theo giai đoạn và theo tác vụ độc lập.

## Nguyên tắc an toàn
- Ưu tiên thao tác **có thể hoàn tác**: chuyển vào thùng rác (không xóa vĩnh viễn), tắt plugin (không xóa), ghi lại trạng thái cũ trước khi đổi.
- Luôn sao lưu trước khi đổi: đã có bản xuất WXR, Elementor JSON, media và REST JSON trong dự án.
- Không động vào `wp-config.php`, `.htaccess`, file trên server (chỉ NhanHoa làm được).
- Không nhập hay yêu cầu mật khẩu, token. Chrome dùng phiên đăng nhập sẵn của chủ site.
- Không bỏ qua cảnh báo chứng chỉ mới trong trình duyệt; chủ site đã chấp nhận ngoại lệ cho phiên này.
- Mỗi thay đổi trên site ghi vào `docs/timeline.md`.

## Giới hạn: việc chỉ NhanHoa làm được
- Giải phóng dung lượng đĩa và xem thư mục nào chiếm quota (lỗi `Disk quota exceeded`).
- Gia hạn chứng chỉ SSL.
- Nâng PHP từ 7.4.33.
- Bản sao đầy đủ file + database, log lỗi PHP, quét mã độc ngoài thư mục WordPress.

## Giai đoạn 1: Kiểm tra (chỉ đọc)
Tác vụ A (subagent, Chrome): kiểm tra `wp-admin`.
- Danh sách người dùng và vai trò, tìm admin lạ.
- Danh sách plugin (bật/tắt, phiên bản, tác giả), plugin bắt buộc (mu-plugins) và drop-in; tìm plugin đáng ngờ.
- Danh sách theme.
- Cài đặt chung: tên site, email admin, URL.
- Site Health: thông tin máy chủ, hằng số, thư mục và kích thước.
- Media lạ (loại tệp không phải ảnh).
- Số bình luận, số vận đơn WPCargo, số mục form liên hệ.
- Kết quả: `docs/audit-wp-admin.md` và danh sách nghi vấn gây lỗi 500.

## Giai đoạn 2: Dựng bản dự phòng (song song với giai đoạn 1)
Tác vụ B (subagent, không dùng trình duyệt): dựng **site tĩnh dự phòng** trong `site/` bằng HTML/CSS/JS thuần, từ nội dung đã khôi phục. Dùng được ngay trên bất kỳ hosting nào nếu WordPress không cứu được.

## Giai đoạn 3: Sửa an toàn trên WordPress (sau khi có kết quả kiểm tra)
Mỗi bước hoàn tác được, làm lần lượt, kiểm tra trang chủ sau mỗi bước:
1. Đổi lại tên site "Hacked by ..." thành tên đúng của công ty.
2. Chuyển bài và trang spam vào thùng rác (khoảng 19 bài, 139 trang), không xóa vĩnh viễn.
3. Hạ quyền hoặc tạm khóa admin lạ (nếu có), sau khi chủ site xác nhận.
4. Tắt từng plugin đáng ngờ rồi thử lại trang chủ để tìm plugin gây lỗi 500. Tắt trước, không xóa.
5. Chặn lộ danh sách user trong sitemap nếu có thể bằng cài đặt.

## Giai đoạn 4: Hoàn tất
- Cập nhật `docs/findings.md`, `docs/timeline.md`, `checklist.md`.
- Commit và đẩy lên GitHub.
- Soạn tin nhắn cho NhanHoa (SSL, dung lượng, bản sao lưu, nâng PHP).

## Việc chủ site cần làm
- Liên hệ NhanHoa theo tin nhắn đã soạn.
- Xác nhận trước khi tôi khóa hoặc hạ quyền bất kỳ tài khoản người dùng nào.
- Đổi mật khẩu các tài khoản đã lộ (WordPress, domain, hosting).
