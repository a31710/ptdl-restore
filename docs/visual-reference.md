# Tham chieu giao dien trang chu cu ptdl.com.vn (WordPress + Elementor 3.21 + theme Transpi)

> Luu y quan trong ve nguon du lieu: KHONG co anh chup man hinh nao cua trang goc render dung. Cac file CSS/anh cua ptdl.com.vn khong duoc Wayback luu (tai CSS qua `cs_` deu tra 404), nen moi ban chup deu hien ra "tran" (Times New Roman, khong anh). Gia tri ben duoi duoc lay tu: (1) HTML + inline CSS cua ban chup luu tru, (2) CSS goc cua chinh theme Transpi lay tu trang demo cua nha cung cap `https://byteflows.net/wp/transpi/` (cung theme, cung class, cung footer template id 487), (3) phan ghi de ("Additional CSS") cua ptdl nam trong HTML. Muc nao la suy luan se duoc danh dau [suy luan].

## (a) Ban chup nao tot nhat

| Ban chup | Ket qua |
|---|---|
| 20250320022357 | HTML day du, CSS/anh khong tai duoc (khong style) |
| 20240517080816 | Noi dung SAI (tieu de "Bloggers Unite", site bi chiem ten mien) - bo qua |
| 20240718022006 | HTML day du, khong style; theme 6.6, Elementor 3.21.5 |
| 20240727143019 | HTML day du, khong style; theme 6.6.1 |
| 20250119172308 (redirect sang 20250122202711) | HTML day du, khong style; theme 6.7.1 |

Ban dung de lay cau truc/noi dung: **20250122202711** (ban 20250119172308 tu chuyen huong ve day; day la ban moi nhat, day du nhat: co 3 bai blog ngay 22/01/2025). Khong ban nao co "render dep". Do do phan visual la tai tao tu CSS theme + ghi de cua ptdl.

## (b) Design tokens

### Bien :root
| Bien | Gia tri |
|---|---|
| `--thm-primary` (ptdl) | `#5c8330` (xanh la; demo goc la `#FF131D` do) |
| `--wpcargo` | `#01ba7c` (plugin WPCargo, khong dung o trang chu) |
| `--thm-body-font` | `'DM Sans', sans-serif` |
| `--thm-heading-font` | `'Outfit', sans-serif` |
| `--e-global-*` | Khong xac dinh duoc (file post-7.css cua ptdl khong luu) |

### Mau
| Vai tro | Hex |
|---|---|
| Chu body | `#848484` |
| Tieu de / chu dam / navy | `#020E28` |
| Primary (xanh la) | `#5C8330` |
| Xanh duong nhan (nut gui, thanh truot, vien SVG shape, input form) | `#28A2F7` |
| Hover menu | `#1768B7` |
| Link menu (ghi de ptdl) | `#fff` |
| Nen the dich vu mac dinh (theme) | `#F5FAFF`; **ptdl ghi de: luon nen `var(--thm-primary)`, chu trang** |
| Nen bang gia | `#0B172F` |
| Nen form lien he | `#020E28`; o nhap `#434A5A` (ptdl: nen box `#5C8330`, input/select `#28A2F7`) |
| Footer nen / CTA | `#020407` / anh `cta-shape.png` |
| Chu footer | tieu de `#fff`, thuong `#B9B9B9`, vien tren bottom bar `#3E4045` |
| Vien nut CTA footer | `#3A4049` |
| Vien social/mui ten | `#CBC8C8`, `#D6D6D6`, `#D3D3D3` |

### Font (Google Fonts nap tu `fonts.googleapis.com`)
- `DM Sans` (100-1000, italic) + `Outfit` (200-900) - theme.
- Elementor kit nap them `Roboto`, `Roboto Slab`, `DM Sans`, ... (subset vietnamese) nhung chi la mac dinh kit.
- Icon: Font Awesome 5 Pro (`fa`, `far`, `fal`, `fas`, `fab` - file local cua theme `fontawesome.css`), `ti-search` (themify), eicons.

