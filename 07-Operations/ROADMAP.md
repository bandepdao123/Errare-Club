# Triển khai theo cổng, không theo số thư mục

## Phạm vi hiện hành

Theo [SCOPE](SCOPE.md): chỉ media research/production/channel management. Watchlist đầu do người dùng cung cấp; vận hành IG/Reels, Facebook/Reels, Threads; được tự sản xuất trong hạn mức đã cấp và người dùng duyệt trước đăng. Được xây dựng lại hệ nhân vật. Không cần R&D sản phẩm hoặc tích hợp checkout để pilot.

## Giai đoạn hiện tại — thiết kế và nền dữ liệu

Đã có cấu trúc, nguồn, registry 8 cast/10 Table/10 design/16 location và QA thiết kế. Chưa có media import, engine tự động, account, store integration hoặc runtime production. Không nhận thiết kế là hoàn tất triển khai.

Cập nhật workspace 0.2.0: bảy skill er-* đã có trong .agents/skills, dùng chung registry nguồn và helper route/find metadata. Có unit tests offline; chưa chạy generation/publish hoặc sync website/đối thủ từ nhiệm vụ tạo skill. Các cổng pilot media/account bên dưới vẫn cần bằng chứng thực.

## Giai đoạn 1 — một đường đi hoàn chỉnh bằng thao tác thủ công

Bắt đầu bằng sản phẩm/collection website hoặc media reference; watchlist ban đầu cần riêng cho nghiên cứu đối thủ, không chặn nhánh sản phẩm. Thu thập đúng thông tin/hình ảnh cần dùng rồi đề xuất persona/roster mới. Chốt các asset thực sự cần cho content (ảnh sản phẩm/artwork đủ rõ, character refs nếu dùng, plate/license), account owner và ngân sách. Không yêu cầu bộ R&D hoặc đầy đủ SKU/giá/tồn/size mới bắt đầu social. Nhập các tài sản cần cho pilot trước, không bắt nhập toàn bộ archive. Profile model/tool chỉ cần cho công cụ thực dùng.

Đề xuất chọn 2–3 Table có sản phẩm/tài sản sẵn nhất, một account chính trên nền tảng đã có quyền. Table còn lại giữ registry; lựa chọn thực phải dựa inventory/audience, chưa chọn thay người dùng. Một người vừa làm planner/producer/publisher, chủ dự án duyệt; pass review tách bước, không bắt đa agent.

Pilot riêng hai đường: một Content từ sản phẩm không dùng reference đối thủ, một Content từ reference; có thể thêm hybrid nếu có nhu cầu. Tối thiểu kiểm một post ảnh (ảnh thật đủ target sizes + caption) và một gói video (frame pair prompt first=t0/last=duration_s + video prompt + caption), dùng chung hồ sơ/template theo Nature-Studio. Video prompt package dừng ở QA văn bản; tạo hai frame qua Codex ImageGen và render/QA/đăng video chỉ khi được giao thêm, không là gate hoàn thành gói prompt. Đăng/receipt/đo thuộc bước vận hành kênh khi có quyền và media thật. Không cần campaign cho mỗi pilot. Nếu chỉ chọn một format trong pilot thì ghi format còn lại chưa kiểm. Đo thời gian/chi phí thật trước khi chốt cadence; không tự hứa số bài/ngày.

Exit gate: tìm lại được nguồn đúng entry_mode và dependency của post; chữ áo/persona đã chọn đúng; caption/account/disclosure/đích đúng; có receipt; social metrics và link/UTM được kiểm trong khả năng; không còn lỗi chặn; restore thử hồ sơ/media thành công. Chưa đủ gate thì chưa mở rộng account.

## Giai đoạn 2 — helper nhỏ, giảm lỗi lặp

Ưu tiên theo việc pilot đã chứng minh tốn công/lỗi: allocator và atomic record writer; asset import/hash; release digest/invalidation; checklist renderer; UTM builder; budget ledger; receipt/metric importer. Test gate sai digest, thiếu rights, duplicate dispatch, timeout và null metrics. Chưa cần router packet/vector database/agent swarm/dashboard lớn.

Nếu có hai worker/scheduler, chuyển runtime sang SQLite transaction ngay trước khi bật concurrency; JSON export chỉ để đọc/backup. Adapter generation/publish phải có dry-run, idempotency/reconcile, ngân sách và pause. Không gọi tool trả phí khi chỉ test helper.

Exit gate: regression trên fixtures đạt, đường thủ công vẫn dùng được khi adapter hỏng, log đủ để đối soát một call và một post. Lượt QA cấu trúc không thay pilot media thật.

## Giai đoạn 3 — thêm phân phối và học có kiểm soát

Mở rộng hoạt động giữa ba nền tảng ưu tiên bằng release/profile riêng khi công suất, quyền nhạc, account và đo lường sẵn sàng. Có thể tái dùng master; không cộng metric lệch định nghĩa. Chỉ bật lịch/auto-post khi chủ dự án giao quyền rõ, workflow đã thử an toàn và có kill switch.

Mở account riêng cho Table khi có audience đủ khác, backlog khác, owner/công suất duy trì và bằng chứng traffic/chuyển đổi đáng thử; ghi quyết định và rollback. Đây là thay đổi chiến lược phân phối cần chốt, không tự mở 10 account từ tài liệu nguồn.

## Các quyết định cần dữ liệu tiếp theo

| Chưa biết | Việc vẫn làm được | Cổng bị chặn |
|---|---|---|
| File artwork/cast chuẩn | Concept, storyboard, phân loại inventory | Master/release quảng bá đúng thiết kế |
| Tham chiếu sản phẩm/hình từ website | Research đối thủ, persona/concept nháp | Media có chữ/thiết kế sản phẩm phải đối chiếu ảnh rõ; claim giá chỉ kiểm khi sử dụng |
| Account/platform hiện có | Chuẩn bị gói trung lập | Đăng/lịch/profile capability account |
| Ngân sách/render tool | Prompt và cost plan | Generation trả phí |
| Analytics social/traffic | Research và sản xuất vẫn tiếp tục | Kết luận hiệu quả cần dữ liệu thật; thương mại sâu tùy chọn |

Không cần trả lời mọi ô để tiếp tục chỉnh kiến trúc. Khi chuyển sang sản xuất/triển khai, chỉ hỏi phần thiếu đang chặn tác vụ cụ thể.
