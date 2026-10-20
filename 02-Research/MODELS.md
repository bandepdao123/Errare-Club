# Model/interface và tài sản tham chiếu

Tách ba lớp: sản phẩm website là dữ kiện tham chiếu; cast/artwork/plate/audio là asset; model profile là khả năng/giới hạn công cụ theo ngày và interface. Không để giá hoặc lời quảng cáo model thành luật sáng tạo.

Theo yêu cầu 0.1.4, tạo/sửa ảnh dùng ImageGen tích hợp Codex; không tự fallback provider khác. Frame-pair prompt yêu cầu hai file riêng nhưng capability profile vẫn phải ghi thực tế tool/interface có trả được hai output hay không; chưa thử thì not_checked. Model video nếu render thật cần kiểm hỗ trợ first/last anchors và duration đã chọn; chưa hỗ trợ không được âm thầm bỏ last anchor.

Khi thực dùng, tạo profile riêng trong .errare/models/<profile-id>.json: provider, model/interface được công bố, checked_at, nguồn/case đã thử, input/output capabilities, ratio/duration/audio/reference limits, known failures, cost units, permissions và fallback. Unknown giữ unknown; không sao chép profile Omni/Underwater từ Nature-Studio sang Errare.

Asset catalog runtime ở .errare/library/assets/, cùng các kho products/, personas/; phân tích media reference chỉ ở .errare/research/references/ theo SOURCE-ROUTING, không sao chép analysis sang catalog asset. Metadata có ID/version, source/rights, role/view, dependencies, storage locator/hash, QA scope và trạng thái. File lớn nằm media root; hồ sơ production tham chiếu asset, không copy cả thư viện. Ảnh cast dùng chứng minh identity không tự chứng minh câu áo hoặc vị trí in.

Trước render chỉ mở đúng ảnh dùng làm actual input, ghi thứ tự/hash và receipt khi có. Planned input khác actual-used input. Thumbnail/chữ mô tả không thay nhìn ảnh. Không chọn câu chuyện chỉ vì thư viện hiện có asset đó; thiếu asset thì lập kế hoạch bổ sung trong quyền/budget hoặc đổi cách thể hiện có chủ đích.

Kế thừa Nature-Studio về profile/capability/provenance; không kế thừa model mặc định, quota năm call hoặc các giới hạn domain thiên nhiên.
