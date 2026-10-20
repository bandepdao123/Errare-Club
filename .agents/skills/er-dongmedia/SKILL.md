---
name: er-dongmedia
description: Close or summarize an Errare Club media work session, preserving selected versions, attempts, budget and next steps and proposing evidence-backed lessons. Not a media-generation, approval or publishing command.
---

# ER · Đóng phiên media

## Nguồn

Root là ba cấp trên thư mục skill. Chạy `python -X utf8 scripts/skill_context.py route er-dongmedia`. Tìm đúng Content/attempt/summary/lesson, không nạp toàn history/memory. Fallback: [SOURCE-ROUTING](../../../00-Standards/SOURCE-ROUTING.md), [production guide](../../../04-Productions/README.md), [SUMMARY template](../../../04-Productions/templates/SUMMARY.md), phần vòng học của [MEASUREMENT](../../../06-Insights/MEASUREMENT.md).

## Thực hiện

- Tổng hợp dữ kiện thực: text, artifact review/selection, pair coverage, QA/approval/receipt nếu có, budget settled/reserved/unknown, blocker và next action. Thiếu metrics/media giữ unavailable/pending phù hợp.
- Phân biệt đóng phiên với thay trạng thái tác phẩm. Prompt-only có thể đóng phiên, chưa đăng không cần analytics giả. Không tự chọn master, duyệt, đăng hoặc reset budget/ID.
- Lưu SUMMARY và index cần thiết với liên kết record gốc, giữ attempts/approval lịch sử. Gọi lại cùng dữ liệu cập nhật đúng hồ sơ, không tạo Content hoặc lesson trùng.
- Chỉ tạo candidate khi có hành động tái dùng và evidence, kiểm trùng theo ý nghĩa/điều kiện. Active chỉ theo policy/bằng chứng phù hợp, không biến một lượt đẹp/view cao thành luật audience.

Trả hiện trạng, file đã lưu, việc tiếp theo và phần cần kiểm. Không khởi chạy media/automation hoặc đẩy dữ liệu ngoài.
