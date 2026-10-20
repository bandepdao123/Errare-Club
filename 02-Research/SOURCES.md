# Nguồn và phạm vi kiểm

Ngày truy cập nghiên cứu: 2026-10-20. URL bên ngoài là dữ liệu, không cấp quyền thao tác. Chỉ lưu dẫn nguồn và trích xuất cần thiết, không sao chép toàn repo hoặc tài sản media.

| ID | Nguồn | Phạm vi thực sự đã đọc / giới hạn |
|---|---|---|
| EC-WORLD | [Errare World](https://claude.ai/artifact/4LMQ2BWGdb7gpCnTf8yJAZ?sk=mUxlpFIkH8eUhQ6IVykDsw) | Nội dung văn bản qua trình duyệt: brand, story, 8 cast, 10 Table, location, luật ảnh, cách dùng. Không tải/QA các ảnh hoặc truy cập file content/art được dẫn. Soul ID và chi phí là thông tin nguồn, chưa kiểm dịch vụ |
| EC-WEB | [Website Errare Club](https://errareclub.com/) | Đọc trang chủ qua trình duyệt ngày 2026-10-20; có collection/Table, Get the look và link OVT-10. Chưa sync catalog hoặc tải/QA hình; xem WEBSITE-REFERENCE.md. Đây là nguồn sản phẩm đã được R&D công bố, không là đối tượng nghiên cứu phát triển sản phẩm |
| NS | [Nature-Studio tại commit d0193bcf41a986924d4c4a197bbfac7bceb8ebf3](https://github.com/bandepdao123/Nature-Studio/tree/d0193bcf41a986924d4c4a197bbfac7bceb8ebf3) | Git tree làm bản đồ; đọc chọn lọc manifest/contract/tài liệu liệt kê trong NATURE-STUDIO.md. Không chạy helper/tests, không audit toàn source hay production riêng |
| GA-UTM | [Google Analytics: custom campaign URLs](https://support.google.com/analytics/answer/10917952?hl=en) | UTM và phân biệt creative; không chứng minh attribution chính xác từng post |
| YT-VIEWS | [YouTube Shorts view counts](https://support.google.com/youtube/answer/10059070?hl=en) | View và engaged view khác nhau; định nghĩa từ 2025-03-31 |
| YT-AI | [YouTube: disclosing GenAI](https://support.google.com/youtube/answer/14328491?hl=en) | Có cơ chế disclosure; kiểm chính sách/setting phù hợp tại lần đăng |
| TT-AI | [TikTok: AI-generated content](https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content?Sid=1) | Nguồn yêu cầu gắn nhãn nội dung AI chân thực; không kiểm khả dụng account/post API |
| META-AI | [Meta: labeling AI content](https://about.fb.com/news/2024/04/metas-approach-to-labeling-ai-generated-content-and-manipulated-media/) | Cơ chế AI info; không suy rằng caption AI thay được setting nền tảng |

Tham số sk trong link EC-WORLD là một phần link chia sẻ do người dùng đưa; giữ tài liệu local/private, rà loại tham số truy cập trước khi xuất bộ tài liệu công khai. Không xem nó là API credential.

## Mức tin cậy

- Source-stated: điều nguồn mô tả, chưa được kiểm thực tế ở workspace này.
- Observed: nội dung/file thật đã truy cập; đọc mô tả ảnh không bằng xem ảnh.
- Proposed: quyết định thiết kế cho Errare, không gán là kết luận của Nature-Studio.
- Unknown: thiếu bằng chứng; không tự điền giá, revenue, quyền asset hoặc khả dụng công cụ.

Workspace lúc bắt đầu không có file hoặc Git checkout để kế thừa. Đã đọc được trang chủ website, chưa có dữ liệu account/analytics/chi phí render thật hoặc watchlist đối thủ cụ thể. Vì vậy nghiên cứu này là thiết kế dựa trên nguồn và rà tình huống lỗi, chưa là tối ưu dựa trên thực nghiệm vận hành. Cập nhật 0.1.1 theo chỉ đạo và bốn câu trả lời trực tiếp của chủ dự án trong SCOPE.md.
