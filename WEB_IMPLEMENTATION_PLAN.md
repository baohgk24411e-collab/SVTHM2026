# KẾ HOẠCH TRIỂN KHAI VÀ THIẾT KẾ WEBSITE: DỰ ÁN "GIỮ MỘT NGHỀ – DỆT NÊN TƯƠNG LAI" (SVTHM 2026)

> **Khẩu hiệu cốt lõi:**  
> *"Không thay đổi cái gốc của nghề, thay đổi cách giá trị của nghề được nhìn thấy. Giữ một nghề không chỉ để giữ lại quá khứ, mà để dệt nên một tương lai có sinh kế và người tiếp nối."*  
> **Địa bàn nghiên cứu & thí điểm:** Xã Ia Mơ Nông, huyện Chư Păh, tỉnh Gia Lai (Cộng đồng dân tộc Jrai).

---

## I. TỔNG QUAN DỰ ÁN & BÀI TOÁN CHUYỂN ĐỔI (ADAPTATION)

### 1. Phân tích hiện trạng & Lý do nâng cấp
- **Web demo của Teammate (`det-nen-tuong-lai.vercel.app`):** Đã có khung ý tưởng về Ngân hàng số hoa văn, tuy nhiên giao diện còn đơn điệu, các section chưa có chiều sâu cảm xúc, hình ảnh và trải nghiệm tương tác chưa làm nổi bật được "tính mới" và sức sống văn hoá Tây Nguyên.
- **Source code đồ án cũ (`tuquygarden.vercel.app` / Repo ESG):** Có nền tảng kiến trúc rất tốt với cấu trúc HTML/CSS/JS module hóa, thanh navigation linh hoạt, hệ thống thẻ card sản phẩm chỉn chu, bộ lọc đa năng, trang giới thiệu đội ngũ sáng lập (Founder, CTO, CMO...) cực đẹp, và đặc biệt là hệ thống **Truy xuất nguồn gốc (Traceability Stepper)** rất thích hợp để chuyển thành quy trình dệt thủ công và tra cứu mã số định danh QR thổ cẩm.
- **Mục tiêu cuộc thi SVTHM 2026:** Giám khảo cuộc thi khởi nghiệp / NCKH sinh viên luôn đòi hỏi:
  1. *Tính mới & Sáng tạo:* Ứng dụng công nghệ số (Digital Cultural Heritage Bank + Dynamic QR Storytelling) để giải bài toán sinh kế làng nghề.
  2. *Mô hình kinh doanh khả thi:* "Bảo tồn – Kết nối – Thí điểm" (bán sản phẩm giá trị cao thông qua câu chuyện văn hoá và kết nối du lịch homestay Gia Lai).
  3. *Tác động xã hội (ESG / Social Impact):* Tạo việc làm cho phụ nữ Jrai, giữ chân người trẻ học nghề.

---

## II. HỆ THỐNG NHẬN DIỆN THẨM MỸ & BẢNG MÀU TÂY NGUYÊN (DESIGN SYSTEM)

Để mang trọn vẹn hơi thở đại ngàn Tây Nguyên nhưng vẫn giữ vẻ đẹp sang trọng, cao cấp (High-end Ethnic Contemporary), website sử dụng bảng màu lấy cảm hứng trực tiếp từ thổ cẩm Jrai và đất đỏ bazan:

### 1. Bảng màu chủ đạo (Color Palette)

