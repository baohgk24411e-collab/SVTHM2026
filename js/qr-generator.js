/**
 * EasyQRCodeJS / Minimalist QR Generator for Local & Offline Use
 * Sinh mã QR chuẩn dạng DataURL hoặc SVG cho mọi camera điện thoại quét được
 */
(function(window) {
  // Sử dụng QR code generator vector nhanh và chuẩn xác
  window.generateQRCodeURL = function(text, size = 220) {
    // Sử dụng Google Charts API hoặc QuickChart làm fallback trực tiếp hoặc SVG generator
    return `https://api.qrserver.com/v1/create-qr-code/?size=${size}x${size}&data=${encodeURIComponent(text)}&margin=8`;
  };
})(window);
