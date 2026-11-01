/**
 * DỰ ÁN SVTHM2026: GIỮ MỘT NGHỀ - DỆT NÊN TƯƠNG LAI
 * MAIN JAVASCRIPT CONTROLLER (CẬP NHẬT LUỒNG TRUNG GIAN BÁN & SINH QR IN TEM)
 */

document.addEventListener('DOMContentLoaded', () => {
  initLanguageSwitcher();
  initMobileMenu();
  initModals();
  initCounters();
  
  const path = window.location.pathname.toLowerCase();
  
  if (path.includes('products.html')) {
    initProductsPage();
  } else if (path.includes('product-detail.html')) {
    initProductDetailPage();
  } else if (path.includes('artisans.html')) {
    initArtisansPage();
  } else if (path.includes('motifs.html')) {
    initMotifsPage();
  } else if (path.includes('traceability.html')) {
    initTraceabilityPage();
  } else {
    initHomePage();
  }
});

/* ==========================================================================
   HERO SLIDER CAROUSEL
   ========================================================================== */
function initHeroSlider() {
  const slider = document.getElementById('hero-slider');
  if (!slider) return;

  const slides = slider.querySelectorAll('.hero-slide');
  const prevBtn = document.getElementById('hero-prev-btn');
  const nextBtn = document.getElementById('hero-next-btn');
  const dotsContainer = document.getElementById('hero-slider-dots');

  if (!slides.length) return;

  let currentIndex = 0;
  let autoTimer = null;

  // Render dots
  if (dotsContainer) {
    dotsContainer.innerHTML = '';
    slides.forEach((_, idx) => {
      const dot = document.createElement('div');
      dot.className = `hero-slider-dot ${idx === 0 ? 'active' : ''}`;
      dot.addEventListener('click', () => goToSlide(idx));
      dotsContainer.appendChild(dot);
    });
  }

  function goToSlide(index) {
    slides[currentIndex].classList.remove('active');
    const dots = dotsContainer ? dotsContainer.querySelectorAll('.hero-slider-dot') : [];
    if (dots[currentIndex]) dots[currentIndex].classList.remove('active');

    currentIndex = (index + slides.length) % slides.length;

    slides[currentIndex].classList.add('active');
    if (dots[currentIndex]) dots[currentIndex].classList.add('active');

    resetAutoPlay();
  }

  function nextSlide() {
    goToSlide(currentIndex + 1);
  }

  function prevSlide() {
    goToSlide(currentIndex - 1);
  }

  function startAutoPlay() {
    stopAutoPlay();
    autoTimer = setInterval(nextSlide, 5000);
  }

  function stopAutoPlay() {
    if (autoTimer) clearInterval(autoTimer);
  }

  function resetAutoPlay() {
    stopAutoPlay();
    startAutoPlay();
  }

  if (nextBtn) nextBtn.addEventListener('click', nextSlide);
  if (prevBtn) prevBtn.addEventListener('click', prevSlide);

  slider.addEventListener('mouseenter', stopAutoPlay);
  slider.addEventListener('mouseleave', startAutoPlay);

  startAutoPlay();
}

/* ==========================================================================
   BỘ ĐẾM SỐ NHẢY DỮ LIỆU (ANIMATED COUNTER)
   ========================================================================== */
function initCounters() {
  const counterEls = document.querySelectorAll('[data-counter]');
  if (!counterEls.length) return;

  const animateElement = (el) => {
    const target = parseInt(el.getAttribute('data-counter'), 10);
    const suffix = el.getAttribute('data-suffix') || '';
    const prefix = el.getAttribute('data-prefix') || '';
    const duration = 1800; // 1.8s
    const startVal = 0;
    const startTime = performance.now();

    function updateCounter(currentTime) {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      // easeOutExpo
      const ease = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
      const current = Math.floor(ease * (target - startVal) + startVal);

      el.textContent = `${prefix}${current}${suffix}`;

      if (progress < 1) {
        requestAnimationFrame(updateCounter);
      } else {
        el.textContent = `${prefix}${target}${suffix}`;
      }
    }
    requestAnimationFrame(updateCounter);
  };

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateElement(entry.target);
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    counterEls.forEach(el => observer.observe(el));
  } else {
    counterEls.forEach(el => animateElement(el));
  }
}

/* ==========================================================================
   3. TRANG CHỦ (INDEX.HTML)
   ========================================================================== */
function initHomePage() {
  renderFeaturedProducts();
  renderTeaserMotifs();
  renderTeaserArtisans();
  initHeroSlider();
  initCounters();
}

/* ==========================================================================
   1. ĐA NGÔN NGỮ (VI / EN)
   ========================================================================== */
function initLanguageSwitcher() {
  const langBtn = document.getElementById('lang-toggle-btn');
  const savedLang = localStorage.getItem('site_lang') || 'vi';
  setLanguage(savedLang);

  if (langBtn) {
    langBtn.addEventListener('click', () => {
      const currentLang = document.body.classList.contains('lang-en') ? 'en' : 'vi';
      const newLang = currentLang === 'vi' ? 'en' : 'vi';
      setLanguage(newLang);
    });
  }
}

function setLanguage(lang) {
  if (lang === 'en') {
    document.body.classList.remove('lang-vi');
    document.body.classList.add('lang-en');
    localStorage.setItem('site_lang', 'en');
  } else {
    document.body.classList.remove('lang-en');
    document.body.classList.add('lang-vi');
    localStorage.setItem('site_lang', 'vi');
  }
}

/* ==========================================================================
   2. MOBILE TOGGLE MENU
   ========================================================================== */
