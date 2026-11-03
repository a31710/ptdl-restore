# Kế hoạch lấy lại nội dung và dựng website mới

Cập nhật: 2026-11-03. Mục tiêu: lấy lại tối đa nội dung của ptdl.com.vn và dựng website mới từ đó, không phụ thuộc vào việc cứu trang quản trị WordPress.

## Đã có (kho nội dung hiện tại)
| Nội dung | Nguồn | Vị trí trong dự án | Mức đầy đủ |
|---|---|---|---|
| 3 bài viết thật | REST + HTML gốc từ trình soạn thảo | `docs/content/post-*` | Đầy đủ |
| Chữ các trang chính | REST, WXR | `docs/content/page-*` | Trang chủ, giới thiệu, dịch vụ có; liên hệ, dịch vụ ngắn |
| Bố cục Elementor | WXR | `docs/elementor/` | Có cho 7 trang và 4 mẫu header/footer |
| Menu, form, CSS | WXR | `docs/config/` | Có |
| Ảnh, logo, biểu tượng | REST + thư viện media | `backup/live/media/` | 174/174 tệp, video chỉ lưu trên máy |
| Trang chủ bản 2025-03-20 | Wayback | `backup/archive/` | Chỉ trang chủ |
| Site tĩnh dự phòng v1 | Dựng từ nội dung trên | `site/` | 9 trang, còn nhiều TODO |

## Còn thiếu (cần tìm)
1. Nội dung riêng cho các tuyến Bắc, Nam, Trung và trang "Chuyển hàng Bắc Nam" (bản hiện tại có vẻ sao chép từ công ty khác).
2. Thông tin liên hệ chính xác: địa chỉ (26 hay 36 Hưng Gia 1), email đang dùng, mạng xã hội, bản đồ.
3. Cài đặt của theme (Transpi Options): thông tin chân trang, liên kết, logo, thứ tự khối. Các cài đặt này không nằm trong file xuất WordPress.
4. Phiên bản cũ của bài viết và trang (revisions) nếu có.
5. Số liệu năng lực, bảng giá, đối tác: chỉ chủ site hoặc NhanHoa có.

## Các tác vụ (làm song song, không giẫm lên nhau)

### Tác vụ A: lấy qua Chrome (chỉ đọc) — subagent
- Kiểm tra các trang con của front end có hiển thị được không (chỉ trang chủ lỗi 500 hay tất cả). Nếu hiển thị được, lấy chữ hiển thị của từng trang.
- Đọc toàn bộ **Transpi Options** trong wp-admin: liên hệ, mạng xã hội, chân trang, logo (loại bỏ khóa API, mật khẩu, token).
- Lấy **bản sửa đổi (revisions)** của 3 bài viết và các trang chính qua REST, so sánh với bản hiện tại.
- Xác định logo và biểu tượng site (site icon), alt và chú thích ảnh.
- Kết quả: `docs/content-recovery-chrome.md` và các file đi kèm.

### Tác vụ B: lấy từ kho lưu trữ khác — subagent (không dùng trình duyệt)
- Common Crawl: liệt kê và tải bản ghi các trang con của ptdl.com.vn từ các đợt thu thập gần đây.
- Tìm thêm bản lưu ở archive.today và các nguồn công khai khác; tìm trang Facebook, Google Maps, danh bạ doanh nghiệp để xác nhận địa chỉ, điện thoại, email, dịch vụ.
- Kết quả: `docs/content-recovery-external.md`, nêu rõ nguồn và mức tin cậy, không chép dài nội dung có bản quyền.

### Tác vụ C: tổng hợp — tôi làm sau khi A và B xong
- Lập `docs/content-inventory.md`: từng trang một, nội dung nào đã đủ, nội dung nào còn thiếu, nguồn lấy.
- Cập nhật `site/` (v2) với nội dung bổ sung, giữ nguyên quy tắc không bịa thông tin.
- Soạn danh sách câu hỏi cho chủ site về phần còn thiếu.

## Nguyên tắc
- Chỉ đọc trên WordPress. Không xóa, không lưu, không đổi cài đặt trong tác vụ này.
- Không chép mã nguồn thương mại của theme Transpi vào repo công khai; chỉ lấy nội dung và dữ kiện của PTDL.
- Không đưa email cá nhân, khóa API, mật khẩu, token vào repo.
- Không bịa thông tin. Chỗ nào chưa có thì ghi `TODO` và hỏi chủ site.
