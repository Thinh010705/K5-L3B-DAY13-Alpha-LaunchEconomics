# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 994/1.200 = **82,83%** |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 48/177 = **27,12%** |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 51/1.200 = **4,25%** |
| Dùng | Tỉ lệ sử dụng trợ lý | Số yêu cầu đủ điều kiện, được phân vào nhóm trợ lý và thực sự chạy agent ít nhất một lần, chia tổng số yêu cầu đủ điều kiện được phân vào nhóm trợ lý | Không cần tính |
| An toàn | Tỉ lệ hoàn tiền trùng | Số yêu cầu có nhiều hơn một giao dịch hoàn tiền thành công cho cùng một nghĩa vụ hoàn phí, chia tổng số yêu cầu có giao dịch hoàn tiền thành công | Không cần tính |

Chỉ số chính trong đợt chạy thử là 82,83%; tỉ lệ bỏ qua gợi ý là 27,12% và tỉ lệ lỗi lọt đến khách là 4,25%. Do chưa có nhóm đối chứng, chưa thể kết luận trợ lý làm tăng hiệu quả xử lý yêu cầu.

## Danh sách event

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `request_received` | Backend CSKH | request_id, staff_id, depot, loai, eligible, assigned_arm, timestamp, trace_id | Khi tiếp nhận và ghi nhận phân nhóm yêu cầu |
| `agent_run_started` | Agent Orchestrator | request_id, run_id, attempt, timestamp, trace_id | Khi agent bắt đầu mỗi lần chạy |
| `review_started` | Giao diện CSKH | request_id, review_id, staff_id, timestamp, trace_id | Khi nhân viên bắt đầu xem lại kết quả |
| `review_completed` | Giao diện CSKH | request_id, review_id, staff_id, decision (giu/sua/bo), timestamp, trace_id | Khi nhân viên hoàn thành xem lại |
| `request_closed` | Backend CSKH | request_id, timestamp, trace_id | Khi yêu cầu được đóng |
| `request_reopened` | Backend CSKH | request_id, reason, timestamp, trace_id | Khi yêu cầu được mở lại |
| `refund_committed` | Dịch vụ hoàn tiền | request_id, refund_id, refund_obligation_id, amount_vnd, status, timestamp, trace_id | Khi kết quả giao dịch hoàn tiền được xác nhận |

Các event được liên kết bằng `request_id` và `trace_id`. Yêu cầu thuộc nhóm đối chứng cũng được cấp mã truy vết, dù không chạy agent. Khi tính chỉ số theo yêu cầu, cần loại bỏ bản ghi trùng và bảo đảm đủ thời gian theo dõi 7 ngày.

**Kiểm tra chéo:**

- Chỉ số chính: `request_received` + `request_closed` + `request_reopened`; kiểm tra thời gian đóng không quá 24 giờ và không mở lại trong cửa sổ theo dõi 7 ngày.
- Tỉ lệ bỏ qua gợi ý: `review_started` + `review_completed`; đếm yêu cầu có quyết định `sua` hoặc `bo` trên tổng số yêu cầu được xem lại.
- Tỉ lệ lỗi lọt đến khách: `request_received` + `request_reopened`; đếm yêu cầu mở lại trong 7 ngày trên tổng số yêu cầu đủ thời gian theo dõi.
- Tỉ lệ sử dụng trợ lý: `request_received` + `agent_run_started`; đối chiếu nhóm được phân với số yêu cầu thực sự chạy agent.
- Tỉ lệ hoàn tiền trùng: `refund_committed`; đếm các `refund_id` thành công khác nhau nhưng cùng `refund_obligation_id`, loại bỏ event trùng.

## E2 · Rủi ro kinh tế

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng | Gấp đôi số ca làm lại khiến CPS tăng 51,8%, từ 4.472 đ lên 6.787 đ (simulated) | Số ca làm lại, tỉ lệ câu trả lời sai | Phân tích nguyên nhân lỗi, cải thiện kiểm tra chính sách và chuyển ca khó sang nhân viên | AI Engineer |
| Chi phí xem lại tăng | Gấp đôi tỉ lệ xem lại khiến CPS tăng 40,7%, lên 6.292 đ (simulated) | Tỉ lệ xem lại, thời gian xem lại trung bình | Phân tầng rủi ro để tối ưu phạm vi xem lại, không giảm kiểm soát an toàn khi chưa có bằng chứng | CSKH Lead |
| Xem lại toàn bộ yêu cầu | CPS đạt 11.743–12.415 đ, gần bằng hoặc vượt mức 12.000 đ nhân viên tự làm (simulated) | Tỉ lệ xem lại đạt 100%, thời gian xem lại vượt ngưỡng hòa vốn 4,8–5,1 phút | Đo thời gian xem lại thực tế trong pilot, cải thiện giao diện và quy trình xác nhận | Product Manager |
| Giới hạn số lần chạy không hợp lý | Tối đa 1 lần có CPS thấp nhất là 4.111 đ nhưng chi phí cả hệ thống là 7.449.781 đ; tối đa 2 lần giảm chi phí cả hệ thống xuống 6.901.220 đ (simulated) | Số lần chạy/yêu cầu, tỉ lệ chuyển nhân viên, chi phí cả hệ thống | Đề xuất kiểm chứng giới hạn 2 lần chạy trong pilot và theo dõi chi phí toàn hệ thống | AI Engineer |
| Chi phí cố định phân bổ cao khi khối lượng pilot thấp | CPS khoảng 15.300 đ ở giai đoạn 4 người và 8.200 đ ở giai đoạn 10 người (simulated) | CPS biến đổi và CPS gồm chi phí cố định theo từng giai đoạn | Tách chi phí cố định khỏi ngưỡng dừng 8.000 đ; đánh giá riêng hiệu quả kinh tế dài hạn | Product Manager |