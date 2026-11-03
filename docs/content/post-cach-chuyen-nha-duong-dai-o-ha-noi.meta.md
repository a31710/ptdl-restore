# Bài viết: Cách chuyển nhà đường dài ở Hà Nội

Thông tin lấy từ REST API của site (ngày 2026-11-03), màn hình sửa bài viết trong `wp-admin` và HTML gốc do chủ site cung cấp.

## Thông tin chung
- ID bài viết: 1755
- Slug: `cach-chuyen-nha-duong-dai-o-ha-noi` (đường dẫn có đuôi `.htm`)
- URL: https://ptdl.com.vn/cach-chuyen-nha-duong-dai-o-ha-noi.htm
- Trạng thái: đã xuất bản (publish)
- Ngày đăng: 2024-05-19 12:03
- Chỉnh sửa lần cuối: 2025-12-06 15:41
- Danh mục: ID 1 (mặc định), không có thẻ
- Trình soạn thảo: có nút "Sửa với Elementor"
- HTML gốc (từ chế độ "Mã" của trình soạn thảo): `post-cach-chuyen-nha-duong-dai-o-ha-noi.source.html`
- Bản chữ thuần: `post-cach-chuyen-nha-duong-dai-o-ha-noi.md`

## Cấu trúc nội dung
1. Đoạn mở đầu: xác định công ty chuyển nhà, ngày giờ chuyển, phí đậu xe và phí cầu đường. Kèm ảnh minh họa.
2. Danh sách dụng cụ đóng gói PTDL chia sẻ: màng bong bóng, thùng carton, màng căng, túi đóng gói, túi nén chân không, băng dính, bút dạ và giấy ghi chú.
3. Hai ảnh có chú thích (`[caption]`) xen giữa danh sách.
4. Hai đoạn kết: phân loại và thanh lý đồ trước khi đóng gói, tự đóng gói hoặc nhờ công ty chuyển nhà đóng gói. PTDL có dịch vụ di chuyển đường dài.

## Tệp đính kèm
| Loại | Tệp | ID | Kích thước hiển thị | Có trong dự án |
|---|---|---|---|---|
| Ảnh trong bài | `wp-content/uploads/2024/05/Undsadsa.jpg` | 1986 | 616x410 | Có, trong `images/` |
| Ảnh có chú thích | `wp-content/uploads/2024/05/Moi-do-dac-se-duoc-bao-boc-ky-luong-bang-mut-xop-vai-carton-mang-pier-hoac-nem-chuyen-dung.jpg` | 1758 | 650x433 | Có, trong `images/` |
| Ảnh có chú thích | `wp-content/uploads/2024/05/Dong-goi-ghi-chu-ro-rang-nhung-do-dung-cong-ty.jpg` | 1757 | 650x470 | Có, trong `images/` |
| Ảnh đại diện (featured) | `wp-content/uploads/2024/05/af6e3f194542ca1c9353.jpg` | 2016 | — | Có, trong `images/` |

## Lưu ý khi dựng lại
- Nội dung dùng shortcode `[caption]...[/caption]` của WordPress. Khi dựng lại bằng HTML thuần, đổi thành thẻ `<figure>` và `<figcaption>`.
- Văn bản gốc viết tắt công ty là "PDTL" ở một số chỗ, trong khi tên đúng là "PTDL". Nên sửa khi dựng lại.
- Các đoạn văn nằm trực tiếp, không bọc thẻ `<p>`. WordPress tự thêm thẻ khi hiển thị, nên cần bọc lại khi chuyển sang HTML thuần.
