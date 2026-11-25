"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
import pandas as pd
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH = 40_000_000  # đồng / tháng


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1.0 / p
    return (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL, luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000.0 * gia_vao + runs['tokens_out'] / 1000.0 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    cps = tong / thanh_cong if thanh_cong > 0 else float('inf')
    hoa_don_moi_yc = (tien_token.sum() + tien_tool.sum()) / len(reqs)
    return {
        'token': tien_token.sum(),
        'tool': tien_tool.sum(),
        'chay_lai': chay_lai,
        'xem_lai': xem_lai,
        'lam_lai': lam_lai,
        'tong': tong,
        'thanh_cong': thanh_cong,
        'cps': cps,
        'hoa_don_moi_yc': hoa_don_moi_yc,
    }


def in_nhiem_vu_a(runs, reqs):
    """In kết quả Nhiệm vụ A2, A3, A4."""
    print('\n=== A2 · MÔ HÌNH CHI PHÍ TỪ TRACE ===')
    kq = mo_hinh(runs, reqs)
    for ten, gia_tri in kq.items():
        if ten == 'hoa_don_moi_yc':
            print(f'{ten:15s} {gia_tri:>14,.1f}')
        else:
            print(f'{ten:15s} {gia_tri:>14,.0f}')
    print(f"Gấp hoá đơn/yc : {kq['cps'] / kq['hoa_don_moi_yc']:.1f}x")
    print(f"Tỉ trọng xem lại [sim]: {kq['xem_lai'] / kq['tong'] * 100:.1f}%")
    print(f"Tỉ trọng làm lại [sim]: {kq['lam_lai'] / kq['tong'] * 100:.1f}%")
    khong_tc = len(reqs) - kq['thanh_cong']
    he_thong_moi_yc = (kq['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f"Chi phí cả hệ thống/yc [sim]: {he_thong_moi_yc:,.0f} đ ({he_thong_moi_yc / BASELINE:.2f}x)")

    print('\n=== A3 · TÁCH THEO LOẠI YÊU CẦU ===')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        r_loai = mo_hinh(runs, sub)
        ti_le_tc = r_loai['thanh_cong'] / len(sub) * 100
        lan_chay_tb = sub['so_lan_chay'].mean()
        print(f"{loai:10s} | n={len(sub):3d} | tc={ti_le_tc:5.1f}% | chạy/yc={lan_chay_tb:.2f} | "
              f"cps={r_loai['cps']:7,.0f} đ ({r_loai['cps'] / BASELINE:.2f}x) [sim]")

    print('\nTỉ lệ ok theo lần thử (attempt) và loại:')
    merged = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    merged['is_ok'] = (merged['status'] == 'ok').astype(float)
    piv = merged.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean') * 100
    print(piv.round(1).to_string())

    print('\n=== A4 · CHI PHÍ CỐ ĐỊNH (noi_dia + hang_nang) ===')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pham_vi)
    ti_le_tc_pv = kq_pv['thanh_cong'] / len(reqs)
    for nhan, khoi_luong in [('45.000 yc/tháng', 45000), ('Một nửa (22.500)', 22500)]:
        viec_tc_thang = khoi_luong * ti_le_tc_pv
        co_dinh_moi_viec = CHI_PHI_CO_DINH / viec_tc_thang
        tong_cps = kq_pv['cps'] + co_dinh_moi_viec
        print(f"{nhan:18s} | tc/tháng={viec_tc_thang:7,.0f} | cố định={co_dinh_moi_viec:5,.0f} đ | "
              f"cps+cố định={tong_cps:6,.0f} đ ({tong_cps / BASELINE:.2f}x) [sim]")


def in_nhiem_vu_b(runs, reqs):
    """In kết quả Nhiệm vụ B1, B2, B3, B4."""
    print('\n=== B1 · BẢNG ĐỘ NHẠY ===')
    goc = mo_hinh(runs, reqs)['cps']
    kich_ban = {
        'Giá token gấp đôi':        dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':   dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':          dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':     dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':          dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':     dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':           dict(luong_phut=2500),
        'Tối đa 2 lần chạy':        dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':           dict(max_lan_chay=1),
    }
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f"{ten:25s} {cps:8,.0f} đ {(cps / goc - 1) * 100:+6.1f}%")

    print('\n=== B2 · ĐỔI MỘT CẶP ===')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f"Token x2 + Xem lại x2     {cps_cap:8,.0f} đ {(cps_cap / goc - 1) * 100:+6.1f}%")

    print('\n=== B3 · GIỚI HẠN CHẠY LẠI & CHI PHÍ CẢ HỆ THỐNG ===')
    for k in [1, 2, 3]:
        r = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - r['thanh_cong']
        ca_he_thong = r['tong'] + BASELINE * khong_tc
        print(f"Tối đa {k} lần | trợ lý={r['tong']:9,.0f} đ | không tc={khong_tc:3d} | "
              f"cả hệ thống={ca_he_thong:9,.0f} đ | cps={r['cps']:6,.0f} đ [sim]")

    print('\n=== B4 · XEM LẠI 100% (noi_dia + hang_nang) ===')
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    pv_runs = runs[runs['request_id'].isin(pv['request_id'])]
    ok_reqs = pv_runs[pv_runs['status'] == 'ok']['request_id'].nunique()
    so_lam_lai = int((pv['ket_qua'] == 'lam_lai').sum())
    so_tc = int((pv['ket_qua'] == 'thanh_cong').sum())
    token_tool = (pv_runs['tokens_in'] / 1000.0 * GIA_VAO
                  + pv_runs['tokens_out'] / 1000.0 * GIA_RA
                  + pv_runs['tool_calls'] * GIA_TOOL).sum()
    phut_lam_lai_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    for nhan, phut_ll in [('9 phút/ca (đề)', 9.0), (f'{phut_lam_lai_tb:.1f} phút/ca (thực tế sim)', phut_lam_lai_tb)]:
        tong_b4 = ok_reqs * 5 * LUONG_PHUT + so_lam_lai * phut_ll * LUONG_PHUT + token_tool
        cps_b4 = tong_b4 / so_tc
        hoa_von = (so_tc * BASELINE - so_lam_lai * phut_ll * LUONG_PHUT - token_tool) / (ok_reqs * LUONG_PHUT)
        print(f"{nhan:28s} | tong={tong_b4:10,.0f} đ | cps={cps_b4:7,.0f} đ ({cps_b4 / BASELINE:.2f}x) | "
              f"hoà vốn xem lại <= {hoa_von:.1f} phút [sim]")


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm khi so sánh hai tỉ lệ độc lập."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil(
        (za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
        / (p2 - p1) ** 2
    )


