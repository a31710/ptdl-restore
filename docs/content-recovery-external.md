# Khôi phục nội dung PTDL từ nguồn bên ngoài

Ngày thực hiện: 2026-11-03. Chỉ dùng curl, WebSearch, WebFetch với TLS bình thường. Không dùng trình duyệt, không đụng tới admin, không chạy git.

## 1. Common Crawl

- `collinfo.json` truy cập được (129 crawl, mới nhất CC-MAIN-2026-43).
- Mọi truy vấn index đều trả HTTP 504 Gateway Time-out: 25 crawl khác nhau (từ CC-MAIN-2018-47 đến CC-MAIN-2026-43) với `url=ptdl.com.vn/*&limit=100`, rồi thêm 3 lượt thử lại cách nhau 20 giây trên CC-MAIN-2025-47 với `matchType=domain` và `limit=5`.
- Kết luận: không lấy được index. Đã hết thời gian cho phép, ghi nhận và bỏ qua.
- Không có trang nào được lưu. Thư mục `backup\archive\commoncrawl\` để trống.
- Việc nên làm sau: thử lại vào giờ khác, hoặc dùng Athena/columnar index. Đến lúc đó vẫn chưa biết Common Crawl có gì về ptdl.com.vn hay không.

## 2. Các kho lưu trữ khác

| Kho | Kết quả |
|---|---|
| archive.ph / archive.today | `/newest/https://ptdl.com.vn/` trả HTTP 429 kèm trang CAPTCHA ("One more step, security check"). Không được vượt CAPTCHA, nên không biết có bản chụp hay không. Người dùng có thể tự kiểm tra bằng tay. |
| Wayback availability API | `ptdl.com.vn` có bản gần nhất `https://web.archive.org/web/20250320022357/https://ptdl.com.vn/` (2025-03-20, trang chủ). `ptdl.com.vn/gioi-thieu` không có bản nào. |
| Wayback CDX | Truy vấn `matchType=domain` trả trang "Internet Archive: Temporarily Offline". Truy vấn `url=ptdl.com.vn/*` không trả dòng nào. Khớp với kết luận trước đó: chỉ có trang chủ. |
| Cache của công cụ tìm kiếm | Công cụ tìm kiếm vẫn có các URL thật của site (xem mục 4). Chưa có cache dạng đọc được. |
| WebFetch tới ptdl.com.vn/lien-he/ | Lỗi "certificate has expired". Không bỏ qua kiểm tra chứng chỉ. |

## 3. Thông tin công khai về công ty

Các trang masothue.com, thuvienphapluat.vn, topcv.vn trả 403 cho WebFetch. Dữ liệu dưới đây lấy từ trang dulieuphapluat.vn đọc trực tiếp, kết quả tìm kiếm ghi tóm tắt các trang còn lại, và trang fidovn.com.

