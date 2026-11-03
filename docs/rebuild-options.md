# Phương án dựng lại website ptdl.com.vn

Ngày soạn: 2026-11-03. Mục tiêu: website mới trông càng giống site cũ càng tốt, tuân thủ giấy phép, bảo trì được.

Quy ước độ tin cậy: **Cao** = đã kiểm tra trực tiếp (máy này hoặc tài liệu chính thức); **Vừa** = nguồn thứ cấp hoặc kết quả tìm kiếm trích lại; **Thấp** = suy luận, chưa kiểm chứng. Lưu ý: ThemeForest và envato.com chặn công cụ tải trang (HTTP 403) nên các số liệu trang bán hàng chỉ lấy được qua trích đoạn kết quả tìm kiếm, cần chủ site mở trang thật để xác nhận.

---

## 1. Theme Transpi

### 1.1 Thông tin theme

| Mục | Nội dung | Độ tin cậy |
|---|---|---|
| Tên chính thức | "Transpi - Logistics and Transportation WordPress Theme", tác giả byteflows | Cao (tiêu đề trang) |
| Trang bán hàng | https://themeforest.net/item/transpi-logistics-and-transportation-wordpress-theme/50659699 | Cao (URL), nội dung chi tiết: Vừa |
| Giá | Các bản chụp không thống nhất: giá niêm yết thường 19 USD, 29 USD, 30 USD; một bản ghi "Regular price $49 / 29$ discount". Cần xem trang thật. | Thấp-Vừa |
| Doanh số / đánh giá | Khoảng 369 đến 692 lượt bán tùy thời điểm chụp; đánh giá khoảng 4,59 sao (46 lượt) | Vừa |
| Tính năng quảng cáo | 2 trang chủ mẫu (bản mới có thêm home 6), hơn 60 widget Elementor, WooCommerce, tương thích WPML/TranslatePress, tùy chọn WPCargo track and trace, Bootstrap 5.x | Vừa |
| Tương thích ghi trên trang | WordPress 4.9.x đến 6.5.x; Elementor | Vừa |
| Phiên bản mới nhất thấy được | 1.0.7 (28/05/2025). Site cũ chạy 1.0.3, tức đã có bản mới hơn. | Vừa |
| Demo | https://byteflows.net/wp/transpi (do chủ giao đề bài; chưa mở kiểm chứng vì không dùng trình duyệt) | Vừa |
| Plugin cần / đi kèm | Theo bài đánh giá bên thứ ba: Elementor, **Transpi Core / Transpi Plugin** (custom post type, widget Elementor, chức năng theme; đây là plugin đóng gói kèm theme, không có trên wordpress.org), Contact Form 7, One Click Demo Import. WPCargo là tùy chọn cho tra cứu vận đơn. Danh sách chính thức phải đọc trong tài liệu theme / màn hình "Install Required Plugins" sau khi cài. | Vừa |
| Người mua nhận được | Thông thường ở ThemeForest: file tải về gồm theme zip, plugin đi kèm (thư mục plugins), tài liệu, dữ liệu demo, giấy phép; cập nhật miễn phí trọn đời qua tải lại hoặc Envato Market plugin; hỗ trợ tác giả 6 tháng (gia hạn được). Cụ thể của Transpi cần xác nhận trên trang. | Vừa (mô hình chung) |

