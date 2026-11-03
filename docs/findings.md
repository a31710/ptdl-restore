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

## Site đang chạy: nội dung có thể lấy được (kiểm tra ngày 2026-11-03)

- Trang chủ trả về lỗi HTTP 500 ("WordPress › Lỗi"), nhưng WordPress vẫn chạy và **REST API công khai vẫn trả dữ liệu**: `/wp-json/wp/v2/posts` (khoảng 81 KB), `/pages` (khoảng 252 KB), `/media` (khoảng 363 KB).
- Sitemap `wp-sitemap.xml` vẫn hoạt động. Nó liệt kê bài viết, trang, template của theme, danh mục và user.
- Chứng chỉ TLS đã hết hạn, nên trình duyệt và công cụ kiểm tra đều từ chối. Bản xuất bằng `scripts/rest_export.py` bị chặn khi tắt kiểm tra chứng chỉ, nên **chưa tải được dữ liệu**. Cần gia hạn chứng chỉ (nhờ NhanHoa) hoặc bạn cho phép chạy với `--insecure`.

### Kết quả xuất qua REST API (2026-11-03, chạy với `--insecure` theo sự đồng ý của chủ site)

- Đã lưu vào `backup/live/` (không đưa lên git): `posts.json` (22), `pages.json` (159), `media.json` (162), `categories.json`, `tags.json`. `comments.json` rỗng.
- **160 ảnh (27 MB)** đã tải về `backup/live/media/`. Bỏ qua 1 file video `.mp4` và 1 file log `.txt` trong thư viện media.
- Nội dung chữ của 10 mục thật (trang chủ, giới thiệu, dịch vụ, chuyển hàng Bắc Nam, liên hệ, tracking, track-form, 3 bài viết) nằm trong `docs/content/*.md`.
- Phân loại: 3 bài viết thật, 19 bài spam; trong 159 trang có khoảng 139 trang spam và nhiều trang mẫu của theme.
- Một số ảnh trong thư viện là ảnh mẫu của theme (ví dụ `boxking_about_img_*`, `Image_Placeholder_*`). Cần xem lại bằng mắt trước khi dùng.
- **Chưa có:** database đầy đủ, dữ liệu đơn hàng, form liên hệ, bản nháp và nội dung riêng tư, cấu hình plugin. Những phần này chỉ có từ backup NhanHoa.

### Nội dung thật và nội dung do kẻ tấn công chèn vào (theo sitemap)

- **Bài viết thật (3):** `cach-chuyen-nha-duong-dai-o-ha-noi`, `huong-dan-gui-hang-di-uc-tai-binh-duong-an-toan-va-nhanh-chong`, `le-ban-giao-lo-xe-thaco` (đuôi `.htm`).
- **Trang thật:** `home`, `gioi-thieu`, `services`, `services/chuyen-hang-bac-nam`, `lien-he`, `blog`, `tracking`, `track-form`, `my-account`.
- **Trang mẫu của theme (không phải nội dung PTDL):** `home-two`, `home-three`, `blog-grid`, `team`, `projects`, `faq-page`, `project-masonry`, `sample-page`.
- **Nhiều khả năng là spam do kẻ tấn công chèn:** hàng trăm trang/bài có tên `cox-htm-*`, `cox-*`, và các chuỗi hex dạng `0ada00df5929-htm`. Đây là kiểu chèn SEO spam. Không dùng lại.
- Sitemap còn công khai danh sách **user** (`wp-sitemap-users-1.xml`). Nên tắt hoặc chặn sau khi khôi phục, vì lộ tên đăng nhập.

## Máy tính này

Đã tìm trong Desktop, Documents, Downloads, OneDrive: không có file backup của site (`.wpress`, `.sql`, thư mục WordPress). Chỉ có file làm việc khác, không liên quan tới website.

## Xuất WordPress (WXR) từ wp-admin (2026-11-03)

Công cụ → Xuất dữ liệu vẫn chạy được dù front end báo lỗi 500. File gốc nằm ở `backup/live/wp-export/` (chỉ lưu trên máy, không đưa lên git vì có thể chứa thông tin người dùng).

- Nội dung file: 389 mục, gồm 22 bài viết, 168 trang, 174 tệp đính kèm, 4 mẫu Elementor, 4 mẫu của theme transpi, 9 mục menu, 3 form Contact Form 7, 1 form MC4WP, 1 đoạn CSS tùy chỉnh và 1 vận đơn WPCargo mẫu.
- `scripts/parse_wxr.py` tách phần thật ra khỏi spam và trang demo của theme:
  - `docs/elementor/`: dữ liệu bố cục Elementor (JSON) của 7 trang thật (home, gioi-thieu, services, chuyen-hang-bac-nam, lien-he, projects, tracking), 4 mẫu header/footer của theme và 3 mẫu Elementor (`hme`, `anh-xe`, `default-kit`).
  - `docs/config/`: menu, form liên hệ, form newsletter, CSS tùy chỉnh.
- Trang chủ dùng các widget riêng của theme transpi (slider, carousel dịch vụ, đếm số, đội ngũ, dự án, blog...). Khi dựng lại cần dựa vào cấu trúc JSON và nội dung trong đó, không dùng trực tiếp widget của theme.
- Vẫn chưa có: đơn hàng thật, dữ liệu khách hàng, nội dung form liên hệ đã gửi, mật khẩu và cấu hình hosting. Phần này cần database từ NhanHoa.

## Tài nguyên media bổ sung từ trang Thư viện đã lưu (2026-11-03)

Trang `wp-admin` "Tất cả tập tin" (thư viện media, dạng lưới) bạn lưu về chứa 80 mục. Trang này chỉ có tên tệp, mã ID và ảnh thu nhỏ 300 px trong thư mục `_files` đi kèm, không có đường dẫn ảnh gốc.

- So với danh sách media từ REST API, có **5 mục REST không liệt kê** (ảnh gắn với bài chưa công khai nên REST trả `rest_forbidden`): ID 1683 (`0db17170-...png`), 1643 (`Logo`), 1523 (`australia.png`), 1521 (`canada-1.png`), 1519 (`saudi-arabia.png`).
- Đã đoán đường dẫn và tải bản gốc từ `wp-content/uploads/2023/12/` vào `backup/live/media/2023/12/`: `0db17170-2f13-4991-b10e-949c7c283133.png` (1147x1327, ảnh đã xuất hiện trong Wayback), `australia.png`, `canada-1.png`, `saudi-arabia.png` (cờ 64x64) và `Logo-1.svg`.
- Ảnh logo `Logo (1)`: tên `logo-1(1).svg` trong thư mục `_files` là do trình duyệt tự đổi tên khi trùng tên, nên tệp gốc là `Logo-1.svg`. Cần kiểm tra bằng mắt vì chưa đối chiếu được ID.
- Các ảnh thu nhỏ còn lại (khoảng 58 tệp) là bản nhỏ của ảnh đã tải đầy đủ trước đó, nên không cần dùng.
- Danh sách media thật có thể còn nhiều mục hơn 80 mục trong trang đã lưu. Muốn chắc chắn, cần xem hết thư viện (cuộn tải thêm) hoặc lấy từ database của NhanHoa.

## Các bước tiếp theo

1. Ưu tiên lấy bản sao đầy đủ từ NhanHoa. Đây là cách duy nhất để khôi phục nội dung thật.
2. Nếu NhanHoa không cung cấp được, dựng lại site bằng code mới dựa trên văn bản trang chủ đã lưu và thông tin bạn thu thập được.
