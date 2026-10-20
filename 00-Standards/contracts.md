# Hợp đồng dữ liệu và trạng thái

Version 0.1.4. Đây là contract thiết kế cho bước triển khai tiếp theo; chưa có schema engine hoặc gate publisher chạy tự động. Validator hiện có chỉ kiểm dữ liệu nền, routing config/template và tài liệu như phạm vi ghi trong script. Phạm vi theo 07-Operations/SCOPE.md; các trường commerce chỉ dùng khi cần tham chiếu/claim, không yêu cầu hệ thống nghiên cứu sản phẩm.

## Identity và quan hệ

ID record mới dùng prefix dễ đọc + UUID khi thực sự tạo record; seed brand dùng ID ổn định trong JSON. Không cấp ID production từ câu hỏi. Campaign ID, Content ID, Attempt ID, Asset ID, Release ID, Post ID và Lesson ID khác nhau. Native post ID luôn đi cùng platform/account; không giả duy nhất xuyên nền tảng.

| Record | Trường bắt buộc và quan hệ |
|---|---|
| Competitor/reference | id, account/platform/canonical URL, role, source proposer, observed_at, visible metrics + definitions/availability, media coverage, analysis status, cơ chế giả thuyết và evidence; không bịa private analytics |
| Product reference | id, website URL/handle, tên/câu áo, collection/Table, image refs, captured_at, source fields; giá/stock chỉ khi content cần, không là record R&D |
| Persona | id/version, identity/voice/motivations, product/Table affinities, hypothesis/evidence, status, sheet/asset refs nếu đã có; không mặc định dùng Soul ID cũ |
| Opportunity | id, entry_mode, source_refs[], reference_ids[] có thể rỗng ở product, product/collection refs có thể chưa chọn ở reference, persona refs, insight/hypothesis, adaptation, target format/platform, test criterion, status |
| Campaign | id, schema_version, owner, objective, audience, table_ids[], product_ids[], budget_limit + unit, status, start/end/timezone; budget chưa có = null, không là được tiêu |
| Content | id, entry_mode, task, campaign_id hoặc null có lý do, objective, table_ids[], persona_refs[], product_refs[], format, layout, target_profile_refs[], duration_s/frame_plan nếu video, visual_override_ref nếu có, concept_ref, brief_ref, source_refs[], status, current_attempt_id hoặc null; cast_ids/product_ids cũ chỉ là legacy references nếu có |
| Attempt | id, content_id, revision_of hoặc null, revision_scope, brief/concept/source versions, planned_inputs[], actual_inputs[] hoặc null, prompts/settings refs, provider_job_id hoặc null, actual_model hoặc unknown, output_text_ref hoặc null, output_asset_ids[], review/cost refs, status |
| Asset | id, version, kind, sha256, storage locator, source/rights, dependency_asset_ids[], review refs; planned asset thiếu file/hash không được dùng như input thật |
| Review | id, artifact refs + hash, criteria_version, checks[], coverage, method, reviewer, findings[], reviewed_at; từng check có result, evidence và applicability |
| Release | id, version, content_id, selected_attempt_id, ordered_asset_refs[], caption/title, cover, platform, account_id, destination/UTM, audio/rights/disclosure, schedule + timezone, manifest_sha256 |
| Approval | id, release_id + manifest_sha256, decision, actor, evidence, approved_at, scope/expiry; không lấy chat im lặng làm duyệt |
| Post | id, release_id/hash, account_id, idempotency_key, dispatch state, native_post_id/url, receipt/evidence, published_at hoặc null, observed_at |
| Metric snapshot | id, post_id hoặc tracking_link_id theo grain, source, measured_at, post_age_hours nếu có, definition version, window, values + units, attribution_model/window; raw source giữ riêng |
| Lesson | id, state, scope, actionable rule, conditions, evidence refs, limitations, version, review_date; insight một lần chưa là active |

Mọi record thực có created_at, updated_at, schema_version; bản sửa giữ supersedes/revision_of, lịch sử và owner. Timestamp RFC3339 có offset, lưu UTC để join; lịch hiển thị có IANA timezone. Quản lý theo Asia/Saigon, scene và lịch khán giả có thể America/New_York; không dùng UTC-5 cố định vì DST.

