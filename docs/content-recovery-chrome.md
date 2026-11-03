# Bao cao phuc hoi noi dung qua Chrome (chi doc) - ptdl.com.vn

Ngay: 2026-11-03. Chi dung GET/HEAD tu tab wp-admin da dang nhap; khong luu, khong sua gi tren site.

## 1. Front end
**Ket qua: TAT CA 12 URL deu tra ve HTTP 500, khong chi trang chu.** Than trang la trang "WordPress > Loi" (loi nghiem trong, ~2,6 KB, giong nhau o moi URL) nen khong co noi dung hien thi de luu vao `backup/live/rendered/` (khong tao file nao). Cac URL co slash cuoi tu redirect sang ban khong slash (roi van 500).

| URL | Trang thai |
|---|---|
| / | 500 |
| /gioi-thieu/ | 500 |
| /services/ | 500 |
| /services/chuyen-hang-bac-nam/ | 500 |
| /lien-he/ | 500 |
| /tracking/ | 500 |
| /projects/ | 500 |
| /blog/ | 500 |
| /le-ban-giao-lo-xe-thaco.htm | 500 |
| /huong-dan-gui-hang-di-uc-tai-binh-duong-an-toan-va-nhanh-chong.htm | 500 |
| /cach-chuyen-nha-duong-dai-o-ha-noi.htm | 500 |
| /category/cam-nang-van-chuyen/ | 500 |

Trong khi do wp-admin, REST API va tep uploads van hoat dong (loi nam o theme/plugin khi render front end).

## 2. Transpi Options
Xem `docs/theme-options.md`. Tom tat: khong co thong tin lien he/footer text/copyright; link mang xa hoi deu la `#`; logo trong options de trong; mau chu dao #5c8330; preloader GIF media 1948.

## 3. Revisions (REST context=edit)
Ghi chu: "=" nghia la noi dung giong het ban hien tai.

| Muc | ID | Do dai hien tai | So revision | Chi tiet |
|---|---|---|---|---|
| Bai le-ban-giao-lo-xe-thaco | 2012 | 6224 | 4 | 2020 (2025-12-06 16:05, =); 2018 (15:55, 9040) KHAC HAN; 2014 (15:31, 6005) va 2013 (15:31, 6007) chi khac dinh dang HTML, cung van ban |
| Bai huong-dan-gui-hang-di-uc... | 1776 | 2460 | 1 | 1778 (2024-05-19, =) |
| Bai cach-chuyen-nha-duong-dai-o-ha-noi | 1755 | 2507 | 3 | 1987 (=); 1985 (2025-12-06 14:57, 2678) co them video Thaco dau bai; 1759 (2024-05-19, 2522) khac nho HTML |
| Trang home | 50 | 85817 | 1 | 1653 (2023-12-08, 86259) khac nhe |
| Trang gioi-thieu | 26 | 33408 | 45 | 2062 (=); ban 2061/2060/2056 dai 34902; tu 2024-05-19 den 2025-12-06 co nhieu moc 3866-33000 ky tu (ban som 3866/4597 la ban rut gon) |
| Trang services | 29 | 39607 | 1 | 1651 (2023-12-08, 39789) |
| Trang chuyen-hang-bac-nam | 1290 | 34399 | 14 | 2794 (**2026-11-03**, =) va 1996 (=); cac ban 2002/2001 (5698), 1995/1994/1842 (5974), 1841 (4675), 1840/1839/1837 (4854), 1836/1835 (3000), 1665 (2024-01-21, 3052) |
| Trang lien-he | 35 | 967 | 14 | 2025 (=, 967); ban 2022-2024 va cac ban 2024 dai 1179; ban cu 807 |
| Trang tracking | 1644 | 19 | 0 | khong co revision |

Luu y bat thuong: `chuyen-hang-bac-nam` co mot revision dated 2026-11-03 (hom nay) giong het noi dung hien tai - co the do nguoi dung/tien trinh vua luu; cu 'content' hien tai cua 5 trang con lai dang o ban 2025-12-06.

