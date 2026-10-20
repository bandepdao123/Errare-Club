# Errare Club — Media System

Phiên bản workspace: 0.2.0 · Ngày: 2026-10-20 · Thị trường: Mỹ. Contract media giữ phiên bản 0.1.4.

Hệ thống sáng tạo từ sản phẩm hoặc media tham khảo, sản xuất nội dung và quản lý kênh social. Kho Drive được chủ dự án cung cấp là hồ sơ sản phẩm chính theo [PRODUCT-SOURCES](01-Brand/PRODUCT-SOURCES.md); website bổ sung thông tin đã công bố để tham chiếu sáng tạo. Đích là tăng khả năng lan truyền và dẫn traffic về website; không cam kết viral. Đọc [phạm vi hiện hành](07-Operations/SCOPE.md) trước: ưu tiên Instagram/Reels, Facebook/Reels, Threads; được xây dựng lại hệ nhân vật; chủ dự án duyệt trước khi đăng.

**Trạng thái:** đã triển khai bảy skill project-local, helper định tuyến/lookup và kiểm thử. Đã nhập thử hồ sơ/ảnh BFF-N01 và ROM-14, tạo hai production thử bằng ImageGen; chưa sync toàn catalog. Chưa có adapter tự động tạo/đăng, account kết nối hoặc bài đăng thật. Hồ sơ thử và media nằm ngoài Git làm việc, được đóng gói riêng cho lần bàn giao; không coi seed là catalog live.

**Chuyển AI / máy khác:** bắt đầu từ [HANDOFF.md](HANDOFF.md), kiểm [manifest bàn giao](handoff/CONTENTS.json), rồi mở đúng SUMMARY của tác vụ. Chuẩn Instagram: [INSTAGRAM-MEDIA.md](00-Standards/INSTAGRAM-MEDIA.md).

## Đọc theo nhu cầu

- Hiểu cấu trúc và lý do chọn: [SYSTEM.md](SYSTEM.md).
- Hiểu thương hiệu: [BRAND.md](01-Brand/BRAND.md); nhập tham chiếu từ [website](01-Brand/WEBSITE-REFERENCE.md).
- Chọn đầu vào từ sản phẩm/reference/hybrid: [INTAKE.md](02-Research/INTAKE.md).
- Nghiên cứu đối thủ khi cần: [SOCIAL-RESEARCH.md](02-Research/SOCIAL-RESEARCH.md).
- Chuẩn toàn dự án: [audience Mỹ](00-Standards/US-AUDIENCE.md), [visual điện thoại/cặp frame](00-Standards/PHONE-MEDIA.md); ảnh tạo/sửa bằng Codex ImageGen.
- Hai gói đầu ra: post ảnh thực + caption; video gồm một frame-pair prompt cho first/last + video prompt + caption. Chuẩn chung: [media contract](00-Standards/media-contract.json), [caption](00-Standards/CAPTION.md).
- Skill đã triển khai và cách đọc dữ liệu tiết kiệm context: [SKILLS.md](07-Operations/SKILLS.md), [SOURCE-ROUTING.md](00-Standards/SOURCE-ROUTING.md).
- Lõi media theo cách Nature-Studio: [production guide và templates](04-Productions/README.md), [output contract](04-Productions/OUTPUT-CONTRACT.md).
- Làm một nội dung từ đầu đến cuối: [workflow](00-Standards/workflow.md).
- Duyệt chất lượng: [quality](00-Standards/quality.md).
- Nắm quan hệ dữ liệu/trạng thái: [contracts](00-Standards/contracts.md).
- Lập kênh và chuẩn bị đăng: [distribution](05-Distribution/README.md).
- Đo hiệu quả và rút kinh nghiệm: [measurement](06-Insights/MEASUREMENT.md).
- Kế hoạch triển khai: [roadmap](07-Operations/ROADMAP.md).
- Căn cứ Nature-Studio: [nghiên cứu](02-Research/NATURE-STUDIO.md), [nguồn](02-Research/SOURCES.md).
- Kết quả QA và giới hạn: [QA.md](08-Evaluation/QA.md).

Kiểm tính toàn vẹn tài liệu và dữ liệu nền, không gọi dịch vụ ngoài:

```text
python -X utf8 scripts/validate_structure.py
```

Tra nguồn/task và kiểm helper offline:

```text
python -X utf8 scripts/skill_context.py route er-video --task prompts --mode product
python -X utf8 scripts/skill_context.py find --kind product --query "home"
python -X utf8 -m unittest discover -s scripts/tests -p test_skill_context.py -v
```

Ví dụ gọi skill: `$er-video` để soạn gói prompt, `$er-taoanh` khi thực sự muốn tạo/sửa ảnh. Skill không tự cung cấp account, dữ liệu hoặc ngân sách chưa được cấp.

Workspace mới tại thời điểm khảo sát trống. Các đường dẫn content/art/... trong Errare World là tham chiếu của hệ thống cũ, chưa có tại đây; đã đọc được trang chủ errareclub.com, chưa đồng bộ toàn catalog hoặc kiểm ảnh V1. Không dựng file media rỗng để thay tài sản thiếu.
