# Skill Errare Club đã triển khai — workspace 0.2.0

Đã tạo bảy skill project-local trong .agents/skills, tên bắt đầu er- theo yêu cầu người dùng; có SKILL.md và metadata UI. Đây là các workflow hướng dẫn, không phải adapter render/publish tự động. Chưa sync catalog, tạo media, kết nối account hoặc đăng bài trong lần triển khai skill này. Media contract giữ phiên bản 0.1.4.

| Skill | Một nhiệm vụ chính | Nguồn phải tham chiếu | Đầu ra |
|---|---|---|---|
| [er-sanpham](../.agents/skills/er-sanpham/SKILL.md) | Tra full hồ sơ đúng sản phẩm trong Drive, nhập/cập nhật ảnh local; website bổ sung | PRODUCT-SOURCES + source config + snapshot/asset record | Thông tin có thực của SKU kèm nguồn/phiên bản/phần thiếu; ảnh nhập có local file/hash, URL-only chưa đủ nhập ảnh |
| [er-nghiencuu](../.agents/skills/er-nghiencuu/SKILL.md) | Phân tích media tham khảo | SOCIAL-RESEARCH + watchlist/media thật/coverage | Reference analysis, cơ chế giả thuyết, opportunity; không tự render |
| [er-taoanh](../.agents/skills/er-taoanh/SKILL.md) | Tạo/sửa post ảnh hoặc cặp frame qua Codex ImageGen | Intake + image/frame-pair contract + source/persona/asset + US/phone/QA + caption/target profiles khi làm post | Post: ảnh thật đủ target + caption; cặp frame: hai file first t0/last tT dùng shared prompt, giữ role/continuity |
| [er-video](../.agents/skills/er-video/SKILL.md) | Làm gói prompt video từ product/reference/hybrid | Intake + frame-pair/video contract + duration/source/persona + US/phone + capability + caption | FRAME PAIR PROMPT + VIDEO PROMPT + caption; không tự render |
| [er-kiemmedia](../.agents/skills/er-kiemmedia/SKILL.md) | Chấm đúng package/artifact | Contract/checklist + phiên bản nguồn/đầu ra | Findings và QA theo coverage; prompt pass không là render pass |
| [er-dongmedia](../.agents/skills/er-dongmedia/SKILL.md) | Tổng kết/lưu trạng thái và bài học | Content/attempt/summary/feedback/lesson đúng scope | Summary đủ tiếp tục, candidate có evidence; không tự duyệt/đăng |
| [er-quanlykenh](../.agents/skills/er-quanlykenh/SKILL.md) | Quản lý lịch, gói duyệt, bài đã đăng và báo cáo social | Distribution + account/profile + release/approval/metric | Lịch/gói đăng/receipt và quyết định vận hành; chỉ đăng sau duyệt |

Cả bảy skill đã có. Quản lý kênh có thể chuẩn bị kế hoạch local ngay, thao tác account thật vẫn cần quyền và dữ liệu. Automatic discovery giữ mặc định; có thể gọi rõ `$er-video`, `$er-taoanh`... Tên skill không phải cam kết có menu slash riêng. Không cần cài bản trùng vào global user skills.

Registry [skills.json](../00-Standards/skills.json) là nguồn task/routes/data-root; helper [skill_context.py](../scripts/skill_context.py) chỉ định tuyến và trả metadata, không thực thi tạo/đăng. Ví dụ:

```text
python -X utf8 scripts/skill_context.py route er-video --task prompts --mode product
python -X utf8 scripts/skill_context.py route er-video --task caption
python -X utf8 scripts/skill_context.py find --kind product --query "home" --limit 10 --offset 0
```

## Giảm chồng chéo

- Một skill er-taoanh dùng ImageGen tích hợp Codex cho post/cặp frame; không thêm skill postanh trùng vai trò hoặc tự chuyển provider ảnh khác.
- Không cần taovideo trong bộ lõi: đầu ra video là prompt package. Nếu được giao tạo cặp frame thật thì er-taoanh dùng shared frame pair prompt và kiểm đủ hai file riêng, không nhận đủ chỉ từ prompt. Render video thật vẫn là tác vụ bổ sung có quyền/budget.
- Persona là record/workflow dùng chung, có thể xây mới trong bước chuẩn bị brief rồi tái dùng; chưa cần skill nhân vật riêng cho đến khi việc quản lý roster/Soul lặp lại đủ nhiều.
- Caption/revision/export là nhánh trong hai skill sản xuất. Không tạo một skill caption tách biệt rồi nạp lại toàn concept/dữ liệu.
- Campaign và skill không tách theo từng Table hoặc nền tảng; khác biệt nằm ở record/profile, giữ cùng production core.

## Contract bắt buộc của mọi skill

Tuân thủ [SOURCE-ROUTING](../00-Standards/SOURCE-ROUTING.md): tra descriptor → mở đúng nguồn → xử lý → ghi refs/version/evidence. SKILL.md không chép toàn brand, product catalog, caption rule hoặc kích thước nền tảng. Chỉ tải đủ nguồn có liên quan; không bỏ dependency bắt buộc để giảm token.

Test routing phải có: product không reference; reference/hybrid; caption-only; ảnh thêm size không viết lại chuyện; video đủ shared frame pair prompt/video prompt/caption nhưng không render; t_end khớp duration 8/10/15s và thời lượng khác; ảnh pair thiếu/ghép không được complete; phone camera mặc định, cinematic cần yêu cầu; toàn creative native Mỹ; tạo ảnh chỉ Codex ImageGen; thiếu nguồn không bịa; QA không tự duyệt đăng. Khi triển khai phải test hành vi skill thật, không lấy validator cấu trúc hiện có thay eval tác vụ.
