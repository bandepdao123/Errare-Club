# Instagram — quy chuẩn sản xuất Errare Club

Version 1.0 · 2026-10-20. Nguồn chung cho skill ảnh, video và QA. Đây là **mặc định sản xuất của dự án**, không là cam kết thuật toán ưu tiên hoặc chứng nhận mọi công cụ đăng hỗ trợ. Đọc đúng placement, không nạp toàn bộ thông số mạng xã hội khác.

## Chọn canvas trước khi viết prompt

| Placement | Tỷ lệ mặc định | File xuất đích | Áp dụng |
|---|---|---|---|
| Feed ảnh đơn / carousel | 3:4 | 1080 × 1440 px | Ưu tiên Instagram; các slide cùng canvas đã chọn |
| Feed bản thay thế | 4:5 | 1080 × 1350 px | Khi brief hoặc đường đăng cần; không tự xuất thêm mọi bài |
| Reels video | 9:16 | 1080 × 1920 px, 30 fps | Mặc định kỹ thuật; thời lượng theo brief, không ép mọi clip cùng độ dài |
| Reels first / last reference | 9:16 | 1080 × 1920 px mỗi ảnh | Cùng canvas với video; hai file riêng theo frame plan |
| Stories ảnh / video | 9:16 | 1080 × 1920 px; video mặc định 30 fps | Chỉ khi được chọn làm đầu ra |

Ảnh vuông 1:1 cũ không tự thành sai hoặc bị ghi đè. Bài mới chỉ có sản phẩm và yêu cầu ảnh: mặc định Feed single 3:4, ghi assumption trong brief. Gói video Instagram mặc định Reels 9:16. Không tự mở rộng thành cả Feed, Story và Reel. Yêu cầu nền tảng khác hoặc target rõ của người dùng ưu tiên hơn mặc định này.

Tỷ lệ là yêu cầu ngay từ prompt, không đợi tới export. Master có thể lớn hơn file đích nhưng cần đủ độ phân giải và bố cục đúng tỷ lệ. Phân biệt requested với actual: đo file tool trả; sai tỷ lệ thì đánh giá crop/reframe hợp lệ, không kéo giãn, không crop mất mặt/câu áo/payoff. Không upscale để nhận đã có chi tiết gốc. Không gọi export_pending là đủ gói.

First/last giữ cùng width/height/aspect và trạng thái t0/tT theo [PHONE-MEDIA](PHONE-MEDIA.md). Profile model không hỗ trợ canvas hoặc cặp anchor thì ghi rõ capability pending; không âm thầm đổi khung hoặc giả đã render.

## Bố cục và file giao

- Mặt, câu áo và hành động cần hiểu phải nằm ở vùng đọc rõ; với Reel/Story tránh sát mép trên/dưới và dải nút bên phải. Không dùng một safe-zone pixel cố định cho mọi giao diện. Cover/Feed/profile preview có thể crop khác; xem preview theo placement khi chuẩn bị release.
- Ưu tiên JPEG chất lượng tốt cho photo export; PNG khi cần. Video mặc định MP4/H.264, âm thanh AAC nếu có; xác minh đường đăng/model thực hỗ trợ trước giao render cuối. Không tự thêm nhạc vào prompt-only.
- Export ghi actual width/height, type, fps/duration nếu là video, asset/hash, master ref và QA cho đúng variant. Không cần sinh thêm ảnh chỉ để có nhiều kích thước.

## Nguồn và xác minh có giới hạn

Các mặc định trên được chủ dự án yêu cầu đưa vào quy chuẩn. Photo 3:4 được thông báo hỗ trợ từ 2025; đọc tham khảo: [thông báo được Social Media Today dẫn lại](https://www.socialmediatoday.com/news/instagram-adds-support-phone-camera-aspect-ratio-images/749205/).

Nguồn chính thức cần kiểm khi chốt capability đường đăng: [photo resolution](https://help.instagram.com/1631821640426723), [Reel size/aspect](https://help.instagram.com/1038071743007909). Lần truy cập 2026-10-20 lỗi/429; không ghi official_verified. 1080p/30 fps là lựa chọn export của dự án, không tuyên bố là mọi giới hạn tối đa/tối thiểu hiện hành.

Không truy cập lại web cho từng prompt khi chỉ áp mặc định dự án. Tái dùng profile đã kiểm cho cùng đường đăng/account/placement; xác minh khi thiếu, có cảnh báo/thay đổi hoặc trước release chưa từng kiểm. Lỗi đọc tài liệu không chặn viết concept/sinh master theo mặc định, nhưng giữ platform verification pending, không tự nhận upload-ready. Không đồng nhất capability app với API/scheduler; không lấy thông số ads làm chứng nhận organic.

## Tối ưu hiệu quả

Tỷ lệ giúp hiển thị, không bảo đảm viral. Thiết kế tình huống/quote có lý do để người xem gửi cho một người cụ thể, hook và payoff rõ. Đánh giá bằng dữ liệu bài thật theo MEASUREMENT, không gắn nhãn winning từ self-review hoặc flag viral trong catalog.