Nguồn: [trang item](https://themeforest.net/item/transpi-logistics-and-transportation-wordpress-theme/50659699), [đánh giá bên thứ ba](https://steemit.steemapps.com/wordpress/@gpldock/transpi-theme-review-a-developer-s-deep-dive-into-the-logistics-wordpress-workhorse-activated).

Dữ liệu thực tế trong thư mục khôi phục cho thấy các widget do plugin Transpi cung cấp được dùng thật: `transpi-heading`, `transpi-counter`, `transpi-team`, `transpi-list`, `transpi-brand`, `transpi-btn`, `transpi-projects`, `transpi-del-process`, `transpi-service-carousel`, `transpi-about-content`, `transpi-ab-img`, `transpi-slider`, `transpi-blog`, `transpi-testimonial-carousel`, `transpi-header-temp` (đếm từ page-home, page-services, header-1, footer JSON). Không có plugin này thì các widget đó không hiển thị. Độ tin cậy: Cao.

### 1.2 Người không mua có được lấy hoặc phân phối zip theme không?

**Không.** Chỉ nguồn hợp pháp là mua trên ThemeForest (hoặc xin tác giả cấp lại). Các trang "GPL" miễn phí (ví dụ nrgibroker.com, plugintheme.net xuất hiện trong kết quả tìm kiếm) là bản sao không được cấp phép, thường kèm mã độc; **không dùng**, đặc biệt vì site vừa bị hack. Độ tin cậy: Cao về nguyên tắc, Vừa về chi tiết giấy phép.

Chủ site đã từng dùng theme và có plugin Envato Market, nên rất có thể đã có tài khoản Envato/purchase code (hoặc thuê đơn vị thiết kế mua hộ). Đây là câu hỏi số 1 cho chủ site; nếu mua qua bên thiết kế thì xin họ chuyển giao file và purchase code.

### 1.3 Giấy phép Envato (Regular / Extended) và GitHub công khai

Nguồn chính thức (không tải được trực tiếp, trích qua tìm kiếm): https://themeforest.net/licenses/regular , https://themeforest.net/licenses/extended , https://themeforest.net/licenses/standard .

- Cả hai gói đều cấm phân phối lại item "as stock, in a tool or template, or with source files", kể cả khi đã chỉnh sửa hoặc đóng gói chung với item khác. Độ tin cậy: Vừa-Cao.
- Regular: dùng cho **một sản phẩm cuối (end product)** cho bạn hoặc một khách hàng, người dùng cuối không bị thu phí. Extended: cần khi sản phẩm cuối được bán hoặc người dùng bị thu phí (SaaS, bán lại). Website công ty vận tải quảng bá dịch vụ thông thường thuộc Regular.
- **Đưa mã theme (PHP/CSS/JS/ảnh) lên repo GitHub công khai = phân phối lại source** nên vi phạm giấy phép (kể cả private repo thì chỉ ổn nếu chỉ chủ site và người làm cho họ truy cập, nhưng vẫn nên tránh để lẫn). Quy tắc thực tế: **không commit zip theme, không commit thư mục theme, không commit plugin Transpi vào repo công khai**; chỉ commit nội dung của chủ site (chữ, ảnh của công ty), mã tự viết, và file cấu hình. Độ tin cậy: Cao (hệ quả suy luận trực tiếp từ điều khoản).
- Mô hình "split license" của Envato: phần PHP và HTML tích hợp thuộc GPL, còn CSS, thiết kế, ảnh, đồ họa thuộc giấy phép Envato (nguồn: https://help.author.envato.com/hc/en-us/articles/360000534626). Một số người cho rằng phần GPL có thể phân phối lại nhưng quan điểm pháp lý còn tranh cãi, và bản chia cụ thể của từng item tác giả có thể đặt khác (có tùy chọn 100% GPL). Hệ quả: **không dựa vào split license** để đưa theme lên GitHub; chỉ nên coi đó là cơ sở để cắm theme vào WordPress. Độ tin cậy: Vừa.
- **Dùng lại CSS/JS/ảnh của theme trong site tĩnh**: các phần này thuộc phần Envato license (không GPL), chỉ dùng trong khuôn khổ một end product và không được phát tán dưới dạng source. Site tĩnh của chính công ty PTDL có thể xem là "end product", nhưng ranh giới mơ hồ và để lộ toàn bộ CSS của theme trên web công khai thì thực chất là phát tán nó. Khuyến nghị: không sao chép CSS/JS/ảnh của theme; ảnh trong `media` do công ty tự tải lên (ảnh xe, văn phòng) là tài sản của công ty, được dùng; ảnh stock đi kèm theme demo thì **không**.
- **Dựng lại thiết kế bằng mã gốc tự viết**: ý tưởng, bố cục, màu sắc chung không bị bảo hộ như mã nguồn; mã tự viết từ quan sát là hợp lệ về nguyên tắc. Tránh sao chép nguyên văn CSS, tên class đặc trưng, icon font, ảnh, và cấu trúc HTML tới mức "bản dịch từng dòng". Đây không phải tư vấn pháp lý, nếu muốn chắc cần luật sư. Độ tin cậy: Vừa.

---

## 2. Phương án A: dựng lại WordPress với đúng theme + plugin

### 2.1 Quy trình

1. **Chủ site cung cấp**: file tải từ ThemeForest (theme zip + `transpi-plugin.zip` trong thư mục plugins), purchase code, hosting/domain.
2. **Hosting mới sạch** (không dùng lại tài khoản NhanHoa cũ nếu chưa dọn). PHP 8.1 hoặc 8.2 (kiểm chứng trong tài liệu theme; theme công bố tới WP 6.5, Elementor 3.21 cũ nên cài Elementor bản mới có thể cần theme 1.0.7). MySQL/MariaDB, HTTPS, HTTP chặn xmlrpc, 2FA cho admin.
3. Cài WordPress mới (6.5 đến 6.9; bản export từ 6.9.4). **Cài sạch, không khôi phục file/DB cũ** vì đã bị nhiễm.
4. Cài theme Transpi (ưu tiên bản mới nhất, 1.0.7), kích hoạt, cài và kích hoạt các plugin theo thứ tự: Elementor, Transpi Plugin, Contact Form 7, MC4WP, WPCargo, SVG Support, Classic Editor (tùy), One Click Demo Import (chỉ khi cần). Envato Market (tùy; hoặc bỏ để giảm bề mặt tấn công).
5. Bật Elementor kit mặc định rồi nhập: Công cụ > Nhập dữ liệu > WordPress Importer, chọn WXR `backup/live/wp-export/hackedbytrenggalek6etar.WordPress.2026-11-03.xml` (2,5 MB), **chọn "Download and import file attachments" sẽ thất bại vì site cũ không còn**, nên: copy `backup/live/media` (174 file, khoảng 95 MB) lên `wp-content/uploads` đúng cấu trúc năm/tháng, hoặc dùng plugin "Add From Server" / WP-CLI `media import`, rồi cho importer gán lại. Đơn giản nhất: nhập WXR không kèm tệp đính kèm, sau đó import media rồi đối chiếu ID/URL bằng Better Search Replace (đổi `https://ptdl.com.vn/wp-content/uploads/` cho khớp).
6. **Lọc WXR trước khi nhập**: file có 168 `page`, 22 `post`, 174 `attachment`, 4 `elementor_library`, 4 `transpi_template`, 9 menu item, 3 form CF7, 1 MC4WP form, 1 `wpcargo_shipment`, 1 `custom_css`. Con số 168 page là bất thường; nhiều khả năng là trang spam do tin tặc tạo. Chỉ nhập các page thật (home, giới thiệu, dịch vụ, chuyển hàng Bắc-Nam, liên hệ, tracking, projects), 4 bài viết thật, 4 template (header-1/2/3, footer), 4 elementor_library. Sửa XML hoặc dùng "chọn nội dung" của importer. Cần kiểm tra thêm: lọc nội dung nghi ngờ (script, iframe, link spam) trong post_content/postmeta.
7. Dữ liệu Elementor: dùng `docs/elementor/*.json` làm nguồn đối chiếu. Khi nhập qua WXR, postmeta `_elementor_data` được nhập nguyên; nếu cần gán lại thủ công, đặt `_elementor_data` (JSON), `_elementor_edit_mode = builder`, `_elementor_template_type`, rồi vào Elementor > Công cụ > Regenerate CSS & Data. Khác biệt: định dạng *template import* của Elementor (file JSON có `content`, `page_settings`, `version`, `type`) khác định dạng `_elementor_data` thô (mảng container/section). Muốn dùng "Import Template" phải bọc thêm lớp ngoài; còn nhập thẳng bằng WP-CLI `wp post meta update <id> _elementor_data "$(cat file.json)" --format=json`.
8. Transpi Options: nhập tay theo `docs/theme-options.md` (Header 1, preloader bật với GIF media 1948, nút cuộn lên, màu chủ đạo `theme-color-1 = #5c8330`, ảnh breadcrumb media 923, `blog_btn_text = Xem thêm`, social icon placeholder, footer style "Footer"). Hoặc tab Backup Export/Import của Redux nếu có bản export (không có sẵn). Các giá trị ở `docs/config` (menus, CF7, CSS tùy chỉnh) nhập theo `menus.json`, `contact-forms.json`, `custom-css-transpi.css`.
9. Permalinks: Cài đặt > Đường dẫn tĩnh > "Tên bài viết" (`/%postname%/`) để giữ URL cũ như `/services/chuyen-hang-bac-nam`; bấm Lưu để làm mới rewrite. Đặt Trang chủ tĩnh, trang Blog, menu (chính + footer), logo/favicon (media 1669).
10. **Dựng lại trang chủ và trang Dịch vụ**: bản export chứa nội dung demo của theme; dựng lại trong Elementor bằng chữ thật từ `docs/content-inventory.md` và `docs/archive-homepage-outline.txt` (ví dụ tiêu đề "PTDL Logistics", "Vận tải Bắc - Nam uy tín chuyên nghiệp", hotline 0285 5555 565, mục "Dịch vụ của chúng tôi"). Khung widget: transpi-slider, transpi-service-carousel, transpi-counter, transpi-team, transpi-brand, transpi-testimonial-carousel, transpi-projects, transpi-heading.
11. Kiểm thử: form CF7, MC4WP, tracking WPCargo (page có shortcode), tốc độ (preloader GIF nặng), SEO (sitemap, robots), 301 cho URL cũ, bảo mật (không nhập lại user cũ, đổi toàn bộ mật khẩu/khóa salt, cài Wordfence/Patchstack, sao lưu tự động).

### 2.2 Bẫy và rủi ro đã biết

- Widget phụ thuộc plugin Transpi: thiếu plugin hoặc sai phiên bản thì Elementor hiện "widget not found". Plugin Transpi phiên bản cũ có thể không chạy với PHP 8.3 trở lên; theme 1.0.7 phù hợp hơn site cũ 1.0.3 nhưng bố cục có thể lệch nhẹ.
- Elementor 3.21.5 là bản cũ có lỗ hổng đã biết; nên dùng Elementor hiện hành, chấp nhận khác biệt nhỏ (container, flex, CSS regeneration). Cần thử sau nâng cấp. Độ tin cậy: Vừa.
- Theme công bố tương thích tới WP 6.5, site cũ dùng 6.9.4; chạy được hay không với WP 6.9 hoặc 7.x phải thử thật; đây là điểm chưa kiểm chứng. Độ tin cậy: Thấp.
- Dữ liệu demo bị lẫn trong export (home, services): không dùng nguyên văn.
- Attachment: WXR chỉ chứa metadata, tệp thật nằm ở `backup/live/media`; mọi URL đã được viết cứng `https://ptdl.com.vn/wp-content/uploads/...` trong `_elementor_data`, phải search-replace nếu đổi domain tạm.
- Nhiễm mã độc: không copy bất cứ file PHP nào từ site cũ; chỉ nhận dữ liệu, ảnh (quét lại) và văn bản.
- Tên miền đã dùng bởi trang bị hack (tên file export có "hackedbytrenggalek6etar"): xử lý DNS/Google Search Console (Safe Browsing) trước khi mở lại.

### 2.3 Chạy thử cục bộ trên máy Windows này

Kiểm tra bằng shell (chỉ đọc): **không có** php, composer, docker, mysql, wp-cli. Có: node v22.6.0, npm 9.2.0, npx, git, Python 3.12. Ổ C: còn khoảng 174 GB trống. Không có XAMPP, không có Local by Flywheel. Độ tin cậy: Cao.

| Cách chạy thử | Cần cài | Dung lượng ước tính | Ghi chú |
|---|---|---|---|
| **WordPress Playground CLI** (`npx @wp-playground/cli server`) | Chỉ Node.js; yêu cầu Node 20.18 trở lên, máy có 22.6 nên đủ. Tải gói qua npx (không cài hệ thống) | Vài trăm MB tạm (WordPress + PHP wasm), cộng media | PHP 7.4 đến 8.5, dùng SQLite, mount thư mục `wp-content`, nạp blueprint. Trên Windows dùng `--mount-dir`. Dữ liệu ở `~/.wordpress-playground/sites/...`. Phù hợp nhất để xem thử, **không** thay hosting. Một số plugin dùng MySQL-only có thể lỗi. Nguồn: https://developer.wordpress.org/playground/developers/local-development/wp-playground-cli/ (Cao). |
| Local (Local by Flywheel / WP Engine) | Trình cài đặt GUI, tạo site nhanh | Khoảng 0,5 đến 1 GB cộng site | Dễ nhất cho người không rành; cần quyền cài app. |
| XAMPP | Apache + PHP + MariaDB, cài thủ công | Khoảng 0,5 đến 1 GB | Cấu hình virtual host, import DB. |
| Docker Desktop + wordpress/mysql image | Docker Desktop (WSL2) | 3 đến 6 GB | Gần môi trường hosting nhất, nặng nhất. |
| PHP built-in server + SQLite Database Integration plugin | PHP (cài zip, khoảng 30 MB), tải WordPress (khoảng 70 MB) | Khoảng 150 MB | Nhẹ; phải tự bật extension (mysqli không cần, dùng sqlite). Cùng cơ chế với Playground. |

Quan trọng: để chạy thử A vẫn **cần zip theme** từ chủ site. Không có zip thì chỉ chạy được WordPress trống, không có giao diện Transpi. Tôi không cài gì trong lần này.

---

## 3. Phương án B: site tĩnh HTML/CSS/JS (mã tự viết)

### 3.1 Hiện trạng

- `site/`: 14 trang (index, gioi-thieu, chuyen-hang-bac-nam, dich-vu, tin-tuc, lien-he, tracking, 404, 4 bài viết) + sitemap.xml, robots.txt; chỉ HTML/CSS và một ít JS (bật tắt menu); font hệ thống, không CDN; tổng khoảng 2,7 MB; màu chủ đạo `#5c8330` lấy từ cài đặt theme.
- `preview/`: bản thử với URL kiểu WordPress (`/services/...`, `.htm` cho bài viết, `.htaccess`, `serve.py`, `run-local.bat`) để xem trước permalink.

### 3.2 Giới hạn

- Không có CMS: mỗi lần sửa nội dung phải sửa HTML thủ công và tải lại.
- Form liên hệ chỉ là `mailto:`, không gửi mail nền, không lưu; MC4WP (đăng ký bản tin) không có.
- Tra cứu vận đơn (WPCargo) chỉ là trang giữ chỗ; không có dữ liệu.
- Không có tracking/analytics trừ khi thêm tay; không có preloader GIF, slider/carousel động như theme gốc (có thể viết bằng JS thuần).
- Độ giống: bố cục và màu rất gần nhưng không pixel-identical; các hiệu ứng, icon font, animation WOW của theme bị đơn giản hóa.

### 3.3 Cách đạt độ trung thực cao một cách hợp pháp

1. Dựa vào **dữ liệu** của chính site: `docs/elementor/*.json` cho cấu trúc, khoảng cách, màu, cỡ chữ, thứ tự section, thông số (ví dụ số counter); đây là dữ liệu của chủ site chứ không phải mã theme.
2. Viết CSS gốc từ quan sát: grid, khoảng cách, màu, bán kính, bóng đổ, font (đặt font tương đương miễn phí như Google Fonts nếu theme dùng, tự host file font để khỏi CDN).
3. Dùng ảnh của công ty trong `backup/live/media`; bỏ ảnh stock của demo theme hoặc thay bằng ảnh hợp lệ.
4. Icon: dùng SVG tự vẽ hoặc bộ mở (Lucide/Phosphor...) thay vì font icon của theme.
5. So sánh ảnh chụp màn hình site cũ (đã lưu trong thư mục khôi phục / Wayback) với bản mới ở các điểm gãy responsive; chỉnh tới khi gần giống. Không bao giờ dán CSS/JS đã minify của theme vào site.
6. JS thuần cho slider hero, carousel dịch vụ, counter, nút cuộn lên; tự viết.

---

## 4. Phương án C: lai

- **C1**: triển khai B ngay (an toàn, tốc độ cao, ít bị tấn công, chi phí hosting thấp), đồng thời chuẩn bị A. Khi có zip theme và hosting, dựng A ở tên miền tạm (staging), kiểm thử rồi chuyển DNS. B làm dự phòng.
- **C2**: giữ nội dung B (đã chuẩn hóa văn bản và ảnh), dùng **trình dựng khác**: nội dung vào WordPress với một block theme miễn phí (Twenty Twenty-Five, Kadence, Astra, GeneratePress) kèm Gutenberg hoặc page builder miễn phí, và tự tạo style riêng giống Transpi (màu `#5c8330`). Ưu: không phụ thuộc giấy phép Envato, có CMS, form (CF7), WPCargo vẫn dùng được. Nhược: hoàn toàn khác theme gốc về chi tiết, cần công thiết kế, độ giống thấp hơn A, cao hơn B một chút về khả năng quản lý.
- **C3**: B làm giao diện, dùng headless/CMS nhẹ (Decap CMS, Netlify Forms, Formspree) cho form. Có CMS dạng file nhưng thêm phụ thuộc dịch vụ ngoài.

---

## 5. So sánh

| Tiêu chí | A: WordPress + Transpi | B: Tĩnh HTML/CSS/JS | C: Lai (B trước, A sau; hoặc C2) |
|---|---|---|---|
| Độ giống site cũ | Cao nhất (90 đến 98%, còn tùy phiên bản và việc dựng lại home/services) | Khá cao về bố cục và màu (khoảng 75 đến 90%, tùy công mài) | B giai đoạn đầu, A sau; C2 khoảng 60 đến 80% |
| Công sức (ước tính) | 3 đến 6 ngày công: chuẩn bị hosting, cài, import, rebuild home/services, kiểm thử; thêm 1 đến 2 ngày bảo mật và chuyển DNS | Đã có sẵn; thêm 2 đến 4 ngày để tinh chỉnh độ trung thực, slider, form qua dịch vụ ngoài | B 2 đến 4 ngày + A 3 đến 6 ngày sau (tổng nhiều hơn nhưng chia đợt); C2 4 đến 7 ngày |
| Rủi ro | Phụ thuộc bản quyền theme; tương thích PHP/WP/Elementor; bị hack lại nếu không vá và theo dõi | Giới hạn chức năng; sửa nội dung thủ công; nguy cơ vi phạm nếu lỡ copy mã theme | Chi phí trùng lặp; duy trì hai bản; C2 độ giống thấp |
| Điều kiện cần | Zip theme + plugin (từ tài khoản Envato), purchase code, hosting PHP/MySQL, người bảo trì | Hosting HTML bất kỳ (hoặc CDN tĩnh), người sửa file | Như B ngay; như A khi có theme/hosting |
| Bảo trì lâu dài | Cần cập nhật plugin/theme, sao lưu, bảo mật liên tục | Gần như không cần bảo trì kỹ thuật, nhưng mọi sửa nội dung phải qua kỹ thuật viên | Chuyển dần sang CMS |
| Tính năng động (form, tracking, bản tin) | Đầy đủ (CF7, MC4WP, WPCargo) | Hạn chế (mailto, dịch vụ ngoài) | Tùy giai đoạn |
| Pháp lý | Hợp lệ nếu có license Regular riêng; không đưa theme lên repo công khai | Hợp lệ nếu mã tự viết, ảnh của công ty | Như A hoặc B tương ứng |

---

## 6. Khuyến nghị

**Chọn C1 (lai): giữ B làm bản chạy ngay, chuẩn bị A để thay thế khi đủ điều kiện.**

Lý do:
1. Site đang hỏng, cần có mặt trực tuyến nhanh và an toàn; B đã có sẵn, không dính PHP nên rủi ro bị hack lại gần như bằng không.
2. Độ giống tối đa chỉ đạt được bằng A, nhưng A phụ thuộc vào thứ hiện chưa có: zip theme từ giấy phép Envato hợp lệ và hosting mới. Không thể tự động tìm cách khác một cách hợp pháp.
3. Dữ liệu đã khôi phục (WXR, media, Elementor JSON, theme options) đủ để dựng A rất nhanh khi có theme.
4. Về pháp lý, B với mã tự viết và ảnh của công ty là an toàn; tuyệt đối không đưa theme/plugin Transpi lên repo công khai.

Nếu chủ site **chắc chắn** đã mua theme và muốn chức năng (form, tracking WPCargo) cùng khả năng tự sửa nội dung, chuyển thẳng sang A sau 1 đến 2 tuần dùng B.
Nếu chủ site **không** có theme và không muốn mua lại (khoảng vài chục USD, cần xác nhận giá thật): ở lại B, bổ sung form qua dịch vụ ngoài, hoặc C2.

Trước khi đưa bất kỳ phương án nào lên mạng: xử lý tên miền bị gắn cờ, đặt lại mật khẩu NhanHoa/domain/email, rà soát file media (quét mã độc nhúng trong ảnh/SVG, đặc biệt các file SVG vì plugin SVG Support cho phép tải SVG).

---

## 7. Câu hỏi và yêu cầu dành cho chủ site

1. Anh/chị có tài khoản Envato / hóa đơn mua theme Transpi (hoặc file zip theme + plugin, purchase code) không? Nếu do đơn vị thiết kế mua, họ còn lưu file không?
2. Hosting dự kiến là gì (vẫn NhanHoa hay nhà cung cấp khác)? Có chấp nhận WordPress/PHP chạy lại không, hay muốn site tĩnh để giảm rủi ro?
3. Ai sẽ cập nhật nội dung và bảo trì (nhân viên, bên thiết kế, hay chúng tôi)? Tần suất sửa nội dung ra sao?
4. Có cần các chức năng động: form liên hệ gửi mail thật, đăng ký bản tin, tra cứu vận đơn có dữ liệu thật?
5. Mức độ giống site cũ cần đạt: giống đến từng chi tiết, hay giống bố cục và màu sắc là đủ?
6. Đã đăng nhập lại được cPanel/hosting và quản lý DNS, email tên miền chưa? Ai đang giữ quyền tên miền?
7. Các thông tin còn thiếu cần xác nhận: logo, địa chỉ, email, hotline chính thức, link mạng xã hội thật (hiện đều `#`), bản quyền chân trang.
8. Trang số lượng 168 page trong export, có phải đều do tin tặc tạo không? Chúng tôi sẽ loại bỏ nếu anh/chị đồng ý.

---

## Nguồn

- Trang item: https://themeforest.net/item/transpi-logistics-and-transportation-wordpress-theme/50659699
- Đánh giá bên thứ ba: https://steemit.steemapps.com/wordpress/@gpldock/transpi-theme-review-a-developer-s-deep-dive-into-the-logistics-wordpress-workhorse-activated
- Giấy phép Envato: https://themeforest.net/licenses/regular , https://themeforest.net/licenses/extended , https://themeforest.net/licenses/standard
- Split license: https://help.author.envato.com/hc/en-us/articles/360000534626
- WordPress Playground CLI: https://developer.wordpress.org/playground/developers/local-development/wp-playground-cli/