| Tên màu | Mã HEX | Ý nghĩa biểu tượng trong văn hoá Jrai | Ứng dụng trên Website |
| :--- | :--- | :--- | :--- |
| **Đỏ Đất Bazan (Bazan Terracotta)** | `#9E2A2B` / `#8B2500` | Màu của đất mẹ Tây Nguyên, máu và ngọn lửa lễ hội Pơthi | Màu thương hiệu chính, nút CTA, điểm nhấn chính |
| **Đen Chàm Mun (Indigo Charcoal)** | `#191716` / `#1F1D1B` | Màu sợi nhuộm chàm tự nhiên, nền thổ cẩm truyền thống | Màu Header, Footer, Hero section nền tối huyền bí |
| **Vàng Nghệ Rừng (Forest Turmeric)** | `#D97706` / `#E5A93C` | Màu hoa dã quỳ Gia Lai, ánh bình minh trên nương rẫy | Viền nhấn, icon huy hiệu, rating, tag nổi bật |
| **Trắng Ngà Bông Thô (Raw Cotton Ivory)** | `#FBF9F5` / `#F3EFE6` | Màu sợi bông nguyên bản khi chưa qua nhuộm | Màu nền toàn trang (body background), nền card |
| **Nâu Vỏ Cây (Bark Earth)** | `#4A2E1B` | Màu nước luộc vỏ cây rừng dùng nhuộm sợi | Màu tiêu đề phụ, border nhẹ nhàng, text thứ cấp |
| **Xanh Rừng Khộp (Highland Moss)** | `#2D5A27` | Màu đại ngàn, rừng Chư Đang Ya, bảo tồn sinh thái | Huy hiệu sinh thái, tác động bền vững (Eco/Impact) |

### 2. Typographic Hierarchy (Kiểu chữ)
- **Font tiêu đề (Display & Heading):** `Lora` hoặc `Cinzel` / `Merriweather` (Google Fonts): Mang nét trang nghiêm, thanh lịch, gợi liên tưởng đến câu chuyện sử thi và hoa văn cổ truyền.
- **Font nội dung (Body text):** `Plus Jakarta Sans` hoặc `Inter`: Rõ nét, hiện đại, tối ưu khả năng đọc trên cả máy tính lẫn điện thoại.

---

## III. TỐI ƯU MENU HEADER & KIẾN TRÚC THÔNG TIN (INFORMATION ARCHITECTURE)

Menu Header sẽ được chốt tinh gọn, phân cấp rõ ràng 5 mục chiến lược:

```
[ LOGO & SLOGAN ] ────► [ 1. Trang Chủ ]
                         [ 2. Về Chúng Tôi ] (Đội ngũ, GVHD, Hành trình dự án)
                         [ 3. Sản Phẩm Dệt ] (Dòng sản phẩm cao cấp & thông tin độc bản)
                         [ 4. Ngân Hàng Hoa Văn ] (Kho di sản số - "Tính mới" SVTHM)
                         [ 5. Tra Cứu QR ] (Quét mác sản phẩm, minh bạch nguồn gốc)
                         [ Nút CTA: Tra Cứu Nhanh / Đặt Mua ]
```

### 1. Trang Chủ (`index.html`): "Điểm chạm đầu tiên chinh phục Giám khảo"
- **Top Bar:** Thông báo câu khẩu hiệu: *"DỰ ÁN SVTHM2026 — GIỮ MỘT NGHỀ, DỆT NÊN TƯƠNG LAI • LÀNG NGHỀ THỔ CẨM IA MƠ NÔNG, GIA LAI"*.
- **Hero Carousel / Hero Banner:**
  - Tiêu đề lớn: *“Giữ một nghề, dệt nên tương lai.”*
  - Đoạn phụ: *"Không thay đổi cái gốc của nghề, thay đổi cách giá trị của nghề được nhìn thấy. Từng đường chỉ dệt là một câu chuyện văn hoá, thời gian và sinh kế của đồng bào Jrai."*
  - 2 Nút hành động: `[Khám phá sản phẩm]` và `[Tra cứu mã QR thổ cẩm]`.
  - 4 Thống kê ấn tượng (Stats Bar):
    + `100%`: Sản phẩm có mã định danh QR cá nhân hóa.
    + `40+ Giờ`: Thời gian dệt thủ công trung bình cho mỗi tác phẩm.
    + `30+`: Nghệ nhân Jrai tại CLB Dệt Ia Mơ Nông tham gia dự án.
    + `30%`: Lợi nhuận trích trực tiếp vào quỹ duy trì lớp dạy dệt cho thế hệ trẻ.
