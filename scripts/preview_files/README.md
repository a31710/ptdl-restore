# Bản xem trước website PTDL (đường dẫn giống WordPress cũ)

Thư mục này được **tạo tự động** từ `site/` bằng `python scripts/build_preview.py`. Đừng sửa trực tiếp; hãy sửa trong `site/` rồi chạy lại script.

## Chạy trên máy

Cách 1: bấm đúp `run-local.bat` (cần Python 3).

Cách 2: mở terminal trong thư mục này rồi chạy:

```
python serve.py
```

Sau đó mở http://localhost:8080 . Trang http://localhost:8080/_links liệt kê mọi đường dẫn để bấm xem. Đổi cổng bằng `python serve.py 9000`.

## Đường dẫn (theo cài đặt đường dẫn cố định của WordPress cũ)

| Nội dung | Đường dẫn |
|---|---|
| Trang chủ | `/` |
| Giới thiệu | `/gioi-thieu` |
| Dịch vụ | `/services` |
| Chuyển hàng Bắc – Nam | `/services/chuyen-hang-bac-nam` |
| Tin tức | `/blog` |
| Chuyên mục Cẩm nang vận chuyển | `/category/cam-nang-van-chuyen` |
| Liên hệ | `/lien-he` |
| Tra cứu vận đơn | `/tracking` |
| Bài viết | `/<tên-bài>.htm` |

Trang không có dấu `/` ở cuối, bài viết kết thúc bằng `.htm`. Gõ `/gioi-thieu/` sẽ tự chuyển về `/gioi-thieu`, giống WordPress. Địa chỉ không có thật sẽ hiện trang 404 với mã trạng thái 404.

## Khi đưa lên hosting

Tải toàn bộ thư mục lên thư mục gốc của hosting Apache hoặc LiteSpeed (NhanHoa dùng LiteSpeed). File `.htaccess` đã có sẵn để giữ đúng các đường dẫn trên. `serve.py`, `run-local.bat` và `README.md` chỉ dùng cho máy cá nhân, có thể xóa khi triển khai. File `sitemap.xml` và thẻ `canonical` đã dùng tên miền `https://ptdl.com.vn`.

Nội dung còn nhiều chỗ chờ xác nhận (địa chỉ, email, số liệu...), xem `docs/content-inventory.md` trong repo.
