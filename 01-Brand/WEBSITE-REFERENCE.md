# Website là nguồn tham chiếu sản phẩm

Nguồn: [errareclub.com](https://errareclub.com/). Chủ dự án xác nhận sản phẩm do R&D nghiên cứu và đã đưa lên website. Hệ thống media chỉ đọc/đồng bộ tham chiếu phục vụ sáng tạo.

Cập nhật nguồn: kho Drive trong [PRODUCT-SOURCES](PRODUCT-SOURCES.md) là hồ sơ sản phẩm chính. Website là nguồn bổ sung thông tin đang công bố hoặc ảnh còn thiếu; các bước vào website dưới đây áp khi dùng nhánh website, không bắt mọi lookup Drive phải truy cập website. Cơ chế lưu file local/source/hash/QA áp cả hai nguồn.

## Quan sát ban đầu — 2026-10-20

Đã đọc trang chủ qua trình duyệt. Có October Drop, các liên kết mười Table, Wear it to, Get the look và sản phẩm [HOME IS MY FAVORITE PLAN](https://errareclub.com/products/ovt-10). Trang chủ hiển thị giá $34.00 cho sản phẩm này và mô tả Draft Cotton 240/The Oversize. Đây là thông tin đang được trang chủ công bố, không là kiểm chứng chất lượng sản phẩm hoặc giá mọi biến thể. Chưa đọc toàn catalog/trang chi tiết, tải ảnh, kiểm stock hoặc QA hình ảnh. Alt text không thay visual review.

## Contract nhập dữ liệu

Mỗi product reference có ID nội bộ + website handle/native ID khi lấy được, canonical URL, tên/câu áo nguyên văn, collection/Table, mô tả công bố, image URLs và role/view nếu xác định, captured_at, source URL, availability của từng trường. Giá/option chỉ nhập nếu cần cho caption; không dựng lại catalog R&D hoặc bắt đủ SKU/size/tồn mới viết ý tưởng.

Image record phân biệt remote URL với file đã tải, giữ source product/page, captured_at, checksum nếu có file, crop/front/back/detail khi thực sự xác định. Khi sản xuất cần tham chiếu chính xác, mở/kiểm ảnh thật; nếu ảnh không đủ rõ chữ/placement thì yêu cầu đúng artwork ở bước bị chặn. Không vẽ lại câu áo từ trí nhớ hoặc nhận mockup đúng chỉ từ tên sản phẩm.

## Nhập ảnh local là bước bắt buộc

Khi thực hiện er-sanpham để nhập/cập nhật sản phẩm, phải vào website, mở đúng product page, lấy ảnh sản phẩm từ gallery/chi tiết và tự lưu file về local trong phạm vi đang làm. Lưu URL không thay file tham chiếu. Chưa có URL cụ thể thì bắt đầu từ trang chủ/collection để tìm sản phẩm liên quan; không cần nhập cả website mới làm được một nội dung.

- File ảnh gốc: media/products/<product-id>/<image-hash>.<ext> hoặc media root đã cấu hình. Không lưu file nhị phân vào skill/prompt và không ghi đè ảnh cũ khi nguồn đổi.
- Product snapshot: .errare/library/products/<product-id>/<version>.json, chứa tên/câu áo/collection/URL và images[] liên kết đúng ảnh của sản phẩm.
- Asset metadata: .errare/library/assets/<asset-id>.json; product record tham chiếu asset ID, không copy file sang từng Content hoặc mỗi skill.
- Mỗi image entry có source_url, product_page_url, downloaded_at, local_path, sha256, asset_id, download_status và visual_review. Role/view, kích thước và chi tiết chỉ điền khi đã kiểm; giữ unknown/not_checked nếu chưa xác định.

Ưu tiên ảnh gốc chất lượng tốt nhất có thể truy cập trên trang, các góc trước/sau và detail cần thấy thiết kế; không lấy logo/UI/ảnh sản phẩm khác làm reference. Dùng download phù hợp hoặc HTTP để nhận file thật, không screenshot trang thay file gốc khi file truy cập được. Không xử lý ảnh hoặc tạo artwork mới từ tác vụ thu thập.

Kiểm file tồn tại, mở được, hash và liên kết sản phẩm; xem ảnh thực để ghi coverage. Tải file chưa bằng QA artwork hoặc chứng minh mặt sau nếu chỉ thấy mặt trước. Source URL + local file + hash phải đi cùng record; downstream mở ảnh local đúng version/hash trước khi dùng làm input hoặc diễn giải thiết kế.

Acquisition status: metadata_only khi mới có thông tin/URL; partial khi thiếu ảnh cần thiết hoặc tải lỗi; downloaded khi đã lưu file ảnh cần dùng, với visual_review độc lập; reference_ready chỉ khi ảnh liên quan đã được xem và đủ rõ cho mục đích được ghi. Không đủ cho in áo/identity thì giữ giới hạn đó dù đã tải file thành công. Không tự coi reference_ready là media QA hoặc approval đăng.

Khi không tải được, lưu metadata/nguồn/lý do và phần đã hoàn thành, báo partial/blocked; không nhờ upload thay trước khi thử các công cụ sẵn có. Nếu nguồn yêu cầu quyền truy cập chưa có, xử lý đúng quyền; không vượt chặn truy cập hoặc bịa thành công. Sync/refresh giữ snapshot và asset cũ, đánh dấu thay đổi ảnh để content phụ thuộc xem lại.

Snapshot không ghi đè lịch sử: lần sync mới có version/change log. Sản phẩm đổi hình/câu chữ/URL → đánh dấu reference/dependent draft cần review; không tự sửa attempt đã hoàn thành. Giá/tồn chỉ cần kiểm lại khi nội dung có claim/offer tương ứng. Dùng asset ID/hash ổn định, không phụ thuộc duy nhất vào URL CDN có thể đổi.

## Dùng để xây persona và media

Tách dữ kiện website khỏi suy luận sáng tạo. Ví dụ câu HOME IS MY FAVORITE PLAN là thông tin sản phẩm; persona thích ở nhà, nghĩ quá nhiều hoặc ngại từ chối lời mời là giả thuyết có thể thử. Không nhận đã chứng minh tệp khách hàng từ một câu áo.

Roster mới có persona_id, identity sheet, voice, motivations, recurring tensions, product/Table affinities, visual continuity và version. Có thể giữ, sửa hoặc thay cast cũ. Trong khi roster chưa chốt, content brief ghi rõ cast nào được chọn cho nội dung; không tự lấy Soul ID của người cũ gắn vào persona mới.

products.json/cast.json hiện là seed lịch sử từ Errare World, chưa phải kết quả sync website hoặc roster mới. Skill er-sanpham đã có workflow vào website, tải ảnh và ghi snapshot; chưa chạy sync thật hoặc tạo roster mới từ lần sửa hướng dẫn này.
