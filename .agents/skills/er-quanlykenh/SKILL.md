---
name: er-quanlykenh
description: Plan Errare Club social calendars, prepare approval packages, publish specifically approved releases when authorized, or analyze post and channel metrics. Prioritize Instagram, Facebook and Threads. Not competitor research or media generation.
---

# ER · Quản lý kênh

## Nguồn và task

Root là ba cấp trên thư mục skill. Chạy `python -X utf8 scripts/skill_context.py route er-quanlykenh --task plan`.

Task: plan / package / publish / analyze. Chỉ mở account/profile/release/metrics liên quan. Fallback: [SOURCE-ROUTING](../../../00-Standards/SOURCE-ROUTING.md), [Distribution](../../../05-Distribution/README.md); publish đọc [contracts](../../../00-Standards/contracts.md), analyze đọc [MEASUREMENT](../../../06-Insights/MEASUREMENT.md).

## Thực hiện

- Dùng account/owner/quyền thực trong nền tảng vận hành đã chốt. Chưa có account vẫn lập lịch/gói local; không nhận đã kết nối hoặc tự mở account từ tên brand.
- `plan`/`package`: chuẩn bị lịch/target/caption/cover/link/disclosure và artifact version. Prompt video chưa có render không là gói video đăng được. Lưu preview/digest/phạm vi lịch để duyệt; không gửi draft/lịch ngoài từ yêu cầu kế hoạch local.
- `publish`: cần yêu cầu đăng, approval còn hiệu lực cho đúng gói/account/lịch, QA/quyền/target preflight theo contract. Payload đổi phải xét lại duyệt. Thiếu căn cứ thì chuẩn bị gói cụ thể và hỏi đúng phần chặn trước hành động; không suy quyền từ QA pass.
- Qua connector/browser thực có, gửi đúng gói được duyệt, lưu native ID/receipt/URL/visibility thực. Outcome unknown phải reconcile trước retry. Không tự tạo credential/API; thiếu công cụ dùng handoff/manual receipt và giữ trạng thái chưa xác minh nếu cần.
- `analyze`: dùng snapshot có nguồn/tuổi bài/metric definitions, so điều kiện tương thích, giữ null/unknown và attribution grain. Không quy đơn từng post từ bio chung hoặc gọi raw views là nhân quả viral.

Trả lịch/gói/receipt hoặc báo cáo theo task, cùng giới hạn dữ liệu. Không sinh media, tự bật automation hoặc gọi nền tảng khi chỉ test/cập nhật skill.