- **Section 1: Vấn đề & Tính mới (Problem & Innovation):**
  - Đặt bài toán: *Vì sao thổ cẩm truyền thống đang dần mai một?* (Mất nhiều công sức nhưng bị ép giá, khó cạnh tranh với thổ cẩm dệt máy công nghiệp giá rẻ).
  - Lời giải đột phá: *Mô hình "Bảo tồn – Kết nối – Thí điểm"*. Không hạ giá để cạnh tranh giá rẻ, mà ứng dụng công nghệ để nâng tầm giá trị: minh bạch thời gian dệt, tôn vinh nghệ nhân và truyền tải chiều sâu văn hóa qua mã QR.
- **Section 2: Sản phẩm tiêu biểu:** Trưng bày 4 dòng sản phẩm chủ lực (Khăn choàng, Túi tote phong cách mới, Áo Gile thổ cẩm, Phụ kiện décor).
- **Section 3: Teaser "Ngân Hàng Số Hoa Văn":** Giới thiệu 3-4 hoa văn Jrai tiêu biểu (Hoa văn Bướm rừng, Hoa văn Chiêng cồng, Hoa văn Mắt rồng, Cây nêu) với hiệu ứng lật thẻ/hover tương tác xem ý nghĩa.
- **Section 4: Không gian trải nghiệm & Du lịch:** Kết nối thổ cẩm với các homestay, tour văn hóa tại Chư Păh - Gia Lai.

---

### 2. Trang Về Chúng Tôi (`about.html`): "Con người, Đội ngũ & Hành trình dệt"
Trang này được chuyển đổi trực tiếp từ `about.html` của Tứ Quý Garden với cấu trúc gồm 4 phần đặc sắc:

1. **Câu chuyện ra đời dự án:** Xuất phát từ chuyến đi điền dã thực tế tại xã Ia Mơ Nông, huyện Chư Păh, Gia Lai. Chuyển dịch từ câu hỏi *"Làm sao để giữ nghề?"* (vòng casting) sang *"Làm sao để nghề có thể sống được?"* (vòng đấu chính thức).
2. **Sứ mệnh & Tầm nhìn:**
   - *Sứ mệnh:* Nâng cao sinh kế bền vững cho phụ nữ Jrai thông qua chuyển đổi số di sản thổ cẩm và thương mại hóa có đạo đức.
   - *Tầm nhìn:* Trở thành hệ sinh thái số dẫn đầu về lưu trữ hoa văn bản địa và phân phối thổ cẩm thủ công nguyên bản tại Việt Nam.
3. **Quy trình 6 bước dệt truyền thống (The Weaving Journey Stepper):**  
   *(Adapt từ component `journey-stepper-section` của Tứ Quý Garden)*:
   - *Bước 1: Trồng bông & Thu hái (Cotton Harvesting)*
   - *Bước 2: Cán bông, kéo sợi & Cuộn con thoi (Spinning & Spooling)*
   - *Bước 3: Nhuộm màu tự nhiên từ lá chàm, vỏ cây rừng, củ nghệ (Natural Dyeing)*
   - *Bước 4: Mắc sợi lên khung cửi hông truyền thống (Loom Setting)*
   - *Bước 5: Dệt tạo hình hoa văn độc bản theo kỹ thuật đếm sợi Jrai (Hand Weaving)*
   - *Bước 6: Hoàn thiện sản phẩm & Đính tag định danh số QR (Digitization & Story Tagging)*
4. **Đội ngũ dự án (Team Members & Mentors):**  
   *(Kế thừa trọn vẹn phong cách `team-card`, `team-bg-shape`, `team-portrait-wrapper` cực kỳ hiện đại của Tứ Quý Garden)*:
   - Thầy/Cô Hướng dẫn khoa học (Giảng viên bảo trợ đề tài).
   - Trưởng dự án (Project Leader / CEO): Định hướng chiến lược & quan hệ cộng đồng.
   - Phụ trách Sản phẩm & Nghiên cứu Văn hoá (CPO / Culture Researcher): Làm việc trực tiếp với nghệ nhân, sưu tầm giải mã hoa văn.
   - Phụ trách Công nghệ & Web (CTO / Lead Developer): Xây dựng nền tảng web, ngân hàng hoa văn số & hệ thống QR code.
   - Phụ trách Tiếp thị & Kết nối Thị trường (CMO / Partnership): Kết nối homestay, quà tặng doanh nghiệp & truyền thông sinh kế.

