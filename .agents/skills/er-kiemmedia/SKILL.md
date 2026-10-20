---
name: er-kiemmedia
description: Review an Errare Club prompt package, photo export, frame pair or rendered video against project sources and actual artifact coverage. Use for QA and rechecks, not as user approval or a publishing action.
---

# ER · Kiểm media

## Nguồn và task

Root là ba cấp trên thư mục skill. Chạy `python -X utf8 scripts/skill_context.py route er-kiemmedia --task video-package`.

Task: photo / frames / video-package / video-render / caption. Resolve đúng attempt/artifact/hash và brief, mở nguồn nó tham chiếu. Fallback: [SOURCE-ROUTING](../../../00-Standards/SOURCE-ROUTING.md), [quality](../../../00-Standards/quality.md), đúng package trong [OUTPUT-CONTRACT](../../../04-Productions/OUTPUT-CONTRACT.md).

## Thực hiện

- Chỉ kết luận phần thực tiếp cận: prompt, ảnh, video, audio và metadata có coverage riêng. Không lấy tự chấm/QA cấu trúc/thumbnail thay artifact thật.
- Đối chiếu scene/audience/product/persona với nguồn. Photo kiểm từng export/target; frames kiểm hai file/role/time/continuity; package video kiểm pair prompt/timing/camera/diễn tiến/caption; render kiểm ending/motion/audio trong phạm vi đã xem/nghe.
- Ghi pass/fail/not_checked/not_applicable có lý do theo criterion; evidence/timecode/frame, mức độ, cách sửa và recheck. Caption kiểm giọng/ý nghĩa ngoài đếm hashtag.
- Không có media thì visual/motion/audio tương ứng not_checked. Không fail gói prompt chỉ vì chưa render; thiếu một frame không là pair complete.
- Lưu review riêng gắn artifact/version/hash, recheck đúng phần và phụ thuộc. Không sửa output/kết luận lịch sử để che lỗi; self-review phải ghi đúng, không nhận độc lập.

Trả findings ưu tiên, phần đã/chưa kiểm và next action. QA pass không tự selected/approved/published. Không tạo/sửa media hoặc đăng trừ khi tác vụ đó được giao thêm.
