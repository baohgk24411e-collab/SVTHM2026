# -*- coding: utf-8 -*-
"""
DỰ ÁN SVTHM 2026: DỆT NÊN TƯƠNG LAI
Script đồng bộ và chuyển đổi toàn bộ cơ sở dữ liệu từ 'database SVTHM 2026':
1. Copy ảnh sản phẩm vào images/products/ với tên chuẩn hóa
2. Tạo js/products-data.js (57 sản phẩm, giá chuẩn, ngày dệt chuẩn, nghệ nhân, hoa văn khớp)
3. Cập nhật js/artisans-data.js (9 nghệ nhân thực tế)
4. Cập nhật js/motifs-data.js (20+ hoa văn với ảnh thật từ database)
"""

import os
import sys
import shutil
import json
import random

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r'd:\SVTHM2026'
SRC_DB = os.path.join(ROOT_DIR, 'database SVTHM 2026')
DST_PRODUCTS_IMG = os.path.join(ROOT_DIR, 'images', 'products')
DST_MOTIFS_IMG = os.path.join(ROOT_DIR, 'images', 'motifs')
DST_ARTISANS_IMG = os.path.join(ROOT_DIR, 'images', 'artisans')

os.makedirs(DST_PRODUCTS_IMG, exist_ok=True)
os.makedirs(DST_MOTIFS_IMG, exist_ok=True)
os.makedirs(DST_ARTISANS_IMG, exist_ok=True)

# ==============================================================================
# 1. DANH SÁCH 9 NGHỆ NHÂN CHUẨN
# ==============================================================================
ARTISANS_DATA = [
    {
        "id": "artisan-001",
        "legacyId": "ARTISAN-01",
        "name": "Nghệ nhân Rơ châm Nghị",
        "age": 70,
        "experience": "30 năm tuổi nghề",
        "experienceYears": 30,
        "village": "Làng Kép, xã Ia Mơ Nông, huyện Chư Păh, Gia Lai",
        "avatar": "images/artisans/ro-cham-nghi.jpg",
        "specialtyVi": "Nghệ nhân Rơ châm Nghị với 30 năm tuổi nghề, là người truyền dạy kỹ thuật dệt cửi hông truyền thống, am hiểu sâu sắc về hoa văn cổ và nghệ thuật phối màu sợi dệt.",
        "specialtyEn": "Nghệ nhân Rơ châm Nghị with 30 years of backstrap loom mastery, preserving sacred ancient motifs and botanical color palettes.",
        "quoteVi": "“Mỗi sợi chỉ giăng trên khung dệt là nhịp đập của buôn làng, là lời ông bà gửi lại cho mai sau.”",
        "quoteEn": "“Every warp thread across the loom carries the sacred heartbeat of our ancestors.”",
        "bioVi": "Bà là hạt nhân gìn giữ nghề dệt của làng Kép, kiên trì truyền dạy từng nhịp luồn suốt cho thế hệ trẻ.",
        "bioEn": "Core keeper of traditional weaving in Lang Kep, patiently mentoring the young generation.",
        "productIds": [],
        "zaloPhone": "0383451929",
        "facebookPageId": "100090304682611"
    },
    {
        "id": "artisan-002",
        "legacyId": "ARTISAN-02",
        "name": "Nghệ nhân Rơ châm Krế",
        "age": 75,
        "experience": "35 năm tuổi nghề",
        "experienceYears": 35,
        "village": "Làng Phung, xã Ia Mơ Nông, huyện Chư Păh, Gia Lai",
        "avatar": "images/artisans/ro-cham-kre.png",
        "specialtyVi": "Nghệ nhân Rơ châm Krế có 35 năm gắn bó cùng quay sợi, bật bông và khung dệt mộc. Bà gìn giữ bí quyết nhuộm màu tự nhiên từ vỏ cây rừng và lá chàm.",
        "specialtyEn": "Master of natural dyeing from wild forest barks and Kopah raw cotton spinning.",
        "quoteVi": "“Cái màu của củ nâu, lá chàm tự nhiên nó bền như tình nghĩa con người Tây Nguyên.”",
        "quoteEn": "“Colors from the highland soil and forest barks endure forever, just like our spirit.”",
        "bioVi": "Gắn bó với nghề từ thuở thiếu thời, bà nổi tiếng với kỹ thuật bật bông tơi xốp và dệt túi tote, áo nam kỳ công.",
        "bioEn": "A lifetime artisan celebrated for spinning fluffy cotton and weaving master vests.",
        "productIds": [],
        "zaloPhone": "0383451929",
        "facebookPageId": "100090304682611"
    },
    {
        "id": "artisan-003",
        "legacyId": "ARTISAN-03",
        "name": "Nghệ nhân Rơ châm Nghel",
        "age": 76,
        "experience": "36 năm tuổi nghề",
        "experienceYears": 36,
        "village": "Làng Kép, xã Ia Mơ Nông, huyện Chư Păh, Gia Lai",
        "avatar": "images/artisans/ro-cham-nghel.jpg",
        "specialtyVi": "Nghệ nhân Rơ châm Nghel với 36 năm cống hiến cho di sản dệt thổ cẩm Jrai, chuyên nghiệp trong kỹ thuật tạo tác hoa văn nổi ba chiều và bảo tồn nghi lễ dệt buôn làng.",
        "specialtyEn": "Celebrated for 3D raised Kơnech patterns and ceremonial stilt weaving.",
        "quoteVi": "“Ngồi bên khung cửi thấy lòng thanh thản, từng đường kim mũi dệt đưa di sản đi muôn phương.”",
        "quoteEn": "“Beside the backstrap loom, our soul finds stillness and sends heritage to the world.”",
        "bioVi": "Nghệ nhân cao niên tâm huyết với từng chiếc khăn quàng cổ và trang phục dệt cho lễ hội mừng lúa mới.",
        "bioEn": "Senior artisan dedicated to ceremonial garments and intricate festival shawls.",
        "productIds": [],
        "zaloPhone": "0383451929",
        "facebookPageId": "100090304682611"
    },
    {
        "id": "artisan-004",
        "legacyId": "ARTISAN-04",
        "name": "Nghệ nhân H' Uyên Niê",
        "age": 60,
        "experience": "20 năm tuổi nghề",
        "experienceYears": 20,
        "village": "Xã Ia Mơ Nông, huyện Chư Păh, Gia Lai",
        "avatar": "images/artisans/h-uyen-nie.jpg",
        "specialtyVi": "Nghệ nhân H' Uyên Niê có 20 năm truyền nghề dệt, mang đến hơi thở ứng dụng hiện đại cho các sản phẩm túi, ví và khăn quàng thổ cẩm di sản.",
        "specialtyEn": "Bridging ancient matrilineal weaving with modern creative lifestyles.",
        "quoteVi": "“Đưa thổ cẩm vào đời sống hiện đại là cách tốt nhất để di sản sống mãi cùng buôn làng.”",
        "quoteEn": "“Blending heritage brocade into modern lifestyles keeps our craft alive forever.”",
        "bioVi": "Tiên phong trong việc thiết kế các mẫu khăn quàng và phụ kiện ứng dụng cho giới trẻ và khách du lịch.",
        "bioEn": "Pioneering modern application designs for domestic and international travelers.",
        "productIds": [],
        "zaloPhone": "0383451929",
        "facebookPageId": "100090304682611"
    },
    {
        "id": "artisan-005",
        "legacyId": "ARTISAN-05",
        "name": "Nghệ nhân Rơ Châm Mân",
        "age": 55,
        "experience": "16 năm tuổi nghề",
        "experienceYears": 16,
        "village": "Làng Kép, xã Ia Mơ Nông, huyện Chư Păh, Gia Lai",
        "avatar": "images/artisans/ro-cham-man.jpg",
        "specialtyVi": "Chuyên sâu vào các dòng phụ kiện mộc, tạp dề thủ công và túi xách bền bỉ phục vụ đời sống hằng ngày.",
        "specialtyEn": "Specializing in sturdy utility brocade accessories and durable artisanal aprons.",
        "quoteVi": "“Từng đường may, từng thớ vải đều phải bền chắc như đá núi Chư Păh.”",
        "quoteEn": "“Every stitch and weave must be as steadfast as the rock of Mount Chu Pah.”",
        "bioVi": "Thành viên nòng cốt của hợp tác xã, phụ trách kiểm soát chất lượng dệt cho các dòng tạp dề và túi đeo.",
        "bioEn": "Core cooperative member overseeing rigorous artisanal quality standards.",
        "productIds": [],
        "zaloPhone": "0383451929",
        "facebookPageId": "100090304682611"
    },
    {
        "id": "artisan-006",
        "legacyId": "ARTISAN-06",
        "name": "Nghệ nhân Rơ Châm Cơm",
        "age": 65,
        "experience": "32 năm tuổi nghề",
        "experienceYears": 32,
        "village": "Làng Phung, xã Ia Mơ Nông, huyện Chư Păh, Gia Lai",
        "avatar": "images/artisans/ro-cham-com.png",
        "specialtyVi": "Đôi bàn tay tài hoa trong việc dệt ví cầm tay, khâu quấn thổ cẩm quanh bầu nước truyền thống và dải viền trang trí.",
        "specialtyEn": "Master in fine clutch weaving, gourd bottle wrapping and delicate edge borders.",
        "quoteVi": "“Trái bầu khô quấn thổ cẩm là người bạn đồng hành của người Jrai lên rẫy bao đời nay.”",
        "quoteEn": "“The brocade-wrapped gourd has accompanied highland farmers for generations.”",
        "bioVi": "Nghệ nhân giữ hồn các vật dụng sinh hoạt truyền thống Jrai, nổi tiếng với kỹ năng phối màu mộc mạc và sắc sảo.",
        "bioEn": "Celebrated for traditional lifestyle artifacts and authentic native aesthetics.",
        "productIds": [],
        "zaloPhone": "0383451929",
        "facebookPageId": "100090304682611"
    },
    {
        "id": "artisan-007",
        "legacyId": "ARTISAN-07",
        "name": "Nghệ nhân Rơ Châm Mril",
        "age": 58,
        "experience": "25 năm tuổi nghề",
        "experienceYears": 25,
        "village": "Làng Kép, xã Ia Mơ Nông, huyện Chư Păh, Gia Lai",
        "avatar": "images/artisans/ro-cham-mril.png",
        "specialtyVi": "Bậc thầy về dệt váy thổ cẩm nữ nguyên khổ và trang phục lễ hội mẫu hệ Jrai.",
        "specialtyEn": "Master weaver of authentic women's ceremonial wrap skirts and festival attire.",
        "quoteVi": "“Tấm váy thổ cẩm đẹp là niềm kiêu hãnh của người phụ nữ Jrai trong ngày hội lớn.”",
        "quoteEn": "“A finely handwoven skirt is the eternal pride of every Jrai woman.”",
        "bioVi": "Tác giả của các bộ váy thổ cẩm độc bản tham gia triển lãm văn hóa các dân tộc Tây Nguyên.",
        "bioEn": "Creator of exclusive ceremonial wrap skirts displayed in national ethnic showcases.",
        "productIds": [],
        "zaloPhone": "0383451929",
        "facebookPageId": "100090304682611"
    },
    {
        "id": "artisan-008",
        "legacyId": "ARTISAN-08",
        "name": "Nghệ nhân Rơ Châm Phaih",
        "age": 68,
        "experience": "28 năm tuổi nghề",
        "experienceYears": 28,
        "village": "Làng Kép, xã Ia Mơ Nông, huyện Chư Păh, Gia Lai",
        "avatar": "images/artisans/artisan_ksor_hyim.jpg",
        "specialtyVi": "Kỹ thuật dệt khăn quàng dải hoa văn cây nêu đỏ thắm và dệt sợi bông thô tự nhiên.",
        "specialtyEn": "Specializing in crimson ceremonial pole patterns and raw Kopah warp threads.",
        "quoteVi": "“Sợi đỏ là lửa, sợi vàng là nắng, dệt thành tấm khăn mang hơi ấm đất mẹ.”",
        "quoteEn": "“Red thread is fire, gold is sunshine, woven into warmth from Mother Earth.”",
        "bioVi": "Gắn bó với nghề dệt từ khi còn con gái, chuyên tạo tác các mẫu khăn quàng khổ lớn mang tính tâm linh.",
        "bioEn": "Weaving since her youth, crafting spiritually resonant large-format shawls.",
        "productIds": [],
        "zaloPhone": "0383451929",
        "facebookPageId": "100090304682611"
    },
    {
        "id": "artisan-009",
        "legacyId": "ARTISAN-09",
        "name": "Nghệ nhân Rơ Châm Monh",
        "age": 62,
        "experience": "26 năm tuổi nghề",
        "experienceYears": 26,
        "village": "Làng Kép, xã Ia Mơ Nông, huyện Chư Păh, Gia Lai",
        "avatar": "images/artisans/artisan_ro_lan_hbik.jpg",
        "specialtyVi": "Chuyên gia dệt túi đeo chéo và khăn quàng phối dải hoa văn ghè cổ và con gà linh vật.",
        "specialtyEn": "Expert in crossbody shoulder bags and dawn rooster heritage shawls.",
        "quoteVi": "“Mỗi chiếc túi đeo vai là một người bạn đường vững chãi của người miền núi.”",
        "quoteEn": "“Each shoulder bag is a steadfast companion across mountain paths.”",
        "bioVi": "Tỉ mỉ trong từng đường luồn chỉ, các tác phẩm của bà luôn có độ bền vượt trội và họa tiết sắc cạnh.",
        "bioEn": "Renowned for tight warp tension and exceptionally crisp geometric pattern definition.",
        "productIds": [],
        "zaloPhone": "0383451929",
        "facebookPageId": "100090304682611"
    }
]

