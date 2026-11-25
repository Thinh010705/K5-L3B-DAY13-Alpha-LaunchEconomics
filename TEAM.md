# Team

## Thông tin nhóm

- Tên nhóm: Alpha
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Alpha-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/Thinh010705/K5-L3B-DAY13-Alpha-LaunchEconomics`

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Cao Minh Quang | 2A202603906 | cquang2k5@gmail.com | quang011105 | Người viết code |
|   2 | Trịnh Ngọc Ninh | 2A202603996 | ninh.trinh.dev@gmail.com | ninhtrinhdev | Người kiểm số |
|   3 | Hoàng Minh Quyền | 2A202603961 | quyentryhard@gmail.com | EddyTryToCode | Người gắn nhãn 1 |
|   4 | Nguyễn Năng Thịnh | 2A202604028 | thinh010705@gmail.com | Thinh010705 | Người gắn nhãn 2, kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## Hoàng Minh Quyền-2A202603961

### Phần việc phụ trách

- Người gắn nhãn 1: đọc đề, theo dõi điều kiện "Xong khi" của CP1–CP5; gắn nhãn 20 ca lỗi ở CP3 (cột "Nhãn người 1" trong `report/team/bang_loi.md`).
- Nhiệm vụ D: viết `report/team/pilot_plan.yaml` (CP4).

### Đóng góp cụ thể

- Chạy lại `src/lab13.py` trên máy thứ hai: ba phép thử A1 `ĐẠT`, output trùng `src/lab13_output.txt`; soát số CP1–CP2 trong `bang_chi_phi.md` với bảng đối chiếu.
- Gắn 20 nhãn người 1 trong `bang_loi.md` (đồng thuận với người gắn nhãn 2: 17/20 = 85%).
- Hoàn thiện `pilot_plan.yaml`: năm câu D1, năm câu D2, đánh đổi mde 6 điểm (power 0,64 nếu tác động thật 5 điểm), chia theo nhân viên 20 + 20, bốn luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ, ngày quyết định 2027-01-15.

### Bằng chứng

- Nhánh `quyen_gannhan1`; commit nhãn `6d734d5`.
- File: `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/2A202603961_HoangMinhQuyen.md`.

## Nguyễn Năng Thịnh-2A202604028

### Phần việc phụ trách

- Vai trò: Người gắn nhãn 2 kiêm giữ hồ sơ.
- Gắn nhãn độc lập 20 ca lỗi theo năm loại lỗi của Google PAIR.
- Tổng hợp kết quả các nhiệm vụ A–E vào hồ sơ Launch v0.
- Xây dựng đặc tả chỉ số, danh sách event và bảng rủi ro kinh tế.
- Tổng hợp báo cáo nhóm và chuẩn bị hồ sơ trình hội đồng Gate 2a.

### Đóng góp cụ thể

- CP1: Tổng hợp kết quả mô hình chi phí và so sánh với phương án nhân viên tự làm.
- CP2: Tổng hợp phân tích độ nhạy, xác định ba yếu tố ảnh hưởng lớn nhất đến chi phí.
- CP3: Gắn nhãn độc lập 20 ca, đạt đồng thuận 85% (17/20 ca); tổng hợp quy tắc phân biệt cho 3 ca bất đồng và 5 phương án khắc phục tương ứng với 5 loại lỗi.
- CP4: Rà soát kế hoạch pilot, đánh giá cỡ mẫu, đánh đổi MDE và đề xuất cải thiện luật dừng.
- CP5: Xây dựng đặc tả 5 chỉ số, 7 event, 4 rủi ro kinh tế; tổng hợp hồ sơ Launch v0 và đề xuất Go có điều kiện.
- Soạn báo cáo nhóm và hoàn thiện báo cáo cá nhân.

### Bằng chứng

- `report/team/bang_loi.md`: Tổng hợp hai bộ nhãn và phương án khắc phục lỗi.
- `report/team/chi_so.md`: Đặc tả chỉ số, event và rủi ro kinh tế.
- `report/team/ho_so_launch_v0.md`: Hồ sơ tổng hợp phục vụ Gate 2a.
- `report/team/group_report.md`: Báo cáo chung của nhóm.
- `report/team/2A202604028_NguyenNangThinh.md`: Báo cáo cá nhân.
- Nhánh đóng góp: `feature/launch-dossier`.
- Commit: 0d7f2c2ada99dd33bf71aeb91f76325536f2ac1f, e071f3832566014380f421e5121ce76c1e81aca1, 53634c75389ecd9772a75677c997ef3b9e71fc4d, 34ce6d990872f891d106d853d285ed8e82300d8a, 1daa437a572ea532d0eefd430dc76ca30895d03d, 70698b2f3fa8a78edf7fb778fc663b3d8b38ff3e.

## Cao Minh Quang-2A202603906
### Phần việc phụ trách

- Cài đặt và kiểm tra môi trường Python (`src/.venv`) theo `src/README.md`.
- Viết và chạy toàn bộ `src/lab13.py` cho các nhiệm vụ A (A1–A4), B (B1–B4), D1 (cỡ mẫu pilot) và hỗ trợ tính thử chỉ số D3, E1.

### Đóng góp cụ thể

- Hoàn thiện ba hàm A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`) đạt 100% ba phép thử biết trước (`1,20 · 1,25 · 1,25`).
- Viết hàm `mo_hinh` (A2) cộng chi phí token + tool trên mọi lần chạy và giờ xem lại/làm lại (`simulated`), chia cho số yêu cầu `thanh_cong`.
- Cài đặt phần tách theo `loai` (A3), tỉ lệ `ok` theo `attempt`, và chi phí cố định 40 triệu đ/tháng (A4).
- Cài đặt bảng độ nhạy 9 kịch bản đơn (B1), kịch bản cặp (B2), chi phí cả hệ thống theo giới hạn chạy lại 1/2/3 lần (B3), và kịch bản xem lại 100% (B4).
- Cài đặt hàm `co_mau` và tính đủ 5 câu cỡ mẫu D1 cùng power ở mức chênh +5 điểm (`0,64`), tỉ lệ `mo_lai_trong_7_ngay` hiện tại và 3 chỉ số chạy thử E1.

