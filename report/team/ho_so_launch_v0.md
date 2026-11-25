# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Alpha · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc (simulated); tổng chi phí 4.373.585 đ trên 978 việc thành công; gấp 16,3 lần hóa đơn token và tool/yêu cầu (A2) | Giả lập | Người viết code |
| 2 · Ba yếu tố nhạy nhất | Số ca làm lại ×2: +51,8%; tỉ lệ xem lại ×2: +40,7%; lương tăng 25%: +23,1% CPS (simulated, B1–B2) | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | CPS 4.472 đ so với 12.000 đ; chi phí cả hệ thống 5.865 đ/yêu cầu (0,49×). Với phạm vi nội địa và hàng nặng, CPS gồm chi phí cố định là 4.599 đ ở 45.000 yêu cầu/tháng và 5.784 đ ở 22.500 yêu cầu/tháng (simulated, A2–A4) | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chính: 82,83% (994/1.200); dùng: 27,12% (48/177); an toàn: 4,25% (51/1.200). Chưa có nhóm đối chứng (E1) | Xong, có bằng chứng | Người giữ hồ sơ |
| 5 · Bảng lỗi và cách khắc phục | Gắn nhãn độc lập 20 ca, đồng thuận 17/20 (85%); 3 ca bất đồng có quy tắc phân biệt; 5 phương án khắc phục đủ 5 loại lỗi (C) | Xong, có bằng chứng | Người gắn nhãn 1 |
| 6 · Pilot plan | Nội địa và hàng nặng tại 12 depot; ngẫu nhiên theo nhân viên, 20 người/nhóm; 5.980 yêu cầu thực tế/nhóm, hiệu dụng 859; MDE 6 điểm, power 80%; 4 luật dừng hiện có. Quyết định 15/01/2027 | Chưa | Người gắn nhãn 1 |
| 7 · Rủi ro kinh tế | Xem lại 100% khiến CPS đạt 11.743–12.415 đ, gần bằng hoặc vượt 12.000 đ tự làm. Ngưỡng hòa vốn xem lại 4,8–5,1 phút; tối đa 2 lần chạy cho chi phí cả hệ thống thấp nhất: 6.901.220 đ (simulated, B3–B4) | Giả lập | Người kiểm số |

**Đề xuất**: Go có điều kiện.

Giám đốc vận hành — 04/12/2026: chấp thuận đánh đổi MDE từ 5 lên 6 điểm; power chỉ khoảng 64% nếu tác động thật là 5 điểm.

Pilot Lead — 04/12/2026: xác nhận phân nhóm ngẫu nhiên 20/20 nhân viên, phạm vi nội địa và hàng nặng, kế hoạch thu tối thiểu 299 yêu cầu/người.

Backend Engineer — 04/12/2026: kiểm chứng chống hoàn tiền trùng và khả năng rollback trong 30 phút.

CSKH Lead — 14/12/2026: đánh giá thời gian xem lại so với ngưỡng hòa vốn 4,8–5,1 phút (simulated); không giảm kiểm soát khi chưa có bằng chứng an toàn.

Pilot Lead — 15/01/2027: xác nhận đủ mẫu, đủ cửa sổ theo dõi 7 ngày và đánh giá kết quả so với nhóm đối chứng.

- Bằng chứng E1–E2: [chi_so.md](chi_so.md), gồm 5 chỉ số, 7 event và 4 rủi ro kinh tế.
- Bằng chứng CP3: [bang_loi.md](bang_loi.md), đồng thuận 85%, đủ 5 loại lỗi và 5 phương án khắc phục.
