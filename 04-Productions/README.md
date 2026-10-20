# Lõi sản xuất media — kế thừa Nature-Studio

Version 0.1.4. Dùng một lõi cho hai đầu vào: [từ sản phẩm hoặc từ reference](../02-Research/INTAKE.md), có thể hybrid. Campaign/series/account là liên kết, không là điều kiện để mở một Content độc lập.

## Tổ chức hồ sơ

Khi có việc sản xuất thật, lưu dưới .errare/productions/<content-id>/:

```text
brief.md                 Ý định đã chốt, Table/cast/product, đầu ra
content.json             Identity và các tham chiếu hiện hành
concept.md               Premise, opening/tension/payoff, cơ chế và giả thuyết
SUMMARY.md               Tóm tắt để tiếp tục ở phiên khác
attempts/<attempt-id>/
  attempt.json           Planned/actual refs, revision scope, receipt/cost refs
  INPUTS.md              Nguồn/version/hash và cách dùng; không sao chép cả kho
  PROMPTS.md             Prompt theo format/shot/slide khi task cần
  SETTINGS.json          Provider/interface/model actual, thông số thật hoặc unknown
  OUTPUT.md              Gói văn bản hiện hành khi có
  outputs/               Media thật hoặc asset refs; chỉ tạo khi thật sự có
reviews/<review-id>.json Artifact hash, checklist, phạm vi xem/nghe, findings
selections/              Quyết định chọn master có hash, lý do và người chọn
releases/<release-id>/   File xuất hoặc asset refs, caption, cover, link, manifest
```

Đây là layout phát sinh theo task, không bắt tạo mọi file/thư mục mỗi lần. OUTPUT.md/PROMPTS.md có thể hợp nhất khi output nhỏ và một file được chọn làm nguồn chính; record trỏ đúng file. Review không tạo attempt/output giả nếu chỉ chấm artifact đã có. Text-only attempt có output_text_ref nhưng không cần render/assets. SETTINGS.json không tự suy seed/model từ prompt.

Mẫu tối thiểu: [content](templates/content.json), [brief](templates/brief.md), [concept](templates/concept.md), [attempt](templates/attempt.json), [summary](templates/SUMMARY.md). Đây là template chưa cấp ID. Khi dùng bỏ is_template/ghi ID thật và điền dữ kiện phù hợp; không đăng ký template như một production hoặc media.

## Quy trình giống Nature-Studio, đầu ra phù hợp Errare

Brief + nguồn → rà history/lesson → concept → prompt package → tạo media khi được giao → review artifact → attempt sửa → chọn master → export/release → chủ dự án duyệt → đăng/đo → tổng kết.

Theo [OUTPUT-CONTRACT](OUTPUT-CONTRACT.md), có hai gói: photo_post gồm ảnh thật theo target profiles + caption en-US/3–5 hashtag; video gồm FRAME PAIR PROMPT (một prompt cho first/last riêng) + VIDEO PROMPT + CAPTION, không mặc định render cặp frame/video. First=t0, last=duration_s. Tất cả creative hướng Mỹ, phone-life/handheld theo chuẩn chung; tạo/sửa ảnh bằng Codex ImageGen. Single/carousel là layout của post ảnh. Prompt ảnh chỉ là hồ sơ nội bộ hoặc draft nếu người dùng chỉ yêu cầu prompt. Không áp nhịp Underwater cho Errare.

Ảnh/video dung lượng lớn nằm ở media root đã cấu hình hoặc object storage, record dùng asset_id + checksum + storage locator. Master không copy sang từng Table. File cuối không được ghi đè; sửa thành version/attempt mới.

Chỉ tạo hồ sơ cần cho tác vụ: copy-only không cần frame/audio; ảnh một tấm không cần shotlist; carousel có thứ tự slide; video có timeline và audio plan. Prompt/brief là nguồn planned, receipts từ công cụ mới chứng minh actual call/input/output. Không tự tạo file rỗng giả media hoặc backfill seed/model không công bố.

SUMMARY ghi: trạng thái, attempt/master đang chọn, QA gì đã làm/chưa làm, approval nào còn hiệu lực, khoản đã dùng/còn lại, file đầu vào còn thiếu và next action. Kết thúc phiên không tự published/closed hoặc tạo lesson active.

## History, asset và memory

Một nội dung giữ Content ID xuyên revision/caption/close. Mỗi lần tạo/sửa output có attempt mới, không ghi đè lần cũ. Source mode lưu ở content; attempt ghi base/version và phần thay. Chọn explicit text/master/review/release, không suy từ tên final/latest.

Idea ledger gọn tại .errare/productions/idea-ledger.json là index có thể dựng lại từ concept/summary; giữ entry_mode, format, Table/persona, fingerprint cơ chế, Content ID và path. Không dùng ledger thay evidence gốc hoặc ép reference phải mới khác mẫu.

Asset nguồn ở .errare/library/products|personas|assets/, phân tích reference ở .errare/research/references/, model profile ở .errare/models/, lesson ở .errare/memory/candidates|active|retired/. Không copy asset hoặc lesson vào từng Content; tham chiếu ID/version/hash và điều kiện áp dụng. Chính sách lesson vẫn theo [measurement](../06-Insights/MEASUREMENT.md); đóng phiên giữ candidate, không tự nâng hiệu quả audience thành luật.