Revision khac dang ke da luu (ban loc: bo chu thich Gutenberg, thuoc tinh style/data, rut gon URL uploads):
- `backup/live/revisions/2012-2018.html` - rev 2018 cua bai Thaco; thuc chat la mot bai khac, "Bao hiem hang hoa" (day du, khoang 6 KB, anh bhhh.png, bhhh2.png). Noi dung nay khong con ton tai o ban hien tai - nen xem xet dung lam bai blog moi.
- `backup/live/revisions/1755-1985.html` - rev 1985 cua bai chuyen nha, co them shortcode video `Ban-giao-lo-10-xe-Thaco-Linker-Binh-Trieu.mp4`.
Khong luu rieng cac revision chi khac HTML (2014, 2013, 1759) vi van ban trung voi ban hien tai. Ban goc "raw" day du khong luu duoc qua kenh nay (gioi han do dai dau ra), nen file la ban da loc.

Noi dung HTML hien tai cua cac trang/bai da co o thu muc backup khac (theo nguoi gui); khong lap lai o day.

## 4. Branding va media
| Muc | Gia tri |
|---|---|
| Site title / tagline | PTDL / Vận Chuyển Bắc Nam |
| site_icon | media 1669: https://ptdl.com.vn/wp-content/uploads/2024/05/cropped-logo.jpg |
| site_logo (custom logo) | null (khong dat) |
| Transpi logo | trong |

Logo trong thu vien: 1668 `2024/05/logo.jpg`; 2043 `2025/12/logo.svg`; 2045 `2025/12/logo-1.svg`; 1643 `2023/12/Logo-1.svg`; 1669 `cropped-logo.jpg`.
Anh xe/Thaco: 1957 `2024/06/truck-all-lite-15-1.png`; 1819 `2024/05/Teal-And-White-Modern-Truck-Rental-Instagram-Post.png`; 2004 `2024/05/Ban-giao-lo-10-xe-Thaco-Linker-Binh-Trieu.mp4`.

Thu vien co 174 muc. **Alt text gan nhu khong co**: chi 2 anh co alt (1758, 1757, deu o bai chuyen nha) va 5 anh co caption (1758, 1757, 1712, 1710, 1709 - chan dung nhan vien/khach). Logo, anh xe, anh Thaco deu khong co alt/caption nen khong the bao cao 15 alt co y nghia; phai viet lai alt khi dung lai.

So sanh anh duoc noi dung trang tham chieu voi thu vien (so URL uploads trong noi dung):
| Trang | URL anh | Thieu trong thu vien |
|---|---|---|
| home | 30 | 4 |
| gioi-thieu | 20 | 0 |
| services | 14 | 2 |
| chuyen-hang-bac-nam | 6 | 2 |

Cac tep thieu: `2023/12/service-2.jpg`, `2023/12/service-3.jpg`, `2023/12/blog-1.jpg` (deu 404, khong khoi phuc duoc - la anh mau cua theme), `elementor/thumbs/Untitled-2-...jpg` va `Untitled-3-...jpg` (HTTP 200, la thumbnail do Elementor sinh, khong nam trong thu vien). Luu y: du lieu `_elementor_data` khong lo qua REST nen so sanh dua tren URL trong `content.raw`, khong phai meta Elementor.

## 5. Mau/template va menu
Template Elementor (admin edit.php, chi tieu de; REST khong lo ra, kich thuoc khong do duoc): "Ảnh xe", "Default Kit" (x2), "hme". Template Transpi (`transpi_template`): Header 1, Header 2, Header 3, Footer. Portfolio: rong.
Cac trang trong admin: About, Blog, Blog Grid, Elementor #17, Elementor #2416, Faq Page, Home, Home Three, Home Two, Liên hệ, My account, Project Masonry, Projects, Project Single, cung 6 trang khong tieu de.

Menu "Main Menu" (ID 31) - tieu de va URL:
| STT | Tieu de | URL | Cap |
|---|---|---|---|
| 1 | Trang chủ | / | goc |
| 2 | Giới thiệu | /gioi-thieu | goc |
| 3 | Dịch vụ | /services | goc |
| 4 | Chuyển hàng bắc nam | /services/chuyen-hang-bac-nam | con cua Dich vu |
| 5 | Chuyển hàng miền bắc | /services/chuyen-hang-bac-nam | con |
| 6 | Chuyển hàng miễn nam | /services/chuyen-hang-bac-nam/ | con |
| 7 | Chuyển hàng miền trung | /services/chuyen-hang-bac-nam/ | con |
| 8 | Tin tức | /blog | goc |
| 9 | Liên hệ | /lien-he | goc |

## Khong khoi phuc duoc
- Van ban hien thi cua front end (moi trang 500).
- Thong tin lien he/footer/copyright tu theme options (khong luu o do).
- Alt text anh quan trong (chua tung duoc nhap).
- 3 anh mau 2023/12 (service-2, service-3, blog-1).
