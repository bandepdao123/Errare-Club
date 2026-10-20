# Hợp đồng đầu ra sản xuất media

Version 0.1.4. Chỉ hai gói đầu ra chính: photo_post và video. Dùng chung cho product/reference/hybrid; source mode không quyết định package. Chuẩn máy đọc: [media-contract](../00-Standards/media-contract.json); audience toàn dự án: [US-AUDIENCE](../00-Standards/US-AUDIENCE.md); ảnh/phone camera/cặp frame: [PHONE-MEDIA](../00-Standards/PHONE-MEDIA.md); caption: [CAPTION](../00-Standards/CAPTION.md); dữ liệu: [SOURCE-ROUTING](../00-Standards/SOURCE-ROUTING.md). Hồ sơ theo [README](README.md), task routing theo [INTAKE](../02-Research/INTAKE.md), QA theo [quality](../00-Standards/quality.md).

## Đầu ra theo task

concept: ý tưởng/chuyện, persona, hook/payoff, liên quan sản phẩm và giả thuyết chia sẻ; không bắt viết mọi prompt hoặc tạo media.

prompts: concept đã chọn + prompt package theo bảng dưới. Giữ model/interface assumptions và refs tách khỏi câu prompt. Mặc định ý tưởng/ghi chú vận hành tiếng Việt; prompt và copy khách hàng tiếng Anh Mỹ tự nhiên. Với video đây là đầu ra mặc định, không tự render.

generate: dùng đúng package/inputs/budget để tạo hoặc sửa media thật. Post ảnh hoàn chỉnh cần ảnh thật; chỉ có prompt là draft, không đủ yêu cầu ảnh + caption. Video package không mặc định chạy generate; chỉ tạo cặp frame/video thật khi được giao riêng. Ảnh tạo/sửa dùng Codex ImageGen, không tự chuyển provider. Lưu file/receipt thật; thiếu công cụ/khả năng thì ghi blocked/partial, không tạo placeholder output.

review: đối chiếu đúng artifact/hash, scope xem/nghe, findings và cách sửa; prompt review không thành media QA. revision/caption: sửa đúng phần và phụ thuộc, giữ Content ID/chuyện. close: summary + quan sát + đề xuất lesson, không tự render/đăng/active lesson rộng.

## 1. Bài post ảnh — photo_post

Instagram dùng [INSTAGRAM-MEDIA](../00-Standards/INSTAGRAM-MEDIA.md) cho mặc định canvas/export theo placement, gồm cả cặp ảnh và video Reels; đây là nguồn kỹ thuật chung, không copy thông số vào skill. Độ tự nhiên của mọi ảnh/frame/video theo PHONE-MEDIA và kiểm trên artifact thật theo quality.

Giao file ảnh thực đã QA theo brief, đúng các kích thước/placement đích được chọn, và caption tiếng Anh Mỹ tự nhiên kèm 3–5 hashtag. Layout single hoặc carousel là hai cách bố trí của cùng photo_post, không là hai pipeline độc lập. Carousel có thứ tự slide và bộ export cùng layout cho từng placement.

Mặc định ảnh nhìn như chụp bằng điện thoại trong đời sống Mỹ, theo PHONE-MEDIA và US-AUDIENCE; không tự thêm cinematic/film look. Skill tạo ảnh gọi ImageGen tích hợp Codex.

Mỗi export record có asset_id/path/hash, slide_order nếu có, platform/placement/profile ID/version, width_px/height_px, aspect ratio, file type, master_ref và crop/QA evidence. Profile quy định kích thước/format/vùng UI, có nguồn và ngày kiểm. Không đoán “mọi mạng cùng một size” hoặc dùng kích thước do model sinh thay kích thước export thật.

