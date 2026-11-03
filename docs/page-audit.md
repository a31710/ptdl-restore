# Bảng đối chiếu nội dung từng trang (cũ so với site mới)

Cập nhật: 2026-11-03. Trạng thái: **Có** (đã giống bản cũ), **Khác** (có nhưng không giống), **Thiếu** (còn thiếu nhưng có nguồn), **Không có nguồn** (không thể khôi phục), **Bỏ có chủ đích** (nội dung của đơn vị khác hoặc bị ẩn ở bản cũ).

## Phát hiện mới ảnh hưởng đến cả bảng

1. **Trang chủ thật là trang WordPress ID 603** (hiện mang slug `home-two`, template `elementor_header_footer`). Dữ liệu Elementor của trang này **còn nguyên bản tiếng Việt** (bản sửa 12/2025), đã lưu ở `docs/elementor/page-home-603.json` và `docs/content/page-home-603.rendered.html`. Trang có slug `home` trong file xuất là bản demo của theme. Trước đây tôi tách nhầm trang 603 vì slug `home-two` nằm trong danh sách "trang demo".
2. Bản 12/2025 khác bản Wayback 03/2025 ở: ảnh hero mới (`2025/12/4444mage.png`), và nút của bảng giá nội thành HCM ghi **0961 565 015** (không phải 0285.5555.565).
3. **Biểu mẫu đăng ký nhận tin của footer bị ẩn trên mọi thiết bị** ở bản cũ (`hidden-desktop`, `hidden-tablet`, `hidden-mobile`). Bản mới đã thêm biểu mẫu hiển thị: sai so với gốc.
4. **Khối Fanpage của footer** là khung Facebook của trang `Ikay.vn` (đơn vị khác, còn sót từ demo). Không đưa vào.
5. **Menu chính cũ** gồm: Trang chủ, Giới thiệu, Dịch vụ (4 mục con), Tin tức, Liên hệ. Không có "Tra cứu vận đơn". Nút bên phải đầu trang cũ ghi "Hotline: 0285 5555 565" (kèm nút "Liên hệ"), mạng xã hội facebook và youtube có liên kết `#`.
6. Các khối nền xanh đặc `#5C8330` (Giới thiệu, Bảng giá, Tin tức, chân trang) và khối CTA có ảnh nền kèm lớp phủ `#020E28`; bản mới dùng nền xanh nhạt `#eef4e6`. Xem `docs/design-spec.md`.

## 1. Trang chủ (`/`)

Thứ tự khối theo dữ liệu Elementor trang 603.