ARTISAN_NAME_TO_OBJ = {
    'Rơ Châm Nghị': ARTISANS_DATA[0],
    'Rơ châm Nghị': ARTISANS_DATA[0],
    'Rơ Châm Krế': ARTISANS_DATA[1],
    'Rơ châm Krế': ARTISANS_DATA[1],
    'Rơ Châm Nghel': ARTISANS_DATA[2],
    'Rơ châm Nghel': ARTISANS_DATA[2],
    'H Uyen Nie': ARTISANS_DATA[3],
    'H\' Uyên Niê': ARTISANS_DATA[3],
    'Rơ Châm Mân': ARTISANS_DATA[4],
    'Rơ châm Com': ARTISANS_DATA[5],
    'Rơ Châm Com': ARTISANS_DATA[5],
    'Rơ Châm Cơm': ARTISANS_DATA[5],
    'Rơ Châm Mril': ARTISANS_DATA[6],
    'Rơ Châm Phaih': ARTISANS_DATA[7],
    'Rơ Châm Monh': ARTISANS_DATA[8]
}

# ==============================================================================
# 2. DANH SÁCH 20 HOA VĂN CHUẨN
# ==============================================================================
MOTIFS_DATA = [
    {
        "id": "motif-jrai-001",
        "motif_code": "JRAI-001",
        "nameJrai": "Mơ-nơ̆ (Con Gà)",
        "nameVi": "Hoa Văn Con Gà (Mơ-nơ̆) — Khởi Đầu & Ánh Sáng",
        "nameEn": "Rooster Motif (Mơ-nơ̆) — Dawn & Life Energy",
        "theme": "nature",
        "themeNameVi": "Thiên nhiên & Muông thú",
        "technique": "Dệt cài sợi nổi Kơnech (Kỹ thuật đếm sợi cách điệu nổi 3D)",
        "philosophyVi": "Người Jrai quan niệm tiếng gà gáy sớm xua tan bóng tối và ma quỷ, đánh thức buôn làng đón ngày mới. Hình ảnh đôi gà song hành là ước vọng về sự ấm no, gia đình thuận hòa.",
        "meaningVi": "Biểu tượng của sự khởi đầu, ánh sáng và hy vọng. Tiếng gà gáy xua tan bóng tối, báo hiệu mùa màng tươi tốt và sinh khí dồi dào.",
        "meaningEn": "Symbol of dawn, celestial light, and fresh beginnings. The rooster's crow awakens the highlands, dispersing shadows and calling forth vitality.",
        "colors": ["Đỏ tươi", "Xanh lá", "Vàng nghệ", "Trắng ngà"],
        "artisanVerification": "Nghệ nhân Rơ châm Nghị (30 năm tuổi nghề)",
        "village": "Làng Kép, xã Ia Mơ Nông, huyện Chư Păh, Gia Lai",
        "appliedProducts": [],
        "image": "images/motifs/con-ga-jrai.png",
        "accentColor": "#9E2A2B"
    },
    {
        "id": "motif-jrai-002",
        "motif_code": "JRAI-002",
        "nameJrai": "Hình Thoi & Chữ X",
        "nameVi": "Hoa Văn Hình Học Cổ — Nảy Nở & Khát Vọng Tự Do",
        "nameEn": "Geometric Diamond & X Motif — Abundance & Freedom",
        "theme": "life",
        "themeNameVi": "Đời sống & Con người",
        "technique": "Dệt luồn chỉ kép ziczac đối xứng qua tâm",
        "philosophyVi": "Hình thoi nở hoa ở trung tâm tượng trưng cho hạt mầm, hoa rừng và sự sinh sôi nảy nở của mẫu hệ. Dải hình chữ X đan chéo cách điệu đôi cánh chim vươn cao giữa núi rừng đại ngàn Chư Păh.",
        "meaningVi": "Hình thoi nở hoa tượng trưng cho hạt giống và sự sinh sôi nảy nở, cầu mong mùa màng bội thu. Hình chữ X màu xanh cách điệu đôi cánh chim đang bay, thể hiện khát vọng tự do và sức sống mãnh liệt.",
        "meaningEn": "Blooming diamond symbolizes fertile seeds and prosperity. Crossing X-bands represent soaring bird wings and unbroken mountain spirit.",
        "colors": ["Xanh lá chàm", "Đỏ thẫm", "Vàng nghệ", "Trắng ngà"],
        "artisanVerification": "Nghệ nhân Rơ châm Krế (35 năm tuổi nghề)",
        "village": "Làng Phung, xã Ia Mơ Nông, Chư Păh, Gia Lai",
        "appliedProducts": [],
        "image": "images/motifs/hinh-hoc-co.png",
        "accentColor": "#D97706"
    },
    {
        "id": "motif-jrai-003",
        "motif_code": "JRAI-003",
        "nameJrai": "Hơma Bông Lúa",
        "nameVi": "Hoa Văn Cây Lúa — Tri Ân Thần Yang & Mùa Vàng",
        "nameEn": "Rice Stalk Motif — Yang Gratitude & Golden Harvest",
        "theme": "nature",
        "themeNameVi": "Thiên nhiên & Nông nghiệp",
        "technique": "Dệt vạch phân tầng ngang truyền thống",
        "philosophyVi": "Bông lúa trĩu hạt là nguồn sống thiêng liêng nuôi dưỡng người Jrai bao đời. Từng nhánh lúa vươn cao trong hoa văn là lòng biết ơn sâu sắc tới mẹ Lúa và thần Yang đã ban mưa thuận gió hòa.",
        "meaningVi": "Cầu mong no đủ, mùa màng bội thu. Thể hiện lòng biết ơn mẹ Lúa và thần linh nuôi dưỡng con người qua bao thế hệ. Bông lúa vươn cao biểu trưng cho sự kiên cường và phát triển dẻo dai.",
        "meaningEn": "Revering the divine Rice Mother and celestial deities. Cascading heavy grains symbolize abundant food stores and village peace.",
        "colors": ["Đỏ tươi", "Tím chàm", "Trắng ngà", "Xanh lá"],
        "artisanVerification": "Nghệ nhân Rơ châm Nghel (36 năm cống hiến)",
        "village": "Làng Kép, xã Ia Mơ Nông, Chư Păh, Gia Lai",
        "appliedProducts": [],
        "image": "images/motifs/cay-lua.png",
        "accentColor": "#2D5A27"
    },
    {
        "id": "motif-jrai-004",
        "motif_code": "JRAI-004",
        "nameJrai": "Hoa Mào Gà",
        "nameVi": "Hoa Văn Hoa Mào Gà — Che Chở & Bình An",
        "nameEn": "Cockscomb Flower Motif — Protection & Steadfast Love",
        "theme": "ritual",
        "themeNameVi": "Tín ngưỡng & Lễ hội",
        "technique": "Dệt đứng hai bông song hành trên nền chàm mun",
        "philosophyVi": "Sắc đỏ thắm của hoa mào gà đại diện cho niềm vui và sinh khí. Gắn liền với linh vật gà trống bảo vệ bình an cho buôn làng, hoa dệt đứng song hành còn là biểu tượng cho tình yêu thủy chung, son sắt.",
        "meaningVi": "Tượng trưng cho sự may mắn, rực rỡ và che chở bình an khỏi điều dữ. Hoa thường được dệt đứng thành đôi, biểu trưng cho tình yêu bền chặt, gia đình hạnh phúc.",
        "meaningEn": "Vibrant cockscomb crimson dispels ill fortune and preserves sacred peace. Paired vertical blooms represent faithful love and familial bonds.",
        "colors": ["Đỏ thắm", "Xanh ngọc", "Hồng nhạt", "Đen chì"],
        "artisanVerification": "Nghệ nhân H' Uyên Niê (20 năm truyền nghề)",
        "village": "Xã Ia Mơ Nông, Chư Păh, Gia Lai",
        "appliedProducts": [],
        "image": "images/motifs/hoa-mao-ga.png",
        "accentColor": "#A6341B"
    },
    {
        "id": "motif-jrai-005",
        "motif_code": "JRAI-005",
        "nameJrai": "Cây Nêu Yang",
        "nameVi": "Hoa Văn Cây Nêu Yang — Trục Vũ Trụ & Kết Nối Thần Linh",
        "nameEn": "Sacred Ceremonial Pole Motif — Cosmic Axis",
        "theme": "ritual",
        "themeNameVi": "Tín ngưỡng & Lễ hội",
        "technique": "Dệt nổi hình thoi chân nêu và tua rua rủ truyền thống",
        "philosophyVi": "Cây nêu dựng giữa sân nhà rông là trục vũ trụ kết nối con người với thần Yang. Các tua hoa văn rủ xuống mang lời nguyện cầu mưa thuận gió hòa, bảo bọc buôn làng khỏi mọi hiểm nguy.",
        "meaningVi": "Cầu nối tâm linh kết nối con người với trời đất trong lễ hội buôn làng, xua đuổi tà khí và bảo vệ sự bình an cho cộng đồng.",
        "meaningEn": "Sacred communal axis connecting earthly mortals to heavenly Yang deities. Woven tassels embody prayers for gentle rains and eternal communal harmony.",
        "colors": ["Đỏ cờ", "Xanh lá chàm", "Vàng tươi", "Trắng ngà"],
        "artisanVerification": "Nghệ nhân Rơ Châm Phaih (28 năm tuổi nghề)",
        "village": "Làng Kép, xã Ia Mơ Nông, Gia Lai",
        "appliedProducts": [],
        "image": "images/motifs/cay-neu-yang.jpg",
        "accentColor": "#8B2500"
    },
    {
        "id": "motif-jrai-006",
        "motif_code": "JRAI-006",
        "nameJrai": "Con Cá Suối",
        "nameVi": "Hoa Văn Con Cá Suối — Nguồn Sống & No Đủ",
        "nameEn": "Stream Fish Motif — Source of Life & Abundance",
        "theme": "nature",
        "themeNameVi": "Thiên nhiên & Muông thú",
        "technique": "Dệt vảy cá đan cài nhịp nhàng",
        "philosophyVi": "Con cá tung tăng dưới dòng suối Ia Mơ Nông là biểu tượng của nguồn nước mát lành và sự sinh sôi vô tận của đất mẹ Tây Nguyên.",
        "meaningVi": "Cầu chúc cho dòng suối buôn làng không bao giờ cạn, tôm cá đầy giỏ, cuộc sống ấm no và tươi vui quanh năm.",
        "meaningEn": "Symbols of pure cascading mountain streams, fertility, and continuous plenty.",
        "colors": ["Xanh suối", "Trắng bạc", "Đỏ thẫm"],
        "artisanVerification": "Nghệ nhân Rơ châm Krế (35 năm tuổi nghề)",
        "village": "Làng Phung, xã Ia Mơ Nông, Gia Lai",
        "appliedProducts": [],
        "image": "images/motifs/con-ca.png",
        "accentColor": "#0284C7"
    },
    {
        "id": "motif-jrai-007",
        "motif_code": "JRAI-007",
        "nameJrai": "Cây Tre & Lũy Tre",
        "nameVi": "Hoa Văn Cây Tre — Bền Bỉ & Che Chở Buôn Làng",
        "nameEn": "Sacred Bamboo Grove — Resilience & Village Shelter",
        "theme": "nature",
        "themeNameVi": "Thiên nhiên & Nông nghiệp",
        "technique": "Dệt sọc đứng phân tầng mô phỏng đốt tre",
        "philosophyVi": "Cây tre uốn mình theo bão giông nhưng không bao giờ gãy. Lũy tre quanh làng che chở ngôi nhà sàn và nếp dệt truyền đời của phụ nữ Jrai.",
        "meaningVi": "Tượng trưng cho sự kiên cường, dẻo dai trước mọi khó khăn thử thách của núi rừng đại ngàn.",
        "meaningEn": "Enduring highland resilience and communal protection against wild storms.",
        "colors": ["Xanh lục", "Vàng tre", "Đen chàm"],
        "artisanVerification": "Nghệ nhân Rơ châm Nghị (30 năm tuổi nghề)",
        "village": "Làng Kép, xã Ia Mơ Nông, Gia Lai",
        "appliedProducts": [],
        "image": "images/motifs/cay-tre.png",
        "accentColor": "#15803D"
    },
    {
        "id": "motif-jrai-008",
        "motif_code": "JRAI-008",
        "nameJrai": "Cây Cỏ Núi Rừng",
        "nameVi": "Hoa Văn Cây Cỏ Núi Rừng — Mầm Xanh Đại Ngàn",
        "nameEn": "Wild Forest Herbs Motif — Highland Vitality",
        "theme": "nature",
        "themeNameVi": "Thiên nhiên & Nông nghiệp",
        "technique": "Dệt mầm nhọn tỏa tia mềm mại",
        "philosophyVi": "Mầm cỏ sau cơn mưa đầu mùa phủ xanh đất đỏ bazan, mang đến nhựa sống và thảo mộc chữa lành cho dân làng.",
        "meaningVi": "Sinh lực tràn đầy, khả năng thích ứng linh hoạt và sự tái sinh mạnh mẽ của tự nhiên.",
        "meaningEn": "Verdant renewal and medicinal blessings of the wild highland flora.",
        "colors": ["Xanh non", "Vàng rơm", "Đỏ đất"],
        "artisanVerification": "Nghệ nhân Rơ Châm Mril (25 năm tuổi nghề)",
        "village": "Làng Kép, xã Ia Mơ Nông, Gia Lai",
        "appliedProducts": [],
        "image": "images/motifs/cay-co.png",
        "accentColor": "#16A34A"
    },
    {
        "id": "motif-jrai-009",
        "motif_code": "JRAI-009",
        "nameJrai": "Chậu Hoa",
        "nameVi": "Hoa Văn Chậu Hoa — Ươm Mầm Tình Yêu & Sự Sống",
        "nameEn": "Blooming Flower Pot Motif — Nurturing Love",
        "theme": "life",
        "themeNameVi": "Đời sống & Con người",
        "technique": "Dệt cánh hoa mở rộng trên giá đỡ đối xứng",
        "philosophyVi": "Bông hoa được vun trồng bên bậc cầu thang nhà sàn thể hiện tình yêu cái đẹp và sự chăm chút khéo léo của người phụ nữ mẫu hệ.",
        "meaningVi": "Ươm mầm hạnh phúc lứa đôi, gia đình sum vầy và không gian sống chan hòa yêu thương.",
        "meaningEn": "Cultivating domestic joy, floral elegance, and familial harmony.",
        "colors": ["Đỏ hoa", "Vàng nhụy", "Xanh đài"],
        "artisanVerification": "Nghệ nhân H' Uyên Niê (20 năm tuổi nghề)",
        "village": "Xã Ia Mơ Nông, huyện Chư Păh, Gia Lai",
        "appliedProducts": [],
        "image": "images/motifs/chau-hoa.png",
        "accentColor": "#E11D48"
    },
    {
        "id": "motif-jrai-010",
        "motif_code": "JRAI-010",
        "nameJrai": "Ghè Rượu Cần",
        "nameVi": "Hoa Văn Ghè Cổ — Lễ Hội & Tình Thân Buôn Làng",
        "nameEn": "Ceremonial Wine Jar Motif — Unity & Festivity",
        "theme": "ritual",
        "themeNameVi": "Tín ngưỡng & Lễ hội",
        "technique": "Dệt khối bầu ghè nổi với hoa văn quấn quanh cổ ghè",
        "philosophyVi": "Ghè rượu cần quý là báu vật truyền đời của gia đình mẫu hệ. Mỗi dịp lễ hội, cần rượu cắm chung là biểu tượng của sự sẻ chia, đoàn kết không rời.",
        "meaningVi": "Tình bạn bè buôn làng khăng khít, lòng hiếu khách và không khí lễ hội tưng bừng quanh bếp lửa.",
        "meaningEn": "Sacred communal gatherings, unconditional hospitality, and shared blessings.",
        "colors": ["Nâu gốm", "Đỏ rượu", "Vàng đồng"],
        "artisanVerification": "Nghệ nhân Rơ Châm Monh (26 năm tuổi nghề)",
        "village": "Làng Kép, xã Ia Mơ Nông, Gia Lai",
        "appliedProducts": [],
        "image": "images/motifs/ghe-co.png",
        "accentColor": "#B45309"
    },
    {
        "id": "motif-jrai-011",
        "motif_code": "JRAI-011",
        "nameJrai": "Giã Gạo",
        "nameVi": "Hoa Văn Giã Gạo Ban Mai — Bàn Tay Người Mẹ Jrai",
        "nameEn": "Mortar Rice Pounding Motif — Maternal Care",
        "theme": "life",
        "themeNameVi": "Đời sống & Con người",
        "technique": "Dệt nhịp chày đôi đối xứng nhịp nhàng",
        "philosophyVi": "Tiếng chày giã gạo rộn rã trong sương sớm là âm thanh bình yên của no ấm, gắn liền với hình bóng người mẹ cần mẫn nuôi nấng đàn con.",
        "meaningVi": "Tôn vinh đức tính siêng năng, sự chịu thương chịu khó và bàn tay ấm áp của người phụ nữ Tây Nguyên.",
        "meaningEn": "Celebrating maternal devotion, industrious morning labor, and domestic nourishment.",
        "colors": ["Đen chàm", "Đỏ gạch", "Trắng ngà"],
        "artisanVerification": "Nghệ nhân Rơ Châm Cơm (32 năm tuổi nghề)",
        "village": "Làng Phung, xã Ia Mơ Nông, Gia Lai",
        "appliedProducts": [],
        "image": "images/motifs/gia-gao.png",
        "accentColor": "#78350F"
    },
    {
        "id": "motif-jrai-012",
        "motif_code": "JRAI-012",
        "nameJrai": "Gánh Buôn",
        "nameVi": "Hoa Văn Gánh Buôn — Chăm Chỉ & Gắn Kết Sinh Kế",
        "nameEn": "Highland Carrier Basket Motif — Commerce & Livelihood",
        "theme": "life",
        "themeNameVi": "Đời sống & Con người",
        "technique": "Dệt gùi mang lưng và đòn gánh bước đi",
        "philosophyVi": "Chiếc gùi sau lưng đưa hạt lúa, bó rau qua dốc đèo, kết nối sản vật buôn làng với chợ phiên vùng xa.",
        "meaningVi": "Tinh thần tự lực, cần cù kiến tạo sinh kế và mang lại ấm no cho gia đình buôn làng.",
        "meaningEn": "Diligence, resilient footsteps, and building sustainable communal livelihoods.",
        "colors": ["Vàng đất", "Xanh rêu", "Nâu sẫm"],
        "artisanVerification": "Nghệ nhân Rơ Châm Monh (26 năm tuổi nghề)",
        "village": "Làng Kép, xã Ia Mơ Nông, Gia Lai",
        "appliedProducts": [],
        "image": "images/motifs/ganh-buon.png",
        "accentColor": "#D97706"
    },
    {
        "id": "motif-jrai-013",
        "motif_code": "JRAI-013",
        "nameJrai": "Dấu Xưa Di Sản",
        "nameVi": "Hoa Văn Dấu Xưa Di Sản — Ký Ức Cội Nguồn",
        "nameEn": "Ancient Heritage Mark Motif — Ancestral Memory",
        "theme": "ritual",
        "themeNameVi": "Tín ngưỡng & Lễ hội",
        "technique": "Dệt ký hiệu cổ truyền mẫu hệ",
        "philosophyVi": "Mỗi đường nét là mật mã văn hóa mà người bà, người mẹ truyền lại bên khung cửi hông từ ngàn đời.",
        "meaningVi": "Ghi nhớ công đức tổ tiên, bảo tồn gốc rễ bản sắc của người Jrai không bao giờ phai nhạt.",
        "meaningEn": "Ancestral remembrance and preserving the eternal identity of Jrai heritage.",
        "colors": ["Đỏ thẫm", "Vàng nghệ", "Đen mun"],
        "artisanVerification": "Nghệ nhân Rơ Châm Cơm (32 năm tuổi nghề)",
        "village": "Làng Phung, xã Ia Mơ Nông, Gia Lai",
        "appliedProducts": [],
        "image": "images/motifs/dau-xua.png",
        "accentColor": "#991B1B"
    },
    {
        "id": "motif-jrai-014",
        "motif_code": "JRAI-014",
        "nameJrai": "Sinh Hoạt Buôn Làng",
        "nameVi": "Hoa Văn Sinh Hoạt Buôn Làng — Nhịp Sống Dưới Mái Nhà Rông",
        "nameEn": "Communal Village Life Motif — Rhythm Under Nha Rong",
        "theme": "life",
        "themeNameVi": "Đời sống & Con người",
        "technique": "Dệt đại cảnh người múa xoang, đánh chiêng, dệt vải",
        "philosophyVi": "Bức tranh toàn cảnh về đời sống sinh hoạt giàu bản sắc, nơi con người sống hòa quyện cùng thiên nhiên và tiếng cồng chiêng vang vọng.",
        "meaningVi": "Tình đoàn kết cộng đồng, niềm tự hào về làng nghề truyền thống và niềm vui sum vầy.",
        "meaningEn": "Communal cohesion, Gong heritage pride, and harmonious village celebration.",
        "colors": ["Đỏ cờ", "Vàng nắng", "Xanh chàm", "Trắng"],
        "artisanVerification": "Nghệ nhân Rơ Châm Mân (16 năm tuổi nghề)",
        "village": "Làng Kép, xã Ia Mơ Nông, Gia Lai",
        "appliedProducts": [],
        "image": "images/motifs/sinh-hoat-buon-lang.jpg",
        "accentColor": "#C2410C"
    },
    {
        "id": "motif-jrai-015",
        "motif_code": "JRAI-015",
        "nameJrai": "Mẹ Và Chị",
        "nameVi": "Hoa Văn Mẹ Và Chị — Tình Thân Mẫu Hệ Truyền Thừa",
        "nameEn": "Mother & Sister Motif — Matrilineal Kinship",
        "theme": "life",
        "themeNameVi": "Đời sống & Con người",
        "technique": "Dệt hai thế hệ phụ nữ song hành nắm tay",
        "philosophyVi": "Chế độ mẫu hệ Jrai trao truyền ngọn lửa giữ nghề từ mẹ sang con gái, từ chị sang em bên bếp lửa nhà sàn.",
        "meaningVi": "Tình mẫu tử thiêng liêng, lòng hiếu thuận và sự tiếp nối bền bỉ của thế hệ trẻ hôm nay.",
        "meaningEn": "Unbreakable matrilineal bond, generational mentorship, and honoring womanhood.",
        "colors": ["Hồng đất", "Đỏ thẫm", "Vàng ngà"],
        "artisanVerification": "Nghệ nhân H' Uyên Niê (20 năm tuổi nghề)",
        "village": "Xã Ia Mơ Nông, huyện Chư Păh, Gia Lai",
        "appliedProducts": [],
        "image": "images/motifs/me-va-chi.png",
        "accentColor": "#BE185D"
    },
    {
        "id": "motif-jrai-016",
        "motif_code": "JRAI-016",
        "nameJrai": "Người Làm Rẫy",
        "nameVi": "Hoa Văn Người Làm Rẫy — Giọt Mồ Hôi Trên Đất Đỏ",
        "nameEn": "Highland Farmer Motif — Sweat on Bazan Soil",
        "theme": "life",
        "themeNameVi": "Đời sống & Con người",
        "technique": "Dệt dáng hình người cuốc đất, tra hạt giống",
        "philosophyVi": "Mỗi hạt thóc, bắp ngô thu hoạch là giọt mồ hôi của người nông dân kiên cường bám đất bám làng trên nương rẫy bazan màu mỡ.",
        "meaningVi": "Tôn vinh giá trị lao động chân chính và sự gắn bó bền chặt giữa con người với đất mẹ quê hương.",
        "meaningEn": "Revering honest labor and the spiritual bond between farmers and fertile bazan soil.",
        "colors": ["Nâu bazan", "Đỏ đất", "Xanh mầm"],
        "artisanVerification": "Nghệ nhân Rơ châm Nghị (30 năm tuổi nghề)",
        "village": "Làng Kép, xã Ia Mơ Nông, Gia Lai",
        "appliedProducts": [],
        "image": "images/motifs/nguoi-lam-ray.png",
        "accentColor": "#854D0E"
    },
    {
        "id": "motif-jrai-017",
        "motif_code": "JRAI-017",
        "nameJrai": "Đám Trẻ Thơ",
        "nameVi": "Hoa Văn Đám Trẻ Thơ — Hồn Nhiên Đại Ngàn",
        "nameEn": "Village Children Motif — Highland Innocence",
        "theme": "life",
        "themeNameVi": "Đời sống & Con người",
        "technique": "Dệt nhóm trẻ con vui đùa nhí nhảnh",
        "philosophyVi": "Nụ cười trong veo của trẻ thơ Jrai chạy nhảy dưới bóng cây Kơ-nia là niềm hy vọng về một tương lai tươi sáng của buôn làng.",
        "meaningVi": "Ước nguyện cho thế hệ con cháu khỏe mạnh, lớn khôn trong sự yêu thương và học hành thành đạt.",
        "meaningEn": "Pure joy of childhood, future hopes, and blessing the next generation.",
        "colors": ["Vàng tươi", "Đỏ cam", "Xanh da trời"],
        "artisanVerification": "Nghệ nhân Rơ Châm Cơm (32 năm tuổi nghề)",
        "village": "Làng Phung, xã Ia Mơ Nông, Gia Lai",
        "appliedProducts": [],
        "image": "images/motifs/dam-tre.png",
        "accentColor": "#EA580C"
    },
    {
        "id": "motif-jrai-018",
        "motif_code": "JRAI-018",
        "nameJrai": "Đôi Lứa",
        "nameVi": "Hoa Văn Đôi Lứa — Thủy Chung Son Sắt",
        "nameEn": "Devoted Couple Motif — Eternal Fidelity",
        "theme": "life",
        "themeNameVi": "Đời sống & Con người",
        "technique": "Dệt hai nhân vật nam nữ đối xứng qua nhành hoa",
        "philosophyVi": "Tình yêu mộc mạc mà son sắt của chàng trai cô gái Jrai được dệt vào tấm chăn, tấm váy cưới chúc phúc trăm năm hạnh phúc.",
        "meaningVi": "Tình duyên bền chặt, sự thấu hiểu và gắn bó trọn đời của vợ chồng bên mái nhà dài.",
        "meaningEn": "Faithful devotion, marital bliss, and enduring partnership.",
        "colors": ["Hồng đào", "Đỏ thắm", "Vàng mật"],
        "artisanVerification": "Nghệ nhân Rơ Châm Mril (25 năm tuổi nghề)",
        "village": "Làng Kép, xã Ia Mơ Nông, Gia Lai",
        "appliedProducts": [],
        "image": "images/motifs/doi-lua.png",
        "accentColor": "#E11D48"
    },
    {
        "id": "motif-jrai-019",
        "motif_code": "JRAI-019",
        "nameJrai": "Khát Vọng Vươn Xa",
        "nameVi": "Hoa Văn Khát Vọng Vươn Xa — Chắp Cánh Tương Lai",
        "nameEn": "Highland Aspirations Motif — Wings of the Future",
        "theme": "life",
        "themeNameVi": "Đời sống & Con người",
        "technique": "Dệt dải sao sáng và chim lượn vút lên trời cao",
        "philosophyVi": "Khát vọng số hóa và đưa thổ cẩm Jrai từ buôn làng Chư Păh bay xa ra toàn quốc và thế giới của nhóm sinh viên UEL và bà con Ia Mơ Nông.",
        "meaningVi": "Ý chí vươn lên, đổi mới sáng tạo trên nền tảng gìn giữ bản sắc văn hóa di sản.",
        "meaningEn": "Empowering youth, cultural innovation, and global outreach from native roots.",
        "colors": ["Vàng kim", "Đỏ bazan", "Trắng tinh khôi"],
        "artisanVerification": "Nghệ nhân Rơ châm Nghel (36 năm cống hiến)",
        "village": "Làng Kép, xã Ia Mơ Nông, Gia Lai",
        "appliedProducts": [],
        "image": "images/motifs/khat-vong-vuon-xa.jpg",
        "accentColor": "#F59E0B"
    },
    {
        "id": "motif-jrai-020",
        "motif_code": "JRAI-020",
        "nameJrai": "Máy Bay Hiện Đại",
        "nameVi": "Hoa Văn Máy Bay — Giao Thoa Đương Đại",
        "nameEn": "Contemporary Airplane Motif — Modern Skies",
        "theme": "life",
        "themeNameVi": "Đời sống & Con người",
        "technique": "Dệt cách điệu cánh máy bay bay qua ngọn núi",
        "philosophyVi": "Người nghệ nhân Jrai nhìn lên bầu trời ngắm những chuyến bay mang khách bốn phương về thăm Gia Lai, đưa hình ảnh đó vào nếp cửi truyền thống.",
        "meaningVi": "Sự giao thoa giữa truyền thống và hiện đại, mở rộng cánh cửa hội nhập văn hóa quốc tế.",
        "meaningEn": "Harmonious fusion of ancient handloom craft with modern aviation horizons.",
        "colors": ["Xanh da trời", "Bạc", "Đỏ cờ"],
        "artisanVerification": "Nghệ nhân H' Uyên Niê (20 năm tuổi nghề)",
        "village": "Xã Ia Mơ Nông, Chư Păh, Gia Lai",
        "appliedProducts": [],
        "image": "images/motifs/may-bay.png",
        "accentColor": "#0284C7"
    }
]

