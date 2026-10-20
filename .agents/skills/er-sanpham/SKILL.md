---
name: er-sanpham
description: Retrieve complete available Errare Club product profiles from the designated Google Drive repository, and import or refresh original product images locally for media creation. Use SKU, name or quote lookups; use the website for published information or missing references. Not product R&D or media generation.
---

# ER · Sản phẩm

## Nguồn

Root là thư mục chứa `.agents/skills/` này, ba cấp trên thư mục skill. Chạy tại root:

`python -X utf8 scripts/skill_context.py route er-sanpham`

Mặc định task `lookup`; dùng `--task sync` khi nhập/cập nhật theo batch. Đọc nguồn helper trả về và [PRODUCT-SOURCES](../../../01-Brand/PRODUCT-SOURCES.md); tra `python -X utf8 scripts/skill_context.py find --kind product --query "<SKU/tên/câu áo>"` trước khi mở snapshot. Nếu helper unavailable, mở [SOURCE-ROUTING](../../../00-Standards/SOURCE-ROUTING.md) và guide nguồn. Không nạp cả catalog.

## Thực hiện

- Drive được chỉ định trong product-sources.json là nguồn chính. Resolve SKU/tên/câu áo → đọc mapping/index và đầy đủ tài liệu/dòng dữ liệu của đúng SKU. Dùng Google Drive skill/connector để ground file ID/MIME và đọc/tải đúng loại. Cache thiếu/cũ thì đọc nguồn trực tiếp, không nhận helper local đã tự đồng bộ Drive.
- Dùng website khi cần thông tin đang công bố, link mua hoặc bổ sung phần Drive thiếu; không bắt vào website mỗi lần nếu hồ sơ Drive đủ. Seed cũ không thay hồ sơ nguồn hiện hành.
- Tách thông tin công bố, suy luận persona và phần chưa kiểm. Thu thập câu áo/collection/ảnh và trường cần thiết theo contract nguồn; giữ URL, captured_at, availability từng trường.
- Khi nhập tham chiếu ảnh, tự tải ảnh sản phẩm gốc từ đúng Drive folder/file hoặc website về local theo PRODUCT-SOURCES và WEBSITE-REFERENCE. Drive dùng authenticated file reference theo Google Drive skill; website dùng download/browser/HTTP phù hợp. Không dừng ở URL/filename/alt text hoặc thumbnail, không bắt người dùng tải hộ khi công cụ làm được, không screenshot thay ảnh gốc truy cập được.
- Lưu file tại media root chuẩn và gắn local_path/asset_id/hash/source URL vào đúng product snapshot. Kiểm file tồn tại/mở được, xem ảnh thật và ghi coverage/role đã xác định; không gọi tải file thành artwork/identity QA nếu chưa kiểm.
- Không tự bỏ qua ảnh cần thấy câu áo, mặt trước/sau hoặc chi tiết liên quan chỉ để ít file hơn. Reuse file cũ khi đúng nguồn/version và hash còn hợp lệ; giữ bản mới khi ảnh đổi. Tải lỗi/không rõ quyền truy cập thì ghi partial/blocked đúng phần, không nhận nhập ảnh đã xong hoặc bịa ảnh thay thế.
- Ghi snapshot phiên bản mới vào kho chuẩn, giữ bản cũ và ghi dependency thay đổi. Không ghi đè seed hoặc production, không bịa artwork/giá/tồn.

Trả full thông tin có thực của đúng sản phẩm khi được hỏi full, kèm nguồn/version, ảnh/source refs và phần thiếu/chưa đọc được. Không bịa trường không có trong hồ sơ, không nhận filename là toàn bộ dữ liệu. Khi sync ảnh, trả thêm file local/snapshot/hash và coverage; chỉ remote URL là metadata_only/partial. Lookup văn bản không cần tải mọi mockup toàn kho. Không tạo media, đặt hàng, sửa Drive/store/quyền hoặc đăng từ tác vụ này; sửa skill/đăng ký nguồn không tự sync toàn catalog.
