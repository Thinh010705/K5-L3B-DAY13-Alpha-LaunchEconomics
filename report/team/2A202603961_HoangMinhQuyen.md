# Báo cáo cá nhân — HoangMinhQuyen-2A202603961

## 1. Thông tin thành viên

- Họ tên: Hoàng Minh Quyền
- MSSV: 2A202603961
- Email: quyentryhard@gmail.com
- Vai trong nhóm: Người gắn nhãn 1

## 2. Phần việc phụ trách

- Đọc đề và theo dõi điều kiện "Xong khi" của 5 checkpoint (CP1–CP5) theo `CHECKPOINTS.md`, `RUBRIC.md`, `SUBMISSION.md`.
- Gắn nhãn 20 ca lỗi của nhiệm vụ C theo năm loại Google PAIR (cột "Nhãn người 1" trong `report/team/bang_loi.md`).
- Nhiệm vụ D: viết `report/team/pilot_plan.yaml` (CP4).

## 3. Đóng góp cụ thể

- Chạy lại `src/lab13.py` của người viết code trên máy thứ hai trong nhóm: output giống hệt `src/lab13_output.txt`, ba phép thử A1 `ĐẠT` (`1,20 · 1,25 · 1,25`).
- Soát số CP1–CP2 trong `report/team/bang_chi_phi.md` với bảng đối chiếu: A2 `4.472 đ` (`simulated`, gấp `16,3x` hoá đơn), A3 `0,22x · 0,69x · 1,88x · 0,85x` (`simulated`), A4 `4.599 đ` và `5.784 đ` (`simulated`), B1–B3 khớp; B4 `12.415 đ` so với đáp án `12.414 đ` (lệch do làm tròn, trong sai số 2%).
- Tính tay lại tỉ trọng giờ nhân viên: `(1.780.000 + 2.264.000) ÷ 4.373.585 = 92,46%` (`simulated`), khớp số trong bảng.
- Phát hiện 2 số tính từ cột `_simulated` trong `bang_chi_phi.md` chưa ghi nhãn `simulated` (`92,5%` ở A2 và mức hoà vốn `≤ 4,8 phút` ở B4); hướng dẫn mẫu cũng thiếu nhãn ở hai chỗ này.
- Điền 20 nhãn vào cột "Nhãn người 1" của `bang_loi.md`: Do người dùng 4 · Hệ thống 5 · Ngữ cảnh 4 · Giới hạn hệ thống 4 · Ngầm 3. Đồng thuận với Người gắn nhãn 2: 17/20 = 85%.
- Hoàn thiện `pilot_plan.yaml` (CP4):
  - Năm câu D1 lấy từ output `lab13.py`: `1.251` · DE `2,48`, `3.103`, cần 84 người > 40 · tối đa `1.000` · tối đa `300` · `m ≥ 299` (DE `6,96`).
  - Chọn chia theo nhân viên 20 + 20, ngẫu nhiên, phân tầng theo depot; trả lời năm câu D2.
  - Ghi rõ đánh đổi: hạ mde xuống 6 điểm, power chỉ còn `0,64` nếu tác động thật là 5 điểm (tính lại bằng statsmodels `NormalIndPower`).
  - Tính tỉ lệ mở lại 7 ngày hiện tại (`4,25%`, `3,97%` trong phạm vi) trước khi đặt ngưỡng an toàn: so với đối chứng chênh ≥ 2 điểm kèm trần 6%, tránh dừng ngay tuần đầu.
  - Năm luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ (an toàn tuyệt đối ở mọi giai đoạn, so với đối chứng ở giai đoạn 10 và 20 nhân viên, chi phí biến đổi không gồm 40 triệu cố định, mức độ sử dụng, thời gian xem lại) với ngưỡng, thời hạn, người có quyền dừng; vế KHÔNG THÌ ghi rõ việc bị cấm và cấm đến khi nào.
  - Tính thời gian đo: khoảng `30,7` yêu cầu/nhân viên/ngày trong phạm vi, nên cần khoảng 10 ngày làm việc để đạt `m ≥ 299`; ngày quyết định 2027-01-15.

## 4. Bằng chứng

- Nhánh làm việc: `quyen_gannhan1` (tạo từ `feat/quang011105-lab13-code`).
- File: `report/team/bang_loi.md` (cột "Nhãn người 1"); commit `6d734d5`, tạo trước khi so nhãn với Người gắn nhãn 2.
- File: `report/team/pilot_plan.yaml`; đọc được bằng `yaml.safe_load`, đủ 11 trường, không còn dấu `?` ngoài dòng chú thích, năm luật dừng đủ bốn vế.
- Output chạy lại `python lab13.py` trên máy cá nhân trùng với `src/lab13_output.txt`.

## 5. Công cụ AI đã dùng

- Công cụ: Claude Code (Claude Opus 5.5).
- Dùng vào việc:
  - Đọc cấu trúc repo, tóm tắt đề, lập kế hoạch cho vai Người gắn nhãn 1.
  - Đối chiếu output `lab13.py` và `bang_chi_phi.md` với bảng số trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, tìm các số thiếu nhãn `simulated`.
  - Soạn nháp `pilot_plan.yaml` từ số của `lab13.py`; ngày bắt đầu, ngày quyết định và ngưỡng luật chi phí (8.000 đ, 7% làm lại) là đề xuất, cần nhóm thống nhất.
- Cách tự kiểm tra:
  - Tự chạy `python lab13.py` trong `src/` và so output với file của người viết code.
  - Tính tay lại tỉ trọng giờ nhân viên `92,46%` (`simulated`).
  - Chạy `yaml.safe_load`, lệnh `grep -v '^ *#' pilot_plan.yaml | grep -n '?'` (không in gì) và `grep -rni` từ cấm trong `report/team` (không in gì); tính lại power `0,64` bằng statsmodels; câu e D1 giải tay: `20m ≥ 859 × (0,98 + 0,02m)` → `m ≥ 298,5` → `299`.

## 6. Tự đánh giá

- Hoàn thành phần soát số CP1–CP2, xác nhận code chạy được trên máy thứ hai, và hoàn thiện `pilot_plan.yaml` qua đủ các bước tự kiểm tra của CP4.
- Bộ nhãn nhiệm vụ C có dùng AI gợi ý; cần tự giải thích được lý do từng ca khi hội đồng hỏi, nhất là các ca dễ lẫn.
- Hạn chế: mde 6 điểm nghĩa là pilot có thể bỏ sót tác động thật 5 điểm (power 0,64); luật dừng về chi phí và làm lại cần thêm event đo chi phí và phút làm lại trong `chi_so.md`.
