---
name: er-taoanh
description: Create or edit Errare Club photo posts or separate first and last frame images with Codex ImageGen. Also handle caption-only or size revisions of an existing photo post. Do not trigger merely for discussing skill design.
---

# ER · Tạo ảnh

## Nguồn và task

Root là ba cấp trên thư mục skill. Chạy tại root:

`python -X utf8 scripts/skill_context.py route er-taoanh --task post --mode product`

Task: post / frames / caption / export / prompts. Mode: product / reference / hybrid. Đọc nguồn helper chọn, không nạp mọi nhánh. Fallback: [SOURCE-ROUTING](../../../00-Standards/SOURCE-ROUTING.md), [media-contract](../../../00-Standards/media-contract.json) và đúng clause của [OUTPUT-CONTRACT](../../../04-Productions/OUTPUT-CONTRACT.md).

## Thực hiện

- Với `post`/`frames`/`prompts`, chốt placement/canvas từ [INSTAGRAM-MEDIA](../../../00-Standards/INSTAGRAM-MEDIA.md) khi đích Instagram, và đoạn quan sát đời sống theo [PHONE-MEDIA](../../../00-Standards/PHONE-MEDIA.md) trong brief hiện có trước viết prompt. `export` chỉ áp đúng target và kiểm file/crop; caption-only không nạp lại chuẩn visual. Không copy chuẩn vào skill/prompt.
- Resolve brief/current attempt và source refs từ metadata; mở ảnh local sản phẩm/persona theo asset ID/version/hash. Nếu tham chiếu sản phẩm chỉ có URL hoặc metadata_only/partial, hoàn thành bước tải/kiểm ảnh theo WEBSITE-REFERENCE trong phạm vi được giao trước khi nhận đủ căn cứ sản xuất. Không dùng thumbnail/alt text thay ảnh thật. Product không chờ reference. Chuẩn bị persona nếu cần, ghi hypothesis; không mặc định roster/Soul legacy.
- `post`: tạo/sửa bằng **image_gen tích hợp Codex** trong quyền/budget đã giao, không chuyển provider/API/CLI. Xem ảnh local trước khi sửa. Lưu actual prompt/input/output/receipt và attempt mới, giữ bản cũ.
- `frames`: dùng shared frame-pair prompt và duration/frame plan đã chốt. Chỉ complete sau khi có hai file first/last riêng được xem/QA; một ảnh hoặc collage giữ partial. Không tự tách thành hai prompt độc lập hay cắt collage giả đủ cặp.
- `caption`/`export`: giữ concept và artifact không được giao đổi. Chỉ mở nguồn ảnh hưởng. Dùng target profile hiện hành; chưa rõ profile/capability thì xác minh hoặc để export_pending, không nhận đủ size.
- `prompts`: chỉ soạn prompt/brief cần thiết, không gọi image_gen. Việc skill được chọn không tự cấp thêm ngân sách.
- QA ảnh/crop/continuity theo chuẩn chung. Nếu công cụ/budget không đủ thì ghi blocker/partial; không hạ chuẩn để gọi hoàn thành.

Giao post: ảnh thật đủ target + caption hoàn chỉnh theo contract. Giao frames: hai file riêng và role/time/hash khi thực có. Prompt-only ghi rõ. Cập nhật summary; không tự duyệt hoặc đăng.