| Thông tin | Giá trị | Nguồn | Độ tin cậy |
|---|---|---|---|
| Tên pháp lý | CÔNG TY TNHH GIẢI PHÁP VẬN CHUYỂN PTDL | https://dulieuphapluat.vn/cong-cu/ma-so-thue/0315825861-cong-ty-tnhh-giai-phap-van-chuyen-ptdl.html ; https://www.fidovn.com/companies/20004889 | Cao |
| Mã số thuế | 0315825861 | dulieuphapluat.vn (như trên); kết quả tìm kiếm cho masothue.com và thuvienphapluat.vn đều ghi cùng MST | Cao |
| Tên tiếng Anh | PTDL TRANSPORT SOLUTIONS COMPANY LIMITED; tên viết tắt PTDL TRANS CO., LTD (tùy nguồn) | kết quả tìm kiếm tổng hợp các trang tra cứu MST | Trung bình |
| Địa chỉ đăng ký | 36 Đường Nội khu Hưng Gia 1, Phường Tân Hưng (trước đây ghi Phường Tân Phong), TP Hồ Chí Minh | dulieuphapluat.vn (dữ liệu đồng bộ 29/09/2026); tìm kiếm báo "Tân Phong, Quận 7" ở các nguồn cũ | Cao với số 36 và tên đường; trung bình với tên phường |
| Người đại diện pháp luật | (đã lược bỏ tên cá nhân khỏi bản công khai) | dulieuphapluat.vn | Cao |
| Ngày thành lập | 05/08/2019 | dulieuphapluat.vn | Cao |
| Tình trạng | Đã cấp MST, đang hoạt động | dulieuphapluat.vn | Trung bình |
| Ngành chính | Vận tải hàng hóa đường bộ (H4933). Còn có kho bãi (H5210), bốc xếp (H5224), bưu chính (H5310), thuê xe (N7710), thủy nội địa (H5022) và nhiều ngành khác (xây dựng, bán buôn, quảng cáo, đào tạo) | dulieuphapluat.vn | Cao |
| Quy mô | 10–24 nhân viên, vốn trong nước | https://www.fidovn.com/companies/20004889 | Thấp |
| Website | https://ptdl.com.vn/ | fidovn.com | Cao |
| Hotline | 0285 5555 565 (08:00–20:00, thứ Hai–Chủ nhật; trang liên hệ ghi "24/7") | kết quả tìm kiếm trích trang https://ptdl.com.vn/lien-he/ | Trung bình (chỉ từ snippet của chính site, không có nguồn độc lập; tìm số này riêng không ra gì) |
| Email | ptdl.support@gmail.com (trang liên hệ); info@ptdl.com.vn (trang chủ) | snippet từ ptdl.com.vn | Trung bình. Hai địa chỉ cùng tồn tại trên các trang khác nhau. |
| Dịch vụ | Hàng ghép (nhận từ 100 kg hoặc 1 khối) và nguyên chuyến Bắc–Nam, miền Trung, nội thành HCM/Hà Nội, container, siêu trường siêu trọng (sơ mi rơ moóc sàn thấp), vận tải sự kiện/quảng cáo, thông quan, chuyển nhà | snippet từ ptdl.com.vn, ptdl.com.vn/services/chuyen-hang-bac-nam/ | Trung bình (chưa kiểm tra nội dung gốc, có thể lẫn nội dung sao chép) |
| Thời gian vận chuyển | Bắc–Nam 2–4 ngày, miền Trung 1–3 ngày | snippet trang Bắc Nam | Trung bình |
| Số liệu quảng bá | Hơn 10 năm kinh nghiệm, vận tải 64 tỉnh thành, đội xe "hàng trăm xe", hơn 400 tấn/ngày | snippet trang gioi-thieu | Thấp (tự khai, mâu thuẫn với năm thành lập 2019 nếu đếm chặt) |
| Đội xe / sự kiện | Bài blog: bàn giao lô xe tải Thaco Linker từ THACO AUTO, ngày 05/05/2026 | https://ptdl.com.vn/blog/ (snippet) | Thấp, ngày có thể sai |
| Mạng xã hội | Không tìm thấy | Tìm kiếm Facebook/Zalo/Google Maps không có kết quả liên quan | Không có |
| TopCV / vieclam24h | Có hồ sơ tuyển dụng của công ty (https://www.topcv.vn/cong-ty/cong-ty-tnhh-giai-phap-van-chuyen-ptdl/196121.html). Không đọc được nội dung do 403. | kết quả tìm kiếm | Cao cho sự tồn tại |

## 4. Tiêu đề và mô tả trong kết quả tìm kiếm

Công cụ tìm kiếm không hỗ trợ toán tử `site:` (truy vấn `site:ptdl.com.vn` không ra gì), nhưng truy vấn có từ khóa và `allowed_domains` ra được 7 URL. Tiêu đề lấy từ kết quả. Mô tả chỉ có dạng tóm tắt của công cụ, không phải meta description thô.

| URL | Tiêu đề trong kết quả | Ghi chú nội dung |
|---|---|---|
| https://ptdl.com.vn/ | "PTDL" | Dịch vụ vận chuyển hàng hóa, tuyến Bắc–Nam, miền Trung, nội thành; còn sót chữ mẫu "Transmax", "Aerospace & Defense"; footer @2024; có mục "Cẩm nang vận chuyển" với bài "Bảo Hiểm Hàng Hóa Là Gì? Tại Sao Doanh Nghiệp Nên Mua?" |
| https://ptdl.com.vn/home/ | "Fastest & Secured Logistics Solution & services - PTDL" (một lượt hiện "Home") | Trang chủ thứ hai do WordPress |
| https://ptdl.com.vn/gioi-thieu/ | "About" | 10+ năm kinh nghiệm, 64 tỉnh thành, "Nhanh - an toàn - tiết kiệm" |
| https://ptdl.com.vn/services/chuyen-hang-bac-nam/ | "Vận Tải Bắc" (bị cắt, có thể là "Vận Tải Bắc Nam") | 3 phương thức vận tải đường bộ Bắc–Nam. Có đoạn lạc đề về "Trust Friend Logistics" và rút tiền ngân hàng, có thể là nội dung spam của kẻ tấn công hoặc văn bản sao chép; không dùng lại. |
| https://ptdl.com.vn/lien-he/ | "Liên hệ" | Liên hệ 24/7, 0285.5555.565, ptdl.support@gmail.com, địa chỉ 36 Hưng Gia 1, Phường Tân Phong, Quận 7 |
| https://ptdl.com.vn/blog/ | "Blog" | Danh sách bài; thấy bài Thaco Linker (05/05/2026), gửi hàng đi Úc từ Bình Dương, chuyển nhà đường dài ở Hà Nội |
| https://ptdl.com.vn/cach-chuyen-nha-duong-dai-o-ha-noi/ | "Cách chuyển nhà đường dài ở Hà Nội" | Hướng dẫn đóng gói; ngày hiển thị khác nhau giữa các bản cache (04/04/2026 và 23/02/2026); có bản viết sai "PDTL" |

Không thấy snippet cho `/services/` (trang gốc) hay hai bài blog còn lại (bài về Úc có chủ đề ở trên nhưng không có URL; bài bảo hiểm hàng hóa chỉ thấy tiêu đề). Cần bổ sung URL từ nguồn khác.

Lưu ý: các snippet này có thể phản ánh cache sau thời điểm bị tấn công, nên đối chiếu với bản Wayback 2025-03-20 và bản sao đã tải về trước khi tin.

## 5. Mâu thuẫn

1. Địa chỉ: "26 Đường Nội khu Hưng Gia 1" (nguồn nội bộ của dự án) và "36 Hưng Gia 1" (trang liên hệ của site, tra cứu mã số thuế). Mọi nguồn công khai tôi đọc được đều ghi số 36. Không tìm thấy nguồn công khai nào ghi số 26. Kết luận: số 36 có độ tin cậy cao, số 26 nhiều khả năng là lỗi gõ ở nguồn của dự án (chưa xác nhận).
2. Tên phường: "Phường Tân Phong, Quận 7" (nguồn cũ) và "Phường Tân Hưng, TP Hồ Chí Minh" (dữ liệu MST đồng bộ 29/09/2026). Có vẻ là do sáp nhập đơn vị hành chính; Quận 7 không còn cấp quận trong địa chỉ mới. Nên giữ cả hai dạng hoặc dùng dạng mới có chú thích.
3. Email: ptdl.support@gmail.com (trang liên hệ) và info@ptdl.com.vn (trang chủ).
4. Hotline: trang liên hệ ghi "24/7", trang khác ghi 8:00–20:00.
5. Tên người đại diện: các nguồn viết dấu khác nhau (tên đã được lược bỏ khỏi bản công khai).
6. "Hơn 10 năm kinh nghiệm" so với công ty thành lập năm 2019.
7. Tên bài: "PDTL" sai chính tả trong một bài.

## 6. Không tìm thấy

- Index Common Crawl (504 liên tục); hiện không có trang nào được lưu.
- archive.ph: bị CAPTCHA chặn.
- Wayback ngoài trang chủ: không có.
- Facebook, Zalo, Google Maps, LinkedIn của công ty.
- Nguồn độc lập xác nhận hotline 0285 5555 565 và hai địa chỉ email.
- Nội dung đầy đủ của các trang masothue.com, thuvienphapluat.vn, topcv.vn, hồ sơ fidovn (403 hoặc thiếu dữ liệu).
- Meta description thô của các trang; danh sách đầy đủ ba bài blog với URL.
- Số liệu đội xe cụ thể (số xe, loại xe, biển số) ngoài mô tả quảng bá và bài Thaco Linker.
- Mã số thuế, địa chỉ chính thức từ cổng Tổng cục Thuế (chưa tra trực tiếp).
