# Website PTDL (bản tĩnh dự phòng)

Bản dự phòng bằng HTML, CSS và một ít JavaScript thuần (không framework, không bước build, không CDN, không font ngoài). Dùng khi website WordPress bị tấn công không cứu được. Ngôn ngữ: tiếng Việt. Màu thương hiệu: xanh `#5c8330` (lấy từ biến `--thm-primary` của theme gốc).

## Cấu trúc

- `index.html` Trang chủ
- `gioi-thieu.html` Giới thiệu
- `dich-vu.html` Dịch vụ (Chuyển hàng Bắc – Nam, miền Bắc, miền Nam, miền Trung, liên tỉnh, nội thành, xe tải và container, chuyển phát nhanh)
- `tin-tuc.html` Danh sách tin tức, cùng 3 bài: `le-ban-giao-lo-xe-thaco.html`, `huong-dan-gui-hang-di-uc-tai-binh-duong.html`, `cach-chuyen-nha-duong-dai-o-ha-noi.html`
- `lien-he.html` Liên hệ (biểu mẫu dạng `mailto:`)
- `tracking.html` Tra cứu vận đơn (trang giữ chỗ, không có dữ liệu giả)
- `assets/css/styles.css`, `assets/js/main.js` (chỉ bật/tắt menu trên điện thoại), `assets/images/`, `assets/video/` (đang trống)

## Mở trên máy

Nhấp đúp `index.html` để mở bằng trình duyệt. Hoặc chạy máy chủ thử: `python -m http.server 8000` trong thư mục `site`, rồi vào http://localhost:8000.

## Đưa lên hosting

Tải toàn bộ nội dung thư mục `site` lên thư mục gốc của hosting (ví dụ `public_html`) bằng FTP hoặc File Manager. Hosting nào chạy được file HTML đều dùng được, không cần PHP hay database. Nhớ thay các file WordPress cũ khi cắt chuyển, và bảo đảm chứng chỉ HTTPS còn hạn.

## Việc cần làm (TODO) và nội dung còn thiếu

Các chỗ cần nội dung thật được đánh dấu trong mã nguồn bằng `<!-- TODO: need real content from PTDL -->`.

1. **Video lễ bàn giao Thaco** (67 MB, không chép vào thư mục này). Chép `backup/live/media/2024/05/Ban-giao-lo-10-xe-Thaco-Linker-Binh-Trieu.mp4` thành `assets/video/ban-giao-lo-10-xe-thaco-linker.mp4`, hoặc đăng YouTube rồi nhúng. Khi chưa có file, bài chỉ hiện ảnh poster.
2. **Biểu mẫu liên hệ**: hiện mở ứng dụng email gửi tới `ptdl.support@gmail.com`, không gửi dữ liệu lên máy chủ. Cần backend thật (Formspree, PHP mail...) rồi đổi `action` trong `lien-he.html`.
3. **Địa chỉ và email**: nguồn mâu thuẫn. Trang Liên hệ cũ ghi "36 Hưng Gia 1", chân trang bản 2025 ghi "26 Đường Nội khu Hưng Gia 1" (đang dùng). Email có `ptdl.support@gmail.com` và `info@ptdl.com.vn`. Cần PTDL xác nhận.
4. **Số liệu năng lực** (tấn mỗi ngày, số khách hàng, số tỉnh thành, đối tác, đại lý): trang gốc có nhưng số liệu mâu thuẫn (63 hay 64 tỉnh) và chưa xác nhận, nên chưa đưa vào. Chỉ giữ "hơn 10 năm kinh nghiệm" và phương châm "nhanh – an toàn – tiết kiệm".
5. **Bảng giá cước** (bản lưu 2025-03 có giá "từ 12.000/km"...): chưa xác nhận còn áp dụng, đã bỏ.
6. **Nội dung các tuyến miền Bắc, miền Nam, miền Trung**: trang gốc chỉ có một nội dung chung; trang "Chuyển hàng Bắc Nam" có vẻ sao chép từ đơn vị khác (nhắc tên "Trust Friend", hotline và giá khác) nên chỉ lấy ý chung, bỏ giá, thời gian, địa chỉ bãi xe.
7. **Đội ngũ, lời nhận xét khách hàng, logo đối tác**: nguồn chỉ có dữ liệu mẫu của theme (hoặc chưa xác nhận), đã bỏ.
8. **Tra cứu vận đơn**: cần khôi phục hệ thống WPCargo và dữ liệu đơn hàng.
9. **Ảnh**: `assets/images/thaco-le-trao-chia-khoa.png` nặng khoảng 3,6 MB, nên nén lại. Ảnh `xe-ptdl-chinh-dien.jpg` dùng ở trang chủ là ảnh xe PTDL từ thư viện media, cần PTDL xem lại. Nên bổ sung ảnh xe, kho bãi thật khác nếu có.
10. Facebook fanpage: nguồn chỉ có widget của trang demo, chưa có đường dẫn thật, nên chưa thêm.