function initMobileMenu() {
  const toggleBtn = document.getElementById('mobile-toggle');
  const mainNav = document.getElementById('main-nav');

  if (toggleBtn && mainNav) {
    toggleBtn.addEventListener('click', () => {
      mainNav.classList.toggle('open');
    });

    mainNav.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        mainNav.classList.remove('open');
      });
    });
  }
}

/* ==========================================================================
   3. TRANG CHỦ (INDEX.HTML)
   ========================================================================== */
function initHomePage() {
  renderFeaturedProducts();
  renderTeaserMotifs();
  renderTeaserArtisans();
}

function renderFeaturedProducts() {
  const container = document.getElementById('featured-products-grid');
  if (!container || typeof PRODUCTS_DATA === 'undefined') return;
  const featured = PRODUCTS_DATA.filter(p => p.featured).slice(0, 4);
  container.innerHTML = featured.map(p => createProductCardHTML(p)).join('');
}

function renderTeaserMotifs() {
  const container = document.getElementById('teaser-motifs-grid');
  if (!container || typeof MOTIFS_DATA === 'undefined') return;
  const sample = MOTIFS_DATA.slice(0, 3);
  container.innerHTML = sample.map(m => createMotifCardHTML(m)).join('');
}

function renderTeaserArtisans() {
  const container = document.getElementById('teaser-artisans-grid');
  if (!container || typeof ARTISANS_DATA === 'undefined') return;
  const sample = ARTISANS_DATA.slice(0, 3);
  container.innerHTML = sample.map(a => createArtisanCardHTML(a)).join('');
}

/* ==========================================================================
   4. TRANG SẢN PHẨM (PRODUCTS.HTML)
   ========================================================================== */
function initProductsPage() {
  const grid = document.getElementById('all-products-grid');
  const filterBtns = document.querySelectorAll('.category-filter-btn');
  const searchInput = document.getElementById('product-search-input');

  if (!grid || typeof PRODUCTS_DATA === 'undefined') return;

  const urlParams = new URLSearchParams(window.location.search);
  const initialCategory = urlParams.get('cat') || 'all';
  const filterArtisan = urlParams.get('artisan');

  function render(filter = 'all', searchQuery = '') {
    let list = PRODUCTS_DATA;
    if (filterArtisan) {
      list = list.filter(p => p.artisanId === filterArtisan);
    }
    if (filter !== 'all') {
      list = list.filter(p => p.category === filter);
    }
    if (searchQuery.trim() !== '') {
      const q = searchQuery.toLowerCase().trim();
      list = list.filter(p => 
        p.nameVi.toLowerCase().includes(q) || 
        p.nameEn.toLowerCase().includes(q) ||
        p.id.toLowerCase().includes(q) ||
        p.artisanName.toLowerCase().includes(q) ||
        (p.motifUsed && p.motifUsed.toLowerCase().includes(q))
      );
    }

    if (list.length === 0) {
      grid.innerHTML = `
        <div style="grid-column: 1/-1; text-align: center; padding: 60px 20px;">
          <h3 style="font-size: 1.3rem; margin-bottom: 8px;">Không tìm thấy sản phẩm phù hợp</h3>
          <p style="color: var(--color-text-muted);">Vui lòng thử lại với danh mục hoặc từ khóa khác.</p>
          ${filterArtisan ? `<a href="products.html" class="btn btn-sm btn-outline-dark" style="margin-top: 15px;">Xóa bộ lọc nghệ nhân</a>` : ''}
        </div>
      `;
      return;
    }

    let artisanBanner = '';
    if (filterArtisan && list.length > 0) {
      const artName = list[0].artisanName;
      artisanBanner = `
        <div style="grid-column: 1/-1; background: #FAF6F0; border: 1.5px solid var(--color-forest-gold); border-radius: var(--radius-md); padding: 12px 20px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
          <div>
            <strong>Đang hiển thị tác phẩm của:</strong> <span style="color: var(--color-bazan-red); font-weight: 800;">${artName}</span> (${list.length} sản phẩm)
          </div>
          <a href="products.html" style="font-size: 0.85rem; color: #78350F; text-decoration: underline; font-weight: 700;">✕ Xem tất cả sản phẩm</a>
        </div>
      `;
    }

    grid.innerHTML = artisanBanner + list.map(p => createProductCardHTML(p)).join('');
  }

  filterBtns.forEach(btn => {
    if (btn.dataset.filter === initialCategory) {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    }

    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      render(btn.dataset.filter, searchInput ? searchInput.value : '');
    });
  });

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      const activeFilter = document.querySelector('.category-filter-btn.active')?.dataset.filter || 'all';
      render(activeFilter, e.target.value);
    });
  }

  render(initialCategory);
}

/* ==========================================================================
   5. TRANG CHI TIẾT SẢN PHẨM (PRODUCT-DETAIL.HTML)
   - ĐÂY LÀ TRANG MÀ CAMERA ĐIỆN THOẠI QUÉT QR SẼ TRỎ THẲNG VÀO
   ========================================================================== */
