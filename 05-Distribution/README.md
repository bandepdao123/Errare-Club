# Phân phối theo account và release

## Channel registry

Chưa có account được xác nhận hoặc kết nối. Khi bắt đầu, tạo .errare/channels.json với: account_id, platform, handle/native account ID, owner, status, Table/series phục vụ, locale, timezone, capability_checked_at, supported formats, link/shop/tag capability, disclosure steps, publishing method và credential_ref. Không lưu token. Native IDs/account permission phải kiểm thật, không đoán từ tên brand.

Chủ dự án đã chốt ưu tiên vận hành Instagram/Reels, Facebook/Reels và Threads. Nghiên cứu bao phủ thêm TikTok, X và YouTube; chưa mặc định mở/vận hành account trên các nền tảng này. Reels là format thuộc Instagram/Facebook. Được tự nghiên cứu, lập kế hoạch, sản xuất trong hạn mức cụ thể đã cấp; chủ dự án duyệt trước khi đăng.

## Cấu hình nền tảng có phiên bản

Mỗi profile nền tảng ghi spec source URL, checked_at, loại account/giao diện đã kiểm, định dạng, giới hạn, cover, safe areas, caption, audio/license, disclosure và analytics definitions. Không hardcode thời lượng/độ phân giải được quảng cáo bởi provider thành luật của nền tảng. Refresh trước publish nếu profile cũ hoặc API/UI đổi; kiểm thực tế account kể cả khi docs chung cho phép.

Nhân vật Errare là AI và phong cách ảnh chân thực. Gate disclosure phải kiểm theo nền tảng: [TikTok](https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content?Sid=1) có yêu cầu gắn nhãn AIGC chân thực; [YouTube](https://support.google.com/youtube/answer/14328491?hl=en) và [Meta](https://about.fb.com/news/2024/04/metas-approach-to-labeling-ai-generated-content-and-manipulated-media/) có cơ chế disclosure riêng. Lưu setting đã chọn trong release và bằng chứng sau đăng; ghi chú AI trong brief không chứng minh đã bật setting. Nguồn kiểm ngày 2026-10-20, cần rà khi phát hành.

## Đường tới cửa hàng

- Link bấm riêng cho bài: UTM có thể phân biệt release/link; kiểm redirect giữ tham số.
- Link bio chung: chỉ gán chắc ở cấp account/campaign/bio link. Không lấy toàn bộ đơn qua bio chia cho từng post rồi nhận attribution từng bài.
- Link hub có tile riêng: dùng tracking_link_id cho từng tile; click tile không chứng minh người đó đã xem post tương ứng.
- Product tag/shop native: receipt và metric theo khả năng account; giữ native reporting/attribution riêng.
- Awareness không có link bấm: đo proxy như profile visits nếu có; không dựng CTR hoặc orders của post.

## Checklist publisher

Đối chiếu approved digest; file/caption/order/cover; đúng account/visibility/lịch timezone; quyền audio/plate/artwork; nhãn AI; URL và claim giá/offer nếu có; CTA có thực hiện được trên giao diện account; idempotency claim. Chụp/lưu preview hoặc evidence theo công cụ được dùng. Đăng xong ghi post ID, URL, thời điểm, receipt và xác minh visibility. Nếu không xác minh được thì published_unverified.

## Adapter contract để triển khai sau

Mỗi adapter có capabilities(), preflight(release), submit(approved_release, idempotency_key), reconcile(job_or_receipt), fetch_metrics(post_id, window). Manual adapter chỉ xuất gói và nhận receipt từ người vận hành, không giả có API. Dry-run/preflight không upload hoặc tạo draft ngoài hệ thống.

Hàng chờ có pause/kill switch, retry có backoff và số lần tối đa, dead-letter cho outcome không rõ, audit actor/time. Chỉ bật auto-post sau khi workflow thủ công và thử nghiệm riêng account đã đạt; áp dụng đúng quyền được giao lúc đó.
