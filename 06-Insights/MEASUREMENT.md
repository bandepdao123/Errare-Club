# Đo hiệu quả: từ nội dung đến mua hàng

Version 0.1.1. Phạm vi chính là media/kênh và traffic về website. Theo SCOPE, không bắt buộc kết nối store/đơn/checkout để chạy social. Các mục orders/net sales/transaction/refund phía dưới chỉ là extension nhận feedback tổng hợp từ bộ phận website khi có, chưa kích hoạt và không là công việc R&D hoặc gate MVP. Chưa có account/store/analytics data. Các mốc và nguyên tắc ra quyết định dưới đây là thiết kế pilot, không phải benchmark ngành hay kết quả đã đo.

## Hai bảng kết quả song song

Production scorecard: thời gian tới artifact đạt, chi phí toàn bộ attempts và hậu kỳ, lỗi lặp, số vòng sửa, continuity cast/artwork, tỷ lệ QA đạt. Cost per accepted asset tính cả attempt bỏ; cost chưa biết phải nêu coverage, không giả bằng 0.

Content/business scorecard theo post/release/Table/campaign:

| Tầng | Chỉ số gợi ý | Điều kiện đọc |
|---|---|---|
| Phân phối | Reach, impressions, native views | Giữ định nghĩa gốc, không cộng reach thành unique audience xuyên kênh |
| Chú ý | Watch time, completion, retention theo mốc, engaged views | Chỉ lấy chỉ số nguồn thực có; so cùng format/duration/tuổi bài |
| Lan truyền | Shares, saves, comments có ý nghĩa, profile visits | Tỷ lệ ghi rõ mẫu số; không coi mọi comment là tín hiệu tốt |
| Ý định mua | Outbound clicks, tagged sessions, product views, add_to_cart | Click và session là hai metric khác; availability theo link/account |
| Chuyển đổi | Checkout, orders, net sales, returns/refunds | Không cộng đơn trùng giữa nền tảng/store/GA |
| Hiệu suất | Chi phí sản xuất/bài đạt; doanh thu có attribution/chi phí | Organic không gọi ROAS khi không có ad spend; chưa có margin thì chưa nói lợi nhuận |

YouTube giữ views và engaged views riêng; cách đếm views Shorts từ 2025-03-31 tính cả bắt đầu phát/xem lại. Vì vậy không xếp chất lượng IG/TikTok/Shorts chỉ từ raw views. [Nguồn YouTube](https://support.google.com/youtube/answer/10059070?hl=en).

## Metric record và mẫu số

Snapshot có source, definition, account/post/link ID, measured_at, published_at, post_age_hours, reporting window, cumulative hay interval, timezone, organic/paid và availability. Giá trị thiếu = null + reason. Ratio có numerator, denominator, unit; mẫu số 0 hoặc null thì ratio null, không gán 0%.

Ví dụ share_rate_by_reach = shares / reach, outbound_ctr_by_impressions = outbound_clicks / impressions, session_to_order_rate = attributed_orders / attributed_sessions. Chỉ tính nếu cả hai cùng grain/cửa sổ/attribution và định nghĩa tương thích. Không trộn numerator platform với denominator GA để gọi là CTR.

Snapshot 24h, 72h và 7d thường cumulative, không cộng ba số. So cùng tuổi bài, platform, format, account scale, objective và paid/organic; dùng cohort gần nhất phù hợp, hiển thị cỡ mẫu và dispersion. Thiếu baseline → baseline_building; thử nghiệm nhỏ không tự có kết luận thống kê.

## UTM và attribution

Quy ước đề xuất: utm_source = tên nền tảng lowercase; utm_medium = organic_social hoặc paid_social; utm_campaign = campaign ID; utm_content = tracking_link_id riêng cho creative khi có link riêng. [Google Analytics](https://support.google.com/analytics/answer/10917952?hl=en) hỗ trợ UTM để phân biệt traffic/creative; UTM không tự chứng minh mỗi đơn do một post gây ra.

Tracking link record: id, destination, campaign/release/account IDs khi biết, placement, utm, active window, attribution_grain = post / tile / account / campaign / unknown. Link bio chung phải có grain account/campaign, không điền post chỉ để đủ bảng.

Store là nguồn đơn/net sales; analytics là nguồn hành trình/tagged sessions; platform là nguồn phân phối. Join qua transaction ID trong vùng dữ liệu riêng để dedup đơn khi có quyền; không cộng cùng đơn từ nhiều nguồn. Báo riêng platform-attributed, analytics-attributed và store totals. Ghi attribution model/window, currency, tax/shipping/refund inclusion và cutoff. Nếu không có event purchase/cross-domain/link preservation được kiểm thì conversion attribution = not_ready.

Extension thương mại tùy chọn: pilot kiểm bằng session/transaction test phân biệt rõ, không tạo đơn trả tiền thật ngoài quyền được giao. Kiểm event view_item → add_to_cart → begin_checkout → purchase khi store hỗ trợ; verify transaction ID/dedup/refund mapping. Không cần xây data warehouse trước khi xác minh được một hành trình đơn giản.

## Quyết định theo kết quả

| Mẫu quan sát | Việc cần kiểm/điều chỉnh |
|---|---|
| Reach cao, không profile/click | Audience, độ rõ áo, liên quan punchline, CTA và khả năng bấm link |
| Click tốt, không add_to_cart | Trang đích, thông điệp, giá/size/tồn, tốc độ và tracking |
| Có cart, ít purchase | Checkout, phí/ship và lỗi; không vội kết luận creative kém |
| Reach vừa, đơn/traffic chất lượng tốt | Giữ concept, thử hook/cách phân phối có kiểm soát |
| View tốt nhưng feedback lệch brand | Không scale chỉ vì views; kiểm đối tượng và chất lượng phản ứng |
| Dữ liệu ít/thiếu attribution | Inconclusive, sửa instrumentation hoặc tiếp tục đo trong budget |

Không có một score tổng che các tầng. Mục tiêu awareness xét reach/shares cùng brand fit, mục tiêu bán xét traffic/đơn cùng chi phí. Paid boost thay đổi distribution context, không trộn với organic baseline.

## Vòng học

Lesson bắt đầu candidate: observation, hypothesis, hành động thử, scope (Table/format/model/platform), evidence, giới hạn và ngày review. Một bài nhiều view không đủ thành luật active. Lesson kỹ thuật hẹp có thể active sau kiểm tái lập và hồi quy phù hợp; lesson audience/creative cần bằng chứng nhiều trường hợp so sánh được và quyết định chấp nhận của chủ dự án. Không đặt số clip tùy tiện như bảo đảm nhân quả.

Mỗi tuần pilot review danh mục: cái gì tiếp tục, cái gì sửa, cái gì dừng và phép thử kế tiếp. Chu kỳ là đề xuất vận hành, chưa tạo automation. Mỗi tháng xét lesson active có bị model/policy/audience mới làm hết hiệu lực không; retired vẫn giữ nguồn và lịch sử.
