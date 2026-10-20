# Phạm vi hiện hành — 0.1.4

Chốt theo chỉ đạo và câu trả lời trực tiếp của chủ dự án, ngày 2026-10-20. Tài liệu này cập nhật phạm vi bản thiết kế 0.1.0; không phải phê duyệt một ngân sách cụ thể hoặc một bài đăng.

## Nhiệm vụ chính

Hai đầu vào độc lập: (1) sản phẩm/collection trên website → insight/persona/tình huống → concept gốc; (2) media tham khảo → phân tích cơ chế → concept Errare. Có thể kết hợp cả hai (hybrid). Hội tụ vào một lõi: brief/concept → prompt package → media khi được giao → QA/attempt sửa → chọn master → release → chủ dự án duyệt → đăng/đo → tổng kết/bài học, kế thừa cách quản lý sản xuất Nature-Studio. Xem 02-Research/INTAKE.md và 04-Productions/README.md.

- Bộ phận R&D chịu trách nhiệm nghiên cứu và phát triển sản phẩm. Hệ thống media không lựa chọn chất liệu, thiết kế sản phẩm, định giá, quản lý tồn hoặc xây checkout.
- Kho Drive được chủ dự án chỉ định trong 01-Brand/product-sources.json là hồ sơ sản phẩm chính; [errareclub.com](https://errareclub.com/) bổ sung thông tin đang công bố. Hệ thống đọc full hồ sơ đúng SKU/tên/câu áo khi được hỏi và nhập ảnh local để xây media; không tự phát triển lại sản phẩm hoặc nạp toàn catalog vào context mỗi lượt.
- Nghiên cứu tập trung vào ảnh, carousel, video/Reels/Shorts và text/thread của đối thủ hoặc kênh tham khảo trên Instagram, Facebook, Threads, TikTok, X và YouTube. Reels là format thuộc Instagram/Facebook, không phải một mạng riêng.
- Chủ dự án cung cấp watchlist ban đầu; về sau hệ thống được chủ động hoặc cùng chủ dự án khám phá thêm. Chưa có link cụ thể thì không ghi đã nghiên cứu đối thủ.
- Kênh vận hành giai đoạn đầu: Instagram/Reels, Facebook/Reels và Threads. TikTok, X, YouTube nằm trong phạm vi nghiên cứu; chưa mặc định mở hoặc vận hành account trên đó.
- Tự chủ nghiên cứu, lập kế hoạch và sản xuất trong ngân sách đã được cấp. Hiện chưa có mức ngân sách cụ thể; không coi lựa chọn mức tự chủ là quyền chi tiền không giới hạn.
- Chủ dự án duyệt trước khi đăng. Có thể chuẩn bị và xếp hàng local; chưa tự gửi nội dung/draft/lịch sang nền tảng ngoài khi chưa có gói được duyệt và quyền thao tác account.
- Được xây dựng lại hệ nhân vật. Tám cast cũ/Soul ID giữ làm tham khảo lịch sử, không là roster bắt buộc hoặc đã chọn cho hệ mới. Persona suy từ sản phẩm/media là giả thuyết sáng tạo, không tự là chân dung khách hàng đã được chứng minh.

## Ranh giới đo lường

Chính: output/cost/QA, hiệu quả bài và sức khỏe kênh, tương tác có ý nghĩa, profile visits/clicks/traffic về website khi có dữ liệu. Mua hàng vẫn là mục tiêu kinh doanh phía sau; hệ thống chỉ nhận feedback chuyển đổi tổng hợp nếu được cung cấp. Không bắt buộc quyền đơn hàng, event checkout, dedup transaction hoặc tích hợp store để bắt đầu sản xuất/quản lý social. Các phần commerce sâu trong MEASUREMENT.md là extension chưa kích hoạt, không là exit gate MVP.

## Những đầu vào còn thiếu theo tác vụ

- Bắt đầu nhánh nghiên cứu đối thủ: cần các link watchlist ban đầu do chủ dự án cung cấp. Thiếu watchlist không chặn nhánh sản phẩm; có thể bắt đầu từ một URL sản phẩm/collection hoặc snapshot đã có nguồn.
- Vận hành kênh thật: cần account/handle và quyền phù hợp, chỉ hỏi khi đến bước đó.
- Sinh media trả phí: cần công cụ và hạn mức/nguyên tắc ngân sách cụ thể.
- Campaign tùy chọn; một yêu cầu media độc lập không cần tạo campaign giả. Nguồn sản phẩm/reference và hai gói photo_post/video là các chiều độc lập. Post ảnh gồm ảnh thật đủ size đích + caption Anh Mỹ/3–5 hashtag. Video gồm một frame pair prompt cho hai ảnh riêng first=t0/last=duration_s + prompt video + caption; chưa render nếu chỉ giao prompt. Toàn creative hướng Mỹ; visual như điện thoại, video do người cầm với góc/rung hợp cảnh, cinematic chỉ khi yêu cầu. Skill ảnh dùng Codex ImageGen, không tự chuyển provider. Carousel là layout ảnh, text-only cũ giữ lịch sử.
- CSDL/nguồn chuẩn được tham chiếu theo SOURCE-ROUTING. Workspace 0.2.0 đã cài bảy skill er-* project-local và helper routing/metadata; chưa nạp catalog/database runtime hoặc kết nối account. Triển khai skill không là quyền tự chạy ảnh/đăng trong lần cập nhật hệ thống.
- Không cần hỏi thêm quyết định kiến trúc cốt lõi ở thời điểm này. Không đặt thêm câu hỏi sản phẩm thuộc R&D.