### Chu (computed theo CSS theme)
| Phan tu | font | size / line-height | weight | mau |
|---|---|---|---|---|
| body | DM Sans | 16px / 28px | 400 | #848484 |
| h1 | Outfit | 36px / 50px (<=992px: 30/42; <=430: 30/45) | 700 | #020E28 |
| h2 | Outfit | 30px / 38px (<=430: 26/35) | 700 | #020E28 |
| h3 | Outfit | 24px / 34px (768-991: 22/32) | 700 | #020E28 |
| h4 | Outfit | 18px / 26px | 700 (hero `.text h4` 400) | #020E28 |
| h5/h6 | Outfit | 15/24, 14/28 | 700 | #020E28 |
| a | ke thua mau, `display:inline-block`, transition 500ms | | | |
| `.transpi__heading-title` | Outfit | 55px / 70px (768-991: 40/50; <=767: 45/55; <=430: 35/45) | 600 | #020E28 |
| `.transpi__sub-heaind span` | DM Sans | 18px (<=430: 16/26) | 700, UPPERCASE | var(--thm-primary) |
| `.transpi__section-heading p` | | 20px / 35px | 400 | #848484 |
| `.rts_hero__title` (h1 hero) | Outfit | 60px / 70px (<=992: 50/60; <=430: 35/45) | 700 | #fff |
| `.content__hero span` ("PTDL Logistics") | | 20px / 20px | 600, UPPERCASE | #fff |
| Menu `.transpi_menu ul li a` | DM Sans | 16px (1024-1199: 15px) | 700, UPPERCASE, padding 15px 0 | #fff (ptdl), hover #1768B7 |
| Menu con `.sub-menu a` | | 16px / 37px | 500, UPPERCASE | #000, hover: padding-left 15px, underline, primary |
| Top bar `.header__top-info li` | | 16px | 700 (gio lam: 400, `strong` 700) | #020E28, icon primary |
| Counter `h1` / `h4` | Outfit | 50px/70px, 600 / 18px, 600 | | h1 #020E28, h4 **#fff** (ptdl) |
| List style-2 `li` | | 20px / 35px | 500 | #020E28 |
| Testimonial p / h4 | | 24px/37px 500 / 20px/30px 500 | | #020E28 (ptdl: #fff vi nen xanh) |
| Pricing h4 / h1 / li | Outfit/Outfit/DM Sans | 22px 600 / 40px 600 / 18px 400 | | primary / #fff / #fff |
| Project title h1 | | 30px/40px (<=1650px) | | #020E28 -> #fff khi active/hover |
| readmore | | 15px | 700 UPPERCASE | #020E28 (ptdl: #fff) |
| Blog `.cate__btn` | | 15px | 600 | primary (ptdl: #fff) |
| Footer tieu de cot | Outfit | 20px / 28px | 500 | #fff |
| Footer text | DM Sans | 16px / 28px (list 16/40) | 400 | #B9B9B9 |
| CTA footer h2 | Outfit | 40px (mobile 36px) | 500 | #fff; p 20px |
| CTA nut so dien thoai | Outfit | 30px | 500 | border 1px #3A4049, radius 10px, padding 15px 25px, nen trong suot, hover nen #fff chu #020E28 |

### Nut `.thm__btn`
`background: var(--thm-primary)`; chu `#fff`; `padding: 12px 20px`; `border-radius: 5px`; `font-weight: 700`; `transition: 500ms all ease`; hover: nen `#020E28`, chu `#fff`. (<=992px padding 10px 15px).
`.thm__btn-border`: nen trong suot, `border:1px solid #fff`, `padding:12px 25px`, hover vien `#020E28`. Trong bang gia: padding `10px 25px`, hover/`.active` nen primary. Nut form gui: `border:none; font-family:Outfit; weight 600; margin-top:10px`, ptdl nen `#28A2F7`, hover nen `#fff` chu `#020E28`.

### Bo cuc chung
- Container Bootstrap: max-width 1320px (core co quy tac 1450px o man rat rong). Elementor container 1320px.
- Cac the/hinh: radius 10px (service), 20px (pricing, form, testimonial item), 18px (khung slider testimonial), 30px (video), 15px (anh blog/projects), 5px (nut, input).
- Do bong: `0 0 50px 0 rgba(0,0,0,.05)` (sub-menu, blog), `.10` (testimonial wrapper, icon service hover).

## (c) Mo ta tung phan, theo thu tu trang

Widget Elementor dung (cho biet template): `transpi-header-temp`, `transpi-hero`, `transpi-heading`, `transpi-service-grid` (x5), `elementor-widget-button`, `transpi-video-popup`, `transpi-counter` (x4, style "two"), `shortcode` (Contact Form 7, class `style-two`), `transpi-list` (style-2), `transpi-testimonial-carousel-tw`, `transpi-pc-table` (x3, pricing), `transpi-projects-two`, `heading`, `transpi-btn`, `transpi-blog`, `transpi-brand`; footer (template 487): `transpi-heading`, `button`, `image`, `shortcode` (MC4WP), `heading`, `icon-list`, `text-editor` (iframe Facebook), `icon-list`.

### Desktop (1440px)

**0. Preloader** `#transpiPreloader`: lop phu nen trang fixed toan man hinh, logo giua (max 250px) cho den khi tai xong. Trang boc trong `#smooth-wrapper/#smooth-content` (GSAP ScrollSmoother).

**1. Header** (`transpi-header-temp`, `main-header main-header-one`, KHONG phai header-2 nen khong overlay tuyet doi):
- Top bar (`.header__top-wraper`, padding 8px 0, vien duoi 1px #D3D3D3, cao ~45px), container 1320, flex space-between:
  - Trai: icon phone (primary) + "0285 5555 565" (700, link), vach ngan doc 1px x 20px #848484, icon dong ho + "T2- CN: (**Tu 8:00 - 20:00**)".
  - Phai: link "Lien he" | "Dat lich Online" (text link 500, #020E28, ngan cach vach doc, hover primary - KHONG phai nut), roi 2 icon social tron 25x25 vien #CBC8C8 (facebook-f, youtube; hover nen primary/mau mang xa hoi).
- Main bar (`.header__top-main-wrap`, padding 20px 0): logo trai (png `2023/12/0db17170-...png`, ~165x50), giua menu ngang 5 muc: Trang chu, Gioi thieu, Dich vu (co dropdown), Tin tuc, Lien he - cach nhau 50px, chu in hoa 16px/700. Dropdown 220px, padding 25px, nen trang, bong nhe, mo bang `scaleY(0->1)` 0.4s tu tren xuong; 4 muc: Chuyen hang bac nam, Chuyen hang mien bac, Chuyen hang mien nam, Chuyen hang mien trung. Mui ten `\f105` xoay 90 do ben phai muc co con. Ben phai: nut tron tim kiem 50x50 nen #F3F3F3 (an <xl), nut `.thm__btn` "Hotline: 0285 5555 565" (hien >=md).
- Menu link ptdl ghi de mau TRANG, hover #1768B7 => thanh menu chac chan co nen mau toi/mau chu dao do Elementor dat tren section `df3f1c4` [suy luan: khong xac dinh duoc mau nen, kha nang xanh la #5C8330 hoac navy].
- Sticky: khong thay class sticky trong HTML [khong xac dinh duoc].
- Tim kiem: popup toan man hinh (`.search__popup`).

**2. Hero** (`section.elementor-element-764fa1e`, nen "classic" - anh/mau do Elementor, khong lay duoc). `.transpi__hero-area` position:relative; trong container, `col-lg-8 offset-lg-2`, `.content__hero text-center`, padding 280px 0:
- Dong nho "PTDL Logistics" (20px, 600, hoa, trang).
- H1 "Van tai Bac - Nam Uy tin chuyen nghiep" (60/70, 700, trang), co hieu ung SplitText `split-in-right`.
- Hang nut `.slider__btm-box` can giua, margin-top 50px: nut vien trang "Xem chi tiet dich vu" (margin-right 20px), kem khoi `.slider-phnoe` (icon phone + "Lien he" 18px/400 + so 24px/700 trang).
- Anh xe tai `truck-all-lite-15-1.png` o `.slider__img-txt` absolute `bottom:-270px; right:0` (mobile: -130px, max 600px; <=430: -50px), hieu ung `wow fadeInRight`. Hinh tran xuong section ke tiep.

**3. Dich vu cua chung toi** (`5204407`): heading can giua: sub-heading "DICH VU" (hoa, 18px/700, primary) hai ben co thanh ngang bo tron 50x5 + cham tron (SVG 59x5, rx 2.5; ptdl ghi de fill `#28A2F7`, gap 10px), tieu de h4 `.transpi__heading-title` "CUA CHUNG TOI" (55/70, 600). Duoi la luoi 3 cot (Elementor columns) the dich vu: "Van Tai Bac Nam", "Van Tai Lien Tinh", "Van Tai Noi Thanh Ha Noi". Dong 2 (`3f913b0`, 2 cot ben trong cot phai, cot trai trong): "Van Tai Noi Thanh TP.HCM", "Xe Tai 1T9 Den 15 Tan. Container" + nut Elementor "Chi tiet dich vu" (icon `fa-angle-double-right`) [bo cuc 2 dong 3+2 la suy luan tu cay DOM].
  - The `.transpi__service-grid`: padding 50px, padding-top 75px, radius 10px, giua, **nen primary xanh la #5C8330, chu trang** (ptdl ghi de), icon tron 100x100 nen trang nam cat vien tren (absolute top:0, translate -50%/-50%) chua SVG icon 39-45px to mau primary, bong `0 0 50px rgba(0,0,0,.10)`. Tieu de h2 (30/38, trang), doan mo ta, link "CHI TIET" (15px/700 hoa, trang, margin-top 20px; hover letter-spacing 1px). Xuat hien `wow fadeInUp`, transition 0.5s.

**4. Ve chung toi** (`a562439`, nen classic): heading "Gioi thieu" / h1 "Ve Chung Toi". Anh video `close-up-portrait-smiling-delivery-man-showing-ok-sign-scaled.jpg` cao 600px, object-fit cover, rộng 100%, radius 30px; nut play tron 100x100 nen primary, icon `fa-play` 20px trang, o giua, hieu ung song toa `playSlowAnimation2` (box-shadow 0 -> 30px, 1.8s lap vo han, mau song ban goc rgba(204,14,22,.6) do) mo lightbox YouTube `dVAvOFELmzU` (Magnific Popup). Duoi la hang 4 counter (`transpi__counter-item-two`, can giua): so odometer 50px/600 + nhan 18px/600 trang: "Chuyen hang", "Khach hang", "Doi tac", "Xe tai & container" (cuoi cung `no-border`). Giua cac counter co vach doc 1px x 80px #ADADAD (top 20px, right 0; an <=767px). HTML luu "00" -> dem len khi cuon toi (odometer). Gia tri dich khong luu duoc. Vi chu nhan trang, hang counter nam tren nen toi/mau [suy luan].

**5. Form + loi ich** (`4427044`, 2 cot): Trai: form CF7 `style-two` trong hop `.contact__form-submit` (width 583px, padding 70px 65px, radius 20px, nen #5C8330 tren trang chu, khong mask): nhan Outfit 20px/500 trang; select "Loai hinh van chuyen" (Duong bo/Hang khong/Duong bien), select "So Kg" (01/05/10/Tren 10 Tan), thanh truot "So KM" (jQuery UI slider `#slider-range` cao 5px, rong 320px, nen #434A5A, phan chay #28A2F7, tay nam tron 18px vien trang 2px), o "Ho va ten", "So dien thoai" (input nen #28A2F7, chu/placeholder trang, radius 5px, padding 12px 15px), nut "Gui yeu cau" xanh #28A2F7, dong ghi chu "Khi an nut Gui yeu cau, chung toi se lien he lai sau 5 phut..." (trang 700, `strong` mau #28A2F7). Phai: heading "Dich vu chuyen nghiep" / h4 "Hanh trinh Bac Nam, van chuyen an toan" va danh sach 6 gach dau (`transpi__list-item style-2`): moi dong co icon `\f058` (check-circle, primary) 20px/35px: "Voi hon 10 nam kinh nghiem", "Doi ngu nhan vien tre nang dong", "Doi ngu quan ly giau kinh nghiem", "Nhanh chong - an toan - tiet kiem", "Hop dong minh bach, trach nhiem", "Giao hang nhanh chong".

**6. Danh gia khach hang** (`e5643f2`): carousel Swiper doc (mui ten len/xuong). Khung `.thm-swiper__testimonial-two` nen trang, radius 18px, bong 0 0 50px rgba(0,0,0,.1). Moi slide `.testimonial__item-two` flex, radius 20px, **nen primary xanh, chu trang** (ptdl): anh trai 400px rong (cao 403px, cover) + noi dung padding 35px (phai 130px): doan trich 24/37 + ten 20px. 3 slide: H. Anh Nguyen, Dang Luong, Trinh Nguyen. Mui ten `.test-slider-arrow` 40x40 tron vien #D6D6D6, icon `fa-angle-up/down` 22px, xep doc o gia ben phai (right 50px, giua doc); hover nen primary. Chấm phan trang tron 12px (active 15px primary).

**7. Bang gia cuoc** (`2763a60`, nen classic): heading "Bang gia cuoc" / h1 "Van Chuyen". 3 cot the `.pricing__item`: nen #0B172F, radius 20px, padding 50px 35px, overflow hidden, hinh trang tri `shape-1.png` goc duoi trai: dau the (gach chan 1px rgba(255,255,255,.1)): ten (primary, 22px/600) + gia "Tu 12.000 / 16.000 / 16.000" (40px/600 trang); danh sach 6 xe (tai 5 ta, cat noc 2 tan, 1 tan, 1.4 tan, 5-7-10-15 tan, 4 chan 18 tan) co icon check `\f058` truoc moi dong (18px trang); nut vien trang giua "Lien he: 0285.5555.565" (hover nen primary). Ba cot: "Bac Nam", "Noi thanh HN", "Noi thanh HCM". The co `wow fadeInUp`.

**8. Nganh nghe kinh doanh** (`8f12117`): heading "Nganh nghe" / h1 "Kinh doanh". `transpi-projects-two`: 4 hang xep doc day 100% rong (`.project__item-box-inner`), moi hang flex space-between padding 40px: trai nhan vung (vien primary, 15px/600, padding 8px 20px, radius 5px) + tieu de h1 + doan mo ta (max 370px) + nut vuong 40x40 radius 5px vien navy co mui ten. Hang `active`/hover: hien anh nen (anh `transpo-4/5`, `transport-1/2` cao 236px, phu lop `#020E28` opacity .5, fade .5s), chu chuyen trang, nhan + nut chuyen nen primary. Mac dinh hang thu 2 active. 4 muc: "Giao Hang Chuyen Phat Nhanh", "Van Chuyen Hang Bang Xe Tai", "Van Chuyen Container", "Van chuyen Hang Sieu Truong Sieu Trong". Hang cach nhau bang duong vien [suy luan].

**9. Banner CTA** (`c1585d8`, nen classic + 1 lop `div` rong: overlay): `h2` "PTDL - LOGISTICS", `h2` "Van chuyen hang hoa Bac Nam "Nhanh Chong - An Toan - Tan Tam"", nut `.thm__btn` "Lien he" (`.btnalign`).

**10. Tin tuc moi nhat** (`59d7b39`, nen classic): heading "Cam nang van chuyen" / h4 "Tin tuc moi nhat". 3 cot (`col-xl-4 col-lg-6 col-md-6`) the blog: anh cao 300px (cover, radius 15px, mask `blog-mask.png` goc, zoom 1.1 khi hover 1s), nut tron trang 70x70 mui ten `fa-arrow-right` o goc duoi phai anh (hover nen primary), nhan the "Cam nang van chuyen" (vien 1px, 15px/600, radius 5px, padding 8px 13px), tieu de h3 (24/34), meta ngay `22/01/2025` + "0 Comments" co icon. Ptdl ghi de chu meta/nhan thanh **trang** => nen section toi. 3 bai: "Bao Hiem Hang Hoa La Gi? Tai Sao Doanh Nghiep Nen Mua?", "Cach chuyen nha duong dai o Ha Noi", "Huong dan gui hang di Uc tai Binh Duong an toan va nhanh chong".

**11. Doi tac** (`3603519`): carousel Swiper logo, anh toi da 100px, mac dinh `opacity .1`, slide active/hover `opacity 1` (0.5s). 6 logo: Pepsico, Shopee, J&T, GHTK, Trung Nguyen, Gamendes (jpg).

**12. Footer** (template 487, giong het demo):
- CTA (`619fdca`, nen gradient/anh `cta-shape.png` cover, padding 50px 0, container 1320): cot 70% trai h2 40px/500 trang "Ban dang tim kiem Dich vu van tai tot nhat?" + p 20px "Lien he voi chung toi de duoc tu van chi tiet."; cot 30% phai nut vien lon "0285.5555.565" (xem tren).
- Footer chinh (`158d170`, nen #020407, padding-top 100px): hang 1: logo (cot 30%) + o dang ky MC4WP (cot 70%); hang 2 (4 cot): thong tin cong ty ("C.TY TNHH GIAI PHAP VAN CHUYEN PTDL" Outfit 20/500 trang, mo ta, email `info@ptdl.com.vn`, dia chi "26 Duong Noi khu Hung Gia 1, Phuong Tan Phong, Quan 7, TP HCM", SDT) | "Dich vu" danh sach 5 link (Chuyen hang Bac - Nam / mien Bac / mien Nam / mien Trung / noi thanh HN - TP.HCM; 16px, line-height 40px, #B9B9B9, hover trang) | cot "Fanpage" iframe Facebook (`facebook.com/Ikay.vn`, 340x120) .
- Bottom bar (`f8eb3b2`): vien tren 1px #3E4045, padding 15px 0, trai "@2024. All Rights Reserved. ptdl.com.vn" (18px, #B9B9B9), phai icon-list (dang trong, hover #FF131D mac dinh theme).

### Mobile (375x812) - suy ra tu `responsive.css` va cay DOM
- Top bar xep 2 dong (`flex-wrap` <=768), chu 14px; <=430px khong con vach ngan va khong con khoang cach 15px.
- Main bar: logo (max 130px o <=430, 150px o <=992), menu ngang AN (`<1024px`); hien nut hamburger `.hamburger_menu` (`fa-bars` 25-30px, vien 1px #D9D9D9, padding 6-7px 10px, radius 5px, mau #020E28). Nut hotline an duoi md; nut tim kiem an.
- Bam hamburger: panel `.slide-bar` truot tu phai (rong 300px, nen trang, padding 60px 20px 25px, chuyen dong 600ms cubic-bezier(.785,.135,.15,.86)), nut dong vuong 40x40 nen primary o goc tren trai, logo + o tim kiem + menu doc (15px/600 hoa, gach chan rgba(0,0,0,.05)), muc "Dich vu" co mui chevron xoay, muc con thut 15px co cham tron dau dong.
- Hero: h1 35/45 (<=430) hay 50/60, padding 280px 0 van giu (khong co quy tac giam) [co the rat cao]; nut xep doc (`flex-wrap`), anh xe tai max 600px, bottom -50px (<=430).
- Service-grid: 1 cot xep doc. Heading 35/45.
- Counter: 2x2 hoac 1 cot, vach doc an.
- Testimonial: flex-wrap, anh tren (100% rong), noi dung duoi, mui ten an (hien lai <=430px).
- Pricing: 1 cot, padding 35px 0 (<=992).
- Projects: item flex-wrap, mo ta xuong duoi, vien doi sang gach chan.
- Blog: 1 cot, anh cao tu dong; meta xuong dong.
- Footer: padding-top 70px, cac cot 100% xep doc (50% o tablet 768-1024), CTA h2 36px, nut so dien thoai xuong duoi.

## (d) Hieu ung / animation
- Preloader trang toan man hinh.
- Cuon muot GSAP ScrollSmoother (`#smooth-wrapper`).
- Chu tieu de: SplitText (`split-in-right`, `split-in-rotate`) chay tung ky tu khi vao viewport.
- WOW.js + animate.css: `fadeInUp` (the dich vu, pricing, blog), `fadeInRight` (anh xe tai hero).
- Odometer: counter dem len tu 0.
- Nut play video: song toa vo han `playSlowAnimation2` (1.8s); Magnific Popup mo YouTube.
- Service grid: transition .5s (khi hover theme doi sang primary - ptdl da co san nen primary; icon trang doi shadow).
- Dropdown menu: scaleY 0.4s; link con hover thut vao 15px + gach chan.
- Nut: transition 500ms; hover nen #020E28; link "chi tiet" hover tang letter-spacing.
- Anh blog zoom 1.1 khi hover; mui ten tron doi nen primary.
- Projects: hang active hien anh nen fade .5s.
- Testimonial: Swiper doc, mui ten len/xuong; Doi tac: Swiper, logo mo -> ro; Tilt.js co nap (khong ro dung cho nao).
- Tim kiem: popup toan man hinh.

## (e) Khong xac dinh duoc
- Mau nen/anh nen/overlay cua tat ca section Elementor (hero, ve chung toi, counter, bang gia, nganh nghe, banner CTA, tin tuc, header main bar, gradient CTA footer `619fdca` chi biet la "gradient"): nam trong `post-603.css`, `post-7.css`, `post-636.css` cua ptdl, khong duoc luu tru. Chi biet loai nen qua `data-settings` (classic/gradient).
- Padding/margin cua tung section/cot Elementor trang chu, chieu cao hero that, ty le cot cua luoi dich vu.
- Cac bien `--e-global-*` va mau/typography mac dinh cua kit.
- Header co sticky hay khong; hinh anh logo thuc (anh khong tai duoc).
- Gia tri that cua counter (HTML luu "00").
- Do bo cuc chinh xac vi khong co anh chup that: nen kiem chung voi demo `https://byteflows.net/wp/transpi/` (cung theme, mau do) hoac dung anh mock.
- Phien ban theme cua ptdl (6.6 - 6.7.1) cu hon demo (7.1.4) nen vai gia tri nho co the lech.
