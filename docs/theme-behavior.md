# Script và hiệu ứng của theme Transpi, và cách site mới tái tạo

Cập nhật: 2026-11-03. Nguồn: danh sách script trong bản HTML Wayback của trang chủ cũ, cài đặt Elementor (`docs/elementor/page-home-603.json`), các thông số carousel đọc từ mã chạy của chính site cũ, và báo cáo `docs/visual-reference.md`.

**Nguyên tắc:** chỉ mô tả hành vi và thông số quan sát được. Site mới dùng **mã tự viết** (`site/assets/js/site.js`, `site/assets/css/site.css`), không chép mã, ảnh hay icon của theme (giấy phép Envato không cho phân phối lại, xem `docs/rebuild-options.md`).

## 1. Thư viện theme nạp trên trang chủ cũ

| Thư viện (theme) | Dùng cho | Cách site mới thay thế |
|---|---|---|
| jQuery + jQuery UI slider, `rangeslider` | Thanh trượt "Số KM" trong form báo giá | `<input type="range">` kèm số hiển thị |
| Swiper | Carousel nhận xét, đối tác, dịch vụ/đội ngũ, slider hero | Carousel tự viết (cuộn mượt, tự chạy, nút, chấm, vuốt) |
| WOW.js + animate.css | Hiện dần khi cuộn: `fadeInUp` (thẻ dịch vụ, bảng giá, tin tức), `fadeInRight` (xe tải hero); trễ 200 đến 800 ms | `IntersectionObserver` thêm lớp hiển thị, cùng độ trễ |
| Odometer + appear | Bốn bộ đếm số đếm lên khi cuộn tới | Đếm lên bằng `requestAnimationFrame` |
| GSAP, ScrollTrigger, SplitText | Tiêu đề tách chữ chạy vào (`split-in-right`), cuộn mượt toàn trang | Tiêu đề hiện theo từng từ; không bật cuộn mượt kiểu "cướp cuộn" (ảnh hưởng truy cập) |
| Magnific Popup | Mở video YouTube khi bấm nút play | Hộp thoại video tự viết, chỉ tải YouTube sau khi bấm |
| MetisMenu | Menu di động có mục con | Menu trượt từ phải, mục con xổ ra |
| Tilt.js | Có nạp nhưng chưa xác định dùng ở đâu | Không dùng |
| Bootstrap, Font Awesome, eicons | Lưới và icon | CSS grid riêng, icon SVG tự vẽ |
| Preloader (`#transpiPreloader`) | Lớp phủ trắng có logo cho tới khi trang tải xong | Lớp phủ logo, ẩn khi tải xong (tối đa 1,5 giây) |

## 2. Thông số carousel đọc được từ mã của site cũ

| Carousel | Thông số |
|---|---|
| Slider hero (nếu dùng) | 1 slide, lặp, hiệu ứng mờ dần (fade), chuyển 2 giây, tự chạy mỗi 5 giây, chấm tròn |
| Dịch vụ, đội ngũ | 3 thẻ một lúc, cách nhau 30 px, lặp, chuyển 1 giây, mũi tên trước/sau |
| Đối tác | 6 logo một lúc, lặp, tự chạy mỗi 5 giây, chuyển 1 giây |
| Nhận xét | 3 thẻ một lúc ở bản demo; trang chủ ptdl dùng bản dọc (mũi tên lên/xuống), tự chạy mỗi 5 giây, lặp |

## 3. Hiệu ứng CSS

- Nút: chuyển màu 0,5 giây, hover nền đổi sang xanh đen `#020E28`.
- Thẻ dịch vụ: icon tròn trắng đè lên mép trên; hover làm đậm bóng.
- Menu con: xổ xuống bằng `scaleY` 0,4 giây; mục con hover thụt vào 15 px.
- Nút play: vòng sóng tỏa ra lặp vô hạn 1,8 giây.
- Ảnh tin tức: phóng to 1,1 lần khi hover (1 giây); nút tròn mũi tên đổi màu.
- Ngành nghề: hàng đang chọn hiện ảnh nền mờ kèm lớp phủ `#020E28`; mặc định hàng thứ hai được chọn.
- Đối tác: logo mờ (độ đục 0,1), rõ lên khi hover hoặc đang hiện.
- Liên kết "Chi tiết": hover tăng khoảng cách chữ.

## 4. Cách site mới xử lý các hiệu ứng

- Tất cả hiệu ứng tắt khi người dùng bật "giảm chuyển động" của hệ điều hành (`prefers-reduced-motion`).
- Không có JavaScript thì nội dung vẫn hiện đầy đủ (hiệu ứng chỉ là phần thêm).
- Không dùng thư viện ngoài. Chỉ có hai kết nối ra Internet: phông chữ Google (DM Sans, Outfit, giống site cũ) và video YouTube (chỉ khi bấm nút play).
- Không làm: cuộn mượt kiểu GSAP ScrollSmoother, popup tìm kiếm toàn màn hình (site tĩnh không có tìm kiếm), icon mạng xã hội (bản cũ chỉ có liên kết `#`).