entry_mode = product | reference | hybrid. source_refs mỗi mục ghi kind (product/reference), source ID hoặc URL/path, version/captured_at và coverage khi biết. Product cần nguồn product/collection; reference cần nguồn media; hybrid cần cả hai. Không bắt reference_ids không rỗng ở product. task = concept | prompts | generate | review | revision | caption | close; format = photo_post | video, độc lập với entry_mode; layout = single | carousel cho photo_post, target_profile_refs chỉ bản xuất đích. Chuẩn đủ gói ở media-contract.json; ảnh hoàn chỉnh cần exports thật và caption, video package cần một frame_pair_prompt (hai ảnh t0/tT) + video_prompt + caption, duration_s/frame_plan đầy đủ nhưng chưa cần render. frame_plan giữ first.time_s=0 và last.time_s=duration_s, shared_prompt_ref, continuity/camera plan và actual asset refs riêng nếu đã tạo ảnh. Dữ liệu nguồn theo SOURCE-ROUTING.md. Cấu hình [entrypoints](entrypoints.json) là bản đồ, không là quyền gọi tool. Dùng [templates và output contract](../04-Productions/README.md) cho production mới.

Unknown dùng null hoặc trạng thái unknown/not_checked; 0 chỉ khi thực đo được 0. Hai kiểu không trộn: số null kèm availability/reason, không dùng chuỗi unknown trong trường số. Hash SHA-256 lowercase 64 hex của byte thật. Không tạo hash của filename thay hash file.

## Máy trạng thái tối thiểu

Content: draft → brief_ready → in_production → review → ready → archived. Review fail quay về in_production qua attempt mới; archived là dừng vận hành, không xóa. Content ready nghĩa gói đầu ra đã đủ: photo_post có ảnh thật đủ target và caption, video có frame pair prompt/video prompt/caption và plan t0/t(duration_s). Video prompt-ready không chứng minh có master video; release để đăng vẫn cần media thật/QA/approval riêng.

Attempt có thể có vòng văn bản hoặc media. Vòng văn bản: planned → drafted khi output_text_ref thực đã được lưu; drafted không là render succeeded/QA pass. Vòng media: planned → submitted → succeeded / failed / unknown. Submitted không có output thật không thể succeeded. Unknown cần reconcile theo job, không tự failed để được gọi lại. Review/caption/close không buộc tạo job model hoặc media.

Release: draft → qa_pass → awaiting_approval → approved → invalidated/superseded. QA gắn đúng export, approval gắn đúng digest. Hết hạn, dependency thay, hoặc policy/stock preflight không đạt làm release tạm chặn; không sửa duyệt lịch sử.

Post: planned → scheduled hoặc dispatching → published_unverified → published_verified; dispatching có thể sang failed hoặc dispatch_unknown. Scheduler xác nhận nhận lịch không bằng đã đăng. Canceled/taken_down giữ native ID và lý do; không xóa metric lịch sử. Một release chỉ phục vụ một account/platform; cross-post tạo release khác.

## Digest và gate release

Manifest canonical JSON: UTF-8, key sorted, compact separators, thứ tự list giữ nguyên. Digest bao gồm version contract, ordered file hashes, media/caption/cover, URL/UTM, product/offer snapshot liên quan, platform/account, rights/disclosure và lịch/phạm vi lịch. Không gồm digest của chính nó, approval, dispatch state hoặc metrics. Cách canonicalize phải có một implementation duy nhất khi triển khai.

Trước dispatch phải đồng thời: artifact đã QA trong đúng scope; dependency/license phù hợp; approval trùng digest và còn hiệu lực; account/format/policy kiểm hiện tại; destination/offer còn hợp lệ; có quyền đăng; chưa có claim/receipt mâu thuẫn. Index/dashboard không thay các record gốc. File chưa hiện hữu, review not_checked bắt buộc, approval gói khác đều chặn.

## Concurrency, retry và schema evolution

MVP một writer, ghi file tạm rồi rename atomic trong cùng filesystem; cập nhật dùng expected_revision để tránh ghi đè bản mới. Hai writer trở lên dùng transaction và unique constraint cho ID/dispatch key/budget reservation; lock có lease, expiry không tự cho quyền retry khi outcome bên ngoài còn unknown.

Migration có schema_version, dry-run, backup, report và rollback. Record cũ đọc được qua adapter, không backfill provenance/approval. Không đồng thời để JSON và database thành nguồn chính. Import metrics theo source+native ID+window+snapshot timestamp/version: ingest lại cùng snapshot không nhân đôi; điều chỉnh nguồn tạo revision, không cộng cumulative snapshots.
