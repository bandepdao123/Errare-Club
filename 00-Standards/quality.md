# QA theo artifact và mục tiêu

Version 0.1.0. Mọi review ghi artifact ID/hash, người/phương pháp, thời điểm, checklist version, phạm vi đã tiếp cận, finding và kết quả kiểm lại. Trạng thái từng mục: pass / fail / not_checked / not_applicable; not_applicable có lý do.

## Bổ sung theo hai gói đầu ra 0.1.4

Photo_post chỉ hoàn chỉnh khi có ảnh thật cho đủ target placements/kích thước đã chọn và caption theo [CAPTION](CAPTION.md). Kiểm kích thước file xuất thực, crop/vùng UI và độ đọc chữ trên từng variant; không lấy master pass thay mọi crop. Single/carousel dùng cùng chuẩn, carousel kiểm cả thứ tự.

Video prompt package bắt buộc đủ frame pair prompt (một prompt chung yêu cầu hai ảnh riêng first/last) + video prompt + caption. Kiểm duration_s dương, first=t0, last=duration_s, trạng thái đầu/cuối và diễn tiến/continuity/đường đi camera khả thi. Ví dụ 8/10/15s phải lần lượt kết ở t8/t10/t15, không lấy frame giữa thay ending. Chỉ chấm text/source/model feasibility; motion/audio/visual render = not_checked nếu chưa có media thật. Caption en-US, 3–5 hashtag; đếm tag không chứng minh giọng native.

Nếu tạo cặp frame thật: đúng hai file riêng, không collage/contact sheet, gán first/last rõ trong metadata, không thêm nhãn timestamp lên ảnh. Kiểm identity/câu áo/không gian/ánh sáng và các thay đổi cuối có nguyên nhân trong video plan; thiếu một ảnh = partial, không pair complete. Prompt chung không tự chứng minh tool tạo đủ output hoặc last là trạng thái đúng.

Mọi creative phải theo [US-AUDIENCE](US-AUDIENCE.md), không chỉ caption. Ảnh/video đời thường như điện thoại theo [PHONE-MEDIA](PHONE-MEDIA.md); video có người cầm với góc/rung tương ứng hành động, không rung phô diễn hoặc camera điện ảnh nếu chưa được yêu cầu. Kiểm actual tool receipt cho ảnh = Codex ImageGen khi đã tạo, không suy từ tên prompt/model.

## Ba cổng khác nhau

### Kiểm độ tự nhiên và kỹ thuật trước khi nhận đủ gói

Tham chiếu PHONE-MEDIA và đúng placement trong INSTAGRAM-MEDIA nếu đích Instagram; không chép checklist vào từng skill. Trong review hiện có, ghi evidence ngắn cho: (1) hành động/tư thế có lý do ngoài việc khoe áo, (2) biểu cảm khớp quote/persona/sự kiện, (3) người cầm máy và chuyển động có thể thực hiện, (4) không gian Mỹ/ánh sáng/texture có tính đời thường, (5) artwork đọc được và actual canvas/export đúng target. Cảnh tạo dáng rõ, ánh sáng/quang học điện ảnh không được giao, rung giả quá mức hoặc bối cảnh bất hợp lý là lỗi cần sửa, dù ảnh đẹp. Bối cảnh gọn hoặc ảnh sắc nét tự nó không phải lỗi.

Prompt package chỉ kiểm được ý định/khả thi; naturalness của render = not_checked nếu chưa có ảnh/clip. Khi có ảnh: xem cả file và kích thước hiển thị nhỏ; khi có video: kiểm chuyển động suốt clip. Không chấm motion từ hai frame. Không dùng điểm số tổng để bù sai artwork/canvas hoặc lỗi pose rõ. Tách creative QA khỏi xác minh đường đăng; profile pending không ngăn tạo master nhưng chưa đủ release-ready.

