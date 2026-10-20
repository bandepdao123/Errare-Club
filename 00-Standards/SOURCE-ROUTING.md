# Skill tham chiếu dữ liệu chuẩn, đọc theo tác vụ

Version 0.2.0. Đã có helper đọc-only scripts/skill_context.py cho bản đồ nguồn và lookup metadata filesystem; chưa có database runtime/catalog được nạp hay semantic/vector search. Seed JSON và tài liệu không là catalog website/roster đã sync.

## Helper dùng chung

Registry [skills.json](skills.json) giữ task/source/data-root, không copy nội dung dữ liệu. Chạy tại root workspace:

```text
python -X utf8 scripts/skill_context.py route er-video --task prompts --mode product
python -X utf8 scripts/skill_context.py route er-video --task caption
python -X utf8 scripts/skill_context.py find --kind product --query "home" --limit 10 --offset 0
```

route chỉ trả path (tùy chọn --hashes), không là read receipt hoặc quyền gọi tool. find hỗ trợ product/reference/persona/asset/model/profile/production/lesson; chỉ đọc JSON trong đúng kho, trả descriptor/path/pointer và phân trang. Mở record gốc/ảnh thực sau lookup. has_more phải xét tiếp khi coverage cần; issue_count khác 0 là có file không đọc được, không suy kho không có dữ liệu. Kho chưa tồn tại trả storage_present=false và không tạo thư mục. Lesson Markdown/legacy chưa có metadata JSON phải tìm gốc theo nhiệm vụ, không biến empty lookup thành chứng nhận không có history.

Caption-only bỏ mode sources dù nhận --mode; product concept không bắt nguồn reference. Data/source thực mà brief yêu cầu vẫn phải mở bổ sung dù chưa có trong bản đồ. Helper chuẩn thư viện Python, không gọi mạng, ghi runtime hoặc render/đăng.

## Một nguồn chính cho mỗi loại

| Dữ liệu | Nguồn chuẩn | Cách truy xuất |
|---|---|---|
| Phạm vi/quyền | SCOPE + yêu cầu hiện hành | Đọc phần áp dụng; không tự mở rộng quyền từ output model |
| Brand/audience/giọng/visual | BRAND.md + US-AUDIENCE.md + PHONE-MEDIA.md + CAPTION.md | Dùng bản hiện hành, đọc clause đúng tác vụ; không chép nguyên vào skill/DB |
| Đầu ra | media-contract.json + OUTPUT-CONTRACT.md | Chỉ mở package photo_post hoặc video cần dùng |
| Sản phẩm | Drive nguồn chính theo product-sources.json; .errare/library/products/ là cache | Lookup SKU/tên/câu áo → mở đầy đủ hồ sơ đúng sản phẩm và ảnh/source refs; cache thiếu/cũ đọc Drive, website bổ sung claim live |
| Media tham khảo | .errare/research/references/ | Lookup reference ID/platform/mechanism → mở analysis và media đúng coverage |
| Persona/asset | .errare/library/personas/ và assets/ | ID/version/view phù hợp; không áp tám cast legacy như roster mới |
| Model | .errare/models/ | Chỉ mở profile đúng tác vụ/interface; video prompt package vẫn cần biết capability liên quan |
| Kích thước/placement | .errare/platform-profiles/ | Profile theo platform + placement + ngày kiểm/nguồn chính thức; chưa có profile thì xác minh lúc chuẩn bị export |
| Lịch sử/lesson | Content gốc + .errare/memory/ | Query điều kiện → mở evidence; candidate không thành luật |

Index/descriptor là bản đồ có thể dựng lại, không là nguồn có quyền cao hơn record gốc. Không giữ hai catalog reference ngang quyền: MEDIA reference dùng .errare/research/references/; library/assets chỉ giữ file asset/rights, không copy analysis. Thư mục này chỉ được tạo khi có dữ liệu thật.

## Bản đồ đọc tối thiểu

| Tác vụ | Đọc | Không bắt đọc |
|---|---|---|
| Tra/đồng bộ sản phẩm | PRODUCT-SOURCES + source config, đúng record/dòng dữ liệu/Drive folder của SKU; website guide khi dùng nhánh website | Toàn catalog vào context, watchlist, toàn production history |
| Research media | SOCIAL-RESEARCH, watchlist/reference được giao, mục tiêu brand | Toàn bộ catalog sản phẩm hoặc model render |
| Post ảnh từ sản phẩm | Brief, brand/ảnh clause, product snapshot/ảnh, persona nếu dùng, caption/export profile, lesson/history liên quan | Reference đối thủ nếu không cần; video prompt contract |
| Video package | Brief/duration, frame plan t0/tT, video clause, product/ref theo entry_mode, persona, audience/phone clauses, model capability, caption và lesson liên quan | Công cụ render thực hoặc toàn bộ export ảnh |
| Chỉ sửa caption | Caption guide, cảnh/phiên bản đã chọn và profile đích | Tạo lại concept; toàn bộ ảnh/cast/watchlist |
| Chỉ thêm kích thước ảnh | Master/hash, target profile, vùng cần giữ và QA crop | Brainstorm lại hoặc render lại mọi variant đã đạt |
| QA/tổng kết | Artifact/package đúng phiên bản, checklist/summary/feedback liên quan | Toàn bộ thư viện hoặc lesson không phù hợp |

## Nguyên tắc tiết kiệm context

Instagram: nguồn kỹ thuật là INSTAGRAM-MEDIA.md, visual là PHONE-MEDIA.md. Task ảnh/video/QA visual đọc phần liên quan; caption-only không đọc lại. Dùng một đoạn quan sát trong brief hiện có và refs/version, không thêm tầng pipeline hoặc checklist riêng mỗi skill. Mặc định dự án không phải official capability receipt; xác minh profile đường đăng khi cần release, không browse lại cho mỗi prompt.

1. SKILL.md chỉ giữ trigger, routing, thứ tự xử lý, quyền và đầu ra. Quy tắc chuyên môn/dữ liệu nằm ở nguồn chung; không sao chép lại theo từng skill.
2. Query metadata gọn trước: id, kind, summary, path, version/hash, tags, applicability, status, captured_at. Chọn theo entry_mode/format/task trước rồi mở gốc; không nạp cả catalog vào prompt.
3. Không cắt nguồn bắt buộc chỉ vì top-k hoặc quota token. Metadata chưa rõ/legacy/stale phải xét record gốc; thiếu index thì tìm file thật. Ưu tiên phụ thuộc đúng nhiệm vụ hơn số lượng file ít nhất.
4. INPUTS ghi record/path/version/hash và vai trò thật đã dùng. Planned khác actual-used. Bản tóm tắt giúp tìm, không chứng minh đã đọc/xem ảnh/clip gốc.
5. Trong cùng context chỉ tái dùng phần đã đọc đủ, còn giữ và không đổi; sau compaction/chat mới hoặc nguồn đổi phải mở lại phần cần. Cache không là lời hứa đã nhớ toàn repo.
6. Không lồng nhiều skill/agent để lặp đọc cùng một bộ dữ liệu. Hai skill sản xuất dùng chung helper/template; subtype caption/revision/export không bắt tạo skill mới.

Chưa đo token/usage đối chứng nên không công bố phần trăm tiết kiệm. Đánh giá sau này bằng context được nạp, thời gian/chi phí và chất lượng đầu ra trên cùng tác vụ; không dùng giảm token làm lý do bỏ QA.