| # | Khối gốc | Nguồn | Trạng thái | Việc cần làm |
|---|---|---|---|---|
| 1 | Thanh trên cùng: hotline, giờ làm việc, "Đặt lịch Online" | Wayback, header-2 | Có | Nút phải đầu trang cũ: "Hotline: 0285 5555 565" |
| 2 | Hero "PTDL Logistics / Vận tải Bắc - Nam / Uy tín chuyên nghiệp", nút, "Liên hệ 0285 5555 565", ảnh hero | Elementor 603 | Khác | Đổi ảnh hero sang `4444mage.png`; nền hero có họa tiết (ảnh nền của theme) |
| 3 | Dịch vụ của chúng tôi, 5 thẻ có biểu tượng | Elementor 603 | Có | Thẻ gốc có biểu tượng SVG của theme; thay bằng biểu tượng tự vẽ |
| 4 | Khối container "Hero" có ảnh trang trí và tiêu đề | Elementor 603 | Không có nguồn | Ảnh trang trí của theme, bỏ |
| 5 | Giới thiệu "Về chúng tôi" (nền xanh đặc), video, 4 bộ đếm 1.289 / 745 / 68 / 49 | Elementor 603 | Khác | Nền xanh đặc, ảnh nút play video |
| 6 | Form báo giá (cột trái) và "Dịch vụ chuyên nghiệp" kèm 6 mục (cột phải) | Elementor 603 | Khác | Bố cục hai cột đúng như gốc, hiện đang tách hai khối |
| 7 | Carousel nhận xét khách hàng (3 người, có ảnh đại diện) | Elementor 603 | Khác | Hiện là 3 thẻ; gốc là carousel. Ảnh đại diện là ảnh người thật/stock, cần xác nhận |
| 8 | Bảng giá cước, 3 thẻ (nền xanh đặc, có họa tiết) | Elementor 603 | Khác | HCM: nút ghi 0961 565 015 |
| 9 | Ngành nghề, 4 mục có ảnh (ảnh demo của theme) | Elementor 603 | Khác | Bỏ ảnh demo, dùng ảnh PTDL |
| 10 | CTA "PTDL - LOGISTICS ... Liên hệ" (ảnh nền, lớp phủ #020E28) | Elementor 603 | Khác | Dùng ảnh xe PTDL làm nền |
| 11 | Tin tức mới nhất (nền xanh đặc) | Elementor 603 | Khác | Nền xanh đặc |
| 12 | Logo đối tác (carousel 6 logo) | Elementor 603 | Có | |
| 13 | Chân trang: CTA "Bạn đang tìm kiếm dịch vụ vận tải tốt nhất?" nền xanh dương, logo, 3 cột, bản quyền | footer 487 | Khác | CTA gốc nền gradient xanh dương; cột "Dịch vụ", công ty, email, địa chỉ |
| 14 | Biểu mẫu "Subscribe" | footer 487 | Bỏ có chủ đích | **Ẩn ở bản cũ**: cần gỡ khỏi site mới |
| 15 | Khối "Fanpage" | footer 487 | Bỏ có chủ đích | Khung Facebook của đơn vị khác |

## 2. Giới thiệu (`/gioi-thieu`)

| Khối gốc | Nguồn | Trạng thái |
|---|---|---|
| Tiêu đề "Giới thiệu", đoạn giới thiệu, 4 mục (10+ năm, 64 tỉnh, nhanh - an toàn - tiết kiệm, đa dạng xe), nút "Liên hệ: 0285.5555.565", ảnh | Elementor | Có |
| Sứ mệnh - Tầm nhìn (Tầm nhìn, Nhiệm vụ, Chiến lược) | Elementor | Có |
| Năng lực vận chuyển (6 mục) | Elementor | Có (đã khôi phục) |
| Tại sao lại chọn chúng tôi (6 mục) | Elementor | Có |
| Logo đối tác | Elementor | Có |
| Form liên hệ (shortcode CF7) cuối trang | Elementor | Thiếu: chưa có form cuối trang Giới thiệu |

## 3. Dịch vụ (`/services`)

Dữ liệu gốc đã bị demo ghi đè, không còn bản Việt đầy đủ. Bản mới ghép từ thẻ dịch vụ, ngành nghề và trang Bắc – Nam. Trạng thái: **Khác** (không thể đối chiếu từng khối, **Không có nguồn** cho bố cục gốc).

## 4. Chuyển hàng Bắc – Nam (`/services/chuyen-hang-bac-nam`)

Có (phần của PTDL). **Bỏ có chủ đích** các đoạn của đơn vị khác. Số 0961.565.015 xuất hiện cả ở bảng giá HCM của chính PTDL, nên có thể là số của PTDL: cần xác nhận.

## 5. Liên hệ (`/lien-he`)

| Khối gốc | Trạng thái |
|---|---|
| Nhận báo giá, Liên hệ 24/7, email, địa chỉ | Có |
| Đăng ký tư vấn kèm cam kết 5 phút, form | Có |
| Bản đồ Google | Có |

## 6. Tin tức (`/blog`, `/category/cam-nang-van-chuyen`) và 4 bài viết

| Mục | Trạng thái |
|---|---|
| Danh sách tin, chuyên mục | Có |
| Bài: Lễ bàn giao xe Thaco, Gửi hàng đi Úc, Chuyển nhà đường dài, Bảo hiểm hàng hóa | Có. Video Thaco chỉ lưu trên máy |
| Bình luận và ô bình luận dưới bài | Không có nguồn (bình luận cũ toàn spam) |

## 7. Tra cứu vận đơn (`/tracking`, `/track-form`)

Gốc: mã nhúng `[wpcargo_trackform]` (WPCargo). **Không có nguồn** dữ liệu; trang giữ chỗ. Cần hệ thống WPCargo hoặc thay bằng giải pháp khác.

## 8. Trang 404

Có (trang mới).

## Cập nhật sau khi tái tạo giao diện và hiệu ứng (2026-11-03)

Đã làm lại toàn bộ giao diện theo thông số của site cũ (`docs/visual-reference.md`, `docs/theme-behavior.md`) bằng CSS và JavaScript tự viết (`site/assets/css/site.css`, `site/assets/js/site.js`).

| Khối | Trạng thái | Ghi chú |
|---|---|---|
| Thanh trên (hotline, giờ làm việc, Liên hệ, Đặt lịch Online) | Có | Nền trắng, viền dưới, icon tự vẽ |
| Thanh menu, mục Dịch vụ có menu con xổ xuống, nút Hotline | Có | Nền xanh `#5C8330` (**suy luận**: bản gốc chỉ biết chữ menu màu trắng) |
| Menu điện thoại | Có | Trượt từ phải, có nút đóng |
| Preloader | Có | Logo, ẩn khi tải xong |
| Hero (chữ căn giữa, tiêu đề hiện theo từng từ, nút, xe tải đè xuống khối sau) | Có | Nền: ảnh xe PTDL phủ gradient (bản gốc dùng ảnh nền của theme) |
| Dịch vụ: 5 thẻ xanh, icon tròn trắng ở mép trên, hiện dần theo độ trễ | Có | Icon tự vẽ |
| Giới thiệu: nền xanh, nút play có vòng sóng, hộp thoại YouTube, 4 bộ đếm | Có | Ảnh nền nút play là ảnh xe PTDL |
| Form báo giá (hộp xanh, ô xanh dương, thanh trượt Số KM) | Có | Khoảng giá trị thanh trượt là 0 đến 2000 km (không rõ ở bản gốc) |
| Nhận xét: carousel tự chạy 5 giây, nút, chấm, vuốt | Có | Ảnh đại diện thay bằng chữ cái đầu |
| Bảng giá: thẻ tối, icon check | Có | |
| Ngành nghề: 4 hàng, hàng đang chọn hiện ảnh nền | Có | Ảnh nền là ảnh xe PTDL (bản gốc dùng ảnh của theme) |
| CTA ảnh nền kèm lớp phủ, tin tức, đối tác (logo mờ, chạy ngang) | Có | |
| Chân trang: dải CTA xanh dương, logo, 3 cột, nền xanh | Có | Dải CTA màu xanh dương theo cài đặt Elementor |

**Còn khác bản cũ:** icon và họa tiết của theme (thay bằng bản tự vẽ), ảnh nền hero và ảnh ngành nghề, hiệu ứng nghiêng (Tilt) và cuộn mượt GSAP (không làm), popup tìm kiếm (site tĩnh không có tìm kiếm), icon mạng xã hội (bản cũ chỉ có liên kết `#`), màu thanh menu chưa xác nhận, và các hiệu ứng được làm đơn giản hơn bản gốc.

## Cập nhật: làm lại phần thân các trang trong (2026-11-03)

Giới thiệu, Dịch vụ, Liên hệ, Tra cứu vận đơn, Tin tức và Chuyển hàng Bắc – Nam đã dùng cùng bộ thành phần với trang chủ (banner trang, thẻ dịch vụ có icon, hộp xanh, danh sách dấu tích, hiệu ứng hiện dần). Đã kiểm tra trên trình duyệt ở 1568 px và 375 px: không tràn ngang. Nội dung chữ không đổi so với bản đã khôi phục; vẫn còn các mục "cần xác nhận" ghi trong chú thích TODO của từng trang.
