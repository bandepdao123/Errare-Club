# QA kiến trúc — 2026-10-20

Phạm vi: tự rà nhiều lượt trên tài liệu thiết kế và kiểm bằng script. Một operator thực hiện, không có reviewer/agent độc lập. Đây không phải báo cáo QA media, runtime, API hoặc hiệu quả bán hàng. Từng kết quả dưới nói về thiết kế đã có quy tắc xử lý, không nói phần mềm đã thực thi đúng.

## Vòng 1 — đối chiếu nguồn và cấu trúc

Đã đối chiếu Nature-Studio theo commit cố định, không dùng README cache v1.7.1 thay VERSION v2.1.5. Giữ phân tách nguồn/quy chuẩn/attempt/memory/QA, bỏ luật Underwater không phù hợp. Đã đối chiếu cast/Table/design/location với văn bản Errare World.

Các điểm được xử lý trong bản thiết kế: Table là taxonomy, không phải mười hệ thống; code áo khác SKU; source-stated khác asset đã nhập; 16 location gồm 15 slot mô tả đầy đủ và Reply All còn thiếu sheet. Chưa chứng nhận hình ảnh, Soul hoặc license.

## Vòng 2 — walkthrough các tình huống lỗi

| Case | Tình huống rà | Quy tắc tìm thấy trong thiết kế / kết quả |
|---|---|---|
| Q01 | Chỉ sửa caption | workflow bước 2/quality: giữ chuyện và visual, tạo release revision; có đường xử lý |
| Q02 | Sửa caption/link sau duyệt | contracts digest/gate: approval gói cũ không hiệu lực; có đường chặn |
| Q03 | Crop export làm cắt chữ áo | quality export + release QA: kiểm bản xuất, không dùng master pass thay; có đường chặn |
| Q04 | Frame đầu đẹp, chữ hỏng ở cuối video | quality video/coverage: motion/reveal/ending phải kiểm; có đường chặn |
| Q05 | Chỉ có transcript/frame mẫu | quality khả năng: audio/motion not_checked; không nhận full QA |
| Q06 | Model timeout rồi retry | workflow budget/attempt + recovery: unknown giữ reservation, reconcile trước; có đường xử lý |
| Q07 | Crash sau upload, chưa ghi post ID | distribution/workflow: dispatch_unknown, kiểm native account trước retry; không hứa exactly-once |
| Q08 | Store hết hàng trước lịch đăng | recovery/release preflight: chặn, sửa CTA/đích/offer và duyệt lại |
| Q09 | Nhạc chỉ có quyền một nền tảng | workflow release/distribution: rights riêng từng release; không cross-post mù |
| Q10 | Thiếu character sheet dù đã có Soul ID | BRAND/registry: file null, availability not_checked; draft được, không giả input thật |
| Q11 | Nhiều Table dùng cùng cast/master | SYSTEM identity + production asset ref: chia sẻ ID/dependency, không nhân bản |
| Q12 | Location gợi ý hai lỗi, Priya có vòng đỏ và giỏ đỏ | workflow chọn một lỗi; quality kiểm vật đỏ trên artifact; cần chọn/che vật phụ trong brief |
| Q13 | Bio chung có nhiều bài dẫn traffic | measurement/link grain: không quy đơn cho từng post; có giới hạn attribution |
| Q14 | 24h/72h/7d là snapshot cumulative | measurement: không cộng; so cùng tuổi bài/cohort |
| Q15 | View Shorts khác định nghĩa nền tảng khác | measurement: giữ metric definitions; không rank raw views xuyên nền tảng |
| Q16 | Không lấy được metric/đơn/chi phí | contracts/measurement: null + reason, không dựng 0; cost ghi coverage |
| Q17 | Hai worker sửa một record | contracts/roadmap: MVP single writer; SQLite trước concurrency, expected_revision |
| Q18 | Index hỏng hoặc thay máy | source-of-truth + recovery: dựng lại index, restore metadata/media/receipt, không reset budget/ID |
| Q19 | Một video tốt được nâng thành luật viral | measurement lesson: candidate, evidence/điều kiện trước active; không cam kết nhân quả |
| Q20 | Ngày lịch Mỹ đổi DST | contracts timezone: UTC để join, IANA để hiển thị/lập lịch; không UTC-5 cố định |

Tất cả case trên đã được rà ở cấp tài liệu. Không case nào là test submit/generation/publish thật. Khi triển khai engine cần chuyển thành fixtures/integration tests phù hợp; cần thử media và pilot để xác nhận khả thi.