MOTIF_MAP_BY_ID = {m['id']: m for m in MOTIFS_DATA}

# ==============================================================================
# 3. DANH SÁCH 57 SẢN PHẨM KHỚP VỚI DATABASE
# ==============================================================================
# (src_folder, src_file, code, nameVi, nameEn, cat_key, cat_nameVi, cat_nameEn, price, min_days, max_days, artisan_key, motif_id, dims, mat_vi, mat_en)
RAW_ITEMS = [
    # 1. Bầu nước (1)
    ('Bầu nước', 'B001- Rơ châm Com -200k.jpg', 'B001', 'Bầu Nước Quấn Thổ Cẩm Jrai', 'Jrai Traditional Gourd Bottle', 'gourd', 'Bầu nước', 'Gourd Bottle', 200000, 3, 5, 'Rơ châm Com', 'motif-jrai-013', 'Cao 25cm, đường kính 14cm', 'Quả bầu khô tự nhiên quấn dải thổ cẩm dệt tay', 'Natural dried gourd wrapped with handwoven brocade band'),
    
    # 2. Váy nữ (2)
    ('Váy', 'V001- Rơ Châm Mril.jpg', 'V001', 'Váy Thổ Cẩm Jrai Nữ Lễ Hội Độc Bản', 'Jrai Ceremonial Handwoven Wrap Skirt', 'dress', 'Váy', 'Dress', 1200000, 10, 15, 'Rơ Châm Mril', 'motif-jrai-018', 'Dài 90cm, vạt quấn tự do theo eo', 'Vải thổ cẩm bông Kơpăh dệt tay nguyên khổ', 'Full-width handwoven Kopah cotton brocade'),
    ('Váy', 'V002- Rơ Châm Mril.jpg', 'V002', 'Váy Thổ Cẩm Jrai Dáng Suông Hiện Đại', 'Jrai Modern Elegant Brocade Skirt', 'dress', 'Váy', 'Dress', 1200000, 8, 12, 'Rơ Châm Mril', 'motif-jrai-002', 'Dài 85cm, cạp co giãn bản rộng', 'Sợi chàm và chỉ tơ màu thảo mộc tự nhiên', 'Indigo cotton and natural botanical dyed threads'),

    # 3. Áo nam (2)
    ('Áo nam', '839754368_1110303048130990_938685961892630333_n.jpg', 'A001', 'Áo Thổ Cẩm Nam Sát Nách Jrai', 'Jrai Men\'s Sleeveless Brocade Vest', 'shirt', 'Áo nam', 'Men\'s Shirt', 900000, 6, 8, 'Rơ Châm Krế', 'motif-jrai-002', 'Size L (Rộng ngực 54cm, Dài 68cm)', 'Thổ cẩm dệt cửi hông, nẹp viền chỉ đỏ', 'Backstrap woven brocade with crimson edge trims'),
    ('Áo nam', '840961868_1110302968130998_280107443586882987_n.jpg', 'A002', 'Áo Ghi-lê Nam Thổ Cẩm Hoa Văn Cổ', 'Jrai Traditional Brocade Vest', 'shirt', 'Áo nam', 'Men\'s Shirt', 900000, 7, 10, 'Rơ Châm Krế', 'motif-jrai-019', 'Size XL (Rộng ngực 57cm, Dài 70cm)', 'Sợi bông Kơpăh phối dải thổ cẩm nổi', 'Kopah cotton with raised 3D brocade bands'),

    # 4. Túi tone (3)
    ('Túi tone', 'TT001- Rơ Châm Krế.jpg', 'TT001', 'Túi Tote Thổ Cẩm Phối Dây Da', 'Jrai Brocade Canvas Tote Bag', 'tote', 'Túi tote', 'Tote Bag', 300000, 5, 7, 'Rơ Châm Krế', 'motif-jrai-015', '38cm x 34cm x 8cm', 'Vải thổ cẩm dệt tay phối quai đeo mộc chắc chắn', 'Handwoven brocade with durable cotton straps'),
    ('Túi tone', 'TT002- Rơ Châm Krế.jpg', 'TT002', 'Túi Tote Du Lịch Thổ Cẩm Ia Mơ Nông', 'Ia Mo Nong Eco Travel Tote Bag', 'tote', 'Túi tote', 'Tote Bag', 300000, 5, 6, 'Rơ Châm Krế', 'motif-jrai-014', '40cm x 36cm, có ngăn kéo phụ', 'Vải chàm đen dệt hoa văn sinh hoạt buôn làng', 'Indigo fabric with village life motifs'),
    ('Túi tone', 'TT003- Rơ Châm Krế.jpg', 'TT003', 'Túi Tote Thổ Cẩm Khát Vọng Tây Nguyên', 'Highland Spirit Brocade Tote Bag', 'tote', 'Túi tote', 'Tote Bag', 300000, 6, 7, 'Rơ Châm Krế', 'motif-jrai-019', '36cm x 32cm, đáy đứng 9cm', 'Vải thổ cẩm dệt tay phối hoa văn vươn xa', 'Handwoven brocade with aspiration motifs'),

    # 5. Tạp dề (5)
    ('tạp dề', '748585460_1039159768578652_527032013318354063_n.jpg', 'TD001', 'Tạp Dề Thổ Cẩm Bếp Lửa Jrai', 'Jrai Hearth Kitchen Brocade Apron', 'apron', 'Tạp dề', 'Apron', 900000, 7, 9, 'Rơ Châm Mân', 'motif-jrai-011', 'Dài 75cm, Rộng 60cm, dây buộc linh hoạt', 'Vải thổ cẩm chống sờn dệt tay truyền thống', 'Durable handwoven brocade cotton'),
    ('tạp dề', '748776945_1039159765245319_1761598040313156166_n.jpg', 'TD002', 'Tạp Dề Nghệ Nhân Dệt Ia Mơ Nông', 'Ia Mo Nong Master Artisan Apron', 'apron', 'Tạp dề', 'Apron', 900000, 8, 10, 'Rơ Châm Nghel', 'motif-jrai-003', 'Dài 78cm, Rộng 62cm, túi trước tiện lợi', 'Vải dệt nguyên khổ đính túi thổ cẩm hoa văn lúa', 'Full-width cotton with rice pattern front pocket'),
    ('tạp dề', '748970116_1039159705245325_5568564852977279034_n.jpg', 'TD003', 'Tạp Dề Thổ Cẩm Quán Cà Phê Barista', 'Highland Barista Artisan Apron', 'apron', 'Tạp dề', 'Apron', 900000, 7, 8, 'Rơ Châm Mân', 'motif-jrai-010', 'Dài 76cm, Rộng 60cm, quai chéo lưng', 'Thổ cẩm chàm phối da bò sáp tự nhiên', 'Indigo brocade with natural strap trims'),
    ('tạp dề', '749197566_1039159645245331_7491090206265339242_n.jpg', 'TD004', 'Tạp Dề Đồng Điệu Đại Ngàn', 'Highland Harmony Craft Apron', 'apron', 'Tạp dề', 'Apron', 900000, 8, 10, 'Rơ Châm Nghel', 'motif-jrai-007', 'Dài 75cm, Rộng 60cm', 'Vải bông thô dệt cửi hông nẹp viền chắc chắn', 'Backstrap woven raw cotton with sturdy borders'),
    ('tạp dề', '749269421_1039159698578659_1575232973601449748_n.jpg', 'TD005', 'Tạp Dề Thổ Cẩm Gốm & Thủ Công', 'Pottery & Craft Brocade Apron', 'apron', 'Tạp dề', 'Apron', 900000, 7, 9, 'Rơ Châm Mân', 'motif-jrai-002', 'Dài 77cm, Rộng 61cm', 'Vải thổ cẩm phối dải hoa văn chữ X đối xứng', 'Handwoven brocade with geometric X bands'),

    # 6. Ví cầm tay (7)
    ('Ví cầm tay', 'Vi001- Rơ Châm Com.jpg', 'VI001', 'Ví Cầm Tay Thổ Cẩm Jrai Tinh Xảo', 'Jrai Delicate Brocade Clutch Wallet', 'wallet', 'Ví cầm tay', 'Wallet', 150000, 3, 5, 'Rơ châm Com', 'motif-jrai-002', '21cm x 12cm, khóa kéo đồng mạ', 'Vải thổ cẩm chàm đen hoa văn nổi', 'Indigo handwoven brocade fabric with zipper'),
    ('Ví cầm tay', 'Vi002- Rơ Châm Com.jpg', 'VI002', 'Ví Cầm Tay Họa Tiết Đám Trẻ Jrai', 'Jrai Village Children Motif Wallet', 'wallet', 'Ví cầm tay', 'Wallet', 150000, 3, 4, 'Rơ châm Com', 'motif-jrai-017', '20cm x 11cm, 2 ngăn tiện lợi', 'Sợi bông Kơpăh nhuộm thảo mộc tự nhiên', 'Natural botanic dyed Kopah cotton threads'),
    ('Ví cầm tay', 'Vi003-Rơ Châm Com.jpg', 'VI003', 'Ví Cầm Tay Họa Tiết Chậu Hoa', 'Flower Pot Motif Handwoven Wallet', 'wallet', 'Ví cầm tay', 'Wallet', 150000, 4, 5, 'Rơ châm Com', 'motif-jrai-009', '22cm x 12cm, lót vải lụa bền', 'Vải dệt tay phối hoa văn chậu hoa may mắn', 'Handwoven fabric with blooming flower motif'),
    ('Ví cầm tay', 'Screenshot 2026-10-22 133309.png', 'VI004', 'Ví Thổ Cẩm Cầm Tay Sắc Màu', 'Vibrant Colored Jrai Mini Clutch', 'wallet', 'Ví cầm tay', 'Wallet', 150000, 3, 4, 'Rơ Châm Nghị', 'motif-jrai-004', '19cm x 11cm', 'Sợi dệt phối tua rua thổ cẩm truyền thống', 'Cotton weave with traditional tassel trims'),
    ('Ví cầm tay', 'Screenshot 2026-10-22 133331.png', 'VI005', 'Ví Đựng Điện Thoại Thổ Cẩm Đa Năng', 'Multi-Purpose Brocade Phone Pouch', 'wallet', 'Ví cầm tay', 'Wallet', 150000, 4, 5, 'H Uyen Nie', 'motif-jrai-001', '20cm x 12cm', 'Vải chàm đen phối dải hoa văn con gà', 'Indigo fabric with traditional rooster band'),
    ('Ví cầm tay', '782997782_1073744071786888_922878377793213224_n.jpg', 'VI006', 'Ví Cầm Tay Thổ Cẩm Làng Kép', 'Lang Kep Artisan Brocade Pouch', 'wallet', 'Ví cầm tay', 'Wallet', 150000, 3, 5, 'Rơ Châm Nghị', 'motif-jrai-003', '21cm x 11.5cm', 'Sợi bông tự nhiên phối hoa văn lúa thiêng', 'Natural cotton with sacred rice motifs'),
    ('Ví cầm tay', '788208712_1073744038453558_1179869312449097150_n.jpg', 'VI007', 'Ví Cầm Tay Dấu Xưa Di Sản', 'Heritage Memory Brocade Wallet', 'wallet', 'Ví cầm tay', 'Wallet', 150000, 3, 4, 'Rơ châm Com', 'motif-jrai-013', '20cm x 11cm', 'Vải thổ cẩm dệt thủ công sắc sảo', 'Meticulously crafted indigenous textile'),

    # 7. Túi đeo chéo (9)
    ('Túi đeo chéo', 'C001- Rơ Châm Monh.jpg', 'C001', 'Túi Đeo Chéo Thổ Cẩm Dáng Vuông', 'Jrai Square Crossbody Brocade Bag', 'crossbag', 'Túi đeo chéo', 'Crossbody Bag', 300000, 5, 7, 'Rơ Châm Monh', 'motif-jrai-002', '24cm x 22cm x 6cm', 'Vải thổ cẩm dệt tay phối dây đeo điều chỉnh', 'Handwoven brocade with adjustable strap'),
    ('Túi đeo chéo', 'C001-Rơ Châm Monh.jpg', 'C002', 'Túi Đeo Chéo Thổ Cẩm Ghè Rượu Cần', 'Wine Jar Motif Crossbody Bag', 'crossbag', 'Túi đeo chéo', 'Crossbody Bag', 300000, 5, 7, 'Rơ Châm Monh', 'motif-jrai-010', '25cm x 23cm x 6cm', 'Thổ cẩm dệt hoa văn lễ hội ghè cổ', 'Highland ceremonial wine jar motifs'),
    ('Túi đeo chéo', '855758751_1123225653505396_8276980259103175926_n.jpg', 'C003', 'Túi Đeo Chéo Thổ Cẩm Nắp Gập', 'Flap Cover Brocade Crossbody Bag', 'crossbag', 'Túi đeo chéo', 'Crossbody Bag', 300000, 6, 7, 'H Uyen Nie', 'motif-jrai-007', '23cm x 21cm x 5cm', 'Vải chàm dệt nẹp viền hoa văn lũy tre', 'Indigo cloth with bamboo grove motifs'),
    ('Túi đeo chéo', '856375653_1123225613505400_2245904726982099718_n.jpg', 'C004', 'Túi Đeo Chéo Thổ Cẩm Đôi Lứa', 'Eternal Couple Brocade Messenger', 'crossbag', 'Túi đeo chéo', 'Crossbody Bag', 300000, 5, 6, 'Rơ Châm Monh', 'motif-jrai-018', '24cm x 22cm x 6cm', 'Sợi dệt tự nhiên hoa văn tình duyên bền chặt', 'Natural threads with couple motifs'),
    ('Túi đeo chéo', '857436974_1123225543505407_409592141514598525_n.jpg', 'C005', 'Túi Đeo Chéo Thổ Cẩm Người Làm Rẫy', 'Highland Farmer Brocade Bag', 'crossbag', 'Túi đeo chéo', 'Crossbody Bag', 300000, 6, 7, 'Rơ Châm Nghị', 'motif-jrai-016', '23cm x 20cm x 5cm', 'Vải thổ cẩm bông Kơpăh mộc', 'Natural Kopah cotton textile'),
    ('Túi đeo chéo', '857580299_1123225606838734_4097083781573838190_n.jpg', 'C006', 'Túi Đeo Chéo Dệt Nổi Kơnech', '3D Raised Kơnech Weave Bag', 'crossbag', 'Túi đeo chéo', 'Crossbody Bag', 300000, 5, 7, 'Rơ Châm Krế', 'motif-jrai-002', '24cm x 22cm x 6cm', 'Kỹ thuật dệt đếm sợi Kơnech 3D', 'Authentic 3D raised backstrap technique'),
    ('Túi đeo chéo', '857977880_1123225713505390_1174421523959925915_n.jpg', 'C007', 'Túi Đeo Chéo Thổ Cẩm Máy Bay', 'Contemporary Airplane Brocade Bag', 'crossbag', 'Túi đeo chéo', 'Crossbody Bag', 300000, 5, 6, 'H Uyen Nie', 'motif-jrai-020', '23cm x 21cm x 5cm', 'Hoa văn máy bay giao thoa hiện đại', 'Contemporary aviation cross-stitch pattern'),
    ('Túi đeo chéo', '858009235_1123225546838740_5012590372733707790_n.jpg', 'C008', 'Túi Đeo Chéo Thổ Cẩm Gánh Buôn', 'Harvesting Journey Crossbody Bag', 'crossbag', 'Túi đeo chéo', 'Crossbody Bag', 300000, 6, 7, 'Rơ Châm Monh', 'motif-jrai-012', '24cm x 22cm x 6cm', 'Thổ cẩm dệt hoa văn gánh buôn chăm chỉ', 'Handwoven fabric with carrier basket pattern'),
    ('Túi đeo chéo', '858524430_1123225666838728_3484319975002289168_n.jpg', 'C009', 'Túi Đeo Chéo Thổ Cẩm Mẹ Và Chị', 'Mother & Sister Heritage Messenger', 'crossbag', 'Túi đeo chéo', 'Crossbody Bag', 300000, 5, 7, 'Rơ Châm Nghel', 'motif-jrai-015', '24cm x 22cm x 6cm', 'Vải chàm đen phối chỉ đỏ vàng ấm cúng', 'Warm red and gold patterns on dark indigo'),

    # 8. Khăn quàng cổ (28)
    ('Khăn quàng cổ', 'K001- H Uyen Nie.jpg', 'K001', 'Khăn Quàng Cổ Thổ Cẩm H\' Uyên Niê', 'H\' Uyen Nie Signature Brocade Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 5, 8, 'H Uyen Nie', 'motif-jrai-004', '180cm x 35cm, tua rua 8cm', 'Sợi chàm rừng dệt tay kết hợp tua rua', 'Natural indigo cotton with tassels'),
    ('Khăn quàng cổ', 'K002-Rơ Châm Nghị.jpg', 'K002', 'Khăn Quàng Cổ Thổ Cẩm Rơ Châm Nghị', 'Ro Cham Nghi Master Brocade Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 6, 8, 'Rơ Châm Nghị', 'motif-jrai-003', '185cm x 38cm, tua rua 10cm', 'Bông Kơpăh nguyên chất phối chỉ vàng nghệ', 'Pure Kopah cotton with golden turmeric threads'),
    ('Khăn quàng cổ', 'K003- Rơ Châm Nghị.jpg', 'K003', 'Khăn Quàng Thổ Cẩm Con Gà Mơ-Nơ̆', 'Rooster Dawn Brocade Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 7, 8, 'Rơ Châm Nghị', 'motif-jrai-001', '190cm x 36cm, tua rua 9cm', 'Dệt hoa văn con gà trống ban mai trừ tà', 'Featuring sacred dawn rooster patterns'),
    ('Khăn quàng cổ', 'K004- Rơ Châm Nghị.jpg', 'K004', 'Khăn Quàng Thổ Cẩm Dải Hình Học Đỏ', 'Crimson Geometric Brocade Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 6, 7, 'Rơ Châm Nghị', 'motif-jrai-002', '180cm x 35cm', 'Sợi nhuộm củ nâu và rễ cây rừng Chư Păh', 'Botanical dyed with native forest roots'),
    ('Khăn quàng cổ', 'K005- Rơ Châm Nghị .png', 'K005', 'Khăn Quàng Cổ Hoa Văn Nổi Kơnech', 'Raised 3D Kơnech Brocade Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 5, 7, 'Rơ Châm Nghị', 'motif-jrai-002', '185cm x 36cm', 'Đếm sợi dệt nổi hoa văn hình thoi đối xứng', 'Counted warp threads with diamond symmetry'),
    ('Khăn quàng cổ', 'K006- Rơ Châm Nghị .png', 'K006', 'Khăn Quàng Thổ Cẩm Cây Tre Đại Ngàn', 'Highland Bamboo Loom Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 6, 8, 'Rơ Châm Nghị', 'motif-jrai-007', '180cm x 34cm', 'Sợi tơ bông mềm mại, giữ ấm tuyệt hảo', 'Soft natural cotton, excellent thermal warmth'),
    ('Khăn quàng cổ', 'K007- Rơ Châm Nghị .png', 'K007', 'Khăn Quàng Cổ Sắc Thu Chư Păh', 'Chu Pah Autumn Brocade Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 5, 7, 'Rơ Châm Nghị', 'motif-jrai-008', '175cm x 35cm', 'Phối màu vàng nghệ, cam đất và chàm sâu', 'Turmeric gold, terracotta and deep indigo'),
    ('Khăn quàng cổ', 'K008- Rơ Châm Nghị .png', 'K008', 'Khăn Quàng Thổ Cẩm Hoa Mào Gà Son', 'Crimson Cockscomb Sacred Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 6, 8, 'Rơ Châm Nghị', 'motif-jrai-004', '185cm x 36cm', 'Hoa văn hoa mào gà bảo hộ gia đình', 'Sacred cockscomb flower protective motif'),
    ('Khăn quàng cổ', 'K009- Rơ Châm Phaih.jpg', 'K009', 'Khăn Quàng Cổ Nghệ Nhân Rơ Châm Phaih', 'Ro Cham Phaih Handwoven Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 7, 8, 'Rơ Châm Phaih', 'motif-jrai-005', '190cm x 38cm', 'Hoa văn cây nêu nối dài mang phước lành', 'Extended ceremonial pole blessing pattern'),
    ('Khăn quàng cổ', 'K010.png', 'K010', 'Khăn Quàng Thổ Cẩm Con Cá Suối', 'Stream Fish Heritage Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 5, 7, 'Rơ Châm Krế', 'motif-jrai-006', '180cm x 35cm', 'Hoa văn con cá suối cầu mong no đủ', 'Fish symbol of abundant forest streams'),
    ('Khăn quàng cổ', 'K011.png', 'K011', 'Khăn Quàng Thổ Cẩm Mẹ Và Chị Jrai', 'Matrilineal Love Brocade Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 6, 8, 'H Uyen Nie', 'motif-jrai-015', '185cm x 36cm', 'Biểu tượng gắn kết ruột thịt mẫu hệ', 'Honoring matrilineal familial bonds'),
    ('Khăn quàng cổ', 'K012 - Rơ Châm Nghị.jpg', 'K012', 'Khăn Quàng Dệt Tay Cây Cỏ Rừng', 'Forest Flora Handcrafted Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 5, 8, 'Rơ Châm Nghị', 'motif-jrai-008', '180cm x 35cm', 'Sợi tự nhiên dệt hoa văn thảo mộc', 'Natural fiber with forest botanic motifs'),
    ('Khăn quàng cổ', 'K12- Rơ Châm Nghị.jpg', 'K013', 'Khăn Quàng Cổ Di Sản Làng Kép', 'Lang Kep Classic Brocade Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 6, 7, 'Rơ Châm Nghị', 'motif-jrai-002', '182cm x 35cm', 'Vải chàm đen dệt nổi chỉ đỏ cổ điển', 'Indigo base with classic red geometric rows'),
    ('Khăn quàng cổ', 'K14- Rơ Châm Phaih.jpg', 'K014', 'Khăn Quàng Cây Nêu Yang Linh Thiêng', 'Yang Ceremonial Pole Sacred Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 7, 8, 'Rơ Châm Phaih', 'motif-jrai-005', '190cm x 37cm', 'Dệt sợi bông thủ công hoa văn cây nêu', 'Sacred cosmic pole motif weave'),
    ('Khăn quàng cổ', 'K15- Rơ Châm Monh.jpg', 'K015', 'Khăn Quàng Cổ Nghệ Nhân Rơ Châm Monh', 'Ro Cham Monh Exclusive Brocade Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 5, 8, 'Rơ Châm Monh', 'motif-jrai-001', '185cm x 36cm', 'Hoa văn gà trống và hạt cườm may mắn', 'Dawn rooster and lucky beads combination'),
    ('Khăn quàng cổ', 'Khăn xanh đậm - Rơ Châm Nghị.jpg', 'K016', 'Khăn Quàng Thổ Cẩm Xanh Rừng Sâu', 'Deep Forest Emerald Brocade Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 6, 8, 'Rơ Châm Nghị', 'motif-jrai-007', '180cm x 35cm', 'Nhuộm vỏ cây tạo sắc xanh rừng thẫm', 'Forest bark dyed deep green tone'),
    ('Khăn quàng cổ', 'Khăn đỏ - Rơ Châm Phaih.jpg', 'K017', 'Khăn Quàng Thổ Cẩm Đỏ Lửa Đất Bazan', 'Bazan Fire Crimson Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 7, 8, 'Rơ Châm Phaih', 'motif-jrai-004', '185cm x 36cm', 'Sắc đỏ bazan tượng trưng cho sức sống mãnh liệt', 'Vibrant bazan crimson vitality symbol'),
    ('Khăn quàng cổ', '597861922_866454419182522_7266380289983260027_n.jpg', 'K018', 'Khăn Quàng Cổ Thổ Cẩm Cánh Chim Trời', 'Soaring Bird Brocade Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 5, 7, 'H Uyen Nie', 'motif-jrai-002', '180cm x 34cm', 'Chữ X cách điệu đôi cánh chim vươn cao', 'Stylized bird wing X-band geometric motifs'),
    ('Khăn quàng cổ', '746528283_1037366938757935_6058564300746321306_n.jpg', 'K019', 'Khăn Quàng Dệt Mùa Lúa Chín', 'Golden Harvest Festival Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 6, 8, 'Rơ Châm Nghel', 'motif-jrai-003', '185cm x 36cm', 'Họa tiết bông lúa trĩu hạt no đủ', 'Heavy golden rice stalk motifs'),
    ('Khăn quàng cổ', '764777653_1057138016780827_1591537068917796002_n.jpg', 'K020', 'Khăn Quàng Thổ Cẩm Dưới Mái Nhà Rông', 'Communal Stilt House Brocade Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 5, 8, 'Rơ Châm Mân', 'motif-jrai-014', '180cm x 35cm', 'Hoa văn sinh hoạt buôn làng cộng đồng', 'Communal village life patterns'),
    ('Khăn quàng cổ', '765941641_1055284940299468_6490995078791230148_n.jpg', 'K021', 'Khăn Quàng Thổ Cẩm Ghè Cổ Rượu Cần', 'Ancient Wine Jar Brocade Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 6, 8, 'Rơ Châm Monh', 'motif-jrai-010', '185cm x 36cm', 'Hình tượng ghè rượu cần trong ngày hội', 'Festive ceremonial jar patterns'),
    ('Khăn quàng cổ', '835873811_1109306708230624_1838852381446170859_n.jpg', 'K022', 'Khăn Quàng Thổ Cẩm Giã Gạo Ban Mai', 'Morning Rice Pounding Brocade Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 5, 7, 'Rơ Châm Krế', 'motif-jrai-011', '180cm x 35cm', 'Hoa văn giã gạo nhịp nhàng ban sớm', 'Morning mortar pounding motifs'),
    ('Khăn quàng cổ', '837569078_1109306958230599_2880854966993627543_n.jpg', 'K023', 'Khăn Quàng Thổ Cẩm Gánh Buôn Nương', 'Highland Carrier Basket Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 6, 8, 'Rơ châm Com', 'motif-jrai-012', '182cm x 35cm', 'Biểu trưng cho đức tính cần mẫn của phụ nữ', 'Honoring diligent upland women'),
    ('Khăn quàng cổ', '838363447_1109306871563941_9181770680404639372_n.jpg', 'K024', 'Khăn Quàng Thổ Cẩm Mầm Xanh Đại Ngàn', 'Highland Sprout Brocade Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 5, 7, 'Rơ Châm Mril', 'motif-jrai-008', '180cm x 34cm', 'Hoa văn cây cỏ mùa xuân Ia Mơ Nông', 'Spring botanic emergence patterns'),
    ('Khăn quàng cổ', '839096310_1109306678230627_7263728456432356535_n.jpg', 'K025', 'Khăn Quàng Cổ Chậu Hoa May Mắn', 'Lucky Bloom Pot Brocade Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 7, 8, 'H Uyen Nie', 'motif-jrai-009', '185cm x 36cm', 'Chậu hoa đâm chồi mang may mắn bình an', 'Auspicious flower pot motifs'),
    ('Khăn quàng cổ', '839618033_1109306578230637_6193505491768580444_n.jpg', 'K026', 'Khăn Quàng Thổ Cẩm Tiếng Gà Gáy Sớm', 'First Dawn Rooster Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 5, 8, 'Rơ Châm Nghị', 'motif-jrai-001', '180cm x 35cm', 'Sợi chỉ chàm đen viền gà trống vàng nghệ', 'Indigo with turmeric yellow rooster motifs'),
    ('Khăn quàng cổ', '840206481_1109306978230597_4548294005441517002_n.jpg', 'K027', 'Khăn Quàng Cổ Khát Vọng Tương Lai', 'Future Horizons Brocade Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 6, 8, 'Rơ Châm Nghel', 'motif-jrai-019', '185cm x 36cm', 'Hoa văn khát vọng vươn xa của thế hệ trẻ', 'Youthful highland aspirations motif'),
    ('Khăn quàng cổ', '840206485_1109306771563951_883964005602373448_n.jpg', 'K028', 'Khăn Quàng Thổ Cẩm Đôi Lứa Thủy Chung', 'Everlasting Love Brocade Scarf', 'scarf', 'Khăn quàng cổ', 'Scarf', 700000, 5, 7, 'Rơ Châm Phaih', 'motif-jrai-018', '180cm x 35cm', 'Hoa văn đôi lứa son sắt mộc mạc', 'Rustic fidelity couple motifs'),
]

# Set fixed random seed for reproducible days
random.seed(2026)

final_products = []

for item in RAW_ITEMS:
    src_folder, src_file, code, nameVi, nameEn, cat_key, cat_nameVi, cat_nameEn, price, min_days, max_days, artisan_key, motif_id, dims, mat_vi, mat_en = item
    
    # 1. Determine clean destination image filename
    ext = os.path.splitext(src_file)[1].lower()
    if ext not in ['.jpg', '.jpeg', '.png']:
        ext = '.jpg'
    dst_img_name = f'{code.lower()}{ext}'
    dst_img_path = os.path.join(DST_PRODUCTS_IMG, dst_img_name)
    src_img_path = os.path.join(SRC_DB, src_folder, src_file)
    
    # Copy image
    if os.path.exists(src_img_path):
        shutil.copy2(src_img_path, dst_img_path)
    else:
        print(f'Warning: src image not found: {src_img_path}')
        
    rel_img_url = f'images/products/{dst_img_name}'
    
    # 2. Days calculation
    days = random.randint(min_days, max_days)
    weaving_str = f'{days} ngày dệt tay tỉ mỉ'
    
    # 3. Lookup Artisan
    artisan_obj = ARTISAN_NAME_TO_OBJ.get(artisan_key, ARTISANS_DATA[0])
    artisan_id = artisan_obj['id']
    artisan_name = artisan_obj['name']
    artisan_village = artisan_obj['village']
    
    # Append code to artisan productIds
    if code not in artisan_obj['productIds']:
        artisan_obj['productIds'].append(code)
        
    # 4. Lookup Motif
    motif_obj = MOTIF_MAP_BY_ID.get(motif_id, MOTIFS_DATA[0])
    motif_name = motif_obj['nameVi']
    if code not in motif_obj['appliedProducts']:
        motif_obj['appliedProducts'].append(code)
        
    price_formatted = f'{price:,.0f} ₫'.replace(',', '.')
    
    prod_data = {
        "id": code,
        "slugId": f"{cat_key}-{code.lower()}",
        "code": code,
        "nameVi": nameVi,
        "nameEn": nameEn,
        "category": cat_key,
        "categoryNameVi": cat_nameVi,
        "categoryNameEn": cat_nameEn,
        "price": price,
        "priceFormatted": price_formatted,
        "artisanId": artisan_id,
        "artisanName": artisan_name,
        "artisanVillage": artisan_village,
        "weavingHours": weaving_str,
        "weavingDays": days,
        "dimensions": dims,
        "materialVi": mat_vi,
        "materialEn": mat_en,
        "motifUsed": motif_name,
        "motifId": motif_id,
        "storyVi": f"Tác phẩm {nameVi} được hoàn thiện qua {days} ngày dệt thủ công bởi {artisan_name} tại {artisan_village}. Sản phẩm lưu giữ trọn vẹn hoa văn di sản {motif_name}, mang hồn thiêng đại ngàn và ước vọng phát triển sinh kế bền vững.",
        "storyEn": f"{nameEn} was crafted over {days} days of dedicated backstrap handweaving by master artisan {artisan_name} in {artisan_village}. It authentically bears the sacred {motif_name} motif.",
        "impactVi": "Trực tiếp đóng góp 100% thù lao dệt công bằng cho nghệ nhân và Quỹ bảo tồn di sản dệt thổ cẩm Ia Mơ Nông.",
        "impactEn": "Directly supports fair living wages for indigenous artisans and the Ia Mo Nong Weaving Preservation Fund.",
        "image": rel_img_url,
        "additionalImages": [rel_img_url],
        "featured": (code in ['K001', 'K002', 'VI001', 'TT001', 'V001', 'A001', 'B001', 'TD001']),
        "inStock": True
    }
    final_products.append(prod_data)

print(f'Processed {len(final_products)} products successfully!')

# 5. Write js/products-data.js
products_js_content = f'''/**
 * DỰ ÁN SVTHM2026: GIỮ MỘT NGHỀ - DỆT NÊN TƯƠNG LAI
 * Dữ liệu 57 Sản Phẩm Thổ Cẩm Đồng Bộ Toàn Diện Từ Database SVTHM 2026
 * Chuẩn hóa: Mã SP độc lập, Giá niêm yết, Số ngày dệt, Liên kết Nghệ nhân, Hoa văn khớp sản phẩm
 */
const PRODUCTS_DATA = {json.dumps(final_products, ensure_ascii=False, indent=2)};
'''

with open(os.path.join(ROOT_DIR, 'js', 'products-data.js'), 'w', encoding='utf-8') as f:
    f.write(products_js_content)
print('Updated js/products-data.js successfully!')

# 6. Write js/artisans-data.js
artisans_js_content = f'''/**
 * DỰ ÁN SVTHM2026: GIỮ MỘT NGHỀ - DỆT NÊN TƯƠNG LAI
 * Dữ liệu 9 Nghệ Nhân Thổ Cẩm Làng Kép & Làng Phung, Xã Ia Mơ Nông, Huyện Chư Păh, Tỉnh Gia Lai
 * Đồng bộ chuẩn xác từ Database SVTHM 2026
 */
const ARTISANS_DATA = {json.dumps(ARTISANS_DATA, ensure_ascii=False, indent=2)};
'''

with open(os.path.join(ROOT_DIR, 'js', 'artisans-data.js'), 'w', encoding='utf-8') as f:
    f.write(artisans_js_content)
print('Updated js/artisans-data.js successfully!')

# 7. Write js/motifs-data.js
motifs_js_content = f'''/**
 * DỰ ÁN SVTHM2026: GIỮ MỘT NGHỀ - DỆT NÊN TƯƠNG LAI
 * Dữ liệu Ngân hàng số 20 Hoa Văn Thổ Cẩm Jrai (Digital Cultural Heritage Bank)
 * Đồng bộ chuẩn xác từ thực địa và Database SVTHM 2026
 */
const MOTIFS_DATA = {json.dumps(MOTIFS_DATA, ensure_ascii=False, indent=2)};
'''

with open(os.path.join(ROOT_DIR, 'js', 'motifs-data.js'), 'w', encoding='utf-8') as f:
    f.write(motifs_js_content)
print('Updated js/motifs-data.js successfully!')

print('ALL 3 DATA FILES SUCCESSFULLY BUILT AND SYNCHRONIZED!')
