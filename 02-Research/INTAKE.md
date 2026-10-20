# Hai đầu vào sáng tạo, một lõi sản xuất

Version 0.1.4 · 2026-10-20. Cấu hình đọc được bằng máy: [entrypoints.json](../00-Standards/entrypoints.json). Đây là routing thiết kế; chưa có dispatcher hoặc slash command được cài.

## Chọn đầu vào từ yêu cầu thực

| entry_mode | Đầu vào để bắt đầu | Cách phát triển | Không bắt buộc |
|---|---|---|---|
| product | Một sản phẩm/collection từ website, hoặc product snapshot đã có nguồn | Hiểu câu áo/hình/giọng → căng thẳng đời thường → persona/tình huống → ý tưởng gốc → chọn cách thể hiện | Watchlist, reference viral hoặc case đối thủ |
| reference | Link/file media tham khảo, hoặc reference record đã lưu | Phân tích phần thực truy cập → cơ chế → giữ/thay theo brand → ý tưởng Errare; chọn sản phẩm khi nội dung cần | Chọn ngay sản phẩm trước lúc phân tích reference |
| hybrid | Có cả sản phẩm/collection và media tham khảo | Khóa thông tin sản phẩm, học chức năng mẫu và phát triển cách thể hiện phù hợp | Đổi câu áo hoặc phát triển lại sản phẩm để giống mẫu |

Nếu chỉ đưa sản phẩm thì chạy product, không tự tìm đối thủ như gate bắt buộc. Nếu đưa media và giao chuyển thể thì chạy reference. Nếu có cả hai và yêu cầu dùng cả hai thì hybrid. Một sản phẩm xuất hiện tình cờ trong brief reference không tự chuyển task thành hybrid; mode thể hiện ý định nguồn sáng tạo đã chọn.

Thiếu file/chi tiết cần thiết thì làm phần đủ dữ kiện, ghi thiếu. Product URL chỉ cần đọc đủ sản phẩm/collection đang dùng, không bắt sync toàn website. Không đọc được câu áo/hình thì không bịa; có thể làm concept nháp và đánh dấu chưa đủ để QA artwork.

## Mode nguồn độc lập với task và format

- task: concept / prompts / generate / review / revision / caption / close.
- format: photo_post / video. Photo_post có layout single/carousel; video mặc định là frame pair prompt (first=t0/last=duration_s) + video prompt + caption. image/carousel/text cũ chỉ giữ lịch sử theo mapping tương thích.
- Gói đầu ra theo 04-Productions/OUTPUT-CONTRACT.md; caption/nguồn dùng chung theo 00-Standards/CAPTION.md và SOURCE-ROUTING.md.
- Campaign là tùy chọn; một nội dung độc lập không cần tạo campaign giả để được sản xuất.
- Mode không đổi khi sửa caption hoặc đóng phiên. Revision giữ Content ID, ý định đã chốt và tạo attempt mới khi có output mới.
- Chỉ task generate kèm yêu cầu tạo media thật và ngân sách phù hợp mới gọi công cụ sinh. Yêu cầu post ảnh hoàn chỉnh bao gồm tạo/export ảnh trong quyền/budget; gói video mặc định chỉ viết prompt. Concept/prompts không tự render; close không tự duyệt hoặc đăng.

## Đọc đúng nguồn, không đọc toàn kho

| Nhiệm vụ | Nguồn cần đọc |
|---|---|
| Product concept | SCOPE, BRAND, snapshot website liên quan, lịch sử/candidate đang chọn, active lesson phù hợp; không nạp watchlist |
| Reference concept | SCOPE, BRAND, phân tích media thực/coverage, SOCIAL-RESEARCH, lịch sử và lesson; product snapshot khi đã chọn để dùng |
| Hybrid concept | Hợp của hai nhóm trên, loại phần trùng |
| Viết prompt video | Brief/concept đã chốt, bắt buộc shared first/last frame prompt + video prompt, duration/frame plan, US-AUDIENCE/PHONE-MEDIA, refs nguồn và profile model/interface liên quan; caption đọc guide chung |
| Generate/review | Attempt đang làm, input/output thật, QA phù hợp, quyền/budget/tool; không đọc lại mọi nghiên cứu |
| Caption/revision | Bản được chọn và phụ thuộc bị ảnh hưởng, giọng brand, nền tảng đích; không brainstorm lại toàn câu chuyện |
| Close | Summary, attempts/feedback/metrics thực đã có và lesson liên quan; không buộc đã đăng |

History và memory được query theo Table/persona/mechanism/format và điều kiện, rồi mở record gốc liên quan. Không có lesson thì vẫn làm được; candidate không áp thành luật. Thiếu index thì tìm hồ sơ thật, không suy không có lịch sử. Không giữ cache/citation hết hạn làm bằng chứng nguồn còn hiện hành.

## Ranh giới sáng tạo

Product mode phát triển ý tưởng độc lập, rà độ mới ở setup/hành vi/nhân quả/punchline, không chỉ đổi cast/địa điểm. Reference mode được giữ cơ chế tham khảo có chủ đích; không ép đổi câu chuyện chỉ để khác mẫu. Vẫn tạo biểu đạt Errare riêng, kiểm quyền dùng asset, tính đúng sản phẩm và brand. Không dùng độ viral của mẫu để nhận kết quả Errare chắc chắn viral.

Các ví dụ như “Từ áo OVT-10 viết ý tưởng Reel”, “Phân tích/chuyển thể video này”, hoặc “Dùng áo này với cơ chế video kia” mô tả ba mode, không cấp ID production, tiêu tiền hoặc tạo media chỉ vì được trích dẫn trong tài liệu.
