# Caption dùng chung cho hai gói media

Version 0.1.4. Policy máy đọc ở [media-contract](media-contract.json); skill không chép lại hoặc giữ bản quy tắc riêng. [US-AUDIENCE](US-AUDIENCE.md) áp cho toàn concept/persona/visual/thoại/prompt, không chỉ caption.

Caption cho người Mỹ, locale en-US: viết trực tiếp bằng tiếng Anh Mỹ tự nhiên, không dịch sát một bản Việt, không ép slang hoặc stereotype. Ngắn/dài theo cảnh, ý định và nền tảng, không ấn một số từ cho mọi bài. Tự giễu ấm áp, câu mở có ích, không kể lại toàn bộ punchline trước lúc người xem thấy. Câu áo, tên sản phẩm và claim phải đối chiếu nguồn gốc.

Mỗi caption có body + 3–5 hashtag liên quan nội dung/brand/audience. Áp dụng cùng mặc định này cho caption video để thống nhất hai gói; đây là quy chuẩn dự án, không là tuyên bố hashtag làm tăng reach. Không dùng tag trending không liên quan hoặc bịa hashtag địa điểm khi cảnh không có nguồn.

Lưu body và hashtags[] riêng, render hashtag đúng một lần sau body; body không lặp lại hashtag để tránh đếm sai. Hashtag phải duy nhất sau chuẩn hóa hoa/thường. Bản giao người dùng là caption hoàn chỉnh có hashtag, không chỉ trường dữ liệu rời. Một caption cho mỗi bản đích, không tự viết ba biến thể nếu không được giao.

QA caption: đọc như một người Mỹ giao tiếp trong đúng tình huống, kiểm nghĩa/idiom/nhịp/cường điệu, phù hợp persona và ảnh hoặc video dự kiến; check câu áo/claim/CTA, đếm 3–5 hashtag và không trùng. Đếm hashtag chỉ là kiểm cấu trúc, không chứng minh native quality. Caption video prompt-only phải khớp chuyện dự kiến, không nhận đã mô tả render đã xem.

Sửa caption chỉ đọc cảnh đã chốt, caption được chọn, guide này và profile đích liên quan; không cần nạp lại toàn watchlist/model/cast catalog hoặc sinh lại ảnh. Nếu caption đổi ý nghĩa/claim làm ảnh hưởng gói duyệt, tạo release revision theo contract.
