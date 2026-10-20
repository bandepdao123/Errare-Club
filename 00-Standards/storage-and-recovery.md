# Lưu trữ, quyền truy cập và phục hồi

## Ba nhóm dữ liệu

1. System: Markdown, registry seed, contract, template, validator. Có thể quản lý Git private; public export phải rà nguồn/quyền trước.
2. Runtime private: brief, prompts, attempts, budget, approvals, receipt, metrics, lessons, quyết định thương mại. Đặt .errare/ hoặc private workspace rõ ràng; không đẩy public chỉ vì đã QA.
3. Media: artwork, sheet, plate, masters, renders, project edit, exports, audio. Lưu ngoài Git thường tại media root/object storage; mỗi file có asset ID/hash và nguồn. Không dùng URL tool tạm thời làm nơi giữ duy nhất.

Registry seed trong 01-Brand là metadata nguồn, không là asset catalog đã kiểm. Khi import ảnh, tạo asset record có storage locator/hash/license; chỉ gắn lại registry sau khi kiểm identity và quyền phù hợp. URL hết hạn không làm mất identity của asset.

## Backup

Đề xuất snapshot runtime hằng ngày khi có thay đổi và trước migration; media master mới cần bản sao thứ hai trước khi đóng phiên. Có ít nhất một bản ngoài máy làm việc, có phiên bản; vị trí/lịch thật cần cấu hình với chủ dự án. Chưa có backup tự động được cài bởi bộ thiết kế này.

Backup phải có registry + metadata + media + approval/receipt + budget chưa đối soát. Git và gói system không thay backup runtime. Định kỳ restore thử một content vào thư mục mới, kiểm hash, mở artifact, đối chiếu digest release và receipt; test khôi phục không gửi generation/upload/publish. Không dọn bản gốc trước khi restore đã đạt.

## Những trường hợp lỗi

| Lỗi | Hành động phục hồi |
|---|---|
| Call model timeout | Giữ job ID/reservation, hỏi trạng thái provider, chưa retry khi outcome unknown |
| Xuất/ghi file dở | Không đổi selection; kiểm hash và mở file; tạo export revision |
| Crash sau upload | Reconcile account/receipt trước gửi lại; khóa dispatch ở trạng thái unknown |
| Caption/media đã duyệt bị sửa | Digest đổi, approval cũ không hợp lệ; tạo release mới |
| Store đổi URL/hết hàng | Chặn bài bán hàng chưa đăng, sửa CTA/đích rồi duyệt lại; bài đã đăng đưa vào hàng review |
| License hết hạn/thu hồi | Query dependency để tìm release/post ảnh hưởng; dừng dùng, chủ dự án quyết định thay/gỡ |
| Metrics mất quyền | Unavailable và lần thử lại, không điền 0 hoặc dựng performance |
| Migration lỗi | Rollback nguồn metadata từ snapshot, giữ media/receipt, không reset ID/budget |

Credential ở secret store/env của adapter, chỉ lưu tên tham chiếu. Metrics thương mại nên là dữ liệu tổng hợp; không nhập email/địa chỉ khách hàng nếu mục tiêu không cần. Thao tác xóa/gỡ bài hoặc thay quyền phải có yêu cầu phù hợp; bản thiết kế không tự thực hiện.
