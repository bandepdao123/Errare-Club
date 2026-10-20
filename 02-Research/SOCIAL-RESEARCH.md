# Nghiên cứu media đối thủ và chuyển thành sáng tạo Errare

Phạm vi theo [SCOPE](../07-Operations/SCOPE.md). Skill er-nghiencuu đã dùng workflow này từ workspace 0.2.0; chưa có watchlist hoặc dữ liệu đối thủ đã nhập.

Đây là nhánh reference/hybrid theo [INTAKE](INTAKE.md), không là gate chung cho mọi sáng tạo. Nhánh product được đi thẳng từ sản phẩm/collection đến persona, tình huống và concept, kể cả khi chưa có watchlist/media đối thủ. Hai nhánh dùng chung lõi sản xuất và lịch sử.

## 1. Watchlist có vai trò

Khởi tạo bằng link chủ dự án gửi. Record gồm competitor_id, account URL/handle, platform, role = direct_competitor / audience_adjacent / format_reference, audience relevance, ngôn ngữ/thị trường, lý do theo dõi, nguồn đề xuất và ngày rà. Hệ thống được đề xuất thêm về sau, không gọi mọi kênh viral là đối thủ trực tiếp.

Watchlist local không đồng nghĩa follow account ngoài nền tảng. Phân biệt quyền nghiên cứu đọc công khai với quyền tương tác/quản lý account. Không tự follow, comment, repost hoặc inbox từ nhiệm vụ research.

## 2. Thu thập và kiểm tín hiệu

Record media: reference_id, canonical post URL/native ID, account/platform, format, published_at nếu có, observed_at, metrics công khai thực thấy, định nghĩa/đơn vị, dữ liệu nguồn hoặc capture, access coverage và availability. Dữ liệu thiếu để null; không suy reach, shares, saves, retention hay doanh thu của đối thủ từ số like/view.

Tách ba nhãn: candidate (tín hiệu đáng kiểm), outlier_supported (nổi bật so với baseline account/format/tuổi bài được ghi rõ), và insufficient_data. Nếu chỉ biết số view cao thì ghi high_visible_views, không nhận đã chứng minh viral. So với bài thường của cùng account, cùng format và thời điểm khi có thể; ghi cỡ mẫu, cách lấy mẫu, paid/collab/repost nếu biết. Không dùng một ngưỡng view chung cho mọi kênh hoặc follower ratio như bằng chứng duy nhất.

Lấy cả bài thành công lẫn một số bài thường/không thành công để giảm chọn mẫu thiên lệch. Phân biệt cùng nội dung cross-post/repost bằng canonical/derived_from, không đếm thành nhiều bằng chứng sáng tạo độc lập. Public metrics là snapshot có thời điểm, không nhận có growth velocity nếu chỉ đo một lần.

## 3. Phân tích đúng loại media

| Loại | Phần cần tiếp cận | Trường phân tích |
|---|---|---|
| Ảnh | Ảnh thật ở kích thước đọc được | Bố cục, điểm chú ý, chữ, tình huống, cảm xúc, caption/CTA |
| Carousel | Thứ tự và toàn bộ slide liên quan | Cover hook, lý do vuốt, diễn tiến, payoff, slide kết |
| Video/Reels/Shorts | Clip và âm theo khả năng thực | Hook/beat/timecode, camera/motion, dựng, audio, reveal/payoff, loop, caption |
| Threads/X/text | Nội dung gốc, chuỗi và ngữ cảnh truy cập được | Câu mở, voice, góc nhìn, nhịp chuỗi, reply/quote mechanism, lời mời tương tác |

Chỉ có thumbnail/transcript thì ghi partial; không nhận đã xem chuyển động/nghe âm. Không có media gốc truy cập được thì vẫn lưu metadata/link, để analysis_pending. Không chuyển transcript-only thành full-video analysis. Comment là mẫu ngôn ngữ/giả thuyết audience có nguồn và phạm vi, không đại diện toàn bộ người xem.

Mỗi phân tích tách: điều quan sát → cơ chế sáng tạo giả định → bằng chứng hỗ trợ → cách áp dụng → giới hạn. Không mặc định audio/hook nào gây viral nếu không tách được biến.

## 4. Chuyển thể có chủ đích

Từ reference rút creative mechanism: ví dụ tình huống dễ nhận mình, reveal, đối lập lời/hành động, escalation, visual gag hoặc tương tác giữa caption và ảnh. Các cơ chế là gợi ý mở, không danh sách đóng.

Opportunity card nối reference_ids → insight/hypothesis → product/collection refs từ website → persona đề xuất → ý tưởng Errare riêng → format/channel fit → lý do chia sẻ → cách đo. Không bắt một reference phải có ngay SKU; có thể nhóm theo Table hoặc insight rồi chọn sản phẩm phù hợp sau. Không tự thay câu in hay phát triển sản phẩm mới để khớp mẫu.

Giữ cơ chế có ích, tự viết tình huống/thoại/visual phù hợp brand; không sao chép footage, câu độc đáo, khuôn mặt hoặc artwork của đối thủ. Quyền đọc/tham khảo không tự cấp quyền tái đăng asset/nhạc. Sản phẩm và cast mới cần khớp typography/identity ở artifact thật.

## 5. Kho tham chiếu và vòng học

Runtime đề xuất .errare/research/watchlist.json, references/<reference-id>/ và opportunities/. Metadata gọn để tìm theo platform/format/insight/mechanism/Table; chỉ mở media/phân tích cần dùng. Media tải về khi có quyền và cần thiết; không mirror toàn bộ account hoặc lưu link tạm làm bằng chứng duy nhất.

Mỗi content ghi reference IDs và phần học/đổi. Sau đăng nối kết quả Errare về opportunity/hypothesis; hiệu quả của đối thủ không tự thành hiệu quả của Errare. Bài học active cần điều kiện và dữ liệu; không tạo công thức bảo đảm viral.

Research routine theo batch/lịch sẽ chốt sau watchlist, khả năng truy cập và công suất thực. Chưa tạo automation, scraper hoặc kết nối social từ bản thiết kế này.
