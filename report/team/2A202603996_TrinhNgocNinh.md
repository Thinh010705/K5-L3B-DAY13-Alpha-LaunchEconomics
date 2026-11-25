# Báo cáo cá nhân — TrinhNgocNinh-2A202603996

## 1. Thông tin thành viên

- Họ tên: Trịnh Ngọc Ninh
- MSSV: 2A202603996
- Email: ninh.trinh.dev@gmail.com
- Vai trong nhóm: Người kiểm số

## 2. Phần việc phụ trách

- CP1: kiểm độc lập các con số của nhiệm vụ A (A1–A4) do người viết code tính ra, trước khi nhóm chép vào `report/team/bang_chi_phi.md`.
- Tính tay A1 và A4 để đối chiếu với `src/lab13.py`.

## 3. Đóng góp cụ thể

- Viết một script riêng (không dùng `src/lab13.py`) đọc `logix_runs.csv` và `logix_requests.csv` (có `keep_default_na=False`) để tính lại A2, A3, A4 và chi phí cả hệ thống.
- Chạy `src/lab13.py` của người viết code và đối chiếu từng dòng A1–B4 với script riêng và bảng đáp án trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
- Tính tay A1: (1 − 0,2²) ÷ 0,8 = 0,96 ÷ 0,8 = 1,20; 1 ÷ 0,8 = 1,25; hệ số tối đa 3 lần = [(1 − 0,2³) ÷ 0,8] ÷ (1 − 0,2³) = 1 ÷ 0,8 = 1,25.
- Tính tay A4: 45.000 × 900 ÷ 1.200 = 33.750 việc/tháng; 40.000.000 ÷ 33.750 = 1.185 đ/việc; 3.414 + 1.185 = 4.599 đ = 0,38× so với 12.000 đ (simulated). Một nửa khối lượng: 40.000.000 ÷ 16.875 = 2.370 đ/việc; 3.414 + 2.370 = 5.784 đ = 0,48× (simulated).

## 4. Bằng chứng

- Nhánh: `feat/ninh-kiem-so` (tách từ `feat/quang011105-lab13-code`).
- Kết quả đối chiếu (script độc lập = `lab13.py` = bảng đáp án, lệch 0%):
  - A2: token 245.585 đ, tool 84.000 đ, lần chạy 2 và 3 là 93.804 đ, xem lại 1.780.000 đ (simulated), làm lại 2.264.000 đ (simulated), tổng 4.373.585 đ, 978 việc thành công, chi phí mỗi việc thành công 4.472 đ (simulated), hoá đơn token + tool mỗi yêu cầu 274,7 đ; gấp 16,3 lần.
  - A3: noi_dia 2.696 đ (0,22×), hang_nang 8.221 đ (0,69×), quoc_te 22.515 đ (1,88×), doi_tac 10.215 đ (0,85×), đều simulated; tỉ lệ ok theo lần thử của quoc_te là 30,0% → 11,4% → 2,2%.
  - A4: 4.599 đ (0,38×) và 5.784 đ (0,48×), simulated.
- Ghi chú kỹ thuật: trên Windows, `python lab13.py` có thể báo `UnicodeEncodeError` khi in tiếng Việt; chạy với `PYTHONIOENCODING=utf-8` thì in đúng.

## 5. Công cụ AI đã dùng

- Công cụ: Claude Code, dùng để viết script kiểm số độc lập từ hai file CSV và chạy `lab13.py` để so output.
- Cách tự kiểm tra: tự tính tay A1 và A4 (mục 3), đối chiếu ba nguồn (script riêng, `lab13.py`, bảng đáp án trong hướng dẫn); không sửa hai file CSV.

## 6. Tự đánh giá

- Đã đối chiếu xong A1–A4, kèm B1–B4 trong output `lab13.py`; mọi số lệch 0% so với đáp án (ngưỡng nhận là 2%). Chưa kiểm phần D1 và E1.
