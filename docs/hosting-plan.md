# Kế hoạch thuê hosting và đưa website lên (soạn 2026-11-13)

Website hiện là **site tĩnh** (HTML, CSS, JS, ảnh; khoảng 5,6 MB). Không cần PHP, không cần database, không cần WordPress. Thư mục cần đưa lên là `preview/` (tạo bằng `python scripts/build_preview.py`).

## 0. Quy tắc an toàn (đọc trước)
- Không bấm link trong email "Gui lai thong tin dang ky domain" hay email bất kỳ về hosting/tên miền. Tự gõ địa chỉ nhà cung cấp.
- Mật khẩu: dùng trình quản lý mật khẩu, bật xác thực 2 bước (2FA) cho tài khoản domain (access.dotvndns.vn) và tài khoản hosting. Không ghi mật khẩu vào file dự án hay chat.
- **Không bao giờ copy file từ hosting cũ (NhanHoa) sang hosting mới.** Hosting cũ đã bị hack. Hosting mới chỉ nhận thư mục `preview/` sạch từ máy này.
- Không upload các thư mục `backup/`, `docs/`, `site/`, `scripts/` (có dữ liệu spam, tài liệu nội bộ).

## 1. Việc làm trước khi thuê (30 phút, quan trọng nhất)
1. Đăng nhập access.dotvndns.vn, chụp ảnh **toàn bộ bản ghi DNS** hiện tại (A, CNAME, MX, TXT, nameserver). Lưu vào chỗ riêng, không đưa vào git nếu có thông tin nhạy cảm.
2. Xác định **email công ty** (info@ptdl.com.vn, ptdl.support@gmail.com): info@ đang chạy ở đâu? Nếu nó nằm trên hosting NhanHoa thì khi bỏ hosting đó, thư sẽ ngừng. Lúc đó có 3 cách: (a) giữ gói email ở NhanHoa, (b) chuyển sang dịch vụ email riêng (Google Workspace, Zoho Mail...), (c) tạo email ngay trên hosting mới. Quyết định trước khi đổi DNS.
3. Quyết định xử lý hosting cũ: giữ vài tuần để so sánh rồi hủy, **không** dùng lại.
4. Mở sẵn `docs/seo.md` và `docs/page-audit.md`.

