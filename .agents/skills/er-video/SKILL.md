---
name: er-video
description: Write or revise Errare Club video prompt packages from products, reference media or both. Deliver one shared first and last frame image prompt, a video prompt and a US-native caption. This workflow does not render images or video.
---

# ER · Gói prompt video

## Nguồn và task

Root là ba cấp trên thư mục skill. Chạy `python -X utf8 scripts/skill_context.py route er-video --task prompts --mode product`.

Task: prompts / revision / caption. Mode: product / reference / hybrid. Tra product/reference/persona/production/lesson descriptors rồi mở gốc. Fallback: [SOURCE-ROUTING](../../../00-Standards/SOURCE-ROUTING.md), [INTAKE](../../../02-Research/INTAKE.md) và mục video của [OUTPUT-CONTRACT](../../../04-Productions/OUTPUT-CONTRACT.md) cùng guide được dẫn.

## Thực hiện

- `prompts`/`revision` tham chiếu [INSTAGRAM-MEDIA](../../../00-Standards/INSTAGRAM-MEDIA.md) cho placement/canvas/fps đích và [PHONE-MEDIA](../../../00-Standards/PHONE-MEDIA.md) cho hành vi/biểu cảm/người cầm máy/bối cảnh. Ghi một đoạn quan sát gọn trong brief; shared frame prompt và video prompt dùng cùng canvas/plan. Caption-only giữ nguyên plan, không đọc lại mọi chuẩn.
- Resolve brief và concept đã chọn. Với dữ liệu sản phẩm website, mở snapshot và ảnh local theo asset ID/version/hash làm căn cứ mô tả áo/placement, không suy từ tên/alt text. Thiếu ảnh thì hoàn thành nhập tham chiếu theo WEBSITE-REFERENCE khi được giao hoặc giữ draft/unknown đúng phần; không tự nhận artwork đã được kiểm. Product phát triển chuyện gốc từ câu áo/collection, không bắt có đối thủ. Reference học cơ chế có coverage, hybrid kết hợp nguồn.
- Chốt duration/frame plan theo contract trước khi gọi gói cuối complete; thiếu thời lượng được draft với T pending, không tự mặc định 10s. Giữ identity/artwork/không gian và camera operator khả thi.
- Viết một FRAME PAIR PROMPT yêu cầu hai file riêng đúng first/last/shared continuity, một VIDEO PROMPT nối anchor tới hết thời lượng và CAPTION. Dùng chuẩn audience/phone/caption chung, không chép quy tắc vào skill.
- Nếu model/interface đích chưa biết, ghi assumption/capability chưa kiểm trong hồ sơ. Không bịa đã bind hai ảnh vào model hoặc đã render. Chỉ mở profile liên quan khi cần feasibility.
- `caption` chỉ sửa caption từ cảnh đã chốt; `revision` giữ Content ID/ý định và phần không được giao đổi. Lưu output/inputs/version, tạo attempt phù hợp, không ghi đè lịch sử.

Trả đúng ba mục theo contract, prompt/copy Anh Mỹ. Ghi chú/nguồn/coverage nội bộ lưu gọn. Không gọi tạo ảnh/video hoặc đăng từ yêu cầu prompt package; sinh cặp frame thật là tác vụ tạo ảnh riêng khi đã được giao.