## Vòng 3 — kiểm dữ liệu và liên kết

Đã chạy python -X utf8 scripts/validate_structure.py: **400 phép kiểm cấu trúc, 0 lỗi, exit code 0**. Script không gọi network, không tạo production ID, không render hoặc đăng.

Đã kiểm thêm bốn negative control trên bản sao trong thư mục tạm: tham chiếu cast không tồn tại (phát hiện 1 lỗi), tự điền giá bán chưa xác minh (1 lỗi), thiếu quality.md (3 lỗi), ID cast trùng (5 lỗi). Cả 4/4 bị validator từ chối như yêu cầu. Không sửa registry nguồn hoặc gọi dịch vụ ngoài. Đây là kiểm khả năng phát hiện sai dữ liệu của validator, không là kiểm publisher/approval engine.

Phạm vi tự động: số lượng/ID registry, tham chiếu Table/cast/design/location, cú pháp Soul UUID, trạng thái nguồn chưa xác minh, null cho tài sản/commerce chưa có, 15 slot + một scene partial, file tài liệu bắt buộc và đích liên kết Markdown nội bộ. Không kiểm anchor, URL ngoài, toàn bộ JSON schema hay nội dung ngữ nghĩa.

## Điều kiện chưa được kiểm

- File artwork/cast/plate thật và quyền sử dụng; identity/Soul khả dụng.
- Một pipeline ảnh/video/copy hoàn chỉnh và thời gian/chi phí thực.
- Release digest/approval invalidation, queue/concurrency/budget engine: mới là contract.
- Account capability, AI disclosure thao tác thực, upload/reconcile và receipt thật.
- Store events, attribution/dedup/refund và restore media thật.
- Tỷ lệ giữ chân, chia sẻ, chuyển đổi và công suất dài hạn.

Chỉ chuyển từ design-reviewed sang operationally-validated khi pilot và các gate trong roadmap có bằng chứng. Không tự mở rộng sản xuất/automation để làm đẹp báo cáo QA.

## Rà thay đổi phạm vi 0.1.1

Theo bốn câu trả lời trực tiếp của chủ dự án: watchlist đầu do người dùng cung cấp; ưu tiên IG/Reels, Facebook/Reels, Threads; tự chủ nghiên cứu/kế hoạch/sản xuất trong budget và duyệt trước đăng; được xây lại hệ nhân vật. R&D sản phẩm ngoài phạm vi, website chỉ là nguồn tham chiếu.

Đã rà ở cấp tài liệu: không yêu cầu checkout/order integration để pilot; không bắt tám cast cũ; không mặc định vận hành TikTok/X/YouTube; không gọi Reels là mạng riêng; không nghiên cứu lại sản phẩm; không nhận high views là viral đã chứng minh; partial video/audio không thành full analysis; lựa chọn mức tự chủ không cấp một ngân sách chưa xác định. Các phần commerce sâu được giữ như extension chưa kích hoạt.

Đã đọc trang chủ errareclub.com qua trình duyệt; chưa sync catalog, tải/QA ảnh, nghiên cứu watchlist hoặc xây roster mới. Các record cũ được giữ làm seed tham khảo, không thay bằng dữ liệu website chưa thu thập. Kết quả validator 400 phép kiểm phía trên là mốc trước thay đổi; lượt kiểm cấu trúc sau cập nhật đạt 421 phép kiểm, 0 lỗi, exit code 0. Không suy kết quả cấu trúc thành QA media hoặc vận hành thật.

## Rà thay đổi 0.1.2 — nguồn sản phẩm và lõi media

Tự rà tài liệu theo ba đường: product chỉ có nguồn sản phẩm vẫn tới concept, reference có thể phân tích mẫu trước chọn áo, hybrid cần cả hai. Cả ba cùng dùng image/carousel/video/text, task độc lập; không buộc campaign/watchlist cho product. Caption/revision giữ chuyện/Content ID; prompt-only và close không tự render/đăng. Video không buộc first frame nếu tuyến sản xuất không cần; text không buộc prompt hình.

Đối chiếu thêm bốn template Nature-Studio tại commit đã chốt: brief, concept, attempt-inputs, episode-summary. Bổ sung template Errare giữ source/input/settings/output, planned khác actual, text/review/master/approval riêng; không tạo production thật từ template. Validator mở rộng kiểm mode config độc lập, source requirements, campaign tùy chọn, paths và placeholder templates. Đây là QA thiết kế/config, chưa chạy creative dispatcher hoặc sinh media.

