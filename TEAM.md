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
