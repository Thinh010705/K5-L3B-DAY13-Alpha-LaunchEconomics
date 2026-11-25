# Báo cáo cá nhân — CaoMinhQuang-2A202603906

## 1. Thông tin thành viên

- Họ tên: Cao Minh Quang
- MSSV: 2A202603906
- Email: cquang2k5@gmail.com
- Vai trong nhóm: Người viết code

## 2. Phần việc phụ trách

- Cài đặt và kiểm tra môi trường Python (`src/.venv`) theo `src/README.md`.
- Viết và chạy toàn bộ `src/lab13.py` cho các nhiệm vụ A (A1–A4), B (B1–B4), D1 (cỡ mẫu pilot) và hỗ trợ tính thử chỉ số D3, E1.

## 3. Đóng góp cụ thể

- Hoàn thiện ba hàm A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`) đạt 100% ba phép thử biết trước (`1,20 · 1,25 · 1,25`).
- Viết hàm `mo_hinh` (A2) cộng chi phí token + tool trên mọi lần chạy và giờ xem lại/làm lại (`simulated`), chia cho số yêu cầu `thanh_cong`.
- Cài đặt phần tách theo `loai` (A3), tỉ lệ `ok` theo `attempt`, và chi phí cố định 40 triệu đ/tháng (A4).
- Cài đặt bảng độ nhạy 9 kịch bản đơn (B1), kịch bản cặp (B2), chi phí cả hệ thống theo giới hạn chạy lại 1/2/3 lần (B3), và kịch bản xem lại 100% (B4).
- Cài đặt hàm `co_mau` và tính đủ 5 câu cỡ mẫu D1 cùng power ở mức chênh +5 điểm (`0,64`), tỉ lệ `mo_lai_trong_7_ngay` hiện tại và 3 chỉ số chạy thử E1.

## 4. Bằng chứng

- Nhánh làm việc: `feat/quang011105-lab13-code` (commit `ff5b231`).
- File code: `src/lab13.py`.
- Kết quả chạy `python lab13.py`:
  - `Ba phép thử đáp án biết trước: ĐẠT`
  - A2: tổng chi phí `4.373.585 đ`, `978` việc thành công, chi phí mỗi việc thành công `4.472 đ` (`simulated`), gấp `16,3x` hoá đơn/yêu cầu (`274,7 đ`).
  - A3: `noi_dia` `2.696 đ` (`0,22x`), `hang_nang` `8.221 đ` (`0,69x`), `quoc_te` `22.515 đ` (`1,88x`), `doi_tac` `10.215 đ` (`0,85x`) (`simulated`).
  - A4: cộng cố định `4.599 đ` (`0,38x`) ở `45.000 yc/tháng` và `5.784 đ` (`0,48x`) ở `22.500 yc/tháng` (`simulated`).
  - B1–B4: yếu tố nhạy nhất là làm lại (`+51,8%` khi gấp đôi); giới hạn 2 lần cho chi phí cả hệ thống thấp nhất (`6.901.220 đ`, `simulated`); xem lại 100% ở `15,3 phút/ca` là `12.415 đ` (`1,03x`, `simulated`).
  - D1 & E1: `1.251 yc/nhóm` theo yêu cầu; `m >= 299` ở mức chênh 6 điểm với 20 nhân viên/nhóm (`DE = 6,96`); chỉ số chính chạy thử `82,83%`, bỏ qua gợi ý `27,12%`, mở lại 7 ngày `4,25%` (`3,97%` trong phạm vi).

## 5. Công cụ AI đã dùng

- Công cụ: Trợ lý AI (Antigravity / Gemini) để đọc cấu trúc repo, gợi ý hoàn thiện code `src/lab13.py` và rà soát công thức.
- Cách tự kiểm tra:
  - Chạy trực tiếp `.\.venv\Scripts\python.exe lab13.py` trong `src/` để xác nhận qua 3 phép thử A1 (`1,20 · 1,25 · 1,25`).
  - Đối chiếu từng con số đầu ra của A2, A3, A4, B1–B4, D1 và E1 với bảng đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (sai số 0%, đạt ngưỡng ≤ 2%).
  - Kiểm tra không có từ cấm trong `report/team/` và giữ nguyên các file CSV đầu vào.

## 6. Tự đánh giá

- Hoàn thành đầy đủ, đúng hạn phần việc của vai trò **Người viết code**, số liệu rõ ràng, có nhãn `simulated` đầy đủ và đã đẩy lên nhánh riêng trên GitHub để nhóm tổng hợp.