---

### 3. Trang Sản Phẩm (`products.html`): "Định hình bán cái gì & Chi tiết sản phẩm"

#### A. Dự án nên bán sản phẩm gì cụ thể?
Không nên chỉ bán tấm vải thô khó ứng dụng, mà phân thành **3 nhóm sản phẩm có tính thương mại cao**:

| Nhóm sản phẩm | Tên sản phẩm mẫu | Giá trị sử dụng & Đối tượng khách hàng |
| :--- | :--- | :--- |
| **Dòng Ứng dụng Thời trang (Wearable Heritage)** | 1. Khăn choàng dạ Jrai phối thổ cẩm<br>2. Áo Gile / Áo khoác thổ cẩm Minimalist<br>3. Khăn Bandana / Khăn turban thổ cẩm | Khách du lịch cao cấp, giới trẻ yêu thời trang bền vững (Eco-fashion), người tham dự sự kiện văn hóa. |
| **Dòng Phụ kiện & Quà lưu niệm (Everyday Accents)** | 4. Túi Tote thổ cẩm phối vải Canvas mộc<br>5. Ví cầm tay & Túi đựng Passport/Thẻ<br>6. Dây đeo máy ảnh / Dây đeo thẻ thổ cẩm<br>7. Bookmark kẹp sách dệt tay | Khách du lịch, sinh viên, nhân viên văn phòng, làm quà tặng hội nghị, hội thảo du lịch. |
| **Dòng Không gian sống & Trải nghiệm (Living & DIY)** | 8. Khăn Runner trải bàn trà & homestay<br>9. Vỏ gối tựa sofa hoa văn Jrai<br>10. Bộ Kit tự dệt mini DIY tại nhà (Mini Handloom) | Các homestay/resort Tây Nguyên trang trí nội thất; phụ huynh và bạn trẻ thích trải nghiệm thủ công. |

#### B. Trong trang chi tiết mỗi sản phẩm cần có những thông tin gì?
Một sản phẩm thổ cẩm giá trị cao cần các thông tin khác biệt hoàn toàn với hàng dệt máy công nghiệp:
1. **Thông tin định danh độc bản (Product ID & Authenticity):** Mã sản phẩm duy nhất (VD: `JRAI-IMN-024`) tương ứng với mã QR in trên tem nhãn.
2. **Hồ sơ Nghệ nhân (Artisan Profile):** Ảnh nghệ nhân, tên (VD: *Nghệ nhân Rơ Chăm H’Mút - 52 tuổi, 38 năm cầm cửi*), làng dệt (Làng Kép, Ia Mơ Nông).
3. **Thời gian chế tác thủ công (Handmade Duration):** Đồng hồ hiển thị số giờ công dệt (VD: *38 giờ dệt liên tục trên khung cửi hông*).
4. **Ý nghĩa hoa văn tích hợp (Pattern Meaning):** Hoa văn chính trên sản phẩm là gì (kèm đường dẫn bấm sang xem chi tiết tại Ngân Hàng Hoa Văn).
5. **Chất liệu & Phương pháp nhuộm:** 100% sợi bông (Kơpăh), nhuộm thảo mộc tự nhiên từ rễ cây Knung (màu vàng), lá chàm (màu đen xanh), vỏ cây Klét (màu đỏ nâu), an toàn cho da và thân thiện môi trường.
6. **Chỉ số Tác động Xã hội (Social Impact Badge):** Công bố minh bạch: *65% giá bán chi trả trực tiếp cho nghệ nhân, 15% trích vào quỹ duy trì lớp dạy dệt cho thiếu nhi làng Kép*.
7. **Hướng dẫn giặt & bảo quản:** Hướng dẫn giặt tay với xà phòng dịu nhẹ, phơi trong bóng râm để giữ màu tự nhiên bền lâu.

---

### 4. Đề xuất vị trí cho "Ngân Hàng Văn Hóa" (`motifs.html` / `cultural-bank.html`)

> **Đánh giá chiến lược:**  
> "Ngân Hàng Văn Hóa" là **linh hồn và tính mới lớn nhất của dự án** trong cuộc thi SVTHM! Do đó, **tuyệt đối không được giấu nó vào trang con hay mục nhỏ**.