function initProductDetailPage() {
  const container = document.getElementById('product-detail-container');
  if (!container || typeof PRODUCTS_DATA === 'undefined') return;

  const urlParams = new URLSearchParams(window.location.search);
  const productId = urlParams.get('id') || 'V001';

  const product = PRODUCTS_DATA.find(p => p.id === productId || p.code === productId || p.slugId === productId) || PRODUCTS_DATA[0];
  const artisan = typeof ARTISANS_DATA !== 'undefined' ? ARTISANS_DATA.find(a => a.id === product.artisanId) : null;
  const motif = typeof MOTIFS_DATA !== 'undefined' ? MOTIFS_DATA.find(m => m.id === product.motifId) : null;

  // Lấy danh sách sản phẩm liên quan cùng nghệ nhân hoặc cùng category
  const related = PRODUCTS_DATA.filter(p => p.id !== product.id && (p.artisanId === product.artisanId || p.category === product.category)).slice(0, 3);

  const fullUrl = window.location.href;
  const qrImageSrc = `https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=${encodeURIComponent(fullUrl)}&margin=6`;

  // Soạn tin nhắn kết nối đặt dệt qua Zalo (vai trò trung gian)
  const zaloMessage = encodeURIComponent(`Xin chào CLB Dệt Ia Mơ Nông, tôi muốn kết nối đặt dệt tác phẩm: ${product.nameVi} (Mã số: ${product.id})`);
  const zaloUrl = `https://zalo.me/0383451929?text=${zaloMessage}`;
  const messUrl = `https://m.me/100090304682611`;

  container.innerHTML = `
    <div style="background: #FFFFFF; border-radius: var(--radius-xl); border: 1px solid var(--color-cotton-border); overflow: hidden; box-shadow: 0 10px 35px rgba(60, 45, 30, 0.08); color: #1F1D1B;">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 40px; padding: 40px;">
        <!-- Cột ảnh sản phẩm + Tem QR -->
        <div>
          <div style="border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-subtle); aspect-ratio: 4/3; margin-bottom: 20px;">
            <img src="${product.image}" alt="${product.nameVi}" style="width: 100%; height: 100%; object-fit: cover;">
          </div>

          <!-- Khung tem mác QR in ấn -->
          <div style="background: #FAF6F0; border: 2px dashed #D8CABE; border-radius: var(--radius-md); padding: 20px; text-align: center;">
            <div style="font-size: 0.72rem; font-weight: 800; color: #B45309; text-transform: uppercase;">MÃ QR TEM MÁC ĐỊNH DANH ĐỘC BẢN</div>
            <div style="font-size: 0.95rem; font-weight: 800; color: #1F1D1B; margin: 4px 0 10px;">${product.id}</div>
            
            <div style="width: 170px; height: 170px; margin: 0 auto 12px; background: #fff; padding: 8px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
              <img src="${qrImageSrc}" alt="QR ${product.id}" style="width: 100%; height: 100%; object-fit: contain;">
            </div>

            <p style="font-size: 0.76rem; color: #5D554D; margin-bottom: 12px;">
              Dùng camera điện thoại quét mã này để mở đúng trang thông tin xác thực.
            </p>

            <button class="btn btn-sm btn-outline-dark" onclick="window.print()">
              🖨️ In tem mác bày bán sản phẩm
            </button>
          </div>
        </div>

        <!-- Cột thông tin chi tiết & Mua hàng qua Zalo/Mess -->
        <div>
          <span style="display: inline-block; background: rgba(168,40,43,0.1); color: var(--color-bazan-red); font-size: 0.76rem; font-weight: 800; padding: 4px 12px; border-radius: var(--radius-full); margin-bottom: 10px; border: 1px solid rgba(168,40,43,0.25);">
            ${product.categoryNameVi} • SỐ HIỆU: ${product.id}
          </span>

          <h1 style="font-size: 1.8rem; font-weight: 900; color: #1F1D1B; margin-bottom: 8px;">
            ${product.nameVi}
          </h1>

          <div style="font-size: 1.65rem; font-weight: 900; color: var(--color-bazan-red); margin-bottom: 10px;">
            ${product.priceFormatted}
          </div>

          <div style="margin-bottom: 22px;">
            <div class="product-intermediary-badge" style="font-size: 0.88rem; padding: 7px 16px; border-radius: 8px;">
              🌿 Giá niêm yết từ nghệ nhân buôn làng • Đặt dệt trực tiếp không qua trung gian ép giá
            </div>
          </div>

          <!-- 2 NÚT KẾT NỐI TRỰC TIẾP QUA ZALO / MESSENGER - KHÔNG RỚT DÒNG, MÀU CAM & VÀNG NỔI BẬT -->
          <div style="display: flex; flex-wrap: wrap; gap: 14px; margin-bottom: 25px; padding-bottom: 25px; border-bottom: 1px solid rgba(229, 138, 31, 0.2);">
            <a href="${zaloUrl}" target="_blank" class="btn btn-zalo" style="flex: 1; min-width: 210px; white-space: nowrap; justify-content: center; padding: 14px 20px;">
              💬 Kết nối đặt dệt qua Zalo
            </a>
            <a href="${messUrl}" target="_blank" class="btn btn-messenger" style="flex: 1; min-width: 210px; white-space: nowrap; justify-content: center; padding: 14px 20px;">
              ⚡ Chat Messenger CLB
            </a>
          </div>

          <!-- Thông tin nghệ nhân dệt ra sản phẩm -->
          <div style="background: #FAF6F0; border: 1px solid #E5DACB; border-radius: var(--radius-md); padding: 18px; margin-bottom: 20px;">
            <div style="font-size: 0.75rem; font-weight: 800; color: #B45309; text-transform: uppercase; margin-bottom: 8px;">NGHỆ NHÂN DỆT TÁC PHẨM NÀY</div>
            <div style="display: flex; gap: 16px; align-items: center;">
              ${artisan && artisan.avatar ? `<a href="artisans.html?artisan=${product.artisanId}"><img src="${artisan.avatar}" alt="${artisan.name}" style="width: 65px; height: 65px; object-fit: cover; border-radius: 50%; border: 2px solid var(--color-forest-gold); flex-shrink: 0;"></a>` : ''}
              <div>
                <div style="font-size: 1.1rem; font-weight: 800; color: var(--color-bazan-red); margin-bottom: 4px;">
                  <a href="artisans.html?artisan=${product.artisanId}" style="color: var(--color-bazan-red); text-decoration: underline;">
                    ${product.artisanName}
                  </a>
                </div>
                <div style="font-size: 0.82rem; color: #5D554D; margin-bottom: 4px;">
                  📍 ${product.artisanVillage} • ⏱️ <strong>${product.weavingHours}</strong>
                </div>
                <p style="font-size: 0.85rem; color: #5D554D; font-style: italic; margin: 0;">
                  ${artisan ? artisan.quoteVi : 'Mỗi nếp dệt là một câu chuyện tình yêu đại ngàn.'}
                </p>
              </div>
            </div>
          </div>

          <!-- Hoa văn tích hợp link sang Ngân hàng hoa văn (khớp hoàn toàn với sản phẩm) -->
          <div style="background: #FAF6F0; border: 1px solid #E5DACB; border-radius: var(--radius-md); padding: 18px; margin-bottom: 20px;">
            <div style="font-size: 0.75rem; font-weight: 800; color: #B45309; text-transform: uppercase; margin-bottom: 8px;">HOA VĂN DI SẢN TRÊN SẢN PHẨM</div>
            <div style="display: flex; gap: 16px; align-items: center;">
              ${motif && motif.image ? `<a href="motifs.html?motif=${product.motifId}"><img src="${motif.image}" alt="${motif.nameVi}" style="width: 70px; height: 70px; object-fit: contain; background: #FFFFFF; border: 1px solid #E5DACB; border-radius: 8px; padding: 4px; flex-shrink: 0;"></a>` : ''}
              <div>
                <div style="font-size: 1.05rem; font-weight: 800; color: var(--color-bazan-red); margin-bottom: 4px;">
                  <a href="motifs.html?motif=${product.motifId}" style="color: var(--color-bazan-red); text-decoration: underline;">
                    ${product.motifUsed}
                  </a>
                </div>
                <p style="font-size: 0.85rem; color: #5D554D; margin: 0; line-height: 1.5;">
                  ${motif ? motif.meaningVi : 'Hoa văn mang biểu tượng phồn vinh và linh thiêng của cộng đồng Jrai.'}
                </p>
              </div>
            </div>
          </div>

          <!-- Chi tiết kỹ thuật & Tác động xã hội -->
          <ul style="font-size: 0.88rem; color: #3A332C; line-height: 1.8; margin-bottom: 20px;">
            <li><strong>Kích thước:</strong> ${product.dimensions}</li>
            <li><strong>Chất liệu:</strong> ${product.materialVi}</li>
            <li><strong>Tác động sinh kế:</strong> ${product.impactVi}</li>
          </ul>
        </div>
      </div>

      <!-- PHẦN 2: HỒ SƠ CÂU CHUYỆN SẢN PHẨM — LỜI KỂ TỪ ĐẠI NGÀN (SERIES THỔ CẨM) -->
      <div class="product-story-section">
        <div style="max-width: 900px; margin: 0 auto;">
          <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin-bottom: 12px;">
            <span style="background: rgba(217, 119, 6, 0.15); color: #B45309; font-size: 0.78rem; font-weight: 800; padding: 5px 14px; border-radius: var(--radius-full); text-transform: uppercase; letter-spacing: 0.5px;">
              📖 HỒ SƠ CÂU CHUYỆN SẢN PHẨM • BẢN SẮC JRAI
            </span>
            <span style="font-size: 0.82rem; color: #8C827A; font-weight: 600;">
              📍 Di sản Ia Mơ Nông, Chư Păh, Gia Lai
            </span>
          </div>

          <h2 style="font-size: 1.65rem; font-weight: 900; color: #1F1D1B; margin-bottom: 16px; line-height: 1.35;">
            ${product.storyTitle || 'Những Đường Nét Kể Chuyện Đại Ngàn'}
          </h2>

          ${product.storyLead ? `
            <div class="product-story-lead-quote">
              <p style="font-size: 1.05rem; font-weight: 600; color: var(--color-bazan-red); font-style: italic; line-height: 1.65; margin: 0;">
                “${product.storyLead}”
              </p>
            </div>
          ` : ''}

          <div style="font-size: 0.98rem; color: #3A332C; line-height: 1.85;">
            ${product.storyParagraphs && product.storyParagraphs.length ? 
              product.storyParagraphs.map(p => {
                if (p.endsWith(':') || (p.length < 75 && !p.endsWith('.') && !p.startsWith('“'))) {
                  return `<div class="product-story-subheading">${p}</div>`;
                }
                return `<p class="product-story-paragraph">${p}</p>`;
              }).join('') 
              : `<p class="product-story-paragraph">${product.storyVi}</p>`}
          </div>

          <div style="background: rgba(168, 40, 43, 0.05); border: 1px dashed rgba(168, 40, 43, 0.35); border-radius: 12px; padding: 20px 24px; margin-top: 30px; display: flex; gap: 16px; align-items: center;">
            <div style="font-size: 2.2rem; flex-shrink: 0;">🌿</div>
            <div style="font-size: 0.9rem; color: #5D554D; line-height: 1.65;">
              <strong style="color: var(--color-bazan-red);">Thông điệp bảo tồn di sản:</strong> Chúng tôi tin rằng, bảo tồn văn hóa không có nghĩa là giữ mọi thứ đứng yên trong quá khứ. Đó là hành trình gìn giữ cái gốc văn hóa Jrai, đồng thời tìm kiếm những cách thức phù hợp để di sản tiếp tục đồng hành cùng đời sống hiện đại, tôn trọng tri thức và tiếng nói của chính cộng đồng nghệ nhân.
            </div>
          </div>
        </div>
      </div>

      <!-- PHẦN 3: GIẢI MÃ TRI THỨC HOA VĂN DI SẢN TRÊN TÁC PHẨM (SERIES THỔ CẨM) -->
      <div class="motif-research-section">
        <div style="max-width: 900px; margin: 0 auto;">
          <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px; margin-bottom: 22px;">
            <div>
              <span style="background: rgba(2, 132, 199, 0.12); color: #0284C7; font-size: 0.78rem; font-weight: 800; padding: 5px 14px; border-radius: var(--radius-full); text-transform: uppercase;">
                🔍 GIẢI MÃ HOA VĂN DI SẢN (P'NGA / RÚP)
              </span>
              <h3 style="font-size: 1.45rem; font-weight: 900; color: #1F1D1B; margin: 8px 0 0;">
                ${product.motifUsed}
              </h3>
            </div>
            <a href="motifs.html?motif=${product.motifId}" class="btn btn-sm btn-outline-dark">
              Xem trong Ngân hàng số hoa văn →
            </a>
          </div>

          ${motif && motif.researchOverview ? `
            <div style="font-size: 0.96rem; line-height: 1.75; color: #3A332C; margin-bottom: 22px; background: #F8F5F0; padding: 18px 22px; border-radius: 10px; border-left: 4px solid #0284C7;">
              <strong>Tổng quan di sản:</strong> ${motif.researchOverview}
            </div>
          ` : ''}

          ${motif && motif.researchBullets && motif.researchBullets.length ? `
            <div style="margin-bottom: 25px;">
              <h4 style="font-size: 0.92rem; font-weight: 800; color: #B45309; text-transform: uppercase; margin-bottom: 14px; letter-spacing: 0.5px;">
                CÁC TẦNG Ý NGHĨA BIỂU TRƯNG VĂN HÓA & TÂM LINH (NGHIÊN CỨU THỰC ĐỊA):
              </h4>
              <div style="display: grid; gap: 10px;">
                ${motif.researchBullets.map(b => {
                  const parts = b.split(':');
                  if (parts.length > 1) {
                    return `
                      <div class="motif-bullet-card">
                        <strong style="color: var(--color-bazan-red);">✦ ${parts[0]}:</strong>${parts.slice(1).join(':')}
                      </div>
                    `;
                  }
                  return `
                    <div class="motif-bullet-card">
                      ✦ ${b}
                    </div>
                  `;
                }).join('')}
              </div>
            </div>
          ` : ''}

          <div style="display: flex; flex-wrap: wrap; gap: 16px; background: #FAF6F0; padding: 16px 20px; border-radius: 10px; font-size: 0.88rem; color: #5D554D; border: 1px solid #EBE3DA;">
            <div><strong>Triết lý vũ trụ:</strong> ${motif ? motif.philosophyVi : 'Vạn vật hữu linh (Yang Kơtơp)'}</div>
            <div><strong>Màu sắc truyền thống:</strong> ${motif && motif.colors ? motif.colors.join(', ') : 'Đỏ, Đen, Trắng, Vàng'}</div>
            <div><strong>Nghệ nhân xác minh:</strong> ${motif ? motif.artisanVerification : product.artisanName}</div>
          </div>
        </div>
      </div>
    </div>

    <!-- SẢN PHẨM LIÊN QUAN -->
    <div style="margin-top: 50px;">
      <h3 style="font-size: 1.35rem; font-weight: 800; color: #FFFFFF; margin-bottom: 20px;">
        Sản Phẩm Cùng Nghệ Nhân & Thổ Cẩm Liên Quan
      </h3>
      <div class="products-grid">
        ${related.map(p => createProductCardHTML(p)).join('')}
      </div>
    </div>
  `;
}