Kết quả thực: python -X utf8 scripts/validate_structure.py đạt **512 phép kiểm, 0 lỗi, exit code 0**. Năm negative control trên bản sao thư mục tạm đều bị từ chối: ép product cần reference, bỏ nguồn reference bắt buộc, bỏ product khỏi hybrid, ép Campaign bắt buộc, và tạo output giả trong template attempt. **5/5 phát hiện**, không sửa dữ liệu gốc hoặc gọi dịch vụ ngoài. Đây là kiểm config/template validator, không là kiểm hành vi AI hay renderer.

## Rà thay đổi 0.1.3 — hai gói đầu ra và nguồn dữ liệu skill

Đã chỉnh ảnh sang photo_post (single/carousel là layout) và video sang gói first frame prompt + video prompt + caption. Ảnh hoàn chỉnh cần file thật theo target profiles; video prompt package không tự render. Caption en-US, 3–5 hashtag lưu một nơi; SOURCE-ROUTING chỉ định nguồn chính, không copy catalog/brand vào từng skill. Thu gọn đề xuất xuống bảy skill, chưa tạo/cài SKILL.md.

Kiểm cấu trúc thực: **562 phép kiểm, 0 lỗi, exit code 0**. Sáu negative control trên bản sao tạm đều bị phát hiện: thiếu first_frame_prompt; hashtag range 2–6; cho photo_post hoàn chỉnh không cần ảnh; bắt video package render; locale en-GB; đường dẫn source guide hỏng. **6/6 phát hiện**, không sửa dữ liệu nguồn hoặc gọi công cụ sinh media. Đã tìm các điều khoản format bốn loại/first frame tùy chọn cũ trong tài liệu routing/production hiện hành, không còn kết quả; lịch sử phiên bản vẫn giữ nguyên.

Giới hạn: chỉ xác minh contract/config/template/link, chưa kiểm caption thật, giọng native, pixel/crop ảnh, source query engine hoặc hành vi skill. Chưa có số đo đối chứng tiết kiệm token; không công bố tỷ lệ cải thiện từ thiết kế.

## Rà thay đổi 0.1.4 — native Mỹ, frame pair và phone style

Chuẩn mới áp audience Mỹ cho toàn creative, không chỉ caption. FRAME PAIR PROMPT là một prompt chung cho hai file riêng first=t0/last=duration_s; video prompt nối hai mốc và camera người cầm điện thoại. Cinematic chỉ khi yêu cầu. Ảnh tạo/sửa qua Codex ImageGen; skill đề xuất errare-taoanh hỗ trợ post/cặp frame, không tự chuyển provider. Film/Soul/Nano route trong nguồn cũ chỉ giữ lịch sử.

Đã tự rà tài liệu hiện hành: không còn field FIRST FRAME PROMPT/first_frame_prompt của hợp đồng trước, không coi first-only thành pair. Đã kiểm ví dụ quy tắc nội dung 8s→t8, 10s→t10, 15s→t15; chúng là ví dụ của last=duration_s, không danh sách thời lượng bắt buộc.

Kiểm cấu trúc thực: **599 phép kiểm, 0 lỗi, exit code 0**. **8/8 negative control** trên bản sao tạm bị phát hiện: hai prompt độc lập, chỉ một ảnh, collage, first khác t0, last cố định t10, native Mỹ chỉ cho caption, cinematic mặc định, fallback provider ảnh ngoài. Không sửa dữ liệu nguồn, không tạo ảnh/video hoặc gọi dịch vụ ngoài.

Giới hạn: chưa kiểm ImageGen thực trả hai file từ một prompt, continuity hai ảnh, motion/handheld render, exact video ending hoặc phản ứng audience Mỹ. Nếu tool thực chỉ trả một ảnh/ảnh ghép phải ghi partial theo PHONE-MEDIA, không lấy QA config làm bằng chứng đã tạo đủ cặp.

## Workspace 0.2.0 — skill đã được triển khai

Đã tạo bảy skill er-* project-local và UI metadata, registry nguồn và helper route/find. Kiểm 7/7 bằng skill-creator validator, 11 unit tests helper đạt, và forward-test độc lập ba tình huống prompt-video/QA partial/local channel plan. Chi tiết, actual output và giới hạn ở [SKILLS-0.2.0](SKILLS-0.2.0.md). Các ghi chú “chưa cài skill” ở vòng cũ phía trên là lịch sử tại thời điểm kiểm, không là trạng thái hiện hành.
