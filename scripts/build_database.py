# -*- coding: utf-8 -*-
"""
DỰ ÁN SVTHM 2026: GIỮ MỘT NGHỀ - DỆT NÊN TƯƠNG LAI
Script đồng bộ và chuyển đổi toàn bộ cơ sở dữ liệu từ 'database SVTHM 2026'
kết hợp dữ liệu chuyên sâu từ 'SERIES THỔ CẨM.docx':
1. Copy ảnh sản phẩm vào images/products/ với tên chuẩn hóa
2. Tạo js/products-data.js (57 sản phẩm, giá chuẩn, ngày dệt chuẩn, câu chuyện sản phẩm văn hóa chân thực)
3. Cập nhật js/artisans-data.js (9 nghệ nhân thực tế)
4. Cập nhật js/motifs-data.js (20 hoa văn với đầy đủ nghiên cứu ý nghĩa hoa văn, triết lý Yang Kơtơp, p'nga/rúp)
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

# Load series_data.json extracted from SERIES THỔ CẨM.docx
SERIES_JSON_PATH = os.path.join(ROOT_DIR, 'scripts', 'series_data.json')
with open(SERIES_JSON_PATH, 'r', encoding='utf-8') as f:
    SERIES_DATA = json.load(f)

DOC_MOTIFS = SERIES_DATA['motifs']
DOC_STORIES = {s['index']: s for s in SERIES_DATA['stories']}

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
# 2. DANH SÁCH 20 HOA VĂN NÂNG CẤP VỚI NỘI DUNG TỪ SERIES THỔ CẨM.DOCX
# ==============================================================================
BASE_MOTIFS = [
    {
        "id": "motif-jrai-001",
        "motif_code": "JRAI-001",
        "nameJrai": "Mơ-nơ̆ (Con Gà)",
        "nameVi": "Hoa Văn Con Gà (Mơ-nơ̆) — Khởi Đầu & Ánh Sáng",
        "nameEn": "Rooster Motif (Mơ-nơ̆) — Dawn & Life Energy",
        "theme": "nature",
        "themeNameVi": "Thiên nhiên & Muông thú",
        "technique": "Dệt cài sợi nổi Kơnech (Kỹ thuật đếm sợi cách điệu nổi 3D)",
        "philosophyVi": "Người Jrai quan niệm tiếng gà gáy sớm xua tan bóng tối và ma quỷ, đánh thức buôn làng đón ngày mới. Hình ảnh con gà thể hiện ước mơ về sự sinh sôi, mùa màng bội thu và lòng thành kính với thế giới tự nhiên.",
        "meaningVi": "Biểu tượng của sự sống, ánh sáng và sinh sôi phát triển. Gắn bó mật thiết với nghi lễ cúng Yang và ước vọng gia đình ấm no.",
        "meaningEn": "Symbol of dawn, celestial light, and fresh beginnings. The rooster disperses shadows and embodies prosperity.",
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
        "nameJrai": "Hình Thoi & Chữ X (P'nga / Rúp)",
        "nameVi": "Hoa Văn Hình Học Cổ — Ngôn Ngữ Biểu Tượng Di Sản",
        "nameEn": "Ancient Geometric Motifs — Sacred Symbolic Language",
        "theme": "life",
        "themeNameVi": "Đời sống & Con người",
        "technique": "Dệt luồn chỉ kép ziczac đối xứng qua tâm",
        "philosophyVi": "Hệ thống ngôn ngữ biểu tượng phản ánh nhân sinh quan và triết lý 'Vạn vật hữu linh' (Yang Kơtơp). Đường thẳng (dưng room) là trật tự buôn làng; ziczac (den đông) là dòng suối uốn lượn; tam giác là mái nhà rông; hình thoi (klang liếp) là sự phồn thực sinh sôi; mái nhà (sat char) là che chở dòng họ.",
        "meaningVi": "Ngôn ngữ ký hiệu phản ánh trật tự buôn làng, núi rừng hoang sơ và ước vọng sống hòa hợp tuyệt đối cùng thần linh và thiên nhiên.",
        "meaningEn": "Ancient Jrai symbolic language reflecting communal order, cosmic harmony, and matrilineal continuity.",
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
        "nameVi": "Hoa Văn Cây Lúa — No Ấm & Lòng Biết Ơn Mẹ Lúa",
        "nameEn": "Rice Stalk Motif — Yang Gratitude & Golden Harvest",
        "theme": "nature",
        "themeNameVi": "Thiên nhiên & Nông nghiệp",
        "technique": "Dệt vạch phân tầng ngang truyền thống",
        "philosophyVi": "Gắn liền với nền kinh tế nương rẫy và triết lý 'vạn vật hữu linh'. Hoa văn cây lúa gửi gắm lòng biết ơn đối với thần Yang và trời đất đã ban mưa thuận gió hòa, cầu mùa màng bội thu trong Lễ mừng lúa mới.",
        "meaningVi": "Biểu tượng của sự ấm no, phồn thực và lòng tri ân nguồn cội nuôi dưỡng buôn làng qua bao thế hệ.",
        "meaningEn": "Revering divine rice harvests and celestial deities. Cascading grains symbolize abundance and peace.",
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
        "nameVi": "Hoa Văn Hoa Mào Gà — Năng Lượng Sống & Che Chở",
        "nameEn": "Cockscomb Flower Motif — Vitality & Sacred Shelter",
        "theme": "ritual",
        "themeNameVi": "Tín ngưỡng & Lễ hội",
        "technique": "Dệt đứng hai bông song hành trên nền chàm mun",
        "philosophyVi": "Sắc đỏ nổi bật của hoa mào gà tượng trưng cho may mắn, niềm vui và năng lượng sống mãnh liệt. Thể hiện sự hòa hợp giữa con người với thiên nhiên và ước nguyện gia đình sung túc, bình an.",
        "meaningVi": "Tượng trưng cho sự may mắn, rực rỡ và che chở bình an. Dệt đứng đôi biểu trưng cho tình yêu bền chặt và ngọn lửa gia đình.",
        "meaningEn": "Vibrant crimson dispels ill fortune and preserves peace. Paired vertical blooms represent faithful love.",
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
        "nameVi": "Hoa Văn Cây Nêu Yang — Trục Vũ Trụ & Cầu Nối Tâm Linh",
        "nameEn": "Sacred Ceremonial Pole Motif — Cosmic Axis",
        "theme": "ritual",
        "themeNameVi": "Tín ngưỡng & Lễ hội",
        "technique": "Dệt nổi hình thoi chân nêu và tua rua rủ truyền thống",
        "philosophyVi": "Cây nêu là 'cầu nối' giữa mặt đất (con người) với bầu trời (thần linh / Yang) trong các nghi lễ nông nghiệp và lễ bỏ mả Pơthi. Thể hiện sự thành kính, cầu mong mưa thuận gió hòa và buôn làng khỏe mạnh.",
        "meaningVi": "Biểu tượng kết nối tâm linh thiêng liêng, gửi gắm ước nguyện bình an, mùa màng tươi tốt và cuộc sống thanh bình.",
        "meaningEn": "Sacred communal axis connecting mortals to heavenly Yang deities, channeling protection and peace.",
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
        "nameVi": "Hoa Văn Con Cá Suối — Nguồn Sống Đại Ngàn & No Đủ",
        "nameEn": "Stream Fish Motif — Source of Life & Abundance",
        "theme": "nature",
        "themeNameVi": "Thiên nhiên & Muông thú",
        "technique": "Dệt vảy cá đan cài nhịp nhàng",
        "philosophyVi": "Gắn liền với các dòng suối mát lành và lưu vực sông Ba – nơi cung cấp nước ngọt và nguồn sinh kế nuôi dưỡng đồng bào Jrai. Thể hiện sự trân trọng mẹ thiên nhiên và ước mơ cuộc sống đủ đầy.",
        "meaningVi": "Biểu tượng của nguồn sống trù phú, sự bình yên và sinh sôi nảy nở quanh dòng suối buôn làng.",
        "meaningEn": "Symbol of pure mountain streams, fertility, and continuous plenty from mother nature.",
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
        "nameJrai": "Tneh (Cây Tre)",
        "nameVi": "Hoa Văn Cây Tre (Tneh) — Dấu Nối Tâm Linh & Sức Sống Dẻo Dai",
        "nameEn": "Sacred Bamboo Grove — Spiritual Continuity & Resilience",
        "theme": "nature",
        "themeNameVi": "Thiên nhiên & Nông nghiệp",
        "technique": "Dệt sọc đứng phân tầng mô phỏng đốt tre",
        "philosophyVi": "Cách điệu từ hình dáng của cây nêu – linh vật kết từ tre nứa trong lễ hội lớn. Cây tre phản ánh mối quan hệ mật thiết giữa con người với núi rừng và sức sống bền bỉ không khuất phục trước bão giông.",
        "meaningVi": "Gắn liền với linh vật cây nêu và triết lý vạn vật hữu linh (Yang Kơtơp), tượng trưng cho sự dẻo dai và kiên cường.",
        "meaningEn": "Enduring highland resilience and spiritual connection through ceremonial bamboo poles.",
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
        "nameJrai": "K’toanh & Kdăk (Cây Cỏ Núi Rừng)",
        "nameVi": "Hoa Văn Cây Cỏ Núi Rừng — Mầm Xanh Tái Sinh & Bản Sắc Sắc Màu",
        "nameEn": "Wild Forest Herbs Motif — Highland Vitality",
        "theme": "nature",
        "themeNameVi": "Thiên nhiên & Nông nghiệp",
        "technique": "Dệt mầm nhọn tỏa tia mềm mại",
        "philosophyVi": "Mô phỏng lá dương xỉ (k’toanh), cây (tneh), quả (kdăk). Tượng trưng cho sức sống bền bỉ của đại ngàn. Nền đen là quyền lực núi rừng; đỏ và trắng là khát vọng sống và lòng dũng cảm; vàng là ánh sáng và ấm no.",
        "meaningVi": "Sức sống mãnh liệt của thiên nhiên nương rẫy, sự hòa quyện giữa đất trời bazan và lòng biết ơn đại ngàn.",
        "meaningEn": "Verdant renewal and botanical blessings of native highland flora.",
        "colors": ["Xanh non", "Vàng rơm", "Đỏ đất", "Đen mun"],
        "artisanVerification": "Nghệ nhân Rơ Châm Mril (25 năm tuổi nghề)",
        "village": "Làng Kép, xã Ia Mơ Nông, Gia Lai",
        "appliedProducts": [],
        "image": "images/motifs/cay-co.png",
        "accentColor": "#16A34A"
    },
    {
        "id": "motif-jrai-009",
        "motif_code": "JRAI-009",
        "nameJrai": "Chậu Hoa Rừng",
        "nameVi": "Hoa Văn Chậu Hoa — Ươm Mầm Sinh Sôi & Vẻ Đẹp Đời Sống",
        "nameEn": "Blooming Flower Pot Motif — Nurturing Love",
        "theme": "life",
        "themeNameVi": "Đời sống & Con người",
        "technique": "Dệt cánh hoa mở rộng trên giá đỡ đối xứng",
        "philosophyVi": "Biểu tượng của sự sinh sôi và sức sống tươi đẹp của núi rừng Tây Nguyên. Gửi gắm ước vọng về cây trái đơm hoa kết trái, buôn làng phát triển và bàn tay khéo léo vun vén của người phụ nữ mẫu hệ.",
        "meaningVi": "Tượng trưng cho sự chăm chút, vun trồng tình yêu thương và khát vọng cuộc sống tốt tươi, no đủ.",
        "meaningEn": "Cultivating domestic joy, floral elegance, and harmonious living in the highlands.",
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
        "nameJrai": "Ceh (Ghè Rượu Cổ)",
        "nameVi": "Hoa Văn Ghè Cổ (Ceh) — Nơi Trú Ngụ Của Yàng & Gắn Kết Cộng Đồng",
        "nameEn": "Ancient Wine Jar Motif — Abode of Yang & Communal Unity",
        "theme": "ritual",
        "themeNameVi": "Tín ngưỡng & Lễ hội",
        "technique": "Dệt khối bầu ghè nổi với hoa văn quấn quanh cổ ghè",
        "philosophyVi": "Ghè cổ là báu vật thiêng liêng, nơi ẩn chứa và ngự trị của các Yang. Ngày xưa ghè quý đổi bằng nhiều con trâu, khẳng định vị thế dòng họ. Vò rượu cần là trung tâm gắn kết sum vầy và lòng hiếu khách của người Jrai.",
        "meaningVi": "Biểu tượng tâm linh thiêng liêng của Yang, sự sung túc và tình đoàn kết gắn bó keo sơn trong buôn làng.",
        "meaningEn": "Sacred communal gatherings, ancestral wealth, hospitality, and shared blessings around the wine jar.",
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
        "nameJrai": "Giã Gạo Ban Mai",
        "nameVi": "Hoa Văn Giã Gạo Ban Mai — Nhịp Lao Động & Âm Thanh No Ấm",
        "nameEn": "Morning Rice Pounding Motif — Rhythm of Abundance",
        "theme": "life",
        "themeNameVi": "Đời sống & Con người",
        "technique": "Dệt nhịp chày đôi đối xứng nhịp nhàng",
        "philosophyVi": "Tái hiện nhịp lao động cần cù mỗi sớm mai. Tiếng chày giã gạo vang lên giữa đại ngàn là âm thanh của sự sống, tượng trưng cho mùa màng bội thu, sự thịnh vượng và bàn tay người mẹ chăm lo cho gia đình.",
        "meaningVi": "Tôn vinh đức tính siêng năng, sự chịu thương chịu khó của phụ nữ Jrai và ước vọng ấm no bền lâu.",
        "meaningEn": "Celebrating industrious morning labor, maternal care, and the nourishing heartbeat of the village.",
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
        "nameJrai": "Gùi Nương (Gánh Buôn)",
        "nameVi": "Hoa Văn Gánh Buôn — Cần Mẫn Vun Đắp Sinh Kế Buôn Làng",
        "nameEn": "Carrier Basket Motif — Diligence & Sustainable Livelihood",
        "theme": "life",
        "themeNameVi": "Đời sống & Con người",
        "technique": "Dệt gùi mang lưng và đòn gánh bước đi",
        "philosophyVi": "Mô phỏng hình ảnh chiếc gùi sau lưng và bước chân người phụ nữ vượt đèo dốc lên rẫy, mang sản vật về nuôi sống gia đình. Thể hiện sự cần cù, dẻo dai và tinh thần tự lực kiến tạo cuộc sống.",
        "meaningVi": "Biểu tượng của sự chịu thương chịu khó, tinh thần tự cường và khát vọng kiến tạo sinh kế no đủ.",
        "meaningEn": "Diligence, steadfast highland steps, and building resilient livelihoods across mountain paths.",
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
        "nameJrai": "Dấu Xưa Di Sản (Mơ Nga Plum)",
        "nameVi": "Hoa Văn Dấu Xưa Di Sản — Ký Ức Cội Nguồn & Luật Tục Truyền Thừa",
        "nameEn": "Ancient Heritage Mark Motif — Ancestral Memory & Sacred Lore",
        "theme": "ritual",
        "themeNameVi": "Tín ngưỡng & Lễ hội",
        "technique": "Dệt ký hiệu cổ truyền mẫu hệ",
        "philosophyVi": "Hệ thống biểu tượng ước lệ cao (cây Mơ nga Plum, cây Kơ chép Brom). Triết lý vạn vật hữu linh (Yang Kơtơp), tuân thủ nghiêm ngặt các quy tắc kiêng kỵ (như cấm dệt mẫu cây Ana Kđa cho người sống). Mỗi đường chỉ là cuốn sách lưu giữ ký ức cộng đồng.",
        "meaningVi": "Gìn giữ bản sắc cội nguồn, tri thức thủ công mẫu hệ và lòng biết ơn đối với các thế hệ tổ tiên đi trước.",
        "meaningEn": "Sacred ancestral memory, strict cultural ethics, and preserving unbroken indigenous identity.",
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
        "nameJrai": "Mơ Nuih (Sinh Hoạt Buôn Làng)",
        "nameVi": "Hoa Văn Sinh Hoạt Buôn Làng — Nhịp Sống Dung Dị & Tình Cộng Đồng",
        "nameEn": "Communal Village Life Motif — Rhythm Under Nha Rong",
        "theme": "life",
        "themeNameVi": "Đời sống & Con người",
        "technique": "Dệt đại cảnh người múa xoang, đánh chiêng, dệt vải",
        "philosophyVi": "Mô-típ hình người (mơ nuih) và mái nhà rông, nhà sàn mô tả nhịp sống dung dị, tinh thần đoàn kết sẻ chia giữa các thành viên buôn làng. Tấm thổ cẩm là minh chứng cho sự kiên trì và tâm hồn phong phú của người phụ nữ Jrai.",
        "meaningVi": "Sự hòa quyện giữa con người, thiên nhiên và tín ngưỡng; tôn vinh sức mạnh gắn kết của cộng đồng buôn làng.",
        "meaningEn": "Communal solidarity, Gong heritage pride, and harmonious village celebration under the stilt roof.",
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
        "nameJrai": "Mẹ Và Chị Mẫu Hệ",
        "nameVi": "Hoa Văn Mẹ Và Chị — Ngọn Lửa Mẫu Hệ & Bàn Tay Trao Truyền",
        "nameEn": "Mother & Sister Motif — Matrilineal Kinship",
        "theme": "life",
        "themeNameVi": "Đời sống & Con người",
        "technique": "Dệt hai thế hệ phụ nữ song hành nắm tay",
        "philosophyVi": "Nghề dệt thổ cẩm là công việc thiêng liêng gắn liền với phụ nữ Jrai theo truyền thống mẫu hệ. Từ nhỏ bé gái đã được bà, mẹ và chị kèm cặp se sợi, nhuộm lá rừng và cài hoa văn. Tấm vải là thước đo sự đảm đang, kiên nhẫn và tình thân gia đình.",
        "meaningVi": "Biểu tượng của tình mẫu tử, sự trao truyền nghề nghiệp và ngọn lửa gìn giữ văn hóa gia đình mẫu hệ.",
        "meaningEn": "Matrilineal bond, generational mentorship, and honoring highland women as cultural guardians.",
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
        "nameVi": "Hoa Văn Người Làm Rẫy — Nương Rẫy Đại Ngàn & Mồ Hôi Đất Mẹ",
        "nameEn": "Highland Farmer Motif — Sweat on Bazan Soil",
        "theme": "life",
        "themeNameVi": "Đời sống & Con người",
        "technique": "Dệt dáng hình người cuốc đất, tra hạt giống",
        "philosophyVi": "Trong không gian nương rẫy nông nghiệp, các đường ziczac (sóng nước, dốc nương) và hạt giống phản ánh nhịp sống lao động vất vả nhưng tràn ngập niềm vui. Đó là lời tri ân đối với thần linh, đất trời và thành quả của giọt mồ hôi chân chính.",
        "meaningVi": "Tôn vinh giá trị lao động cần lao, sức bền bỉ kiên cường trước thiên nhiên và sự gắn bó với đất mẹ Tây Nguyên.",
        "meaningEn": "Honoring honest toil and the spiritual bond between upland farmers and fertile volcanic soil.",
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
        "nameJrai": "Đám Trẻ Thơ (Mơ Nuih)",
        "nameVi": "Hoa Văn Đám Trẻ Thơ — Ước Vọng Phồn Thực & Kế Thừa Di Sản",
        "nameEn": "Village Children Motif — Highland Innocence & Continuity",
        "theme": "life",
        "themeNameVi": "Đời sống & Con người",
        "technique": "Dệt nhóm trẻ con vui đùa nhí nhảnh",
        "philosophyVi": "Chế độ mẫu hệ đặt niềm hy vọng vào thế hệ tiếp nối. Tiếng cười trẻ thơ bên hiên nhà sàn là minh chứng cho buôn làng ấm no. Nhắc nhở trách nhiệm trao truyền lại những giá trị văn hóa cốt lõi cho những người sẽ làm chủ buôn làng mai sau.",
        "meaningVi": "Biểu tượng của sự trường tồn dòng họ mẫu hệ, sự bình yên của buôn làng và niềm hy vọng vào tương lai tươi sáng.",
        "meaningEn": "Auspicious symbol of matrilineal continuity, joyous highland childhood, and cultural succession.",
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
        "nameJrai": "Đôi Lứa Thủy Chung",
        "nameVi": "Hoa Văn Đôi Lứa — Thủy Chung Son Sắt & Giao Hòa Hai Dòng Họ",
        "nameEn": "Devoted Couple Motif — Eternal Fidelity & Kinship",
        "theme": "life",
        "themeNameVi": "Đời sống & Con người",
        "technique": "Dệt hai nhân vật nam nữ đối xứng qua nhành hoa",
        "philosophyVi": "Tình yêu nam nữ gắn kết keo sơn như những sợi chỉ đan khít vào nhau trên khung cửi. Trong chế độ mẫu hệ, hôn nhân là sự giao hòa, gắn kết giữa hai dòng họ và buôn làng. Thước đo sự tinh tế, đảm đang của người phụ nữ dệt tấm váy cưới.",
        "meaningVi": "Biểu tượng tình yêu thủy chung, sự hòa hợp gia đình và sự kết nối bền chặt giữa các gia tộc trong cộng đồng.",
        "meaningEn": "Enduring fidelity, marital harmony, and matrilineal kinship solidarity across generations.",
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
        "nameVi": "Hoa Văn Khát Vọng Vươn Xa — Sức Sống Vươn Lên & Hội Nhập Tương Lai",
        "nameEn": "Highland Aspirations Motif — Wings of the Future",
        "theme": "life",
        "themeNameVi": "Đời sống & Con người",
        "technique": "Dệt dải sao sáng và chim lượn vút lên trời cao",
        "philosophyVi": "Các họa tiết vươn lên cao tượng trưng cho sức sống mạnh mẽ của đại ngàn, ý chí vượt khó vươn tới ấm no. Trong thời đại mới, đây là tinh thần đưa thổ cẩm và sản vật địa phương vươn xa ra thị trường toàn quốc và quốc tế.",
        "meaningVi": "Ý chí kiên cường, khát vọng đưa di sản buôn làng bay cao mà vẫn vững vàng giữ trọn cội nguồn bản sắc.",
        "meaningEn": "Empowering youth, indigenous innovation, and taking traditional craftsmanship to global horizons.",
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
        "nameJrai": "Xe Bay (Máy Bay)",
        "nameVi": "Hoa Văn Máy Bay — Giao Thoa Đương Đại & Thế Giới Quan Mới",
        "nameEn": "Contemporary Airplane Motif — Modern Skies & Innovation",
        "theme": "life",
        "themeNameVi": "Đời sống & Con người",
        "technique": "Dệt cách điệu cánh máy bay bay qua ngọn núi",
        "philosophyVi": "Sự sáng tạo độc đáo khi người nghệ nhân Jrai 'dệt những gì họ thấy và thích'. Cách điệu phương tiện hiện đại thành hoa văn đối xứng hài hòa trên nền vải chàm thể hiện tay nghề bậc thầy và ước vọng kết nối với thế giới bên ngoài.",
        "meaningVi": "Biểu tượng cho sự đổi mới, tinh thần cởi mở tiếp nhận nhịp sống hiện đại mà không đánh mất bản sắc cổ truyền.",
        "meaningEn": "Harmonious fusion of ancient handloom craft with contemporary aviation, connecting highlands to the world.",
        "colors": ["Xanh da trời", "Bạc", "Đỏ cờ"],
        "artisanVerification": "Nghệ nhân H' Uyên Niê (20 năm tuổi nghề)",
        "village": "Xã Ia Mơ Nông, Chư Păh, Gia Lai",
        "appliedProducts": [],
        "image": "images/motifs/may-bay.png",
        "accentColor": "#0284C7"
    }
]

# Enrich BASE_MOTIFS with DOC_MOTIFS research data
MOTIFS_DATA = []
for m in BASE_MOTIFS:
    m_id = m['id']
    doc_info = DOC_MOTIFS.get(m_id, {})
    m_enriched = dict(m)
    m_enriched['researchOverview'] = doc_info.get('overview', '')
    m_enriched['researchBullets'] = doc_info.get('bullets', [])
    m_enriched['researchFullText'] = doc_info.get('full_text', '')
    MOTIFS_DATA.append(m_enriched)

MOTIF_MAP_BY_ID = {m['id']: m for m in MOTIFS_DATA}

# ==============================================================================
# 3. DANH SÁCH 57 SẢN PHẨM KHỚP VỚI DATABASE & GÁN CÂU CHUYỆN TỪ DOCX
# ==============================================================================
# Bảng ánh xạ sản phẩm sang câu chuyện (Story ID 1-20)
PRODUCT_TO_STORY_MAP = {
    'B001': 4,   # DẤU XƯA CÒN MÃI – DI SẢN TIẾP NỐI (Rơ Châm Cơm & Bầu nước)
    'V001': 5,   # HOA VĂN ĐÔI LỨA – SỢI CHỈ DỆT NÊN TÌNH YÊU VÀ SỰ GẮN KẾT (Rơ Châm Mril)
    'V002': 17,  # KHĂN THỔ CẨM JRAI – DỆT NHỊP SỐNG, NỐI DÀI NHỮNG CHÂN TRỜI (Rơ Châm Mril)
    'A001': 3,   # TỪ ĐẠI NGÀN VƯƠN RA THẾ GIỚI (Rơ Châm Krế)
    'A002': 3,   # TỪ ĐẠI NGÀN VƯƠN RA THẾ GIỚI (Rơ Châm Krế)
    'TT001': 6,  # TỪ BÀN TAY MẸ VÀ CHỊ – DỆT NÊN HỒN CỐT ĐẠI NGÀN (Rơ Châm Krế)
    'TT002': 15, # TỪ BUÔN LÀNG ĐẾN NHỮNG CHÂN TRỜI MỚI (Rơ Châm Krế)
    'TT003': 3,  # TỪ ĐẠI NGÀN VƯƠN RA THẾ GIỚI (Rơ Châm Krế)
    'TD001': 1,  # NHỮNG ĐƯỜNG NÉT KỂ CHUYỆN ĐẠI NGÀN (Rơ Châm Mân & Giã gạo)
    'TD002': 19, # RƠ CHÂM NGHEL – Nhịp sống buôn làng (Bông lúa mùa vàng)
    'TD003': 13, # NHỊP SỐNG BUÔN LÀNG – Ghè rượu cần & Cà phê
    'TD004': 19, # RƠ CHÂM NGHEL – Nhịp sống buôn làng & Cây tre
    'TD005': 1,  # NHỮNG ĐƯỜNG NÉT KỂ CHUYỆN ĐẠI NGÀN – Hình học cổ & Gốm
    'VI001': 4,  # DẤU XƯA CÒN MÃI – DI SẢN TIẾP NỐI (Rơ Châm Cơm)
    'VI002': 16, # TỪ TÌNH THÂN ĐẾN SỨC SỐNG ĐẠI NGÀN (Rơ Châm Cơm & Đám trẻ thơ)
    'VI003': 16, # TỪ TÌNH THÂN ĐẾN SỨC SỐNG ĐẠI NGÀN (Rơ Châm Cơm & Chậu hoa)
    'VI004': 7,  # Sắc hoa mào gà & Rơ Châm Nghị
    'VI005': 18, # H’ UYÊN NIÊ – Con Gà Mơ-nơ̆ & Khát vọng vươn xa
    'VI006': 9,  # TỪ NHỊP SỐNG ĐẠI NGÀN ĐẾN ƯỚC NGUYỆN BÌNH AN (Rơ Châm Nghị)
    'VI007': 4,  # DẤU XƯA CÒN MÃI – DI SẢN TIẾP NỐI (Rơ Châm Cơm)
    'C001': 13,  # NHỊP SỐNG BUÔN LÀNG QUA TỪNG ĐƯỜNG DỆT (Rơ Châm Monh)
    'C002': 13,  # NHỊP SỐNG BUÔN LÀNG – Ghè rượu cần (Rơ Châm Monh)
    'C003': 7,   # TỪ NHỊP SỐNG ĐẠI NGÀN (H' Uyên Niê & Lũy tre)
    'C004': 13,  # NHỊP SỐNG BUÔN LÀNG – Đôi lứa thủy chung (Rơ Châm Monh)
    'C005': 7,   # Người làm rẫy – Gửi công sức vào từng mùa vụ (Rơ Châm Nghị)
    'C006': 2,   # KHĂN QUÀNG ĐẠI NGÀN – Kỹ thuật dệt Kơnech (Rơ Châm Krế)
    'C007': 18,  # H' UYÊN NIÊ – Máy bay & Giao thoa hiện đại
    'C008': 13,  # NHỊP SỐNG BUÔN LÀNG – Gánh buôn nương rẫy (Rơ Châm Monh)
    'C009': 14,  # TỪ BÀN TAY MẸ VÀ CHỊ, DỆT NÊN SỨC SỐNG ĐẠI NGÀN (Rơ Châm Nghel)
    'K001': 7,   # TỪ NHỊP SỐNG ĐẠI NGÀN – DỆT NÊN CÂU CHUYỆN NO ẤM (H’ Uyên Niê)
    'K002': 9,   # KHĂN THỔ CẨM JRAI – TỪ NHỊP SỐNG ĐẠI NGÀN ĐẾN ƯỚC NGUYỆN BÌNH AN (Rơ Châm Nghị)
    'K003': 18,  # H’ UYÊN NIÊ – Con Gà Mơ-nơ̆ – Biểu tượng khởi đầu (Rơ Châm Nghị / H' Uyên Niê)
    'K004': 14,  # TỪ BÀN TAY MẸ VÀ CHỊ, DỆT NÊN SỨC SỐNG ĐẠI NGÀN (Rơ Châm Nghị)
    'K005': 14,  # TỪ BÀN TAY MẸ VÀ CHỊ, DỆT NÊN SỨC SỐNG ĐẠI NGÀN (Rơ Châm Nghị)
    'K006': 8,   # CÂY TRE ĐẠI NGÀN – DẤU NỐI TÂM LINH VÀ BẢN SẮC JRAI (Rơ Châm Nghị)
    'K007': 11,  # DẤU ẤN TỔ TIÊN, SẮC HOA VÀ HƠI THỞ ĐẠI NGÀN (Rơ Châm Nghị)
    'K008': 7,   # Sắc hoa mào gà – Sắc màu của niềm vui và hy vọng (Rơ Châm Nghị)
    'K009': 20,  # RƠ CHÂM PHAIH – Nhịp sống bên dòng suối – Dệt nên ước vọng no ấm
    'K010': 2,   # KHĂN QUÀNG ĐẠI NGÀN – Con cá suối (Rơ Châm Krế)
    'K011': 6,   # TỪ BÀN TAY MẸ VÀ CHỊ – DỆT NÊN HỒN CỐT ĐẠI NGÀN (H' Uyên Niê)
    'K012': 11,  # DẤU ẤN TỔ TIÊN, SẮC HOA VÀ HƠI THỞ ĐẠI NGÀN (Rơ Châm Nghị)
    'K013': 9,   # TỪ NHỊP SỐNG ĐẠI NGÀN ĐẾN ƯỚC NGUYỆN BÌNH AN (Rơ Châm Nghị)
    'K014': 10,  # CÂY NÊU YANG – GỬI ƯỚC NGUYỆN BÌNH AN VÀO TỪNG SỢI CHỈ (Rơ Châm Phaih)
    'K015': 13,  # NHỊP SỐNG BUÔN LÀNG QUA TỪNG ĐƯỜNG DỆT (Rơ Châm Monh)
    'K016': 8,   # CÂY TRE ĐẠI NGÀN – DẤU NỐI TÂM LINH VÀ BẢN SẮC JRAI (Rơ Châm Nghị)
    'K017': 20,  # RƠ CHÂM PHAIH – Nhịp sống bên dòng suối & Đỏ lửa Bazan
    'K018': 12,  # TỪ DÒNG SUỐI ĐẠI NGÀN ĐẾN NHỮNG CHÂN TRỜI MỚI (Rơ Châm Nghị / H' Uyên Niê)
    'K019': 19,  # RƠ CHÂM NGHEL – Nhịp sống buôn làng & Mùa lúa chín
    'K020': 13,  # NHỊP SỐNG BUÔN LÀNG – Dưới mái nhà rông (Rơ Châm Mân)
    'K021': 13,  # NHỊP SỐNG BUÔN LÀNG – Ghè cổ rượu cần (Rơ Châm Monh)
    'K022': 2,   # KHĂN QUÀNG ĐẠI NGÀN – Giã gạo ban mai (Rơ Châm Krế)
    'K023': 16,  # TỪ TÌNH THÂN ĐẾN SỨC SỐNG ĐẠI NGÀN – Gánh buôn nương (Rơ Châm Cơm)
    'K024': 17,  # DỆT NHỊP SỐNG, NỐI DÀI NHỮNG CHÂN TRỜI (Rơ Châm Mril)
    'K025': 18,  # Chậu hoa may mắn & Khát vọng tương lai (H' Uyên Niê)
    'K026': 18,  # Tiếng gà gáy sớm – Khởi đầu thuận lành (Rơ Châm Nghị)
    'K027': 15,  # TỪ BUÔN LÀNG ĐẾN NHỮNG CHÂN TRỜI MỚI (Rơ Châm Krế / Rơ Châm Nghel)
    'K028': 20,  # RƠ CHÂM PHAIH – Đôi lứa thủy chung & Nhịp sống dòng suối
}

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
    
    # 1. Image path
    ext = os.path.splitext(src_file)[1].lower()
    if ext not in ['.jpg', '.jpeg', '.png']:
        ext = '.jpg'
    dst_img_name = f'{code.lower()}{ext}'
    dst_img_path = os.path.join(DST_PRODUCTS_IMG, dst_img_name)
    src_img_path = os.path.join(SRC_DB, src_folder, src_file)
    
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
    
    if code not in artisan_obj['productIds']:
        artisan_obj['productIds'].append(code)
        
    # 4. Lookup Motif
    motif_obj = MOTIF_MAP_BY_ID.get(motif_id, MOTIFS_DATA[0])
    motif_name = motif_obj['nameVi']
    if code not in motif_obj['appliedProducts']:
        motif_obj['appliedProducts'].append(code)
        
    price_formatted = f'{price:,.0f} ₫'.replace(',', '.')
    
    # 5. Lookup Authentic Story from SERIES THỔ CẨM.docx
    story_id = PRODUCT_TO_STORY_MAP.get(code, 1)
    story_data = DOC_STORIES.get(story_id, DOC_STORIES[1])
    
    story_title = story_data['title']
    story_lead = story_data['lead']
    story_paragraphs = story_data['paragraphs']
    
    # Format full narrative story
    full_narrative = f"{story_lead}\n\n" + "\n\n".join(story_paragraphs)
    
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
        
        # CÂU CHUYỆN SẢN PHẨM CHUẨN XÁC TỪ SERIES THỔ CẨM
        "storyTitle": story_title,
        "storyLead": story_lead,
        "storyParagraphs": story_paragraphs,
        "storyVi": full_narrative,
        "storyExcerptVi": f"{story_lead[:160]}...",
        "storyEn": f"Crafted over {days} days of dedicated backstrap handweaving by master artisan {artisan_name} in {artisan_village}. This piece preserves the authentic {motif_name} motif, weaving together highland natural lore, ancestral memories, and fair communal livelihood.",
        
        # Ý NGHĨA HOA VĂN TÍCH HỢP
        "motifResearchOverview": motif_obj.get('researchOverview', ''),
        "motifResearchBullets": motif_obj.get('researchBullets', []),
        
        "impactVi": "Trực tiếp đóng góp 100% thù lao dệt công bằng cho nghệ nhân và Quỹ bảo tồn di sản dệt thổ cẩm Ia Mơ Nông.",
        "impactEn": "Directly supports fair living wages for indigenous artisans and the Ia Mo Nong Weaving Preservation Fund.",
        "image": rel_img_url,
        "additionalImages": [rel_img_url],
        "featured": (code in ['K001', 'K002', 'VI001', 'TT001', 'V001', 'A001', 'B001', 'TD001']),
        "inStock": True
    }
    final_products.append(prod_data)

print(f'Processed {len(final_products)} products with genuine docx stories successfully!')

# 6. Write js/products-data.js
products_js_content = f'''/**
 * DỰ ÁN SVTHM2026: GIỮ MỘT NGHỀ - DỆT NÊN TƯƠNG LAI
 * Dữ liệu 57 Sản Phẩm Thổ Cẩm Đồng Bộ Toàn Diện Từ Database SVTHM 2026
 * và Hồ Sơ Câu Chuyện Sản Phẩm "SERIES THỔ CẨM" (Ia Mơ Nông, Chư Păh, Gia Lai)
 */
const PRODUCTS_DATA = {json.dumps(final_products, ensure_ascii=False, indent=2)};
'''

with open(os.path.join(ROOT_DIR, 'js', 'products-data.js'), 'w', encoding='utf-8') as f:
    f.write(products_js_content)
print('Updated js/products-data.js successfully!')

# 7. Write js/artisans-data.js
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

# 8. Write js/motifs-data.js
motifs_js_content = f'''/**
 * DỰ ÁN SVTHM2026: GIỮ MỘT NGHỀ - DỆT NÊN TƯƠNG LAI
 * Dữ liệu Ngân hàng số 20 Hoa Văn Thổ Cẩm Jrai (Digital Cultural Heritage Bank)
 * Tích hợp toàn bộ hồ sơ giải mã ý nghĩa hoa văn & triết lý nhân sinh bản địa từ "SERIES THỔ CẨM"
 */
const MOTIFS_DATA = {json.dumps(MOTIFS_DATA, ensure_ascii=False, indent=2)};
'''

with open(os.path.join(ROOT_DIR, 'js', 'motifs-data.js'), 'w', encoding='utf-8') as f:
    f.write(motifs_js_content)
print('Updated js/motifs-data.js successfully!')

print('ALL 3 DATA FILES SUCCESSFULLY BUILT AND ENRICHED WITH SERIES THỔ CẨM!')