/* ==========================================================================
   6. TRANG NGHỆ NHÂN (ARTISANS.HTML)
   ========================================================================== */
function initArtisansPage() {
  const grid = document.getElementById('all-artisans-grid');
  if (!grid || typeof ARTISANS_DATA === 'undefined') return;
  grid.innerHTML = ARTISANS_DATA.map(a => createArtisanCardHTML(a)).join('');

  // Tự động cuộn và làm nổi bật nghệ nhân nếu có tham số URL
  const urlParams = new URLSearchParams(window.location.search);
  const targetArtisan = urlParams.get('artisan') || window.location.hash.replace('#', '');
  if (targetArtisan) {
    setTimeout(() => {
      const el = document.getElementById(targetArtisan);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        el.style.border = '2.5px solid var(--color-forest-gold)';
        el.style.boxShadow = '0 0 35px rgba(217, 119, 6, 0.45)';
      }
    }, 300);
  }
}

function createArtisanCardHTML(a) {
  return `
    <div class="artisan-card" id="${a.id}">
      <div class="artisan-img-wrap">
        <img src="${a.avatar}" alt="${a.name}" loading="lazy">
        <span class="artisan-exp-badge">${a.experienceYears} Năm Giữ Nghề</span>
      </div>
      <div class="artisan-body">
        <h3 class="artisan-name">${a.name}</h3>
        <div class="artisan-village">📍 ${a.village}</div>
        <p class="artisan-quote">${a.quoteVi}</p>
        <p style="font-size: 0.85rem; color: #5D554D; margin-bottom: 15px;">
          <strong style="color: #1F1D1B;">Chuyên môn:</strong> ${a.specialtyVi}
        </p>

        <div style="margin-top: auto; display: flex; gap: 8px;">
          <a href="products.html?artisan=${a.id}" class="btn btn-sm btn-primary" style="flex: 1;">
            Xem tác phẩm dệt (${a.productIds.length})
          </a>
        </div>
      </div>
    </div>
  `;
}

