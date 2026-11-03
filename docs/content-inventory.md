# Kiểm kê nội dung ptdl.com.vn

Cập nhật: 2026-11-03. Tổng hợp sau khi lấy dữ liệu từ REST API, file xuất WordPress (WXR), thư viện media, các bản sửa đổi, Wayback Machine và nguồn công khai.

## 1. Tình trạng nguồn
- Front end WordPress: **mọi trang đều trả về lỗi 500** (đã thử 12 địa chỉ). Không lấy được chữ hiển thị trực tiếp.
- `wp-admin` và REST vẫn chạy; đó là nguồn chính của dữ liệu đã lấy.
- Wayback Machine: chỉ có trang chủ. Common Crawl và archive.today: không lấy được (lỗi 504 và CAPTCHA).
- Theme options (Transpi Options) không chứa thông tin liên hệ, chân trang hay mạng xã hội (liên kết đều là `#`).

## 2. Kiểm kê theo trang
| Trang / bài | Mức đầy đủ | Nguồn | Ghi chú |
|---|---|---|---|
| Trang chủ | Khá đầy đủ | Elementor JSON, WXR, Wayback 2025-03-20 | Có tiêu đề, dịch vụ, khối giới thiệu. Một số số liệu chưa xác nhận. |
| Giới thiệu | Đủ chữ | Elementor JSON, WXR, 45 bản sửa đổi | Bản cũ có thêm câu "64 tỉnh thành", "đối tác của nhiều tập đoàn". Cần chủ site xác nhận. |
| Dịch vụ | Mỏng | Elementor JSON, WXR | Trang gốc chỉ khoảng 1 KB chữ. |
| Chuyển hàng Bắc Nam | Có nhưng **không dùng được nguyên văn** | WXR, 14 bản sửa đổi | Bản ngày 06/12/2025 có dấu hiệu sao chép từ công ty khác (thương hiệu, hotline, giá khác). Bản gốc 05/2024 chỉ là chữ mẫu lorem ipsum của theme. |
| Chuyển hàng miền Bắc, Nam, Trung | **Thiếu** | Không có | Trong menu nhưng không có nội dung riêng. |
| Liên hệ | Đủ | WXR, Elementor JSON | Địa chỉ, hotline, hai email. |
| Tracking (Tra cứu vận đơn) | Chỉ khung | WXR | Cần hệ thống WPCargo. Chỉ có 1 vận đơn mẫu. |
| Bài: Lễ bàn giao lô xe Thaco | Đầy đủ | HTML gốc, WXR | Video 67 MB chỉ lưu trên máy. |
| Bài: Gửi hàng đi Úc tại Bình Dương | Đầy đủ | HTML gốc, WXR | |
| Bài: Cách chuyển nhà đường dài ở Hà Nội | Đầy đủ | HTML gốc, WXR | |
| Bài: Bảo hiểm hàng hóa là gì? | **Khôi phục từ bản sửa đổi** | Revision 2018, Wayback | Không còn trong bản hiện tại. Cần xác nhận chính sách đền bù. |
| Trang Projects, Team, FAQ, Home Two/Three... | Không dùng | Trang mẫu của theme | Bỏ. |
| Trang spam ("Hacked by ...") | Không dùng | | 139 trang và 19 bài, đã chuyển vào thùng rác. |

## 3. Thông tin công ty (nguồn công khai, chưa xác nhận từ chủ site)
| Mục | Giá trị | Mức tin cậy |
|---|---|---|
| Tên pháp lý | CÔNG TY TNHH GIẢI PHÁP VẬN CHUYỂN PTDL | Cao |
| Tên tiếng Anh | PTDL Transport Solutions Co., Ltd. | Trung bình |
| Mã số thuế | 0315825861 | Cao |
| Ngày thành lập | 05/08/2019 | Cao |
| Ngành chính | Vận tải hàng hóa đường bộ (mã H4933), kho bãi, xếp dỡ | Cao |
| Địa chỉ | 36 Đường Nội khu Hưng Gia 1, TP. Hồ Chí Minh (phường: Tân Hưng theo dữ liệu thuế 09/2026, Tân Phong theo nguồn cũ) | Cao cho số 36, trung bình cho phường |
| Hotline | 0285 5555 565 | Từ chính website, chưa có nguồn độc lập |
| Email | ptdl.support@gmail.com (trang liên hệ), info@ptdl.com.vn (trang chủ) | Trung bình, hai địa chỉ cùng tồn tại |
| Giờ làm việc | T2 - CN: 8:00 - 20:00 (đầu trang); "24/7" (trang liên hệ cũ) | Mâu thuẫn |

## 4. Mâu thuẫn cần chủ site quyết định
1. Địa chỉ số **26** (chân trang cũ) hay **36** (mọi nguồn công khai). Site mới đang dùng 36.
2. "Hơn 10 năm kinh nghiệm" so với ngày thành lập 2019 (khoảng 7 năm).
3. "63 hay 64 tỉnh thành", các số liệu năng lực (khách hàng, số xe, tải trọng).
4. Giờ làm việc: 8:00 - 20:00 hay 24/7.
5. Email chính thức: ptdl.support@gmail.com hay info@ptdl.com.vn.

## 5. Còn thiếu (chủ site hoặc NhanHoa cung cấp)
- Nội dung riêng cho các tuyến miền Bắc, miền Nam, miền Trung và Bắc Nam.
- Bảng giá, đối tác, số liệu năng lực, khách hàng tiêu biểu (hiện không có nguồn đáng tin).
- Nội dung thật các form liên hệ đã gửi, dữ liệu vận đơn WPCargo, đơn hàng (nằm trong database trên server NhanHoa).
- Ảnh gốc của công ty chất lượng cao (nếu có bản gốc trước khi nén).
- Xác nhận quyền dùng các ảnh stock trong bài bảo hiểm.

## 6. Việc đã làm trên site mới (`site/`, bản 2)
- Dùng địa chỉ số 36, phường Tân Hưng, TP. Hồ Chí Minh, thêm mã số thuế vào chân trang (có chú thích TODO xác nhận).
- Thêm bài "Bảo hiểm hàng hóa là gì? Tại sao doanh nghiệp nên mua?" vào mục Tin tức.
- Ghi chú TODO ở khẳng định "Hơn 10 năm kinh nghiệm".
