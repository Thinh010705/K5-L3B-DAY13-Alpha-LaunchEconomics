# Báo cáo cá nhân — Nguyễn Năng Thịnh-MSSV

## 1. Thông tin thành viên

- Họ tên: Nguyễn Năng Thịnh
- MSSV: 2A202604028
- Email: thinh010705@gmail.com
- Vai trong nhóm: Người gắn nhãn 2 kiêm giữ hồ sơ.
- Nhóm: Alpha
- Lớp: L3B

## 2. Phần việc phụ trách

- Tổng hợp kết quả của từng checkpoint vào `ho_so_launch_v0.md`.
- Đối chiếu kết quả mô hình chi phí và bảng độ nhạy từ người viết code.
- Gắn nhãn độc lập 20 ca lỗi theo năm loại lỗi của Google PAIR.
- Phối hợp với người gắn nhãn 1 để tính tỉ lệ đồng thuận, thống nhất nhãn và xây dựng phương án khắc phục.
- Chuẩn bị đặc tả chỉ số, danh sách event và bảng rủi ro kinh tế.
- Tổng hợp kế hoạch pilot và hoàn thiện hồ sơ trình hội đồng Gate 2a.

## 3. Đóng góp cụ thể

| Checkpoint | Công việc thực hiện | Kết quả |
| --- | --- | --- |
| CP1 | Tổng hợp mô hình chi phí vào mục 1 và 3 của hồ sơ launch | CPS 4.472 đ/việc; chi phí cả hệ thống 5.865 đ/yêu cầu (simulated) |
| CP2 | Tổng hợp ba yếu tố nhạy nhất và rủi ro kinh tế vào mục 2 và 7 | Làm lại: +51,8%; xem lại: +40,7%; lương nhân viên: +23,1% (simulated) |
| CP3 | Gắn nhãn độc lập 20 ca, đối chiếu hai bộ nhãn và tổng hợp bảng lỗi. | Đồng thuận 17/20 ca (85%); xây dựng quy tắc phân biệt cho 3 ca bất đồng và 5 phương án khắc phục |
| CP4 | Tiếp nhận và tổng hợp kế hoạch pilot vào hồ sơ launch | Chờ thành viên phụ trách hoàn thiện kế hoạch. |
| CP5 | Soạn đặc tả chỉ số, event, rủi ro kinh tế và đề xuất Gate 2a | 5 chỉ số, 7 event, 4 rủi ro kinh tế; đề xuất sơ bộ Go có điều kiện |

## 4. Bằng chứng

| File | Nội dung đóng góp |
| --- | --- |
| `report/team/ho_so_launch_v0.md` | Tổng hợp kết quả kinh tế, độ nhạy, phân loại lỗi và hồ sơ launch |
| `report/team/bang_loi.md` | Bộ nhãn cá nhân 20 ca, đối chiếu hai bộ nhãn, quy tắc phân biệt và bảng khắc phục |
| `report/team/chi_so.md` | Đặc tả chỉ số, danh sách event và rủi ro kinh tế đã soạn |

Nhánh làm việc: `feature/launch-dossier`.

Các kết quả nổi bật:

- Gắn nhãn độc lập đủ 20/20 ca.
- Tỉ lệ đồng thuận ban đầu đạt 85%, vượt ngưỡng 80% của đề bài.
- Tổng hợp 3 ca bất đồng gồm ca 16, 18 và 20.
- Xây dựng bảng khắc phục gồm 5 ca đại diện cho 5 loại lỗi.

Commit minh chứng: 0d7f2c2ada99dd33bf71aeb91f76325536f2ac1f, e071f3832566014380f421e5121ce76c1e81aca1, 53634c75389ecd9772a75677c997ef3b9e71fc4d, 34ce6d990872f891d106d853d285ed8e82300d8a.

## 5. Công cụ AI đã dùng

| Công cụ | Mục đích sử dụng | Cách kiểm tra kết quả |
| --- | --- | --- |
| ChatGPT | Hỗ trợ đọc đề bài, xác định phạm vi công việc và tổng hợp hồ sơ launch | Đối chiếu với đề bài và cấu trúc file mẫu trong repository |
| ChatGPT | Hỗ trợ diễn giải mô hình chi phí, phân tích độ nhạy và rủi ro kinh tế | So sánh với output của `lab13.py` và `bang_chi_phi.md` |
| ChatGPT | Hỗ trợ trình bày bảng gắn nhãn, đối chiếu hai bộ nhãn và đề xuất phương án khắc phục | Tự thực hiện lượt gắn nhãn ban đầu; đối chiếu nhãn dựa trên định nghĩa trong đề bài |
| ChatGPT | Hỗ trợ đề xuất chỉ số, event và chuẩn bị báo cáo | Kiểm tra khả năng tính chỉ số từ các event và đối chiếu yêu cầu E1–E3 |

## 6. Tự đánh giá

**Điểm làm tốt:** Hoàn thành lượt gắn nhãn độc lập 20 ca, đạt đồng thuận 85% với người gắn nhãn 1. Chủ động tổng hợp kết quả từng checkpoint và chuẩn bị công việc CP5 trong thời gian chờ các thành viên khác.

**Điểm cần cải thiện:** Cần phân biệt rõ hơn giữa lỗi hệ thống, lỗi ngữ cảnh và giới hạn hệ thống; đặc biệt trong các trường hợp hệ thống thực hiện đúng thiết kế nhưng không đáp ứng kỳ vọng của người dùng.

**Bài học rút ra:** Chi phí thực tế của agent phụ thuộc lớn vào thời gian xem lại và làm lại của nhân viên, không chỉ chi phí token. Một quyết định mở pilot cần dựa trên bằng chứng kinh tế, mức độ sử dụng, an toàn và thiết kế thí nghiệm có nhóm đối chứng.

**Hướng cải thiện:** Nâng cao khả năng phân tích nguyên nhân gốc của lỗi, thiết kế chỉ số đo lường và kiểm chứng các giả định kinh tế trước khi đưa ra quyết định tại Gate 2a.