## 2. Chọn hosting
Tiêu chí tối thiểu (gói rẻ nhất là đủ, vì chỉ có 5,6 MB file tĩnh):
- Apache hoặc LiteSpeed (đọc được `.htaccess`), có cPanel hoặc DirectAdmin, File Manager hoặc FTP/SFTP.
- SSL miễn phí (Let's Encrypt/AutoSSL), tự gia hạn.
- Máy chủ ở Việt Nam hoặc Singapore, ổ SSD/NVMe.
- Có sao lưu tự động hằng ngày hoặc hằng tuần; cho phép tạo email theo tên miền (nếu chọn cách c ở mục 1).
- Có thể thuê gói 12 tháng hoặc hơn, và ghi nhận tên chủ sở hữu tài khoản là công ty.
- Chỉ mua trên website chính thức của nhà cung cấp, tự gõ địa chỉ.

Phương án thay thế (không phải thuê hosting): Cloudflare Pages hoặc Netlify, miễn phí, có CDN, không có PHP nên ít bị tấn công. Điều kiện: phải chuyển nameserver tên miền sang Cloudflare, và phải viết lại luật chuyển hướng (không dùng `.htaccess`). Tôi làm được nếu bạn muốn; kế hoạch dưới đây là cho hosting thuê (đã chuẩn bị `.htaccess`).

## 3. Thiết lập hosting mới
1. Mua gói, đăng nhập control panel, bật 2FA, đổi mật khẩu mặc định.
2. Thêm tên miền chính `ptdl.com.vn` vào hosting (domain chính, không phải addon). Ghi lại: **địa chỉ IP của hosting** và **nameserver của hosting** (nếu có).
3. Xóa file mẫu trong `public_html` (index.html mặc định của nhà cung cấp).
4. Chọn phiên bản PHP mới nhất đang hỗ trợ (site không dùng PHP nhưng tránh phiên bản cũ), tắt chạy PHP ở thư mục tải lên nếu có tùy chọn.

## 4. Đưa source lên
Trên máy này:
```bash
python scripts/build_preview.py
```
Rồi đưa **nội dung bên trong** `preview/` (không phải thư mục `preview` cha) vào `public_html`:
- Cách dễ nhất: nén nội dung `preview/` thành zip, upload bằng File Manager, giải nén trong `public_html`.
- Hoặc FTP/SFTP bằng FileZilla.
- Phải có cả file ẩn `.htaccess` (bật "hiện file ẩn" khi kiểm tra).
- Xóa trên server sau khi upload: `README.md`, `serve.py`, `run-local.bat`, `_links.html` (chỉ dùng trên máy cá nhân).

Kết quả đúng: `public_html/index.html`, `public_html/.htaccess`, `public_html/assets/`, `public_html/services/`, `public_html/category/`, các file `.htm` và `.html`, `sitemap.xml`, `robots.txt`, `404.html`.

## 5. Thử trước khi đổi DNS
Mục tiêu: chắc chắn site chạy đúng trên hosting mới trước khi người dùng thấy nó.
- Nhiều nhà cung cấp cho một địa chỉ tạm (dạng `ip/~tên-tài-khoản` hoặc tên miền tạm). Hoặc sửa file `hosts` trên máy: `IP_HOSTING ptdl.com.vn`. Nhớ xóa dòng này sau khi thử xong.
- Danh sách kiểm tra: mở lần lượt các đường dẫn trong `/_links` (xem `preview/README.md`); trang không có thật phải trả về 404 thật; `/gioi-thieu/` chuyển về `/gioi-thieu`; `/gioi-thieu.html` chuyển về `/gioi-thieu`; ảnh, font, CSS, JS đều tải; thanh tìm kiếm chạy; menu điện thoại.
- Nếu hosting báo lỗi 500 hoặc vòng lặp chuyển hướng, nguyên nhân thường là `.htaccess` (chuyển hướng https/www). Tạm đổi tên `.htaccess` để thử, rồi báo tôi chỉnh lại.

## 6. Chuyển DNS (ngày go-live)
1. **Trước 1 ngày:** hạ TTL các bản ghi A của `@` và `www` xuống 300 giây (5 phút) nếu trang quản lý cho phép.
2. Vào access.dotvndns.vn, sửa bản ghi:
   - `@` (A) trỏ tới IP hosting mới.
   - `www` (A hoặc CNAME) trỏ tới IP hosting mới (hoặc CNAME về `ptdl.com.vn`).
   - **Không đụng tới MX, TXT (SPF, DKIM) và các bản ghi mail** nếu email vẫn chạy chỗ khác.
3. Nếu hosting mới yêu cầu đổi nameserver thay vì đổi bản ghi A: phải tạo lại **đầy đủ** các bản ghi (nhất là MX, TXT) ở nameserver mới trước khi đổi.
4. Chờ lan truyền (thường vài chục phút đến vài giờ). Kiểm tra bằng whatsmydns.net.
5. Khi `ptdl.com.vn` đã trỏ đúng, vào control panel bấm cấp SSL (AutoSSL/Let's Encrypt). Chứng chỉ cần DNS đã trỏ về hosting mới.
6. Mở https://ptdl.com.vn, https://www.ptdl.com.vn, http://ptdl.com.vn: cả ba phải về `https://ptdl.com.vn/`.
7. **Phương án quay lại:** giữ nguyên giá trị DNS cũ đã chụp ở bước 1; nếu có sự cố lớn, trả bản ghi A về giá trị cũ.
8. Chỉ khi https chạy ổn định vài ngày mới nên giữ dòng HSTS trong `.htaccess` (đã có sẵn; nếu https lỗi, HSTS làm trình duyệt không vào được).

## 7. SEO sau khi lên mạng
Chi tiết ở `docs/seo.md`. Thứ tự làm:
1. Google Search Console: thêm `https://ptdl.com.vn/` (xác minh bằng bản ghi TXT hoặc file HTML), gửi `https://ptdl.com.vn/sitemap.xml`.
2. Công cụ **Removals** trong Search Console: yêu cầu xóa các URL spam "Hacked by ..." đang còn trong Google. Với các URL spam, nên trả mã **410 Gone** để Google bỏ nhanh hơn (tôi có thể thêm luật vào `.htaccess` cho các đường dẫn dạng chuỗi ký tự ngẫu nhiên và `/wp-*`).
3. Bing Webmaster Tools (nhập từ Search Console).
4. Rich Results Test (kiểm tra schema) và PageSpeed Insights (mục tiêu: LCP < 2,5 giây, CLS gần 0).
5. Google Business Profile: tên, địa chỉ (36 Đường Nội khu Hưng Gia 1, Phường Tân Phong, Quận 7), số điện thoại phải khớp với trên web.
6. Đặt nhắc việc sau 2 tuần và 6 tuần: xem báo cáo Pages (trang nào chưa được lập chỉ mục), Core Web Vitals, truy vấn tìm kiếm.

## 8. Biểu mẫu liên hệ (quyết định cần làm)
Biểu mẫu báo giá và liên hệ đang là `mailto:`, nghĩa là mở ứng dụng email trên máy khách, nhiều người sẽ bỏ dở. Không chặn việc lên mạng, nhưng nên làm sớm. Lựa chọn:
- Một script PHP nhỏ trên hosting gửi email tới `ptdl.support@gmail.com` (cần hosting có PHP và gửi mail; cần thêm chống spam).
- Dịch vụ biểu mẫu bên ngoài (gửi thẳng vào email, không cần PHP).
Nói với tôi để chọn và viết.

## 9. Bảo trì và an toàn sau khi lên
- Nguồn sự thật là repo GitHub này. Muốn sửa: sửa trong `site/`, chạy `build_preview.py`, upload lại `preview/`. Không sửa trực tiếp trên server.
- Bật sao lưu tự động của hosting; thỉnh thoảng tải một bản về máy.
- Không cài WordPress hay plugin nào trên hosting này. Không cần tài khoản FTP khi không dùng, hãy tắt.
- Gia hạn tên miền và hosting: bật tự gia hạn, đặt lịch nhắc 30 ngày trước hạn.
- Việc chủ site còn lại: xác nhận nội dung có đánh dấu TODO trong `docs/page-audit.md`; chuyện tài khoản quản trị `acadtapi` chỉ còn liên quan nếu giữ WordPress cũ.

## 10. Lịch gợi ý
| Ngày | Việc |
|---|---|
| Ngày 1 (sáng) | Mục 1, chọn và thuê hosting (mục 2 và 3). Hạ TTL DNS. |
| Ngày 1 (chiều) | Build và upload (mục 4), thử bằng hosts (mục 5). Sửa lỗi nếu có. |
| Ngày 2 | Đổi DNS (mục 6), cấp SSL, kiểm tra. Rồi Search Console, Removals (mục 7). |
| Tuần 1-2 | Biểu mẫu liên hệ (mục 8), Business Profile, theo dõi báo cáo. |

## 11. Email mới (bắt buộc nếu mất hosting cũ) - cập nhật 2026-11-13
Nếu không lấy lại được hosting cũ thì hộp thư info@ptdl.com.vn cũ (và thư bên trong) coi như mất, trừ khi NhanHoa còn bản sao lưu. Cần email mới **trước hoặc cùng lúc** đổi DNS.

**Rủi ro cần nhớ:** bản ghi MX hiện vẫn trỏ về máy chủ cũ. Nếu để nguyên, thư gửi tới @ptdl.com.vn sẽ vào máy chủ đã bị xâm nhập, và người nắm quyền máy chủ đó có thể đọc, kể cả thư đặt lại mật khẩu. Vì vậy phải đổi MX sang nhà cung cấp email mới ngay ở bước go-live, không để nguyên.

**Chọn nhà cung cấp email (không dùng email của hosting, vì dễ vào spam và cùng chỗ với web):**
- Google Workspace: giao diện Gmail quen thuộc, gửi/nhận ổn định, trả phí theo hộp thư.
- Zoho Mail: có gói miễn phí giới hạn và gói trả phí rẻ; kiểm tra điều kiện gói hiện tại trên trang chính thức.
- Chỉ đăng ký trên trang chính thức, tự gõ địa chỉ.

**Thứ tự làm:**
1. Đăng ký và xác minh tên miền với nhà cung cấp email (thêm bản ghi TXT xác minh ở access.dotvndns.vn).
2. Tạo hộp thư: info@ptdl.com.vn và (nếu cần) tên khác cho từng người. Bật 2FA cho quản trị.
3. Thêm bản ghi DNS theo hướng dẫn của nhà cung cấp: **MX** (thay hoàn toàn MX cũ), **SPF** (TXT, chỉ một bản ghi SPF duy nhất), **DKIM** (TXT), **DMARC** (TXT tại `_dmarc`, bắt đầu bằng `p=none`, sau vài tuần nâng lên `quarantine`).
4. Gửi thử thư hai chiều (từ Gmail cá nhân tới info@ và ngược lại); kiểm tra thư không vào spam bằng mail-tester.com.
5. Xóa các bản ghi MX/SPF cũ trỏ về NhanHoa để không còn đường thư vào máy chủ cũ.

**Việc liên quan:**
- Đổi **email khôi phục / email chủ tài khoản** của mọi dịch vụ đang dùng info@ptdl.com.vn (Google Search Console, Google Business Profile, tài khoản domain, hosting mới...). Dùng hộp thư mà công ty thật sự nắm quyền (ví dụ ptdl.support@gmail.com hoặc hộp thư mới) trong lúc chuyển.
- Biểu mẫu liên hệ hiện gửi tới ptdl.support@gmail.com (Gmail), **không bị ảnh hưởng** bởi việc mất hosting.
- Website đang hiện info@ptdl.com.vn ở chân trang, trang Liên hệ, trang 404 và dữ liệu schema. Nếu địa chỉ email mới khác, báo tôi để cập nhật đồng bộ mọi chỗ; nếu chưa có email mới ngày go-live, có thể tạm bỏ dòng info@ khỏi web.
- Hỏi NhanHoa (qua kênh chính thức) xem họ còn bản sao lưu thư không; nếu còn, xin tải về trước khi tài khoản bị hủy.

### Quyết định (2026-11-13): dùng email kèm hosting mới
Chủ site chọn thuê hosting có email (một nhà cung cấp cho cả web và thư). Vì vậy:
- Khi chọn gói, kiểm tra có: hộp thư theo tên miền, IMAP/SMTP, SPF và DKIM tự bật (hoặc có hướng dẫn), webmail, bật được 2FA cho control panel.
- Sau khi tạo hộp thư, thêm DMARC (TXT `_dmarc`, bắt đầu `p=none`) và gửi thử hai chiều + mail-tester.com.
- **Sao lưu thư:** git chỉ giữ được website, không giữ thư. Đặt chuyển tiếp (forward) info@ sang ptdl.support@gmail.com để luôn có một bản thư ở Gmail, và/hoặc dùng IMAP với một ứng dụng thư trên máy.
- Mật khẩu hộp thư mạnh, khác nhau, giữ trong trình quản lý mật khẩu. Nguy cơ thực tế còn lại là lộ mật khẩu hộp thư hoặc control panel, không phải mã độc trên web.
- Nếu thư hay vào spam hoặc không ổn, có thể chuyển sang Google Workspace/Zoho sau này bằng cách đổi MX; website không bị ảnh hưởng.
- Vẫn đổi MX về hosting mới ngay ở bước go-live và xóa MX/SPF cũ trỏ NhanHoa (mục 11).