/* ==========================================================================
   7. TRANG NGÂN HÀNG HOA VĂN (MOTIFS.HTML)
   ========================================================================== */
function initMotifsPage() {
  const grid = document.getElementById('all-motifs-grid');
  const filterBtns = document.querySelectorAll('.motif-filter-btn');
  if (!grid || typeof MOTIFS_DATA === 'undefined') return;

  function render(theme = 'all') {
    let list = MOTIFS_DATA;
    if (theme !== 'all') {
      list = list.filter(m => m.theme === theme);
    }
    grid.innerHTML = list.map(m => createMotifCardHTML(m)).join('');

    // Tự động cuộn và làm nổi bật hoa văn nếu có tham số URL
    const urlParams = new URLSearchParams(window.location.search);
    const targetMotif = urlParams.get('motif') || window.location.hash.replace('#', '');
    if (targetMotif) {
      setTimeout(() => {
        const el = document.getElementById(targetMotif);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth', block: 'center' });
          el.style.border = '2.5px solid var(--color-bazan-red)';
          el.style.boxShadow = '0 0 35px rgba(158, 42, 43, 0.45)';
        }
      }, 300);
    }
  }

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      render(btn.dataset.theme);
    });
  });

  render();
}

/* ==========================================================================
   8. TRANG TRA CỨU QR & NGUỒN GỐC (TRACEABILITY.HTML)
   ========================================================================== */
