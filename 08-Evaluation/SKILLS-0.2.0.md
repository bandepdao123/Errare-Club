# Kiểm triển khai bảy skill ER — 2026-10-20

Phạm vi: instruction skills project-local, metadata UI, routing registry/helper đọc-only, liên kết nguồn. Không có website sync, image/video generation, account connection, upload hoặc publish trong đợt này. Media contract giữ 0.1.4.

## Kiểm đã chạy

- Bundled skill-creator quick_validate.py trên 7/7 skill: hợp lệ frontmatter/tên/scaffold. PyYAML 6.0.3 có sẵn trong interpreter kiểm; helper runtime chỉ dùng thư viện chuẩn Python.
- python -X utf8 -m unittest discover -s scripts/tests -p test_skill_context.py -v: **11 test đạt**. Bao gồm product không reference, hybrid đủ nguồn, caption-only không tải research/model, mode/task không hợp lệ, mọi task có nguồn, lookup phân trang/versions, dữ liệu thiếu không tự tạo runtime, payload ngoài descriptor không xuất, file malformed có issue và chặn path vượt workspace.
- python -X utf8 scripts/validate_structure.py: lượt cuối sau khi thêm registry/skill/report links đạt **878 phép kiểm cấu trúc, 0 lỗi**. Không gọi con số này là phép kiểm chất lượng creative.
- Smoke test CLI: er-video/prompts/product trả 12 source paths; er-video/caption trả 4 source paths và chỉ lookup production/profile. Đây là số nguồn cho hai task khác nhau, không phải số đo tiết kiệm token. Find product hiện storage_present=false, 0 matches/0 issues; không tạo .errare hoặc nhận catalog đã sync.

## Giới hạn kiểm

Validator metadata và unit tests không chứng minh model sẽ chọn/tuân thủ skill đúng mọi lần. Chưa đo token/usage đối chứng, native US audience fit, công cụ ImageGen trả hai file từ một shared prompt, continuity, video motion, quyền account hoặc publish/reconcile thật. Task publish vẫn cần yêu cầu và approval đúng release.

## Môi trường kiểm

Sandbox process bị lỗi khởi tạo setup refresh, nên các validator/test cục bộ đã chạy thành công qua exec require_escalated với phạm vi read-only/fixture tạm được auto-review cho phép. Không thay đổi bảo vệ máy, credential hoặc network để xử lý lỗi. Lỗi sandbox không được ghi thành lỗi skill hay giả là test đã chạy trước khi có output thực.

## Forward-test độc lập

Một subagent độc lập đọc ba skill và nguồn tối thiểu, nhận dữ liệu tổng hợp cùng yêu cầu thực tế, không được sửa workspace/gọi mạng/media/publish. Không cung cấp đáp án kỳ vọng hoặc lỗi nghi ngờ. Sau khi vượt blocker sandbox bằng lệnh đọc được auto-review cho phép, evaluator trả đầu ra cả ba trường hợp; agent chính đối chiếu contract và không phát hiện lỗi chặn trong phạm vi test.

| Tình huống | Đầu ra thực quan sát |
|---|---|
| er-video: từ fixture tee HOME IS MY FAVORITE PLAN, không reference, video 8s | Đủ frame pair prompt chung yêu cầu hai file riêng t0/t8, video prompt timeline 0–8s và caption Anh Mỹ với bốn hashtag. Người quay là roommate cầm điện thoại, framing/rung nhẹ; không cinematic hoặc call render. Placement trước ngực/9:16 được ghi giả định draft, không nhận đã có artwork/model thật |
| er-kiemmedia: chỉ mô tả một output ảnh, chưa được xem file | Không xác nhận pair complete hoặc QA pass; role/time/identity/artwork/continuity đều not_checked, yêu cầu hai file riêng và brief/duration/source để kiểm. Không cắt collage giả cặp |
| er-quanlykenh: kế hoạch Instagram tuần tới, chưa account/media/caption/approval | Trả local_draft cho tuần 26/10–01/11/2026, giờ/timezone pending, checklist chuẩn bị media/QA/preview/duyệt. Không suy account đã kết nối, không gửi draft/lịch ra ngoài hoặc nhận quyền đăng |

Caption thực của fixture video: “I got ready. That should count for something.” với #ErrareClub #Homebody #StayingIn #StillHuman. Đây là output test tổng hợp, không là bài đăng/campaign/asset thực hoặc bằng chứng native audience đã thích. Không lưu test vào catalog/production runtime.

Ba lượt này bổ sung bằng chứng hành vi offline cho đúng phạm vi đã nêu; không chứng nhận mọi routing/creative future, công cụ hai ảnh, render video hoặc publish thật. Không có tool media và không phát sinh phí sinh media.

## Cập nhật nhập ảnh sản phẩm bắt buộc

Theo yêu cầu người dùng, er-sanpham phải truy cập website và tải ảnh gallery/detail về local, lưu product snapshot/asset/local_path/hash/provenance. URL-only/metadata_only không còn là kết quả nhập ảnh hoàn chỉnh. er-taoanh và er-video được sửa để mở đúng file tham chiếu đã tải, giữ draft/unknown nếu chưa đủ căn cứ. Acquisition và visual/artwork QA tách trạng thái theo WEBSITE-REFERENCE.md.

Đã chạy skill-creator validator trên ba skill sửa: 3/3 hợp lệ; validate_structure.py: 878 phép kiểm, 0 lỗi. Đây là kiểm hướng dẫn/liên kết; chưa chạy sync website hoặc tải ảnh thật trong nhiệm vụ cập nhật skill này, không nhận đã có thư viện ảnh local.

## Đăng ký kho Drive và lookup full hồ sơ

Đã kiểm bằng Google Drive connector: root Product Listing đọc được, có hai nhóm mockup, hai CSV map và một workbook XLSX. Đọc header/dòng mẫu CSV ngày 2026-10-20: sku/table/quote/viral20/folder_id/folder_url và tên ảnh theo màu/mặt. Kiểm metadata BFF-N01 xác nhận bốn file JPEG có tên đen/trắng trước/sau; chưa xem/download ảnh hoặc đọc workbook. Listing mockup root trả 100 mục được coi có khả năng partial, không chứng nhận đủ catalog.

Drive là nguồn chính theo chỉ định người dùng, website bổ sung claim live. Skill mặc định lookup; đọc đủ tài liệu/dòng dữ liệu đúng SKU, thiếu trường phải báo, không coi mapping filename là full hồ sơ. Chưa có bulk index/cache/download trong lần đăng ký nguồn.

Kiểm sau sửa routing: 11 unit test đạt, er-sanpham hợp lệ qua skill-creator validator, 894 phép kiểm cấu trúc không lỗi. Các phép kiểm này không chứng minh đã đọc toàn Drive, đủ mọi trường sản phẩm hoặc đã có ảnh local.