**Đề xuất vị trí tối ưu:**
1. **Trên Header Menu:** Đặt thành một tab độc lập ngang hàng với Sản phẩm: **"Ngân Hàng Hoa Văn"** (hoặc **"Kho Di Sản Số Jrai"**).
2. **Trải nghiệm trong trang Ngân hàng hoa văn:**
   - Bộ lọc phân loại hoa văn: *Theo chủ đề (Thiên nhiên & Động vật, Đời sống lao động, Tín ngưỡng & Lễ hội Pơthi)*; *Theo kỹ thuật dệt (Kỹ thuật cài sợi Kơnech, Kỹ thuật luồn chỉ kép)*.
   - Thẻ hoa văn (Motif Card): Hiển thị hình ảnh hoa văn sắc nét (Vector/Hi-res), Tên tiếng Jrai (VD: *Kơkơh, Asao, H’Ngô*), Tên tiếng Việt, Nghệ nhân bảo trợ thông tin, Triết lý nhân sinh đằng sau hoa văn.
   - Liên kết chéo (Cross-link): Bấm vào một hoa văn sẽ hiển thị ngay danh sách các sản phẩm đang ứng dụng hoa văn đó để người dùng có thể mua ngay!
3. **Tích hợp vào Trang Chi Tiết Sản Phẩm:** Ở phần mô tả sản phẩm, có một chiếc widget "Giải mã hoa văn trên tấm dệt này" dẫn trực tiếp về Ngân hàng hoa văn.

---

### 5. Trang Tra Cứu QR (`traceability.html`): "Adapt từ Tứ Quý Garden"

Kế thừa giao diện tra cứu cực kỳ chuyên nghiệp của Tứ Quý Garden, chuyển đổi bài toán từ nông sản sang thổ cẩm:

- **Giao diện quét / nhập mã:**
  - Ô quét camera QR Code trực tiếp trên điện thoại/máy tính.
  - Ô nhập mã số nhanh (VD: gõ thử `JRAI-001` hoặc `IMN-TOTE-04`).
  - Gợi ý sẵn các mã demo để giám khảo bấm thử ngay mà không cần quét camera.
- **Nội dung kết quả tra cứu hiển thị:**
  - *Thẻ định danh sản phẩm độc bản:* Ảnh sản phẩm thật chụp kèm số series.
  - *Người làm ra sản phẩm:* Chân dung nghệ nhân, tên tuổi, câu châm ngôn giữ nghề của cô.
  - *Bản đồ nguồn gốc địa phương:* Tọa độ định vị làng Kép, xã Ia Mơ Nông, huyện Chư Păh, tỉnh Gia Lai.
  - *Nhật ký tiến trình hoàn thiện:*
    + Ngày 01: Chuẩn bị sợi bông & nhuộm mẻ màu vỏ cây rừng.
    + Ngày 04: Mắc sợi lên khung cửi tại nhà rông làng Kép.
    + Ngày 07 - 12: Dệt 1.200 lượt thoi đưa theo hoa văn Rồng lửa / Cây nêu.
    + Ngày 14: May hoàn thiện mép tua rua thủ công và kiểm định chất lượng.
    + Ngày 15: Cấp mã định danh số QR và xuất xưởng đến tay khách hàng.
  - *Chứng nhận xác thực văn hoá:* Ký tên xác nhận của Câu lạc bộ dệt thổ cẩm xã Ia Mơ Nông.

---

## IV. CẤU TRÚC THƯ MỤC SOURCE CODE DỰ KIẾN (HTML/CSS/JS)

Dự án áp dụng mô hình web tĩnh thuần (Vanilla HTML/CSS/JS) như `tuquygarden`, tốc độ tải siêu tốc, không phụ thuộc backend cồng kềnh, dễ dàng deploy lên Vercel/GitHub Pages:

