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

## 7. Rà soát lại trang chủ và trang Giới thiệu (cập nhật sau phản hồi của chủ site)

Chủ site nhận thấy trang chủ và trang Giới thiệu của bản mới thiếu nhiều nội dung so với bản gốc. Rà soát cho thấy bản dựng đầu đã lược bỏ cả những phần PTDL tự viết vì nghi là chữ mẫu của theme. Đã khôi phục:

**Nguồn trang chủ thật.** Dữ liệu Elementor của trang `home` và mẫu `hme` trong file xuất WordPress hiện chỉ là **bản demo tiếng Anh của theme** (Transmax, Lorem ipsum). Có khả năng demo của theme đã được nhập lại đè lên ngày 06/12/2025 (plugin One Click Demo Import đang cài; các bản sửa đổi của trang Giới thiệu ngày hôm đó cho thấy nội dung bị cắt rồi dựng lại). Vì vậy trang chủ tiếng Việt thật chỉ còn trong **bản Wayback 20/03/2025** (`backup/archive/ptdl.com.vn/index.html`, dàn ý đầy đủ ở `docs/archive-homepage-outline.txt`). Trang Giới thiệu thì dữ liệu Elementor vẫn còn bản tiếng Việt đầy đủ.

| Khối | Trạng thái trước | Hiện tại |
|---|---|---|
| Dịch vụ của chúng tôi (5 thẻ, mô tả gốc) | Viết lại ngắn | Khôi phục nguyên văn, sửa lỗi gõ "247" |
| Số liệu 1.289 chuyển hàng, 745 khách hàng, 68 đối tác, 49 xe tải & container | Bỏ | Khôi phục (lấy từ bộ đếm trên trang chủ cũ) |
| Video giới thiệu YouTube | Bỏ | Có liên kết |
| Form báo giá nhanh (loại hình, số kg, số km, họ tên, SĐT) | Bỏ | Khôi phục, gửi qua email |
| Đội ngũ trẻ năng động, quản lý giàu kinh nghiệm | Thiếu | Khôi phục |
| 3 nhận xét khách hàng (tên thật trên trang cũ) | Bỏ vì nghi mẫu | Khôi phục nguyên văn |
| Bảng giá cước (Bắc Nam từ 12.000/km, nội thành từ 16.000/km, 6 loại xe) | Bỏ | Khôi phục |
| Ngành nghề (chuyển phát nhanh, xe tải, container, siêu trường siêu trọng) | Thiếu 3/4 | Khôi phục (đã bỏ tên công ty khác và số "hơn 200 đầu xe") |
| Logo 6 đối tác (Pepsico, Shopee, J&T, Giaohangtietkiem, Viettel, Gemadept) | Bỏ | Khôi phục |
| Biểu mẫu đăng ký nhận tin | Bỏ | Khôi phục (gửi qua email) |
| Nút "Đặt lịch Online", menu Dịch vụ có mục con, khẩu hiệu "số 1 thị trường", email info@ | Thiếu | Khôi phục |
| Trang Giới thiệu: mục Năng lực vận chuyển (6 mục), "Tại sao chọn chúng tôi", "Vận tải 64 tỉnh thành", logo đối tác | Bỏ | Khôi phục |

**Cần chủ site xác nhận trước khi đăng.** Các mục khôi phục là nội dung nguyên văn của website cũ nhưng chưa có nguồn độc lập và có mâu thuẫn: 63 hay 64 tỉnh, "hơn 10 năm" so với thành lập 2019, "400 tấn mỗi ngày", "hơn 10.000 khách hàng", "hơn 1.000 đại lý", tên Samsung và Honda là đối tác, bảng giá, "liên hệ lại sau 5 phút", nhận xét khách hàng, quyền hiển thị logo đối tác. Một số câu có dấu hiệu sao chép từ công ty khác (nhầm tên "TPTDL Transport", "Trọng tấn"). Mọi chỗ này đều có chú thích `TODO` trong mã nguồn.

## 8. Rà soát trang Dịch vụ, Chuyển hàng Bắc – Nam và Liên hệ

**Nguồn.** Dữ liệu Elementor của trang `services` cũng đã bị thay bằng bản demo tiếng Anh của theme, nên trang Dịch vụ tiếng Việt gốc không còn bản đầy đủ. Nội dung được dựng lại từ các thẻ dịch vụ và ngành nghề trên trang chủ Wayback và từ trang "Chuyển hàng Bắc Nam". Trang Liên hệ vẫn còn dữ liệu tiếng Việt đầy đủ.

| Trang | Đã bổ sung |
|---|---|
| Dịch vụ | Mô tả gốc (liên tỉnh "1,25 – 10 tấn", "24/7"; xe tải 1T9 đến 15 tấn; container; chuyển phát nhanh), mục **Hàng siêu trường siêu trọng** (trước đó bị mất), liên kết tới bảng giá |
| Chuyển hàng Bắc – Nam (`/services/chuyen-hang-bac-nam`, trang riêng như WordPress cũ) | Các dịch vụ vận tải, vận chuyển container, 3 phương thức giao nhận, cách tính cước và số khối, thời gian giao hàng, đóng gói hàng hóa, chính sách đền bù PTDL |
| Liên hệ | "Nhận báo giá", "Liên hệ 24/7", "Đăng ký tư vấn" kèm cam kết 5 phút, ô Chủ đề, bản đồ Google |

**Đã cố ý không đưa vào trang Bắc – Nam** (nằm trong bản 12/2025 của website cũ nhưng là nội dung của công ty khác hoặc không phải dịch vụ của PTDL): mọi đoạn nêu tên "Trust Friend", giá "từ 1.500 nghìn", danh sách bãi xe Hà Nội, TP.HCM, Bình Dương, thời gian chạy, "hơn 100 đầu xe", giảm giá 10% và 30%, hotline 0961.565.015, mục "Thanh toán tiền thu hộ" (rút tiền về ngân hàng) và dòng nhắc mã vận đơn của đơn vị khác.

**Cần chủ site xác nhận:** phí giao nhận theo yêu cầu "300.000đ đến 1.200.000đ", mức bồi thường "4 lần cước" và "100% giá trị hàng hóa", "Liên hệ 24/7" so với giờ văn phòng 8:00 - 20:00, địa chỉ trên bản đồ (phường Tân Phong hay Tân Hưng).

Trang Tra cứu vận đơn vẫn là trang giữ chỗ: bản gốc chỉ có mã nhúng `[wpcargo_trackform]`, cần khôi phục hệ thống WPCargo.
