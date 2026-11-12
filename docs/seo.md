# SEO (cập nhật 2026-11-13)

Tên miền chính: `https://ptdl.com.vn/` (không www, luôn https).

## Đã làm trong code (tự động khi chạy `scripts/build_preview.py`)
- Canonical trên mọi trang; trang 404 và `_links.html` đặt `noindex`.
- `robots` meta (index, follow, max-image-preview:large), Open Graph, Twitter Card (ảnh chia sẻ là ảnh thật có sẵn của site).
- JSON-LD (schema.org): LocalBusiness (tên, địa chỉ cũ Phường Tân Phong Quận 7, hotline, email, giờ 08:00-20:00), WebSite, WebPage/AboutPage/ContactPage, BreadcrumbList, BlogPosting cho 4 bài viết. Chỉ dùng thông tin đã có trên site; không có đánh giá sao, giá hay FAQ (Google đã ngừng hiển thị FAQ).
- Tiêu đề ngắn dưới ~60 ký tự; mô tả mỗi trang; mỗi trang một h1; ảnh đều có `alt`, có kích thước (tránh nhảy bố cục), ảnh hero có `fetchpriority="high"`, ảnh dưới màn hình tải lười.
- `sitemap.xml` (có `lastmod` cho bài viết), `robots.txt` trỏ tới sitemap.
- `.htaccess`: chuyển về https + không www, bỏ đuôi `.html`, nén, cache trình duyệt, header bảo mật.

## Việc cần làm tay sau khi đưa lên hosting
1. Google Search Console: thêm `ptdl.com.vn` (xác minh DNS), gửi `https://ptdl.com.vn/sitemap.xml`, xem báo cáo Pages và Core Web Vitals.
2. Yêu cầu xóa các URL spam "Hacked by ..." còn trong chỉ mục Google (công cụ Removals); trả 404/410 cho các URL đó.
3. Bing Webmaster Tools: nhập từ Search Console.
4. Google Business Profile: tên, địa chỉ, SĐT phải khớp với website.
5. Kiểm tra bằng Rich Results Test và PageSpeed Insights sau khi lên https.
6. Chủ site xác nhận địa chỉ và giờ làm việc trong schema trước khi đăng.
