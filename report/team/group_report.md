# Báo cáo nhóm

## 1. Thông tin nhóm

- Tên nhóm: Alpha
- Lớp: L3B
- Thành viên: xem [TEAM.md](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Đánh giá hiệu quả kinh tế, mức độ sử dụng và rủi ro của trợ lý hoàn phí LogiX-VN trên dữ liệu giả lập gồm 1.200 yêu cầu và 1.624 lượt chạy agent, từ đó xây dựng kế hoạch pilot phục vụ quyết định tại Gate 2a.

Nhóm tiếp cận theo năm nhiệm vụ: mô hình chi phí, phân tích độ nhạy, phân loại lỗi, thiết kế pilot và tổng hợp hồ sơ Launch v0.

## 3. Giải pháp

| Nhiệm vụ | Cách thực hiện | Sản phẩm |
| --- | --- | --- |
| A – Mô hình chi phí | Tính chi phí token, tool, xem lại và làm lại; kiểm chứng bằng ba phép thử; phân tích theo loại yêu cầu. | [bang_chi_phi.md](bang_chi_phi.md) |
| B – Phân tích độ nhạy | Thay đổi từng yếu tố chi phí, so sánh giới hạn chạy lại và đánh giá kịch bản xem lại 100%. | [bang_chi_phi.md](bang_chi_phi.md) |
| C – Phân loại lỗi | Hai thành viên gắn nhãn độc lập 20 ca theo Google PAIR, đối chiếu và xây dựng phương án khắc phục. | [bang_loi.md](bang_loi.md) |
| D – Thiết kế pilot | Tính cỡ mẫu, lựa chọn phân nhóm ngẫu nhiên theo nhân viên, xác định phạm vi, luật dừng và rollback. | [pilot_plan.yaml](pilot_plan.yaml) |
| E – Hồ sơ launch | Đặc tả chỉ số, event, rủi ro kinh tế và tổng hợp bằng chứng phục vụ Gate 2a. | [chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md) |

## 4. Kết quả

| Nội dung | Kết quả chính |
| --- | --- |
| Kiểm chứng mô hình | 3/3 phép thử đạt. |
| Hiệu quả kinh tế | CPS 4.472 đ/việc; chi phí cả hệ thống 5.865 đ/yêu cầu so với 12.000 đ tự làm (simulated). |
| Phạm vi pilot | Nội địa: 2.696 đ; hàng nặng: 8.221 đ; quốc tế: 22.515 đ/việc (simulated). Đề xuất chỉ nhận nội địa và hàng nặng. |
| Độ nhạy | Ba yếu tố ảnh hưởng lớn nhất: làm lại (+51,8%), xem lại (+40,7%), lương nhân viên (+23,1%) (simulated). |
| Phân loại lỗi | Đồng thuận 17/20 ca (85%); 3 ca bất đồng có quy tắc phân biệt; 5 phương án khắc phục đủ 5 loại lỗi. |
| Thiết kế pilot | 20 nhân viên/nhóm; tối thiểu 5.980 yêu cầu thực tế/nhóm; cỡ mẫu hiệu dụng 859; MDE 6 điểm phần trăm, power 80% theo giả định thiết kế. |
| Chỉ số đợt chạy thử | Chỉ số chính: 82,83%; bỏ qua gợi ý: 27,12%; mở lại trong 7 ngày: 4,25%. |
| Đặc tả đo lường | 5 chỉ số, 7 event và 4 rủi ro kinh tế. |

**Đề xuất Gate 2a: Go có điều kiện.** Pilot giới hạn ở nội địa và hàng nặng, cần chấp thuận đánh đổi MDE, kiểm chứng các biện pháp an toàn và hoàn thiện luật dừng trước khi bắt đầu.

**Kết quả duyệt chéo:** Chưa cập nhật, chờ quyết định và nhận xét thực tế của hội đồng.

## 5. Khó khăn và cách xử lý

- Chi phí token không phản ánh toàn bộ chi phí: bổ sung chi phí xem lại, làm lại và xử lý thủ công; ghi nhãn simulated.
- Ba ca gắn nhãn bất đồng: đối chiếu định nghĩa, phân tích nguyên nhân gốc và ghi quy tắc phân biệt.
- Thiếu cỡ mẫu khi chia theo nhân viên ở MDE 5 điểm: đề xuất MDE 6 điểm, đồng thời công khai power chỉ khoảng 64% nếu tác động thực tế là 5 điểm.
- Nguy cơ mất lợi thế kinh tế khi xem lại 100%: đưa thời gian xem lại và chi phí vào nội dung cần kiểm chứng trong pilot.

## 6. Tổng hợp đóng góp

- Người viết code: triển khai mô hình chi phí, phân tích độ nhạy, tính cỡ mẫu và chỉ số.
- Người kiểm số: kiểm chứng công thức, đối chiếu số liệu và hoàn thiện bảng chi phí.
- Người gắn nhãn 1: gắn nhãn độc lập 20 ca, phối hợp phân tích lỗi và xây dựng kế hoạch pilot.
- Người gắn nhãn 2 kiêm giữ hồ sơ: gắn nhãn độc lập 20 ca, tổng hợp bảng lỗi, đặc tả chỉ số, rủi ro kinh tế và hồ sơ Launch v0.

Chi tiết đóng góp của từng thành viên nằm trong [TEAM.md](../../TEAM.md) và báo cáo cá nhân.

## 7. Hạn chế và hướng cải thiện

Dữ liệu thời gian xem lại và làm lại là simulated; đợt chạy thử chưa có nhóm đối chứng nên chưa thể kết luận tác động nhân quả của trợ lý.

Pilot cần thu thập thời gian lao động thực tế, kiểm soát ảnh hưởng gián tiếp giữa hai nhóm, theo dõi lỗi hoàn tiền và xác minh đủ cỡ mẫu trước khi ra quyết định. Việc mở rộng phạm vi phải dựa trên bằng chứng kinh tế và an toàn.

## 8. Tài liệu tham khảo

- Google PAIR. *People + AI Guidebook: Errors + Graceful Failure*. https://pair.withgoogle.com/
- Tài liệu dữ liệu và công thức: [du_lieu_va_cong_thuc.md](../../docs/du_lieu_va_cong_thuc.md).
- Statsmodels. *Statistical power analysis*. https://www.statsmodels.org/