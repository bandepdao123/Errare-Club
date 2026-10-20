# Workflow sản xuất và phát hành

Version 0.1.4. Phạm vi hiện hành theo SCOPE: sáng tạo từ sản phẩm hoặc media tham khảo, sản xuất media và quản lý social; website cung cấp tham chiếu sản phẩm đã được R&D chốt. Đây là quy trình tác nghiệp cần thực hiện, chưa được tự động hóa bằng validator hiện có.

## 1. Chốt brief đủ để bắt đầu

Chọn entry_mode theo [INTAKE](../02-Research/INTAKE.md): product / reference / hybrid. Hai đầu vào độc lập cùng dùng lõi sản xuất; product không chờ watchlist, reference được phân tích trước khi chọn áo. Tách entry_mode, task và format. Campaign tùy chọn, nội dung standalone có lý do không cần campaign giả.

Planner lấy mục tiêu campaign, audience, Table, cast, design, định dạng và mục tiêu bài. Brief ghi hook, lỗi nhỏ duy nhất, punchline, bối cảnh, CTA, giới hạn brand và giả thuyết cần kiểm. Nếu location nguồn có nhiều lỗi gợi ý, chọn một lỗi chính cho cảnh, không đưa tất cả vào ảnh.

Tra persona/cast được chọn cho nội dung, product/location, snapshot website và bài học liên quan. Không mặc định tám cast cũ là roster mới. Khi nhánh cần research đối thủ, dùng 02-Research/SOCIAL-RESEARCH.md; dữ kiện sản phẩm theo 01-Brand/WEBSITE-REFERENCE.md. Tham chiếu source code áo không chứng minh có artwork. Thiếu artwork có thể làm concept/storyboard/áo trơn draft, nhưng chưa xuất bản quảng bá như sản phẩm đã khớp. Brief awareness chưa gắn sản phẩm cần lý do rõ; conversion bắt buộc có sản phẩm và đích hợp lệ. Kiểm vật đỏ trong toàn cảnh, kể cả phụ kiện cast: nếu Priya cầm giỏ đỏ thì bố trí để vòng chỉ đỏ không thành vật đỏ thứ hai đọc được; không âm thầm bỏ đặc điểm nhân vật khỏi hồ sơ chuẩn.

Không bắt người dùng điền biểu mẫu dài. Operator tự hoàn thành phần thường lệ, đánh dấu thiếu đúng trường có ảnh hưởng; tiếp tục việc độc lập trong khi chờ. Không tự suy giá, tồn, domain hay quyền sử dụng.

## 2. Phát triển concept trước khi render

Với product: đọc câu áo/hình/collection từ website, rút tension/insight giả định rồi phát triển persona và tình huống gốc. Rà lịch sử/lesson để tránh lặp; đối thủ là tham khảo tùy chọn, không là gate. Với reference: đọc media thực theo coverage, rút cơ chế và chuyển thể vào Errare; chọn sản phẩm khi content cần. Với hybrid: kết hợp cả hai, không đổi dữ kiện sản phẩm để giống mẫu. Phát triển một số tiền đề thực sự khác nhau khi cần; điểm chấm chỉ hỗ trợ thứ tự, không là xác suất viral.

Lưu concept chọn và fingerprint ngắn: setup → lỗi/tension → phản ứng → payoff/câu áo khi dùng → CTA. Mẫu nguồn không là danh sách kín. Product mode kiểm độ mới ở hành vi/nhân quả; reference được giữ cơ chế mẫu có chủ đích, không ép đổi chuyện chỉ để mới. Revision chỉ sửa phần được giao; đổi caption không cấp Content ID mới. Đổi hẳn câu chuyện/tư cách experiment mới mới cân nhắc Content mới có derived_from.

## 3. Lập kế hoạch sản xuất và ngân sách

Chọn gói photo_post hoặc video theo OUTPUT-CONTRACT. Post ảnh cần ảnh thật theo target placements + caption; video mặc định là frame pair prompt + video prompt + caption. Prompt chung yêu cầu hai file first=t0/last=duration_s, không tự tạo ảnh/video khi chỉ viết prompt. Mọi creative native cho Mỹ theo US-AUDIENCE; ảnh/video phone đời thường và camera cầm tay theo PHONE-MEDIA, cinematic chỉ khi yêu cầu. Tạo/sửa ảnh dùng Codex ImageGen, không tự đổi provider. Copy-only cũ giữ lịch sử, không là gói đầu ra mặc định mới. Kiểm tool thực có trong phiên; model profile ghi provider, interface, ngày kiểm, khả năng, giới hạn và giá hiện biết. Không lấy chi phí 0,12/2/~50 credit trong nguồn làm báo giá hiện hành.

