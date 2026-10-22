/**
 * DỰ ÁN SVTHM2026: GIỮ MỘT NGHỀ - DỆT NÊN TƯƠNG LAI
 * Dữ liệu 5 Nghệ Nhân Thổ Cẩm Chuẩn Từ Demo https://det-nen-tuong-lai.vercel.app/artisans
 * Xã Ia Mơ Nông, Huyện Chư Păh, Tỉnh Gia Lai
 */
const ARTISANS_DATA = [
  {
    "id": "artisan-001",
    "legacyId": "ARTISAN-01",
    "name": "Nghệ nhân Rơ châm Nghị",
    "age": 70,
    "experience": "30 năm tuổi nghề",
    "experienceYears": 30,
    "village": "Làng Kép, xã Ia Mơ Nông, huyện Chư Păh, Gia Lai",
    "avatar": "images/artisans/ro-cham-nghi.jpg",
    "specialtyVi": "Nghệ nhân Rơ châm Nghị với 30 năm tuổi nghề, là người truyền dạy kỹ thuật dệt thổ cẩm Jrai truyền thống, am hiểu sâu sắc về hoa văn cổ và nghệ thuật phối màu sợi dệt.",
    "specialtyEn": "Nghệ nhân Rơ châm Nghị với 30 năm tuổi nghề, là người truyền dạy kỹ thuật dệt thổ cẩm Jrai truyền thống, am hiểu sâu sắc về hoa văn cổ và nghệ thuật phối màu sợi dệt.",
    "quoteVi": "“Nghệ nhân Rơ châm Nghị với 30 năm tuổi nghề, là người truyền dạy kỹ thuật dệt thổ cẩm Jrai truyền thống, am hiểu sâu sắc về hoa văn cổ và ng...”",
    "quoteEn": "“Preserving the authentic spirit of Jrai indigenous weaving through every craft generation.”",
    "bioVi": "Nghệ nhân Rơ châm Nghị với 30 năm tuổi nghề, là người truyền dạy kỹ thuật dệt thổ cẩm Jrai truyền thống, am hiểu sâu sắc về hoa văn cổ và nghệ thuật phối màu sợi dệt.",
    "bioEn": "Nghệ nhân Rơ châm Nghị với 30 năm tuổi nghề, là người truyền dạy kỹ thuật dệt thổ cẩm Jrai truyền thống, am hiểu sâu sắc về hoa văn cổ và nghệ thuật phối màu sợi dệt.",
    "productIds": [
      "V001",
      "VA001",
      "V003"
    ],
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
    "avatar": "images/artisans/ro-cham-kre.jpg",
    "specialtyVi": "Nghệ nhân Rơ châm Krế có 35 năm gắn bó cùng quay sợi, bật bông và khung dệt mộc.",
    "specialtyEn": "Nghệ nhân Rơ châm Krế có 35 năm gắn bó cùng quay sợi, bật bông và khung dệt mộc.",
    "quoteVi": "“Nghệ nhân Rơ châm Krế có 35 năm gắn bó cùng quay sợi, bật bông và khung dệt mộc. Bà gìn giữ bí quyết nhuộm màu tự nhiên từ vỏ cây rừng và lá...”",
    "quoteEn": "“Preserving the authentic spirit of Jrai indigenous weaving through every craft generation.”",
    "bioVi": "Nghệ nhân Rơ châm Krế có 35 năm gắn bó cùng quay sợi, bật bông và khung dệt mộc. Bà gìn giữ bí quyết nhuộm màu tự nhiên từ vỏ cây rừng và lá chàm.",
    "bioEn": "Nghệ nhân Rơ châm Krế có 35 năm gắn bó cùng quay sợi, bật bông và khung dệt mộc. Bà gìn giữ bí quyết nhuộm màu tự nhiên từ vỏ cây rừng và lá chàm.",
    "productIds": [
      "A001",
      "V002"
    ],
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
    "specialtyEn": "Nghệ nhân Rơ châm Nghel với 36 năm cống hiến cho di sản dệt thổ cẩm Jrai, chuyên nghiệp trong kỹ thuật tạo tác hoa văn nổi ba chiều và bảo tồn nghi lễ dệt buôn làng.",
    "quoteVi": "“Nghệ nhân Rơ châm Nghel với 36 năm cống hiến cho di sản dệt thổ cẩm Jrai, chuyên nghiệp trong kỹ thuật tạo tác hoa văn nổi ba chiều và bảo t...”",
    "quoteEn": "“Preserving the authentic spirit of Jrai indigenous weaving through every craft generation.”",
    "bioVi": "Nghệ nhân Rơ châm Nghel với 36 năm cống hiến cho di sản dệt thổ cẩm Jrai, chuyên nghiệp trong kỹ thuật tạo tác hoa văn nổi ba chiều và bảo tồn nghi lễ dệt buôn làng.",
    "bioEn": "Nghệ nhân Rơ châm Nghel với 36 năm cống hiến cho di sản dệt thổ cẩm Jrai, chuyên nghiệp trong kỹ thuật tạo tác hoa văn nổi ba chiều và bảo tồn nghi lễ dệt buôn làng.",
    "productIds": [
      "VY001",
      "VA002"
    ],
    "zaloPhone": "0383451929",
    "facebookPageId": "100090304682611"
  },
  {
    "id": "artisan-004",
    "legacyId": "ARTISAN-04",
    "name": "Nghệ nhân H Uyen Nie",
    "age": 60,
    "experience": "20 năm tuổi nghề",
    "experienceYears": 20,
    "village": "Xã Ia Mơ Nông, huyện Chư Păh, Gia Lai",
    "avatar": "images/artisans/h-uyen-nie.jpg",
    "specialtyVi": "Nghệ nhân H Uyen Nie có 20 năm truyền nghề dệt, mang đến hơi thở ứng dụng hiện đại cho các sản phẩm túi, ví và khăn quàng thổ cẩm di sản.",
    "specialtyEn": "Nghệ nhân H Uyen Nie có 20 năm truyền nghề dệt, mang đến hơi thở ứng dụng hiện đại cho các sản phẩm túi, ví và khăn quàng thổ cẩm di sản.",
    "quoteVi": "“Nghệ nhân H Uyen Nie có 20 năm truyền nghề dệt, mang đến hơi thở ứng dụng hiện đại cho các sản phẩm túi, ví và khăn quàng thổ cẩm di sản....”",
    "quoteEn": "“Preserving the authentic spirit of Jrai indigenous weaving through every craft generation.”",
    "bioVi": "Nghệ nhân H Uyen Nie có 20 năm truyền nghề dệt, mang đến hơi thở ứng dụng hiện đại cho các sản phẩm túi, ví và khăn quàng thổ cẩm di sản.",
    "bioEn": "Nghệ nhân H Uyen Nie có 20 năm truyền nghề dệt, mang đến hơi thở ứng dụng hiện đại cho các sản phẩm túi, ví và khăn quàng thổ cẩm di sản.",
    "productIds": [
      "K001",
      "K002",
      "K003"
    ],
    "zaloPhone": "0383451929",
    "facebookPageId": "100090304682611"
  },
  {
    "id": "artisan-005",
    "legacyId": "ARTISAN-05",
    "name": "Nghệ nhân Rơ Châm Mân",
    "age": 56,
    "experience": "16 năm tuổi nghề",
    "experienceYears": 16,
    "village": "Làng Kép, xã Ia Mơ Nông, huyện Chư Păh, Gia Lai",
    "avatar": "images/artisans/ro-cham-man.jpg",
    "specialtyVi": "Nghệ nhân Rơ Châm Mân với 16 năm tuổi nghề, nhiệt huyết trong việc hướng dẫn thế hệ trẻ và thực hành kỹ thuật luồn thoi dệt hoa văn tinh xảo.",
    "specialtyEn": "Nghệ nhân Rơ Châm Mân với 16 năm tuổi nghề, nhiệt huyết trong việc hướng dẫn thế hệ trẻ và thực hành kỹ thuật luồn thoi dệt hoa văn tinh xảo.",
    "quoteVi": "“Nghệ nhân Rơ Châm Mân với 16 năm tuổi nghề, nhiệt huyết trong việc hướng dẫn thế hệ trẻ và thực hành kỹ thuật luồn thoi dệt hoa văn tinh xảo...”",
    "quoteEn": "“Preserving the authentic spirit of Jrai indigenous weaving through every craft generation.”",
    "bioVi": "Nghệ nhân Rơ Châm Mân với 16 năm tuổi nghề, nhiệt huyết trong việc hướng dẫn thế hệ trẻ và thực hành kỹ thuật luồn thoi dệt hoa văn tinh xảo.",
    "bioEn": "Nghệ nhân Rơ Châm Mân với 16 năm tuổi nghề, nhiệt huyết trong việc hướng dẫn thế hệ trẻ và thực hành kỹ thuật luồn thoi dệt hoa văn tinh xảo.",
    "productIds": [
      "T001",
      "V004"
    ],
    "zaloPhone": "0383451929",
    "facebookPageId": "100090304682611"
  }
];