function initTraceabilityPage() {
  const searchInput = document.getElementById('trace-code-input');
  const searchBtn = document.getElementById('trace-search-btn');
  const samplePills = document.querySelectorAll('.sample-pill');
  const resultContainer = document.getElementById('trace-result-container');

  function lookupCode(code) {
    if (!code || !code.trim() || typeof PRODUCTS_DATA === 'undefined') return;
    const cleanCode = code.trim().toUpperCase();
    const product = PRODUCTS_DATA.find(p => 
      p.id.toUpperCase() === cleanCode || 
      (p.code && p.code.toUpperCase() === cleanCode) || 
      (p.slugId && p.slugId.toUpperCase() === cleanCode)
    );

    if (!resultContainer) return;

    if (!product) {
      resultContainer.innerHTML = `
        <div style="background: #fff; border-radius: var(--radius-xl); padding: 50px 30px; text-align: center; border: 1px dashed var(--color-bazan-red); margin-top: 30px;">
          <h3 style="font-size: 1.3rem; margin-bottom: 8px;">Mã số định danh "${cleanCode}" chưa tồn tại</h3>
          <p style="color: var(--color-text-muted);">Vui lòng kiểm tra lại ký tự in trên mác vải hoặc bấm vào mã mẫu.</p>
        </div>
      `;
      return;
    }

    // Chuyển hướng tới trang chi tiết chuẩn xác
    window.location.href = `product-detail.html?id=${product.id}`;
  }

  if (searchBtn && searchInput) {
    searchBtn.addEventListener('click', () => lookupCode(searchInput.value));
    searchInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') lookupCode(searchInput.value);
    });
  }

  samplePills.forEach(pill => {
    pill.addEventListener('click', () => {
      const code = pill.dataset.code;
      if (searchInput) searchInput.value = code;
      lookupCode(code);
    });
  });

  const urlParams = new URLSearchParams(window.location.search);
  const codeParam = urlParams.get('code');
  if (codeParam) {
    lookupCode(codeParam);
  }
}

/* ==========================================================================
   9. CARD HTML & MODAL POPUP HELPERS
   ========================================================================== */
function createProductCardHTML(p) {
  const fullDetailUrl = `product-detail.html?id=${p.id}`;
  const zaloMessage = encodeURIComponent(`Xin chào, tôi muốn kết nối đặt dệt sản phẩm thổ cẩm: ${p.nameVi} (Mã số: ${p.id})`);
  const zaloUrl = `https://zalo.me/0383451929?text=${zaloMessage}`;

    const hoursDisplay = String(p.weavingHours).includes('ngày') || String(p.weavingHours).includes('giờ')
      ? p.weavingHours 
      : `${p.weavingHours}h dệt tay`;

    return `
    <div class="product-card">
      <div class="product-img-wrap">
        <a href="${fullDetailUrl}">
          <img src="${p.image}" alt="${p.nameVi}" class="product-img" loading="lazy">
        </a>
        <span class="product-hours-badge">
          ⏱️ ${hoursDisplay}
        </span>
        <span class="product-qr-badge" onclick="openQRCodeModal('${p.id}')" title="Xem & In tem mã QR">
          QR CODE
        </span>
      </div>
      <div class="product-body">
        <span class="product-category">${p.categoryNameVi}</span>
        <h3 class="product-title">
          <a href="${fullDetailUrl}">${p.nameVi}</a>
        </h3>
        ${p.storyTitle ? `<div style="font-size: 0.78rem; font-weight: 700; color: #B45309; margin: 4px 0 6px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" title="${p.storyTitle}">📖 ${p.storyTitle}</div>` : ''}
        
        <a href="artisans.html?artisan=${p.artisanId}" class="product-artisan-link">
          👤 ${p.artisanName}
        </a>

        <div class="product-footer">
          <div class="product-price-row">
            <span class="product-price" style="font-size: 1.15rem; font-weight: 800; color: var(--color-bazan-red);">${p.priceFormatted}</span>
            <button class="btn-detail" onclick="openQRCodeModal('${p.id}')" title="Mở mã QR tem mác">
              Mã QR
            </button>
          </div>

          <div class="product-actions-row">
            <a href="${fullDetailUrl}" class="btn btn-sm btn-outline-dark" style="flex: 1;">
              Chi tiết
            </a>
            <a href="${zaloUrl}" target="_blank" class="btn btn-sm btn-zalo" style="flex: 1.2;">
              Kết nối Zalo
            </a>
          </div>
        </div>
      </div>
    </div>
  `;
}

