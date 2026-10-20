# Nhật ký quyết định thiết kế

Ngày 2026-10-20. Các quyết định dưới là đề xuất thiết kế trong phạm vi yêu cầu, chưa là phê duyệt chi phí/đăng/kết nối dịch vụ.

| ID | Quyết định | Lý do / điều kiện xem lại |
|---|---|---|
| EC-D001 | Một brand workspace; Table là taxonomy | Tránh 10 bản sao brand/cast/pipeline |
| EC-D002 | Campaign → Content → Attempt → Release → Post | Tách chuyện, artifact, gói duyệt và phân phối |
| EC-D003 | File-first single writer | MVP đơn giản; SQLite trước scheduler/multi-writer |
| EC-D004 | Approval theo digest đầy đủ | Sửa caption/link/account cũng có thể làm sai gói đã duyệt |
| EC-D005 | Tách media QA, approval và performance | Không lấy views hoặc schema pass thay chất lượng/quyền đăng |
| EC-D006 | Post/link attribution theo grain thực có | Bio chung không chứng minh nguồn từng post |
| EC-D007 | Runtime/media private, backup riêng | Repo system không thay backup vận hành |
| EC-D008 | Pilot ít series/account | Điều chỉnh hướng mỗi Table một kênh; chờ chốt trước mở account |
| EC-D009 | Không hardcode model/giá/spec nền tảng | Xác minh tại thời điểm và interface thực thi |
| EC-D010 | Chỉ nhập metadata nguồn trong lần này | Chưa có ảnh, artwork, license, store hay account để xác minh |
| EC-D011 | Media/kênh là phạm vi chính, R&D sản phẩm ngoài phạm vi | Chủ dự án xác nhận sản phẩm đã lên errareclub.com; chỉ nhập thông tin/hình tham chiếu |
| EC-D012 | Research media IG/Facebook/Threads/TikTok/X/YouTube | Watchlist đầu do người dùng cung cấp, sau đó hệ thống được chủ động tìm thêm |
| EC-D013 | Vận hành đầu kỳ IG/Reels, Facebook/Reels, Threads | Câu trả lời trực tiếp của chủ dự án; chưa có account cụ thể |
| EC-D014 | Tự nghiên cứu/kế hoạch/sản xuất trong budget; duyệt trước đăng | Chưa có con số budget, không tự chi tiền không giới hạn |
| EC-D015 | Được xây dựng lại hệ nhân vật | Tám cast cũ giữ tham khảo, không áp thành roster bắt buộc; không tự tái dùng Soul ID cho identity mới |

EC-D011–015 là cập nhật theo chỉ đạo người dùng, thay các giả định phạm vi tương ứng ở 0.1.0. Analytics đơn/checkout chỉ là extension tùy chọn; không là gate MVP social.

## Cập nhật 0.1.2 — hai đầu vào, chung lõi media

| ID | Quyết định | Lý do / nguồn |
|---|---|---|
| EC-D016 | Product và reference là hai đầu vào độc lập; hybrid khi dùng cả hai | Người dùng yêu cầu thêm option xuất phát từ sản phẩm; watchlist không chặn product |
| EC-D017 | Nguồn × task × format là các chiều riêng; Campaign tùy chọn | Không nhân đôi workflow hoặc ép tạo campaign cho một media độc lập |
| EC-D018 | Kế thừa Nature-Studio ở hồ sơ/attempt/output/QA/summary | Có template Errare, output contract cho image/carousel/video/text; không sao chép luật Underwater |

EC-D002 vẫn giữ sự phân tách Content/Attempt/Release/Post, nhưng Campaign là nhóm tùy chọn thay chuỗi bắt buộc. Không sửa/xóa lịch sử source seed hoặc giả có dispatcher/skill thực thi.

## Cập nhật 0.1.3 — hai gói đầu ra và skill đọc nguồn chung

EC-D019: photo_post giao ảnh thật đủ target size/placement và caption Anh Mỹ + 3–5 hashtag; single/carousel là layout, không là pipeline riêng. Video giao first frame prompt + video prompt + caption; first frame prompt bắt buộc, không tự tạo first frame/video thật. Chuẩn hashtag được áp dụng mặc định cho cả caption video để thống nhất, không phải claim hiệu quả nền tảng.