Đủ loại cỡ nghĩa là đủ target đã chọn cho các kênh/placement đang làm, không sinh mọi kích thước có thể tồn tại trên mọi mạng. Nếu chưa có target/profile thì để export_pending và xác minh trước giao bản hoàn chỉnh. Khi một master đủ dùng, tái bố cục/crop/export thay vì render lại toàn bộ; vẫn kiểm câu áo, người và vùng an toàn ở từng variant. Caption có thể dùng chung nếu phù hợp hoặc riêng theo nền tảng, mỗi bản hoàn chỉnh có 3–5 hashtag.

IMAGE PROMPT, concept và source refs là hồ sơ sản xuất nội bộ. Nếu chỉ được giao viết prompt ảnh thì trả prompt-only có nhãn, không gọi đó là post ảnh đã hoàn thành.

## 2. Video — prompt package theo Nature-Studio

Giao đúng ba mục: **FRAME PAIR PROMPT (FIRST + LAST)**, **VIDEO PROMPT**, **CAPTION**. FRAME PAIR PROMPT là một prompt chung yêu cầu hai ảnh riêng: first t0 và last t=T, với T là duration_s của video đã chốt. Không là hai prompt độc lập hoặc một ảnh collage. Prompt/copy đầu ra dùng Anh Mỹ tự nhiên; caption gồm 3–5 hashtag. Ý tưởng/timeline/source/coverage lưu trong brief/concept, không bắt xuất thêm báo cáo dài khi chỉ cần ba mục này.

FRAME PAIR PROMPT khóa identity/áo/bối cảnh chung, trạng thái first và last, camera/continuity và hai file độc lập. First=0, last=duration_s: 8s→t8, 10s→t10, 15s→t15. Không mặc định thời lượng hoặc lấy một beat giữa clip làm last. VIDEO PROMPT nối hai trạng thái bằng hành động/nhân quả/âm và chuyển động người cầm điện thoại hợp cảnh. Góc/độ rung như phone footage đời thường, không dùng camera điện ảnh trừ yêu cầu cụ thể. Brief/model profile kiểm khả thi và ratio/duration, không áp nhịp Underwater.

Có frame pair prompt không đồng nghĩa đã tạo/xem hai ảnh thật. Có video prompt không đồng nghĩa đã render video. Gói hoàn chỉnh về văn bản khi đủ ba mục, duration và frame plan t0/tT nhất quán, kiểm đúng nguồn; không cần render để hoàn thành gói prompt. Khi được giao tạo cặp ảnh, dùng Codex ImageGen và chỉ nhận đủ khi có hai file riêng; tool trả một ảnh/ảnh ghép phải ghi partial, không giả đủ cặp. Đăng video vẫn cần render thực/QA/approval; prompt-ready không là release-ready.

Hồ sơ first-frame-only trước 0.1.4 giữ lịch sử, không tự đổi tên thành frame_pair_prompt để nhận đã có last frame. Revision mới cần bổ sung plan/prompt last và kiểm lại phần phụ thuộc.

## Tương thích hồ sơ cũ

image ánh xạ sang photo_post/layout single; carousel sang photo_post/layout carousel. text cũ giữ lịch sử nhưng không là đầu ra độc lập mặc định mới; Threads vẫn dùng caption/ảnh trong phạm vi hai gói, research bài chữ vẫn được giữ. Không xóa/migrate hàng loạt lịch sử, không tự dựng media hoặc quay lại sửa attempt cũ cho khớp contract mới.

## Những trạng thái phải tách

Text hiện hành, artifact đã review, master đang chọn và release đã duyệt có thể là các phiên bản khác nhau. Bản prompt sửa mới không làm render cũ thành output của prompt mới. Ghi explicit refs/hash thay quy tắc “file mới nhất”. Caption sửa tạo attempt/release revision đúng phần; QA visual cũ chỉ tái dùng khi artifact/criteria/dependencies phù hợp.

QA pass không bằng selection, approval hoặc published. Close trước khi có render ghi prompt-only; close trước đăng không yêu cầu analytics giả. Kết quả social và lesson empirical chỉ bổ sung khi thật sự có evidence.