### Bằng chứng

- Nhánh làm việc: `feat/quang011105-lab13-code` (commit `ff5b231`).
- File code: `src/lab13.py`.
- Kết quả chạy `python lab13.py`:
  - `Ba phép thử đáp án biết trước: ĐẠT`
  - A2: tổng chi phí `4.373.585 đ`, `978` việc thành công, chi phí mỗi việc thành công `4.472 đ` (`simulated`), gấp `16,3x` hoá đơn/yêu cầu (`274,7 đ`).
  - A3: `noi_dia` `2.696 đ` (`0,22x`), `hang_nang` `8.221 đ` (`0,69x`), `quoc_te` `22.515 đ` (`1,88x`), `doi_tac` `10.215 đ` (`0,85x`) (`simulated`).
  - A4: cộng cố định `4.599 đ` (`0,38x`) ở `45.000 yc/tháng` và `5.784 đ` (`0,48x`) ở `22.500 yc/tháng` (`simulated`).
  - B1–B4: yếu tố nhạy nhất là làm lại (`+51,8%` khi gấp đôi); giới hạn 2 lần cho chi phí cả hệ thống thấp nhất (`6.901.220 đ`, `simulated`); xem lại 100% ở `15,3 phút/ca` là `12.415 đ` (`1,03x`, `simulated`).
  - D1 & E1: `1.251 yc/nhóm` theo yêu cầu; `m >= 299` ở mức chênh 6 điểm với 20 nhân viên/nhóm (`DE = 6,96`); chỉ số chính chạy thử `82,83%`, bỏ qua gợi ý `27,12%`, mở lại 7 ngày `4,25%` (`3,97%` trong phạm vi).

## TrinhNgocNinh-2A202603996

### Phần việc phụ trách

- Người kiểm số: kiểm độc lập các con số do người viết code tính ra, trước khi nhóm chép vào hồ sơ.
- CP1: kiểm A1–A4; CP2: kiểm bảng độ nhạy B1–B4; CP4: kiểm D1 và các trường của `report/team/pilot_plan.yaml`; CP5: tính lại ba chỉ số E1.

### Đóng góp cụ thể

- Viết script riêng (không dùng `src/lab13.py`) đọc `logix_runs.csv` và `logix_requests.csv` để tính lại A2, A3, A4, B1–B4 rồi đối chiếu với `src/lab13.py` và bảng đáp án: lệch 0%.
- Tính tay A1 (1,20 · 1,25 · 1,25) và A4 (4.599 đ, 0,38×; một nửa khối lượng 5.784 đ, 0,48×, simulated).
- Tính lại D1 độc lập (1.251; 3.103 với DE 2,48; 859 với DE 6,96): khớp `pilot_plan.yaml`; kiểm file đọc được bằng `yaml.safe_load`, không còn dấu `?`, bốn luật dừng đủ bốn vế.
- Tính lại E1 trên 1.200 yêu cầu: 82,83% · 27,12% · 4,25%.
- Nêu các góp ý cho hồ sơ: ngưỡng chi phí 8.000 đ khá lỏng so với 3.414 đ, ngưỡng xem lại 5,1 phút lỏng hơn hoà vốn 4,8 phút, tên vai trò chưa đồng bộ giữa các file.

### Bằng chứng

- Nhánh `feat/ninh-kiem-so`; commit gần nhất `9247c66`.
- File: `report/team/2A202603996_TrinhNgocNinh.md` (báo cáo cá nhân, có toàn bộ số đối chiếu).
