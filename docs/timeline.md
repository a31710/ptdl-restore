# Timeline sự cố

- 2024-05 đến 2025-03: Wayback Machine lưu trang chủ ptdl.com.vn (nhiều bản).
- 2025-05-17: Ngày hết hạn domain ghi trong email lừa đảo (không xác nhận được).
- 2026-11-02: Phát hiện site bị defacement, "Hacked by Trenggalek6etar" trên thanh admin.
- 2026-11-02: Lỗi `Disk quota exceeded` khi tự động cập nhật WordPress lên 7.1.4.
- 2026-11-02: Lỗi chứng chỉ SSL hết hạn khi truy cập site qua trình duyệt.
- 2026-11-02: Nhận email "Gui lai thong tin dang ky domain" (đáng ngờ, chứa mật khẩu trong nội dung). Đã đăng nhập trang quản lý domain từ link trong email, sau đó xác minh địa chỉ thật là access.dotvndns.vn.
- 2026-11-02: Thông tin đăng nhập WordPress admin bị gửi qua chat cho bên thứ ba. Cần đổi mật khẩu.
- 2026-11-02: Xác định hosting là NhanHoa Software.
- 2026-11-02: Tạo dự án khôi phục, tải trang chủ từ Wayback, kiểm tra khả năng lấy dữ liệu.
- 2026-11-03: Cài Claude in Chrome, vào được wp-admin qua phiên đăng nhập của chủ site. Đọc đủ 174 tệp media và tải 12 tệp REST không liệt kê.
- 2026-11-03: Kiểm tra wp-admin chỉ đọc (docs/audit-wp-admin.md). Phát hiện admin lạ `acadtapi` (ID 11, đăng ký 2026-07-27), 139 trang và 19 bài spam "Hacked by trenggalek6etar" tạo từ 2026-08-12 đến 2026-10-26, 209 bình luận chờ duyệt (đa số spam), 12 plugin đều hợp lệ, PHP 7.4.33. Nghi vấn lỗi 500: hết quota đĩa hoặc file PHP do kẻ tấn công cài, cần log máy chủ.
- 2026-11-03: Dựng site tĩnh dự phòng trong `site/`. Soạn tin nhắn gửi NhanHoa (`docs/nhanhoa-request.md`).
- 2026-11-03: Chạy thử lọc spam (139 trang, 19 bài, khớp 100% tiêu đề "Hacked by trenggalek6etar"). Thao tác chuyển hàng loạt vào thùng rác bị hệ thống chặn, chưa thực hiện, chờ chủ site đồng ý.
- 2026-11-03: Chủ site đồng ý, đã chuyển vào thùng rác (không xóa vĩnh viễn) 139 trang và 19 bài spam "Hacked by trenggalek6etar" (ID trang từ 2141 đến 2767, bài từ 2654 đến 2768). Kiểm tra sau đó: còn 20 trang xuất bản, 9 bản nháp và 3 bài viết thật, không có mục nào ngoài nhóm "Hacked by" bị chuyển. Để khôi phục: wp-admin → Trang (hoặc Bài viết) → Thùng rác → Khôi phục.
- 2026-11-03: Đổi lại tên site thành "PTDL" và khẩu hiệu thành "Vận Chuyển Bắc Nam" (suy ra từ tiêu đề "PTDL – Vận Chuyển Bắc Nam" trên Wayback; cần chủ site xác nhận khẩu hiệu gốc). Giá trị cũ để khôi phục nếu cần: tên "Hacked by Trenggalek6etar", khẩu hiệu "Hacked by Trenggalek6etar - JATIM4U". Giữ nguyên tài khoản `acadtapi` theo yêu cầu của chủ site (đang kiểm tra).
- 2026-11-03: Chạy thử phân loại 176 bình luận chờ duyệt: cả 176 là spam (133 quảng cáo trang game kèm liên kết, 43 bình luận lừa đảo "Transfer/TRC20-USDT Bonus"), không có bình luận thật. Việc đánh dấu hàng loạt là Spam bị hệ thống chặn, chưa thực hiện, chờ chủ site đồng ý.
- 2026-11-03: Tác vụ lấy lại nội dung. Mọi trang front end đều lỗi 500. Đọc Transpi Options (không có thông tin liên hệ), 45 bản sửa đổi của trang Giới thiệu, bản sửa đổi các bài viết: khôi phục bài "Bảo hiểm hàng hóa là gì?" từ bản sửa đổi 2018 và đưa vào site mới. Tìm nguồn công khai: tên pháp lý, mã số thuế, ngày thành lập và địa chỉ số 36 Hưng Gia 1. Common Crawl và archive.today không lấy được. Trang chuyen-hang-bac-nam có bản lưu ngày 2026-11-03 (không do phiên này thực hiện).
- 2026-11-03: Cập nhật site tĩnh bản 2 (địa chỉ, mã số thuế, bài bảo hiểm hàng hóa) và lập `docs/content-inventory.md`.
