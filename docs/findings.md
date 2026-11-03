# Kết quả kiểm tra

## Khả năng lấy dữ liệu từ Wayback Machine (kiểm tra ngày 2026-11-02)

Snapshot bạn đang đăng nhập: `web.archive.org/web/20250320022357/https://ptdl.com.vn/`

- Chỉ số CDX cho domain `ptdl.com.vn`: **36 bản ghi, chỉ 4 URL khác nhau**. Phần lớn là trang chủ (`/`), các biến thể http/https/www, và chuyển hướng 301/302.
- Các trang con (dịch vụ, tin tức, bài viết, liên hệ) **không có bản lưu** trong Wayback. Thử tải các URL này đều trả về 404.
- Ảnh trong `wp-content/uploads` cũng đa số 404, vì Wayback không lưu.
- Các bản ghi nằm trong khoảng 2024-05 đến 2025-03.

**Kết luận:** Wayback chỉ có trang chủ. Không thể khôi phục toàn bộ site từ đây.

## Những gì đã lấy được

- `backup/archive/ptdl.com.vn/index.html` — HTML trang chủ, snapshot 2025-03-20.
- `docs/archive-homepage-text.txt` — chữ hiển thị trên trang chủ: tên công ty, menu, dịch vụ (vận tải Bắc Nam, nội thành Hà Nội và TP.HCM, xe tải và container), form báo giá, số hotline, và phần giới thiệu "hơn 10 năm kinh nghiệm".
- `backup/archive/byteflows.net/...` — 5 ảnh từ **demo của theme transpi**, không phải ảnh của PTDL. Đừng dùng để khôi phục nội dung.

## Dữ liệu KHÔNG thể lấy từ Wayback

- Bài viết, trang con, và hình ảnh của công ty.
- Database: đơn hàng, khách hàng, form liên hệ, bình luận (209 bình luận đang chờ), cấu hình plugin WPCargo và Shipment.
- Plugin, theme, và file cấu hình (`wp-config.php`).
- Lịch sử thay đổi trên server.

Những dữ liệu này chỉ có thể lấy từ **NhanHoa** (file và database) hoặc từ chính bạn (bản backup cục bộ, email, Google Drive).

## Thông tin hạ tầng

- IP: 103.124.95.33 (AS131353, NhanHoa Software, Hà Nội).
- Hosting: NhanHoa, tài khoản `nhxuoq3c`, thư mục `/home/nhxuoq3c/ptdl.com.vn`.
- Dung lượng WordPress: khoảng 394 MB (uploads 162 MB, plugin 100 MB, theme 29 MB, core 78 MB, database 25 MB). Lỗi `Disk quota exceeded` nằm ở hạn mức của **cả tài khoản**, nên thủ phạm nằm ngoài thư mục WordPress.
- Nameserver: ns1, ns2, ns3.dotvndns.vn và nsbak.dotvndns.com.

## Các bước tiếp theo

1. Ưu tiên lấy bản sao đầy đủ từ NhanHoa. Đây là cách duy nhất để khôi phục nội dung thật.
2. Nếu NhanHoa không cung cấp được, dựng lại site bằng code mới dựa trên văn bản trang chủ đã lưu và thông tin bạn thu thập được.
