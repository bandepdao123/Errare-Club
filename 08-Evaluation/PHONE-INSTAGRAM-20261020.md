# Chuẩn Instagram và quan sát đời sống — 2026-10-20

Phạm vi: cập nhật hướng dẫn/routing, không sản xuất media hoặc tự đổi lịch sử BFF-N01.

- INSTAGRAM-MEDIA.md giữ mặc định kỹ thuật và trạng thái nguồn; PHONE-MEDIA.md giữ hành vi/biểu cảm/bối cảnh/camera tự nhiên, bao phủ post/frame/video.
- er-taoanh và er-video dẫn nguồn chung; 10 visual task routes gồm QA mở nguồn kỹ thuật, caption-only không thêm nguồn đó.
- Brief thêm hai dòng canvas và quan sát gọn; QA dùng review hiện có, không thêm pipeline/skill/agent.
- Helper: 11 tests pass. Skill quick_validate: er-taoanh, er-video valid. Structure: 916 checks, 0 failures.
- Giới hạn: chưa có render theo chuẩn mới, native audience test, profile đường đăng được xác minh hoặc dữ liệu hiệu quả social. Official Help lần đọc trước lỗi/429; production defaults không được ghi official_verified.

Artifact hệ thống đang chọn: INSTAGRAM-MEDIA v1.0 + phần quan sát đời sống trong PHONE-MEDIA; routing skills.json hiện hành. Next: áp vào yêu cầu sản xuất kế tiếp, QA file thật theo brief; kiểm profile placement trước release nếu chưa có. Không có blocker cho việc cập nhật hệ thống.
