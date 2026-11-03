# Kiểm tra wp-admin ptdl.com.vn (chỉ đọc)

Ngày kiểm tra: 2026-11-03. Thực hiện qua Chrome (phiên đăng nhập của chủ site), chỉ dùng GET/fetch đọc và các truy vấn admin-ajax/REST dạng đọc. Không lưu, không kích hoạt, không xóa gì. Không ghi email, nonce, cookie vào báo cáo.

## 1. Người dùng

| Tên đăng nhập | Vai trò | Ngày đăng ký | Ghi chú |
|---|---|---|---|
| admin_vllzta4i (ID 1, tên hiển thị "admin") | Administrator (Quản lý) | 2024-05-17 | Tác giả của 2222 mục (bài, trang, bản sửa đổi, media...). Tên đăng nhập lạ (có hậu tố ngẫu nhiên), có thể do nhà cung cấp/hosting đổi. |
| acadtapi (ID 11) | Administrator (Quản lý) | **2026-07-27** | **Đáng ngờ.** Admin tạo gần đây (ID 11, các ID 2-10 đã bị xóa hoặc không tồn tại), không có bài viết. Trước đợt trang spam đầu tiên (2026-08-12) khoảng 2 tuần. Rất có thể là tài khoản backdoor của kẻ tấn công. |

Tổng 2 người dùng, cả hai là admin. Cài đặt: không cho đăng ký tự do, vai trò mặc định subscriber.

## 2. Plugin

12 plugin (10 bật, 2 tắt), 6 có bản cập nhật.

| Plugin | Phiên bản | Tác giả | Trạng thái | Cập nhật | Đánh giá |
|---|---|---|---|---|---|
| Contact Form 7 | 5.9.4 | Takayuki Miyoshi | Bật | không báo | Hợp lệ (3 form) |
| Elementor | 3.21.5 | Elementor.com | Bật | 4.3.6 | Hợp lệ, rất cũ |
| Envato Market | 2.0.11 | Envato | Bật | không báo | Hợp lệ |
| Image Optimizer by Elementor | 1.3.0 | Elementor.com | Bật | 1.7.7 | Hợp lệ; đang báo lỗi thiếu PHP fileinfo |
| MC4WP: Mailchimp for WordPress | 4.9.13 | ibericode | Bật | 4.14.1 | Hợp lệ |
| One Click Demo Import | 3.2.1 | OCDI | Bật | 3.4.1 | Hợp lệ (plugin đi kèm theme), nên gỡ vì không cần nữa |
| SVG Support | 2.5.5 | Benbodhi | Bật | 2.6.3 | Hợp lệ nhưng cho phép tải SVG: rủi ro XSS/upload |
| Transpi Plugin | 1.0.3 | byteflows | Bật | không báo | Plugin đi kèm theme Transpi (ThemeForest), mô tả "install transpi-plugin first". Bình thường nhưng không thể kiểm tra mã. |
| Classic Editor | 1.6.3 | WordPress Contributors | Bật | 1.7.0 | Hợp lệ |
| WPCargo | 7.0.4 | WPTaskForce | Bật | không báo | Hợp lệ |
| WooCommerce | 8.8.3 | Automattic | Tắt | không báo | Hợp lệ nhưng không dùng, nên gỡ |
| Hello Dolly | 1.7.2 | Matt Mullenweg | Tắt | - | Mặc định, nên xóa |

- Must-Use: không có tab Must-Use (không có mu-plugin).
- Drop-ins (1): `maintenance.php` ("Thông báo về việc bảo trì"). Đây là drop-in hợp lệ của WordPress, nhưng cho thấy có file `wp-content/maintenance.php` sẽ thay thế trang bảo trì khi nâng cấp; cần xem nội dung file này trên server (có thể là trang deface hoặc mã độc).
- Không thấy plugin lạ, generic hay nulled trong danh sách WordPress hiển thị. Lưu ý: mã độc thường nằm ngoài danh sách này (file lẻ trong thư mục plugin/theme/uploads) nên danh sách sạch không có nghĩa là sạch.

## 3. Giao diện

| Theme | Phiên bản | Ghi chú |
|---|---|---|
| **Transpi (đang bật)** | 1.0.3, byteflows | Theme con không có (không phải child theme), tự cập nhật tắt |
| Twenty Twenty-Five | 1.0 (mới nhất 1.5) | Không dùng |
| Twenty Twenty-Four | 1.1 (1.6) | Không dùng |
| Twenty Twenty-Three | 1.4 (1.7) | Không dùng |
| Twenty Twenty-Two | 1.7 (2.2) | Không dùng |

## 4. Cài đặt chung

- Tiêu đề site: "Hacked by Trenggalek6etar"
- Khẩu hiệu: "Hacked by Trenggalek6etar - JATIM4U"
- WordPress Address và Site Address: https://ptdl.com.vn
- Permalink: `/%postname%.htm`
- Múi giờ +07:00, ngôn ngữ vi, môi trường production.

