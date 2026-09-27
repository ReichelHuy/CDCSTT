# -*- coding: utf-8 -*-
"""
bai3_mach_dien.py
Mạng tính toán — MẠCH ĐIỆN MỘT CHIỀU, một điện trở.

Thuộc tính (M): U, I, R, P, S, d, rho, l
    U   : hiệu điện thế (V)          I   : cường độ dòng điện (A)
    R   : điện trở (Ohm)             P   : công suất mạch (W)
    S   : tiết diện dây (m^2)        d   : đường kính dây (m)
    rho : điện trở suất (Ohm.m)      l   : chiều dài dây (m)
Luật (F):
    (1) U = I*R
    (2) P = U*I
    (3) R = rho*l/S
    (4) S = pi*d^2/4

Nâng cao: nhiều điện trở mắc NỐI TIẾP / SONG SONG (phần cuối file).
"""
import sympy as sp
from mang_tinh_toan import Rule, ComputationNetwork, in_loi_giai

U, I, R, P, S, d, rho, l = sp.symbols('U I R P S d rho l', positive=True)

M = [U, I, R, P, S, d, rho, l]
F = [
    Rule(sp.Eq(U, I * R),          "U = I*R"),
    Rule(sp.Eq(P, U * I),          "P = U*I"),
    Rule(sp.Eq(R, rho * l / S),    "R = rho*l/S"),
    Rule(sp.Eq(S, sp.pi * d**2 / 4), "S = pi*d^2/4"),
]
MACH_DIEN = ComputationNetwork(M, F)

DV = {"U": " V", "I": " A", "R": " Ohm", "P": " W",
      "S": " m2", "d": " m", "rho": " Ohm.m", "l": " m"}


# ---------------------------------------------------------------------------
# NÂNG CAO: mạch nhiều điện trở nối tiếp / song song
# ---------------------------------------------------------------------------
def dien_tro_tuong_duong(Rs, cach="noi_tiep"):
    if cach == "noi_tiep":
        return sum(Rs)
    if cach == "song_song":
        return 1.0 / sum(1.0 / r for r in Rs)
    raise ValueError("cach phải là 'noi_tiep' hoặc 'song_song'")


def giai_mach_nhieu_dien_tro(Rs, U_nguon, cach="noi_tiep"):
    """Cho danh sách điện trở Rs và nguồn U, tính Rtđ, I, P và (U_i, I_i) mỗi trở."""
    Rtd = dien_tro_tuong_duong(Rs, cach)
    I_tong = U_nguon / Rtd
    P_tong = U_nguon * I_tong

    print("=" * 60)
    print(f"NÂNG CAO — {len(Rs)} điện trở mắc {cach.upper().replace('_',' ')}")
    print("=" * 60)
    print(f"Nguồn U = {U_nguon:g} V ; các R = {', '.join(f'{r:g}' for r in Rs)} Ohm")
    print(f"Điện trở tương đương  Rtđ = {Rtd:.4g} Ohm")
    print(f"Dòng điện toàn mạch   I  = {I_tong:.4g} A")
    print(f"Công suất toàn mạch   P  = {P_tong:.4g} W\n")
    print(f"{'R (Ohm)':>10}{'U_i (V)':>12}{'I_i (A)':>12}{'P_i (W)':>12}")
    for r in Rs:
        if cach == "noi_tiep":      # cùng dòng điện, khác hiệu điện thế
            Ii, Ui = I_tong, I_tong * r
        else:                       # song song: cùng U, khác dòng
            Ui, Ii = U_nguon, U_nguon / r
        print(f"{r:>10g}{Ui:>12.4g}{Ii:>12.4g}{Ui*Ii:>12.4g}")
    print()


if __name__ == "__main__":
    # 1 điện trở: biết I, R -> tìm U, P
    in_loi_giai(MACH_DIEN, {I: 2, R: 10}, goals=[U, P], don_vi=DV,
                tieu_de="MẠCH 1 ĐIỆN TRỞ — biết I=2A, R=10Ohm; tìm U, P")

    # Từ thông số dây dẫn: biết rho, l, d và U -> tìm S, R, I, P
    in_loi_giai(MACH_DIEN, {rho: 1.7e-8, l: 20, d: 0.001, U: 12},
                goals=[S, R, I, P], don_vi=DV,
                tieu_de="MẠCH 1 ĐIỆN TRỞ — dây đồng rho=1.7e-8, l=20m, d=1mm, U=12V")

    # Nâng cao
    giai_mach_nhieu_dien_tro([10, 20, 30], U_nguon=12, cach="noi_tiep")
    giai_mach_nhieu_dien_tro([10, 20, 30], U_nguon=12, cach="song_song")
