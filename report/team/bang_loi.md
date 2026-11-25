# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Hoàng Minh Quyền · Người gắn nhãn 2: [Điền họ tên] (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Hệ thống | Không | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Hệ thống | Không | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Giới hạn hệ thống | Không | Hệ thống |

**Tỉ lệ đồng thuận:** 17 / 20 = **85%** (đạt ngưỡng 80%).

## Quy tắc phân biệt cho các ca không trùng

- Ca 16: Nếu hệ thống làm đúng thiết kế nhưng thời điểm thông báo không phù hợp với hoàn cảnh người dùng thì phân loại Ngữ cảnh.
- Ca 18: Nếu số tiền hoàn chính xác nhưng cách giải thích khiến khách hiểu sai kết quả thì phân loại Ngữ cảnh.
- Ca 20: Nếu chức năng thuộc phạm vi hỗ trợ nhưng thực hiện sai do thiếu cơ chế chống trùng giao dịch thì phân loại Hệ thống.

Tỉ lệ đồng thuận đạt 85%, không cần viết lại toàn bộ định nghĩa phân loại.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `refund_account_validation_failed`; kiểm tra 100% thông tin tài khoản trước khi gửi lệnh hoàn tiền. | Kiểm tra định dạng theo quy định của ngân hàng, yêu cầu khách sửa thông tin không hợp lệ trước khi thực hiện. | Backend Engineer |
| 7 | Hệ thống | Event `refund_failed` và `refund_notification_sent`; cảnh báo ngay khi có thông báo thành công nhưng sổ cái chưa xác nhận giao dịch. | Chỉ báo thành công sau khi xác nhận giao dịch; chuyển nhân viên nếu vẫn lỗi sau giới hạn chạy lại, kiểm tra trạng thái trước khi thử lại. | Backend Engineer |
| 3 | Ngữ cảnh | Event `refund_destination_confirmed`; theo dõi hằng ngày số yêu cầu mở lại với lý do khách không nhận được tiền đúng phương thức kỳ vọng. | Hiển thị rõ phương thức nhận tiền, thời gian dự kiến và yêu cầu khách xác nhận trước khi hoàn. | Product Manager |
| 19 | Giới hạn hệ thống | Event `request_out_of_scope`; phát hiện yêu cầu có tuổi dữ liệu vượt 12 tháng. | Thông báo rõ giới hạn truy cập, chuyển nhân viên kèm bản tóm tắt yêu cầu. | AI Engineer |
| 5 | Ngầm | Event `refund_reconciliation_mismatch`; đối soát hằng ngày 100% giao dịch hoàn phí có mã giảm giá, cảnh báo khi số tiền hoàn lệch số tiền hợp lệ. | Tính tiền hoàn theo giá sau giảm và chính sách áp dụng; kiểm tra trước giao dịch, đối soát và chuyển xử lý nếu phát hiện sai lệch. | QA Engineer |