# Errare Club — bắt đầu trên AI / máy khác

Ngày bàn giao: 2026-10-20. Đọc AGENTS.md → README.md → tài liệu theo SOURCE-ROUTING. Không nạp toàn repo vào context. Đây là hệ thống hướng dẫn + helper filesystem, chưa phải app tự động vận hành kênh.

## Khôi phục

1. Clone repo private bằng tài khoản được cấp quyền; không cần dùng đường dẫn C:/Errare-Club.
2. Dùng Python 3.11+ (helper chỉ cần standard library). Chạy hai lệnh kiểm tra bên dưới.
3. Nếu cần tiếp tục từ ảnh/hồ sơ đã làm, giải nén `handoff/runtime-media-20261020.zip` **vào root repo**. ZIP gồm `.errare/library/`, `.errare/productions/`, `media/` và manifest hash; xem `handoff/CONTENTS.json` để biết coverage. Chạy `python scripts/check_handoff.py` trước giải nén để kiểm tính toàn vẹn. Runtime/media được bàn giao riêng, không đổi chính sách Git ignore của dữ liệu làm việc.
4. Kết nối Google Drive bằng tài khoản có quyền đọc folder trong `01-Brand/product-sources.json`. Quyền và phiên đăng nhập không đi kèm Git. Cache chỉ có SKU đã nhập, không phải full catalog.
5. AI khác đọc các SKILL.md trong `.agents/skills/` như hướng dẫn và tuân thủ routing. Cơ chế tự khám phá skill tùy nền tảng AI. Công cụ và account không được cài bởi việc clone.

```text
python -X utf8 scripts/validate_structure.py
python -X utf8 -m unittest discover -s scripts/tests -p test_skill_context.py
python -X utf8 scripts/skill_context.py find --kind product --query BFF-N01
```

## Trạng thái thực để tiếp tục

- Bảy skill er-* đã triển khai; Drive nguồn chính, website bổ sung. BFF-N01 đã đọc workbook/CSV, tải và xem bốn mockup, có snapshot và asset/hash. Có thêm hồ sơ thử product-rom-14 trong archive, không tự coi là catalog hiện hành.
- BFF-N01: Content `content-497f129e-616e-479b-a374-af9bcd91779e`, attempt `attempt-6941a556-b8b4-48b0-87b7-1d44852a5b16`. Có master, export vuông 1080, caption, prompt và self-review. Là creative draft; chưa xác minh profile đường đăng, chưa duyệt/đăng. Mở SUMMARY của content trước sửa.
- Có một production thử ROM-14 trước đó, giữ review/giới hạn trong SUMMARY; không chọn nhầm làm master BFF-N01.
- Chuẩn mới: INSTAGRAM-MEDIA.md cho kỹ thuật; PHONE-MEDIA.md cho đời sống Mỹ, hành động/biểu cảm tự nhiên, người cầm máy và cặp frame. BFF-N01 tạo trước lần chuẩn hóa mới; chưa có render kiểm theo chuẩn mới. Không tự regenerate từ yêu cầu bàn giao.
- Chưa có watchlist ban đầu, ngân sách tiền cụ thể, account đăng hoặc publisher adapter. Không có bài đăng/analytics để chứng nhận hiệu quả viral.
- Khuyến nghị bước tiếp: nhận tác vụ tiếp theo của chủ dự án; nếu tiếp tục BFF-N01, mở đúng hồ sơ rồi đánh giá/chỉnh theo chuẩn mới và target Feed 3:4. Không coi chuyển máy là quyền render/chi tiền/đăng.

## Tính di động và giới hạn

Repo dùng path tương đối. Hồ sơ lịch sử có thể giữ absolute path máy cũ: khi resolve, ánh xạ prefix `C:/Errare-Club/` hoặc `C:\\Errare-Club\\` sang root checkout mới, giữ hash của file thật. Không dùng đường dẫn `$CODEX_HOME/generated_images` làm bản duy nhất; master đã được copy vào media trong archive. Không ghi đè provenance/lịch sử chỉ để sửa đường dẫn.

Image generation hiện yêu cầu Codex built-in ImageGen. AI/môi trường không có công cụ này vẫn nghiên cứu/soạn prompt/QA phần truy cập được; báo thiếu công cụ khi được giao tạo ảnh, không tự đổi sang provider khác. Video skill hiện soạn gói prompt, không có renderer tự động. First/last chưa được kiểm khả năng trả đủ hai file qua một call. Credential/API key/quyền account/budget phải cấu hình riêng, không có trong bản bàn giao.

Nguồn kỹ thuật Instagram phân biệt mặc định dự án và capability app/API/đường đăng; official Help từng lỗi/429. Không tự ghi official_verified. Kiểm lại trước release khi thiếu profile.

Archive là snapshot tại thời điểm này, không được cập nhật tự động. Dữ liệu sau bàn giao cần backup/commit có chủ đích, không coi ZIP cũ là trạng thái mới nhất. Lịch sử chat không đi kèm repo; HANDOFF + decisions + SUMMARY là điểm tiếp tục.