| Cổng | Có thể chứng minh | Không chứng minh |
|---|---|---|
| Text/concept review | Ý định, liên kết brand/sản phẩm, logic, khả năng làm | Render đẹp, giữ chân hay mua hàng |
| Artifact/release QA | File thật phù hợp brief và xuất bản | Người dùng đã duyệt, hiệu quả social |
| Post measurement | Kết quả đã quan sát theo nguồn và tuổi bài | Quan hệ nhân quả hoặc lặp lại thành công |

## Checklist theo loại

| Nhóm | Kiểm bắt buộc khi liên quan | Lỗi chặn phát hành |
|---|---|---|
| Brand/story | Cảnh đọc được, tự giễu ấm, lỗi chính/punchline khớp | Sai giọng, chế giễu người, claim bịa |
| Cast | Mặt/tóc/kính/trang phục, số người, continuity | Trôi danh tính hoặc cấu tạo sai rõ |
| Product | Artwork, câu chữ/dấu/ngắt dòng, placement, màu/form | Sai thiết kế, chữ biến dạng, giả thông số |
| Lifestyle | Ánh sáng, người chạm cảnh, lỗi, vật đỏ/grade | Bố cục mâu thuẫn brief hoặc lỗi ghép rõ |
| Video | Timeline, chuyển động, tay/ngón, identity/print khi reveal/ending | Frame đầu đạt nhưng đoạn sau hỏng |
| Audio | Nghe thật, sync, voice/music quyền phù hợp, mức theo brief | Âm lỗi hoặc chưa có quyền; meter không thay nghe |
| Copy | Anh Mỹ tự nhiên, đúng câu áo, CTA/claim | Caption hứa sai hoặc trái nội dung |
| Export | File mở được, raster/aspect/duration, UI-safe/text readability | Chữ bị cắt hoặc payload không hợp account |
| Distribution | Caption/cover/order, link/UTM, disclosure, account, lịch | Sai account/link, thiếu nhãn bắt buộc |

Không áp checklist mặt/cảnh người cho flatlay, typography hoặc copy-only. Brief chỉ định format và ngoại lệ; không dùng not_applicable để né lỗi liên quan. Bản đen trắng cần kiểm độ đọc/contrast riêng, vật đỏ đối chiếu master màu.

## Vòng kiểm thực tế

1. Producer tự kiểm đúng brief, artifact và phiên bản.
2. Pass reviewer đối chiếu lại từ file, không chỉ đọc kết luận producer. Khi cùng operator thực hiện phải ghi self-review. Không gọi hai lượt của cùng AI là audit độc lập.
3. Sửa lỗi chặn và kiểm lại artifact mới; chỉ chạy lại các mục bị ảnh hưởng và phụ thuộc. Thay artwork ảnh hưởng typography trong motion/crop; caption-only không buộc render lại visual đã giữ nguyên.
4. Chủ dự án duyệt release cụ thể; quyền duyệt không tự biến QA fail thành pass. Nếu muốn ngoại lệ, ghi criterion, artifact, phạm vi và lý do. Chưa rõ quyền/license hoặc vi phạm yêu cầu nền tảng không được miễn chỉ bằng đổi điểm số.

## Giới hạn khả năng xem/nghe

Chỉ có ảnh mẫu frame thì motion/audio = not_checked. Chỉ có transcript thì không nhận đã nghe texture/sync. Video review ghi khoảng thời gian đã xem; kiểm toàn clip và điểm lộ câu áo/kết thúc khi công cụ cho phép. Nếu chưa có khả năng, giao người reviewer phần còn thiếu; vẫn tiếp tục các kiểm khác. Không nhận QA toàn bộ từ metadata, thumbnail hoặc prompt.

## QA thiết kế khác QA nội dung

Validator hiện tại chỉ kiểm liên kết/ID/dữ liệu nền. Bộ tình huống ở 08-Evaluation kiểm logic tài liệu, chưa chạy workflow sinh ảnh/đăng/attribution thật. Không dùng kết quả đó để bật QA pass cho bất kỳ media nào.
