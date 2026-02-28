# test_client.py — Chạy thử client trước khi tích hợp Flask
# XOA FILE NAY SAU KHI TEST XONG

import sys
sys.path.insert(0, './generated')
import client

print("=" * 40)
print("TEST MATH SERVICE")
print("=" * 40)

# Test TinhTong
r1 = client.TinhTong(3.5, 2.0)
print(f"TinhTong(3.5, 2.0) -> {r1.mo_ta}")

# Test TinhNhanTu
r2 = client.TinhNhanTu(12)
print(f"TinhNhanTu(12) -> {r2.mo_ta}")

print("\n" + "=" * 40)
print("TEST STUDENT SERVICE")
print("=" * 40)

# Test ThemSinhVien
r3 = client.ThemSinhVien("SV200", "Phan Thi Ba", 7.8)
print(f"ThemSinhVien -> {r3.thong_bao}")

# Test LayDanhSach
r4 = client.LayDanhSach("all")
print(f"LayDanhSach(all) -> {r4.tong_so} sinh vien")

print("\n" + "=" * 40)
print("TEST SYSTEM SERVICE")
print("=" * 40)

# Test KiemTraTrangThai
r5 = client.KiemTraTrangThai("MathService")
print(f"TrangThai MathService -> hoat_dong={r5.hoat_dong}, luc {r5.thoi_gian}")