function createMotifCardHTML(m) {
  const colorsHTML = m.colors && m.colors.length 
    ? `<div class="motif-colors-pills">${m.colors.map(c => `<span class="motif-color-pill">🎨 ${c}</span>`).join('')}</div>` 
    : '';

  return `
    <div class="motif-card" id="${m.id}">
      <div class="motif-header">
        <img src="${m.image}" alt="${m.nameVi}" loading="lazy">
        <div class="motif-jrai-name">${m.nameJrai}</div>
      </div>
      <div class="motif-body">
        <span class="motif-theme-tag">
          ${m.themeNameVi} • MÃ: ${m.motif_code || m.id}
        </span>
        <h3 class="motif-title">${m.nameVi}</h3>
        ${colorsHTML}
        <p class="motif-meaning">${m.meaningVi}</p>
        <div class="motif-verified">
          <span>✓ Xác minh: ${m.artisanVerification}</span>
        </div>
        <div style="margin-top: 15px; display: flex; gap: 8px; justify-content: space-between;">
          ${m.appliedProducts && m.appliedProducts.length ? `<a href="products.html" class="btn btn-sm btn-primary" style="flex: 1; text-align: center; justify-content: center;">Xem SP (${m.appliedProducts.length})</a>` : ''}
          <button class="btn btn-sm btn-outline-dark" onclick="openMotifModal('${m.id}')" style="flex: 1.3;">
            Xem triết lý & câu chuyện
          </button>
        </div>
      </div>
    </div>
  `;
}

function initModals() {
  const backdrop = document.getElementById('global-modal-backdrop');
  const closeBtn = document.getElementById('modal-close-btn');

  if (backdrop && closeBtn) {
    closeBtn.addEventListener('click', closeModal);
    backdrop.addEventListener('click', (e) => {
      if (e.target === backdrop) closeModal();
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeModal();
    });
  }
}

function closeModal() {
  const backdrop = document.getElementById('global-modal-backdrop');
  if (backdrop) backdrop.classList.remove('open');
}

/* MODAL HIỂN THỊ VÀ IN MÃ QR TEM NHÃN SẢN PHẨM */
window.openQRCodeModal = function(productId) {
  if (typeof PRODUCTS_DATA === 'undefined') return;
  const p = PRODUCTS_DATA.find(item => item.id === productId);
  if (!p) return;

  const content = document.getElementById('modal-dynamic-content');
  const backdrop = document.getElementById('global-modal-backdrop');
  if (!content || !backdrop) return;

  // Link mà camera điện thoại sẽ mở ra khi quét
  const targetUrl = window.location.protocol.startsWith('http') 
    ? new URL(`product-detail.html?id=${p.id}`, window.location.href).href 
    : `product-detail.html?id=${p.id}`;
  const qrUrl = `https://api.qrserver.com/v1/create-qr-code/?size=240x240&data=${encodeURIComponent(targetUrl)}&margin=8`;

  content.innerHTML = `
    <div class="qr-modal-card">
      <span style="font-size: 0.75rem; font-weight: 800; color: var(--color-forest-gold); text-transform: uppercase;">
        DỆT NÊN TƯƠNG LAI — TEM MÁC ĐỊNH DANH ĐỘC BẢN
      </span>
      <h2 style="font-size: 1.4rem; font-weight: 900; color: #FFFFFF; margin: 6px 0 4px;">
        ${p.nameVi}
      </h2>
      <div style="font-size: 0.88rem; font-weight: 800; color: var(--color-amber-glow); margin-bottom: 12px; letter-spacing: 0.5px;">
        MÃ ĐỊNH DANH SẢN PHẨM: ${p.id} • DỆT THỦ CÔNG GIA RAI
      </div>

      <div class="qr-code-canvas-wrap">
        <img src="${qrUrl}" alt="Mã QR ${p.id}">
      </div>

      <p style="font-size: 0.85rem; color: var(--color-text-muted); max-width: 420px; margin: 0 auto 18px;">
        Nghệ nhân: <strong>${p.artisanName}</strong> (${p.artisanVillage})<br>
        Quét camera điện thoại sẽ mở trực tiếp trang thông tin và nút đặt hàng Zalo/Messenger của CLB.
      </p>

      <div style="display: flex; justify-content: center; gap: 12px;">
        <button class="btn btn-primary btn-sm" onclick="window.print()">
          🖨️ In tem mác gắn vào sản phẩm
        </button>
        <a href="${targetUrl}" class="btn btn-outline-dark btn-sm">
          Mở trang chi tiết
        </a>
      </div>
    </div>
  `;

  backdrop.classList.add('open');
};