```
d:/SVTHM2026/
├── index.html              # Trang chủ: Giới thiệu đề tài, tính mới, hero, teaser
├── about.html              # Về chúng tôi: Đội ngũ, GVHD, Hành trình 6 bước dệt
├── products.html           # Danh mục sản phẩm & bộ lọc phân loại
├── product-detail.html     # Chi tiết sản phẩm: Mã độc bản, nghệ nhân, hoa văn
├── motifs.html             # Ngân hàng số hoa văn Jrai (Cultural Bank)
├── traceability.html       # Tra cứu nguồn gốc & quét mã QR định danh
├── styles/
│   ├── main.css            # Toàn bộ design system, biến màu Tây Nguyên, reset, layout
│   ├── components.css      # Thẻ sản phẩm, thẻ nghệ nhân, stepper, carousel, modal
│   └── responsive.css      # Tương thích mượt mà màn hình Mobile, Tablet, Desktop
├── js/
│   ├── main.js             # Menu mobile, search bar, language toggle (VI/EN)
│   ├── carousel.js         # Hero slider mượt mà tự động chuyển
│   ├── products-data.js    # Cơ sở dữ liệu JSON các sản phẩm dệt Jrai
│   ├── motifs-data.js      # Cơ sở dữ liệu JSON các hoa văn Jrai & chuyện kể
│   └── traceability.js     # Logic tra cứu mã QR, giải mã URL param (?code=...)
└── images/                 # Kho hình ảnh tư liệu chất lượng cao
    ├── logo/               # Logo nhận diện Dệt Nên Tương Lai
    ├── motifs/             # Hình ảnh chụp macro các mẫu hoa văn
    ├── products/           # Hình ảnh sản phẩm (Khăn, Túi, Gile, Ví...)
    ├── artisans/           # Chân dung nghệ nhân làng Kép - Ia Mơ Nông
    └── team/               # Ảnh chân dung thành viên nhóm & GVHD
```

---

## V. LỘ TRÌNH THỰC HIỆN CỤ THỂ (ACTION PLAN)

1. **Giai đoạn 1: Chuẩn hóa hệ thống dữ liệu (Data & Assets)**
   - Chuẩn bị file dữ liệu JSON cho 8-12 sản phẩm thổ cẩm tiêu biểu (khăn, túi xách, gile, bookmark...).
   - Chuẩn bị file dữ liệu JSON cho 6-8 mẫu hoa văn Jrai tiêu biểu (tên Jrai, ý nghĩa, ảnh minh họa).
   - Tối ưu hóa các hình ảnh tư liệu máy ảnh hiện có trong thư mục `images/` sang định dạng web nhẹ.

2. **Giai đoạn 2: Xây dựng Core Framework & Design System (`styles/main.css`)**
   - Định nghĩa biến CSS Tokens: Bảng màu Đỏ bazan - Đen chàm - Vàng nghệ rừng - Trắng ngà.
   - Thừa hưởng và nâng cấp các component từ Tứ Quý Garden: Header Sticky, Team Member Cards, Horizontal Stepper, QR Result Card.

3. **Giai đoạn 3: Hiện thực hóa các trang (Pages Implementation)**
   - Hoàn thiện `index.html`: Banner hero hoành tráng, giải thích bài toán SVTHM, tính mới mô hình "Bảo tồn - Kết nối - Thí điểm".
   - Hoàn thiện `about.html`: Section đội ngũ sinh viên & GVHD + Stepper Hành trình dệt 6 bước.
   - Hoàn thiện `products.html` & `product-detail.html`: Trưng bày sản phẩm kèm thông tin nghệ nhân, thời gian dệt, liên kết hoa văn.
   - Hoàn thiện `motifs.html`: Ngân hàng hoa văn tương tác, lọc theo chủ đề và ý nghĩa.
   - Hoàn thiện `traceability.html`: Quét QR hoặc tra cứu mã sản phẩm sinh ra trang câu chuyện minh bạch.

4. **Giai đoạn 4: Kiểm thử, hỗ trợ song ngữ VI/EN & Đưa lên Vercel**
   - Kiểm tra hiển thị responsive trên điện thoại (đặc biệt là trải nghiệm khi khách quét QR tại gian hàng triển lãm).
   - Triển khai hosting Vercel sẵn sàng thuyết trình trước Hội đồng Giám khảo SVTHM2026.