Tiêu đề và khẩu hiệu đã bị kẻ tấn công sửa (đây là tùy chọn trong DB, không phải do file).

## 5. Site Health

Thông tin hệ thống:
- WordPress 6.9.4 (mới nhất 7.1.4). Core tự cập nhật thất bại ("Tự động nâng cấp WordPress không thành công").
- PHP 7.4.33 (LiteSpeed SAPI), giới hạn bộ nhớ 512M, thời gian 30s, upload 1G, post_max_size 128M (nhỏ hơn upload_max_filesize, cảnh báo).
- Máy chủ Linux 4.18 (CloudLinux LVE, cPanel theo đường dẫn /home/...), MySQL server 8.0.36, mysqli, bảng mã utf8mb4. Tiền tố bảng ngẫu nhiên (đã đổi tiền tố).
- Trình xử lý ảnh: GD 2.3.3, không có Imagick; Ghostscript 9.27.
- PHP extension `fileinfo` thiếu (theo thông báo Image Optimizer). Còn một số "mô-đun đề xuất" khác thiếu.
- Hằng số: WP_DEBUG tắt, WP_DEBUG_LOG tắt, WP_DEBUG_DISPLAY bật (không tác dụng khi WP_DEBUG tắt), SCRIPT_DEBUG tắt, WP_CACHE tắt, WP_MEMORY_LIMIT 40M, WP_MAX_MEMORY_LIMIT 512M.
- .htaccess: chỉ có quy tắc lõi WordPress (không có rewrite lạ). Quyền: các thư mục gốc, wp-content, uploads, plugins, themes đều ghi được.
- Không có thư mục fonts.

Dung lượng thư mục:

| Thư mục | Kích thước |
|---|---|
| WordPress (lõi) | 77,81 MB |
| Themes | 28,57 MB |
| Plugins | 100,61 MB |
| Uploads | 162,12 MB |
| Database | 24,55 MB |
| Tổng | 393,66 MB |

Kết quả Status: 18 tốt, 7 khuyến nghị, 1 nghiêm trọng.
- Nghiêm trọng: PHP 7.4.33 đã hết hỗ trợ bảo mật.
- Khuyến nghị: có WordPress 7.1.4; gỡ plugin không kích hoạt; xóa theme không dùng; thiếu mô-đun PHP đề xuất; post_max_size < upload_max_filesize; thiếu bộ nhớ đệm trang; cập nhật nền có thể không hoạt động; thiếu Authorization header.
- Tốt: REST API hoạt động, yêu cầu HTTP/loopback hoạt động, wp-cron chạy, kết nối WordPress.org được, "dung lượng đĩa trống đủ để cập nhật" (WordPress tự đo trên đĩa, khác với quota cPanel nên không mâu thuẫn với lỗi "Disk quota exceeded").

## 6. Media

Có 174 attachment. Loại không phải `image/*` hoặc `video/mp4`: chỉ 1 file.
- `log_file_2024-05-17__08-17-40.txt` (text/plain), ngày trùng với ngày cài site (2024-05-17), có vẻ là log của One Click Demo Import. Không đáng ngờ về mặt loại, nhưng nên xóa vì có thể lộ thông tin đường dẫn.

## 7. Số liệu

| Hạng mục | Số lượng |
|---|---|
| Bài viết (post) | 22 (22 đã xuất bản) |
| Trang (page) | 168: 159 đã xuất bản, 9 bản nháp |
| Trong đó trang deface "Hacked by trenggalek6etar" | **139** (tất cả đã xuất bản, tạo 2026-08-12 đến 2026-10-26: 5 trong tháng 8, 36 trong tháng 9, 98 trong tháng 10) |
| Trang hợp lệ còn lại | 29 (gồm 9 nháp) |
| Bình luận | 209, tất cả chờ duyệt (0 đã duyệt, 0 spam, 0 thùng rác). Mẫu 100 bình luận đầu: ngày 2026-06 đến 2026-11, 87 có liên kết/từ khóa spam. Gần như toàn bộ là spam. |
| WPCargo shipment (`wpcargo_shipment`) | 1 (đã xuất bản) |
| Contact Form 7 | 3 form (Contact Form, Contact form 1, Contact form 1). Không có plugin lưu entry (Flamingo) nên không có bản ghi gửi form. |
| Portfolio | 0 |
| Elementor library | 4 (đã xuất bản) |

Chi tiết trang deface: slug dạng hash 12 ký tự hex (ví dụ `7a2054ec6134`, kèm biến thể `-htm`, `-2`, `-3`), tác giả là admin ID 1, nội dung bắt đầu bằng thẻ `<style>` ép nền đen (khoảng 941 ký tự). Việc tạo bằng tài khoản ID 1 cho thấy kẻ tấn công có phiên/thông tin đăng nhập admin hoặc chạy mã trực tiếp trên server (REST/PHP). Trang gần đây nhất còn chỉnh sửa: "Vận Tải Bắc - Nam" (ID 1290) ngày 2026-11-03 và "Elementor #2416" (nháp) ngày 2026-11-02 (có thể là thao tác của chủ site khi khôi phục).