window.openMotifModal = function(id) {
  if (typeof MOTIFS_DATA === 'undefined') return;
  const m = MOTIFS_DATA.find(item => item.id === id);
  if (!m) return;

  const content = document.getElementById('modal-dynamic-content');
  const backdrop = document.getElementById('global-modal-backdrop');
  if (!content || !backdrop) return;

  // Find applied products for this motif
  const appliedProds = typeof PRODUCTS_DATA !== 'undefined'
    ? PRODUCTS_DATA.filter(p => p.motifId === m.id).slice(0, 10)
    : [];

  const bulletsHTML = m.researchBullets && m.researchBullets.length ? `
    <div style="margin-bottom: 22px;">
      <h4 style="font-size: 0.85rem; font-weight: 800; color: var(--color-amber-glow); text-transform: uppercase; margin-bottom: 12px; letter-spacing: 0.5px;">
        Ý NGHĨA BIỂU TRƯNG & VĂN HÓA BẢN ĐỊA (HỒ SƠ SERIES THỔ CẨM):
      </h4>
      <div style="display: grid; gap: 10px;">
        ${m.researchBullets.map(b => {
          const parts = b.split(':');
          if (parts.length > 1) {
            return `
              <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(229,138,31,0.2); padding: 12px 16px; border-radius: 8px; font-size: 0.88rem; line-height: 1.6; color: #EDE4DB;">
                <strong style="color: var(--color-forest-gold);">✦ ${parts[0]}:</strong>${parts.slice(1).join(':')}
              </div>
            `;
          }
          return `
            <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(229,138,31,0.2); padding: 12px 16px; border-radius: 8px; font-size: 0.88rem; line-height: 1.6; color: #EDE4DB;">
              ✦ ${b}
            </div>
          `;
        }).join('')}
      </div>
    </div>
  ` : '';

  const appliedProdsHTML = appliedProds.length ? `
    <div style="margin-top: 22px; padding-top: 18px; border-top: 1px solid rgba(255,255,255,0.1);">
      <div style="font-size: 0.85rem; font-weight: 800; color: var(--color-forest-gold); text-transform: uppercase; margin-bottom: 10px;">
        TÁC PHẨM ỨNG DỤNG HOA VĂN NÀY (${appliedProds.length}):
      </div>
      <div style="display: flex; flex-wrap: wrap; gap: 10px;">
        ${appliedProds.map(p => `
          <a href="product-detail.html?id=${p.id}" class="motif-applied-pill">
            <span style="font-weight: 800; color: var(--color-amber-glow);">${p.id}</span>
            <span>${p.nameVi}</span>
          </a>
        `).join('')}
      </div>
    </div>
  ` : '';

  content.innerHTML = `
    <div class="motif-modal-research-wrap">
      <div style="display: flex; gap: 24px; align-items: center; margin-bottom: 22px; flex-wrap: wrap;">
        <div style="width: 110px; height: 110px; border-radius: 16px; background: radial-gradient(circle at center, #2c2520 0%, #151210 100%); display: flex; align-items: center; justify-content: center; padding: 12px; border: 2px solid var(--color-forest-gold); flex-shrink: 0;">
          <img src="${m.image}" alt="${m.nameVi}" style="max-width: 100%; max-height: 100%; object-fit: contain;">
        </div>
        <div style="flex: 1;">
          <span style="font-size: 0.75rem; font-weight: 800; color: var(--color-forest-gold); text-transform: uppercase;">
            ${m.themeNameVi} • MÃ: ${m.motif_code || m.id}
          </span>
          <h2 style="font-size: 1.45rem; font-weight: 900; color: #FFFFFF; margin: 4px 0 6px;">
            ${m.nameJrai} — ${m.nameVi}
          </h2>
          <div style="font-size: 0.85rem; color: var(--color-text-muted);">
            📍 ${m.village} • Xác minh: <strong>${m.artisanVerification}</strong>
          </div>
        </div>
      </div>

      ${m.researchOverview ? `
        <div style="background: rgba(2, 132, 199, 0.12); border-left: 3px solid #0284C7; padding: 14px 18px; border-radius: 0 8px 8px 0; margin-bottom: 20px; font-size: 0.92rem; color: #D1E9FA; line-height: 1.7;">
          <strong style="color: #60A5FA;">Tổng quan nghiên cứu:</strong> ${m.researchOverview}
        </div>
      ` : ''}

      ${bulletsHTML}

      <div style="margin-bottom: 20px;">
        <h4 style="font-size: 0.85rem; font-weight: 800; color: var(--color-bazan-red); text-transform: uppercase; margin-bottom: 6px;">
          TRIẾT LÝ NHÂN SINH BẢN ĐỊA & VẠN VẬT HỮU LINH (YANG KƠTƠP)
        </h4>
        <p style="font-size: 0.92rem; color: #EDE4DB; line-height: 1.7;">
          ${m.philosophyVi}
        </p>
      </div>

      <div style="background: var(--color-cotton-surface); padding: 16px 20px; border-radius: var(--radius-md); margin-bottom: 20px; border: 1px solid var(--color-cotton-border); display: grid; gap: 8px;">
        <div style="font-size: 0.88rem; color: #FFFFFF;"><strong>Kỹ thuật dệt:</strong> ${m.technique}</div>
        <div style="font-size: 0.88rem; color: #EDE4DB;"><strong>Màu sắc truyền thống:</strong> ${m.colors ? m.colors.join(', ') : 'Đỏ, Đen, Trắng, Vàng'}</div>
        <div style="font-size: 0.88rem; color: #6EE7B7;"><strong>Chứng nhận nghệ nhân:</strong> ${m.artisanVerification}</div>
      </div>

      ${appliedProdsHTML}

      <div style="display: flex; gap: 12px; margin-top: 25px;">
        <a href="products.html" class="btn btn-primary btn-sm">
          Khám phá tất cả sản phẩm
        </a>
        <button class="btn btn-outline-dark btn-sm" onclick="closeModal()">
          Đóng cửa sổ
        </button>
      </div>
    </div>
  `;

  backdrop.classList.add('open');
};