EC-D020: media-contract.json + OUTPUT-CONTRACT.md là nguồn đầu ra, CAPTION.md là nguồn giọng/hashtag; SOURCE-ROUTING.md xác định kho dữ liệu và đọc theo task. Index không thay record gốc; không copy quy chuẩn/catalog vào skill.

EC-D021: đề xuất bảy skill trong SKILLS.md, sáu skill sản xuất/hỗ trợ ưu tiên và một quản lý kênh khi có account. Không cần đồng thời chaymedia/taoanh/postanh hoặc một skill taovideo trong bộ mặc định prompt video. Đây là đề xuất, chưa tạo SKILL.md hoặc dispatcher.

## Cập nhật 0.1.4 — audience Mỹ, hai anchor và Codex ImageGen

EC-D022: toàn creative native cho audience Mỹ, không giới hạn ở caption. Internal ops có thể tiếng Việt. US-AUDIENCE.md là nguồn chung.

EC-D023: gói video đổi sang FRAME PAIR PROMPT + VIDEO PROMPT + CAPTION. Một prompt chung yêu cầu hai ảnh riêng first=t0 và last=duration_s, không collage; duration là biến brief, không mặc định 10s. Prompt-only vẫn chưa tự render, không tự nâng hồ sơ first-only cũ thành pair.

EC-D024: mặc định ảnh/video smartphone đời thường, camera video do người cầm, góc/rung hợp cảnh; cinematic cần yêu cầu. PHONE-MEDIA.md ưu tiên hơn film/editorial look nguồn cũ.

EC-D025: skill tạo/sửa ảnh dùng Codex ImageGen, không tự fallback provider. Đề xuất skill errare-taoanh thay tên postanh và hỗ trợ post/cặp frame theo tác vụ. Tool/interface thực có trả đủ hai file hay không cần kiểm bằng output, chưa được chứng nhận trong lần sửa tài liệu này.

## Workspace 0.2.0 — triển khai skill theo chấp thuận của chủ dự án

EC-D026: tạo bảy skill project-local, đổi prefix đề xuất errare- thành er- theo yêu cầu: er-sanpham, er-nghiencuu, er-taoanh, er-video, er-kiemmedia, er-dongmedia, er-quanlykenh. Giữ automatic discovery mặc định; không cài bản global trùng hoặc đăng ký slash command riêng.

EC-D027: dùng skills.json làm bản đồ task/source/data-root và một helper skill_context.py đọc-only cho route/find metadata phân trang. Skill giữ workflow/quyền/đầu ra, nguồn chuẩn vẫn là tài liệu/record gốc. Chưa có CSDL runtime được nhập, provider/account adapter tự động hoặc call media/publish. Contract media 0.1.4 không đổi.

Kiểm tạo skill theo skill-creator, test helpers offline và review tình huống riêng; bằng chứng và giới hạn ở 08-Evaluation/SKILLS-0.2.0.md.

EC-D028 — cập nhật nguồn sản phẩm: chủ dự án chỉ định Drive Product Listing làm hồ sơ chính, website là bổ sung thông tin đang công bố. er-sanpham mặc định lookup đầy đủ dữ liệu có thực của đúng SKU/tên/câu áo; sync dùng khi nhập/cập nhật batch. Đăng ký nguồn không có nghĩa đã index toàn catalog hoặc tải mọi ảnh. File nguồn/inspection scope ở 01-Brand/product-sources.json, cơ chế ở PRODUCT-SOURCES.md.

EC-D029 — 2026-10-20: dùng INSTAGRAM-MEDIA.md làm chuẩn kỹ thuật chung và mở rộng PHONE-MEDIA.md thành chuẩn quan sát đời sống tự nhiên cho ảnh post, frame Reel và video. Đoạn quan sát gọn nằm trong brief hiện có, QA thêm evidence cho hành vi/biểu cảm/người cầm máy/bối cảnh/artwork/canvas. Routing ảnh/video/QA đọc chuẩn; caption-only không nạp lại. Không tạo skill/agent/pipeline mới. Mặc định production không phải xác minh official API/account; cảnh đã tạo giữ nguyên lịch sử, không tự regenerate. Lần cập nhật này chỉ sửa hệ thống, chưa chứng minh hiệu quả social hoặc render đạt chuẩn mới.