Trước call trả phí ghi attempt, request ID, input chính xác, output kỳ vọng, ngân sách tối đa đã cho phép và chi phí dự kiến. Đơn vị credit/USD giữ riêng. Dừng trước call khi không đủ headroom hoặc chưa biết mức trần chi phí có thể phát sinh. Call đã gửi kể cả timeout tính vào số lượt; không gọi lại mù. Nếu cần retry, đối chiếu job receipt/provider trước.

Nhật ký budget gồm reserved / submitted / settled / failed / unknown; unknown giữ reservation đến khi đối soát, không tự hoàn ngân sách. Giới hạn gắn campaign/task, tồn tại qua chat. Chưa được giao render thì chỉ làm kế hoạch/prompt.

## 4. Sản xuất và chọn master

Hồ sơ theo [production guide](../04-Productions/README.md) và [output contract](../04-Productions/OUTPUT-CONTRACT.md), tương ứng photo_post/video; caption theo CAPTION.md, source đọc theo SOURCE-ROUTING.md. Kế thừa Nature-Studio về brief/concept, inputs/prompt/settings/output từng attempt, review, selection và summary; không bê luật thời lượng/model của Underwater. Yêu cầu concept/prompts kết thúc ở output văn bản, không tự generate.

Mỗi attempt bất biến. Ghi planned và actual riêng; model actual unknown nếu tool không công bố. Output thành asset có hash, provenance và dependencies (cast sheet, artwork, plate, voice/music). Đặt artwork lên áo từ mockup thật; kiểm typography sau motion/warp, không chỉ ở frame đầu.

QA artifact theo [quality](quality.md). Sửa lỗi hậu kỳ được thì không render lại toàn cảnh vô cớ. Chọn master bằng selection explicit, không theo tên final/latest. Giữ bản bị loại cùng lý do để không mất bài học.

## 5. Tạo release theo nền tảng

Release trỏ master/derived export cụ thể; chứa thứ tự slide/media, caption/title, cover, CTA, URL/UTM, account, platform, audio/license, disclosure và lịch/timezone. Checklist platform kiểm đúng file xuất: crop/vùng UI, text đọc được, âm, quyền nhạc và loại post hỗ trợ. Không giả link caption luôn bấm được hoặc account nào cũng có product tag.

Tái dùng visual không đồng nghĩa tái dùng nhạc. Master sạch có thể dùng nhiều nơi; audio từ thư viện của một nền tảng chưa chứng minh quyền ở nơi khác.

## 6. Duyệt đúng gói và đăng

Chủ dự án nhận preview gói cụ thể. QA pass khác user approval. Duyệt lưu evidence, người, thời gian, digest gói và phạm vi gồm account + lịch. Thay media, caption, URL, account, disclosure, rights hoặc lịch ngoài phạm vi đã cho phép tạo revision mới và cần duyệt lại. Rà URL/quyền và các claim giá/offer nếu gói có sử dụng ngay trước lịch đăng; đổi offer cũng làm gói cũ cần xét lại.

Publisher chỉ đăng trong quyền cụ thể đã được giao. MVP đăng thủ công từ gói đã duyệt và ghi receipt. Không đưa auto-post vào giai đoạn đầu chỉ vì có adapter API.

Đăng lỗi/timeout → dispatch_unknown → đối chiếu scheduler/provider/native account trước retry. Idempotency key theo release digest + account; nếu provider không hỗ trợ thì giữ claim/lock, tìm post/receipt trong cửa sổ gửi, unresolved thì dừng retry và nhờ người vận hành kiểm account. Mục tiêu tránh trùng, không tuyên bố đảm bảo exactly-once trên hệ thống ngoài.

## 7. Xác minh và đo

Đã upload không đủ để published_verified: cần native post ID, URL/receipt và xác nhận trạng thái có thể xem theo visibility đã duyệt. Scheduled chưa là published. Đăng thủ công cũng phải có receipt. Lưu snapshot ngay khi có dữ liệu, rồi các mốc 24h/72h/7d/30d là lịch đo đề xuất; thiếu quyền hoặc chưa đến mốc ghi pending/unavailable, không tạo automation ngoài yêu cầu.

Phân tích theo [measurement](../06-Insights/MEASUREMENT.md), trả quyết định: giữ, sửa hook, sửa CTA/đích, mở rộng có kiểm soát hoặc dừng. Đóng phiên ghi trạng thái hiện hành; lesson bắt đầu candidate, chỉ active theo bằng chứng phù hợp.