## 8. Thông báo lỗi và nghi vấn gây lỗi 500 phía trước

Thông báo trên Dashboard/Themes:
1. "WordPress 7.1.4 đang có sẵn".
2. "Image Optimizer isn't running because: The following required PHP extensions are missing: fileinfo".
3. "Tự động nâng cấp WordPress không thành công - Thử lại".
4. Bốn thông báo cập nhật theme Twenty Twenty-x.
5. Plugin có 6 bản cập nhật.

Phía admin vẫn tải bình thường (PHP 7.4, Elementor 3.21.5, theme Transpi chạy được trong admin), nên lỗi chỉ xảy ra khi render front end hoặc ở đường dẫn không chạy trong admin.

Danh sách nghi vấn xếp theo khả năng (suy luận từ bằng chứng, chưa xác nhận bằng log):

| # | Nghi vấn | Lý do |
|---|---|---|
| 1 | **Hết quota đĩa** làm thất bại ghi file/cập nhật dở dang (core, plugin, theme bị bỏ nửa chừng, hoặc ghi cache/session/log thất bại) | Có lỗi "Disk quota exceeded" khi cập nhật; "Tự động nâng cấp WordPress không thành công"; tổng dung lượng WordPress chỉ ~394 MB nên quota rất nhỏ hoặc có file lớn nằm ngoài (log, backup, file của kẻ tấn công, error_log). Cập nhật lõi hỏng có thể để lại file thiếu trong wp-includes. Lưu ý: admin vẫn chạy, nên hỏng không nằm ở lõi chung mà ở phần front. |
| 2 | **Mã/biến thể do kẻ tấn công cài** (file PHP lạ trong theme Transpi, plugin hoặc uploads, hoặc chỉnh sửa header/footer/functions của theme) | Site bị deface, có tài khoản admin mới (acadtapi) tạo 2026-07-27, 139 trang spam; theme front end là phần chỉ chạy ở front. Danh sách plugin/theme sạch nhưng không kiểm tra được nội dung file. |
| 3 | **Theme Transpi 1.0.3 + Transpi Plugin tương tác với dữ liệu bị sửa** (ví dụ 139 trang deface chứa `<style>`, tùy chọn Transpi Options bị sửa, Elementor template lỗi) trên PHP 7.4 | Chỉ front end dùng template/Elementor render; dữ liệu trang bị thay đổi hàng loạt. Cần log để xác nhận. |
| 4 | **Đọc/ghi hỏng do thiếu fileinfo** (Image Optimizer) hoặc plugin cũ (Elementor 3.21.5 và WPCargo) không tương thích WP 6.9.4 | Ít khả năng hơn: lỗi này chỉ làm plugin tự tắt chức năng và hiện thông báo, không gây 500 thông thường. Nhưng Elementor 3.21.5 quá cũ so với WP 6.9.4 nên không loại trừ. |
| 5 | **Drop-in `maintenance.php`** | Là drop-in hợp lệ nhưng chỉ thay trang bảo trì khi có file `.maintenance`; nếu file này chứa mã lạ hoặc lỗi cú pháp thì gây lỗi. Ít khả năng là nguyên nhân 500 vì admin vẫn vào được. |
| 6 | **Chứng chỉ TLS hết hạn** | Không gây 500, chỉ cảnh báo trình duyệt; không liên quan lỗi "critical error". |

Chưa thể xác định nếu không có log máy chủ: lỗi PHP cụ thể (file, dòng) gây "critical error"; tệp nào bị sửa/thêm trên đĩa; ai và khi nào bắt đầu truy cập (log truy cập); quota thực tế và thư mục chiếm nhiều dung lượng; nội dung `.htaccess` ở thư mục con, `wp-config.php`, `maintenance.php`; cron job hoặc file ẩn do kẻ tấn công cài; plugin/theme có bị sửa mã so với bản gốc; nội dung bảng options (active_plugins, cron, widget) và các bảng DB khác. Cần error_log của PHP/LiteSpeed (hoặc bật WP_DEBUG_LOG tạm thời) để xác định chính xác.

## Việc nên làm tiếp (đề xuất, chưa thực hiện)

1. Vô hiệu/xóa tài khoản acadtapi và đổi mật khẩu admin còn lại sau khi đã khôi phục và xác nhận sạch; thu hồi phiên, đổi khóa trong wp-config, đổi mật khẩu hosting/FTP/DB.
2. Xóa 139 trang deface và 209 bình luận spam, đặt lại tiêu đề/khẩu hiệu site.
3. Giải phóng quota đĩa và đọc error_log; so sánh file theme/plugin/lõi với bản gốc; quét web shell.
4. Nâng PHP lên bản được hỗ trợ (cần kiểm tra tương thích Elementor/WPCargo), bật fileinfo, cập nhật plugin/theme, gỡ plugin và theme không dùng.
