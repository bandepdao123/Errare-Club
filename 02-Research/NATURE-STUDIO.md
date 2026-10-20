# Nature-Studio: kế thừa có chọn lọc

Đối chiếu VERSION = 2.1.5 tại commit d0193bcf41a986924d4c4a197bbfac7bceb8ebf3. Kết quả tìm kiếm ban đầu trả README v1.7.1 đã cache; phân tích dưới dùng file API theo commit, không dựa bản cache đó.

## Tập đã đọc

AGENTS.md, START-HERE.md, SYSTEM.md, VERSION; CHANGELOG.md phần đầu đến lịch sử v1.4; các tài liệu production, quality-review, memory-policy, context-routing, media-review-and-finishing trong 00-Standards; templates current-state, asset-record, performance, lesson; Underwater PROJECT.md, context-map.json, creative-direction.md; 06-Evaluation/README.md và 08-Assets/README.md. Đã xem danh sách đường dẫn qua Git tree, không đọc toàn catalog/ảnh/test/source. Nguồn chính: [SYSTEM](https://github.com/bandepdao123/Nature-Studio/blob/d0193bcf41a986924d4c4a197bbfac7bceb8ebf3/SYSTEM.md), [production](https://github.com/bandepdao123/Nature-Studio/blob/d0193bcf41a986924d4c4a197bbfac7bceb8ebf3/00-Standards/production.md), [quality](https://github.com/bandepdao123/Nature-Studio/blob/d0193bcf41a986924d4c4a197bbfac7bceb8ebf3/00-Standards/quality-review.md), [memory](https://github.com/bandepdao123/Nature-Studio/blob/d0193bcf41a986924d4c4a197bbfac7bceb8ebf3/00-Standards/memory-policy.md).

## Những cấu trúc hữu ích

| Quan sát từ nguồn | Kế thừa cho Errare | Điều chỉnh cần thiết |
|---|---|---|
| Standards / Knowledge / Models / Projects / Productions / Memory / Evaluation / Releases tách nhiệm vụ | Quy tắc, dữ kiện, sản xuất, đo lường và bài học có nguồn chính riêng | Một thương hiệu: gom nền brand; chưa cần framework đa project |
| PROJECT.md xác lập hiện hành, index chỉ là bản đồ | Brief và registry có ID/version; router đọc đúng task | Table không thành mười bản copy project |
| Attempt bất biến, input/settings/hash | Truy ngược từ bài đăng tới bản xuất, render, prompt, cast, artwork | Ảnh, video, carousel và copy đều có thể là đầu ra chính |
| Current text, selected render, QA và approval riêng | Gói release được duyệt theo digest, không dùng latest file | Approval bao gồm caption/link/account/disclosure, không chỉ media |
| Prompt/image/video/published có cấp bằng chứng riêng | Không lấy text review thay QA media | Bổ sung QA brand, typography áo, continuity cast và conversion |
| Candidate / active / retired, scope và điều kiện áp dụng | Chỉ áp lesson phù hợp; ghi giả thuyết riêng | Kết quả tăng views chưa chứng minh tăng doanh thu |
| Runtime riêng, public release được lọc | Media và dữ liệu thương mại tách khỏi gói tài liệu public | Backup phải giữ cả metadata, asset và receipt; gitignore không là backup |
| Routing nguồn theo task/effect | Caption edit chỉ đọc giọng, scene đã chốt và release liên quan | Chưa triển khai packet/receipt engine trước khi cần |
| Catalog planned refs khác actual model inputs | Cast/plate/artwork có provenance | Soul ID chưa chứng minh file đã tồn tại hoặc đã gửi vào model |

## Cập nhật lõi sản xuất 0.1.2

Đọc bổ sung bốn template nguồn tại cùng commit: brief.md, concept.md, attempt-inputs.md và episode-summary.md trong 00-Standards/templates. Errare kế thừa cách khóa brief/concept, ghi source/input/settings/output từng attempt, chọn text/master rõ ràng và summary đủ để tiếp tục qua phiên. Template Errare nằm ở 04-Productions/templates; output contract mở rộng cho image/carousel/video/text. Hai nguồn product/reference/hybrid là lựa chọn đầu vào, không nhân đôi production pipeline. Chưa cài skill/dispatcher hoặc gọi render từ các mẫu này.

## Phần bổ sung cho Errare

1. Product bridge: content phải có product/design reference hoặc lý do chưa gắn; CTA khớp trang đích và tồn/giá kiểm lúc phát hành.
2. Release và Post riêng: cùng file có thể đăng ba nơi, caption/nhạc/quyền/account khác nhau. Mỗi post có native ID và metrics riêng.
3. Hai vòng phản hồi: chất lượng media và kết quả kinh doanh; không dùng một tổng điểm viral để thay hai vòng.
4. Experiment record: giả thuyết, biến thay, cohort, tuổi bài, cửa sổ đo và tiêu chí hành động chốt trước đọc kết quả.
5. Phục hồi: crash khi upload, retry, chi phí call lỗi, file hỏng, store thay URL hoặc hết hàng.
6. Pilot ít account: giữ đủ mười Table trong mô hình, chỉ vận hành số series phù hợp công suất. Đề xuất này điều chỉnh hướng mỗi Table một kênh trong nguồn, cần chủ dự án chốt trước mở account.

## Không kế thừa máy móc

Không áp domain sinh học/rig/cá, video 10s một shot/key sau 5s, mã hai chữ bốn số, lựa chọn model và quota năm call như luật Errare. Không bê hơn 20 helper hoặc các số test nguồn sang để nhận đã có hệ thống chạy. Số test/QA nêu trong CHANGELOG là tự báo cáo lịch sử của repo, không phải phép kiểm đã chạy trong nghiên cứu này.

Không đủ dữ liệu để kết luận Nature-Studio đã thiếu hay hỏng phần thương mại: chỉ nói tập nguồn đã đọc không cung cấp một luồng commerce/attribution hoàn chỉnh để tái dùng. Không tuyên bố bản thiết kế Errare đã chứng minh tốt hơn trong vận hành.