def in_nhiem_vu_d_e(reqs):
    """In kết quả Nhiệm vụ D1 (cỡ mẫu) và E1 (tính thử chỉ số)."""
    print('\n=== D1 · CỠ MẪU PILOT (baseline=0.70, alpha=0.05, power=0.80, ICC=0.02) ===')
    icc = 0.02
    n_req = co_mau(0.70, 0.75)
    de_75 = 1 + (75 - 1) * icc
    n_nv_75 = math.ceil(n_req * de_75)
    c_nv_75 = math.ceil(n_nv_75 / 75)
    n_hieu_dung_20 = 20 / icc
    n_hieu_dung_6 = 6 / icc
    n_mde6 = co_mau(0.70, 0.76)
    m_mde6 = math.ceil(n_mde6 * (1 - icc) / (20 - n_mde6 * icc))
    de_mde6 = 1 + (m_mde6 - 1) * icc
    pwr_at_5 = NormalIndPower().power(
        effect_size=proportion_effectsize(0.75, 0.70), nobs1=n_mde6, alpha=0.05, ratio=1.0
    )

    print(f"a) Theo yêu cầu (+5đ)          : {n_req:,} yc/nhóm")
    print(f"b) Theo nhân viên (m=75)       : DE={de_75:.2f}, {n_nv_75:,} yc/nhóm -> {c_nv_75} người/nhóm (tổng {2*c_nv_75} > 40)")
    print(f"c) 20 nhân viên/nhóm (tối đa)  : n_hiệu_dụng < {n_hieu_dung_20:,.0f} (< {n_req:,} -> không đạt)")
    print(f"d) 6 depot/nhóm (tối đa)       : n_hiệu_dụng < {n_hieu_dung_6:,.0f}")
    print(f"e) Mức chênh 6đ ({n_mde6}/nhóm), 20 nv: m >= {m_mde6} yc/người (DE={de_mde6:.2f}); power nếu thật chỉ +5đ = {pwr_at_5:.2f}")

    print('\n=== D3 & E1 · CHỈ SỐ ĐỢT CHẠY THỬ (1.200 yêu cầu) ===')
    chinh = ((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)).mean()
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).mean()
    an_toan = (reqs['mo_lai_trong_7_ngay'] == 1).mean()
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    an_toan_pv = (pv['mo_lai_trong_7_ngay'] == 1).mean()
    print(f"Chính (đóng 24h & không mở lại 7 ngày): {chinh*100:.2f}% ({int(chinh*len(reqs))}/{len(reqs)})")
    print(f"Dùng (tỉ lệ sửa + bỏ khi xem lại)     : {bo_qua*100:.2f}% ({xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).sum()}/{len(xem)})")
    print(f"An toàn (mở lại 7 ngày - toàn mẫu)    : {an_toan*100:.2f}% ({int((reqs['mo_lai_trong_7_ngay']==1).sum())}/{len(reqs)})")
    print(f"An toàn (mở lại 7 ngày - phạm vi)     : {an_toan_pv*100:.2f}% ({int((pv['mo_lai_trong_7_ngay']==1).sum())}/{len(pv)})")


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    in_nhiem_vu_a(runs, reqs)
    in_nhiem_vu_b(runs, reqs)
    in_nhiem_vu_d_e(reqs)
