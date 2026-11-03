# Tin nhắn gửi NhanHoa (hỗ trợ kỹ thuật)

Gửi qua kênh chính thức: hotline hoặc hệ thống ticket trong trang của NhanHoa (tự tìm trên nhanhoa.com, không dùng đường dẫn trong email hay tin nhắn lạ). Không gửi mật khẩu trong tin nhắn.

---

Kính gửi bộ phận kỹ thuật NhanHoa,

Tôi là đại diện Công ty TNHH Giải pháp Vận chuyển PTDL, chủ tài khoản hosting của website **ptdl.com.vn** (máy chủ gir02.nhanhoa.com, IP 103.124.95.33, tài khoản hosting `nhxuoq3c`). Website đang gặp sự cố, nhờ quý công ty hỗ trợ:

**Hiện trạng**
1. Website bị chèn nội dung ("Hacked by ..." trên thanh quản trị) và có hàng trăm trang spam không phải của chúng tôi.
2. Trang chủ trả về lỗi HTTP 500 ("đã có một lỗi nghiêm trọng trên trang web").
3. Cập nhật WordPress thất bại với lỗi `fopen(/tmp/...): failed to open stream: Disk quota exceeded`. Dung lượng WordPress chỉ khoảng 394 MB, nên có thể có dung lượng lớn nằm ngoài thư mục WordPress.
4. Chứng chỉ SSL của ptdl.com.vn đã hết hạn (lỗi ERR_CERT_DATE_INVALID).
5. Phiên bản PHP đang là 7.4.33, đã hết hỗ trợ.

**Đề nghị hỗ trợ**
1. Xác minh chủ sở hữu tài khoản và cấp lại quyền truy cập control panel cho chủ tài khoản.
2. Cho biết dung lượng đang dùng so với hạn mức và thư mục nào chiếm nhiều nhất (kể cả `/tmp`, hộp thư, backup, log).
3. Kiểm tra và quét mã độc, file lạ hoặc tác vụ định kỳ (cron) trong toàn bộ tài khoản, không chỉ thư mục WordPress.
4. Gia hạn hoặc cài lại chứng chỉ SSL (AutoSSL/Let's Encrypt) cho ptdl.com.vn và www.ptdl.com.vn.
5. Gửi cho chúng tôi bản sao lưu gần nhất còn sạch (file và database), kèm ngày của bản sao lưu. Nếu có thể, bản trước tháng 12/2025.
6. Gửi file log lỗi PHP (`error_log`) tại thời điểm trang chủ báo lỗi 500, để xác định plugin hoặc theme gây lỗi.
7. Nâng phiên bản PHP lên bản được hỗ trợ, tương thích với WordPress đang dùng.
8. Kiểm tra các tài khoản FTP/SSH/email và các quyền truy cập đã tạo gần đây.

Rất mong sớm nhận được phản hồi. Xin cảm ơn.

Người liên hệ: [Họ tên, chức vụ] — Số điện thoại: [số điện thoại] — Email: [email liên hệ]
