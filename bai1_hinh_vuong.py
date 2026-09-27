# -*- coding: utf-8 -*-
"""
bai1_hinh_vuong.py
Mạng tính toán trên miền tri thức HÌNH VUÔNG.

Thuộc tính (M): a (cạnh), p (chu vi), S (diện tích), d (đường chéo)
Luật (F):
    (1) p = 4a
    (2) S = a^2
    (3) d = a*sqrt(2)
"""
import sympy as sp
from mang_tinh_toan import Rule, ComputationNetwork, in_loi_giai

a, p, S, d = sp.symbols('a p S d', positive=True)

M = [a, p, S, d]
F = [
    Rule(sp.Eq(p, 4 * a),          "p = 4a"),
    Rule(sp.Eq(S, a**2),           "S = a^2"),
    Rule(sp.Eq(d, a * sp.sqrt(2)), "d = a*sqrt(2)"),
]
HINH_VUONG = ComputationNetwork(M, F)

if __name__ == "__main__":
    # Bài toán thuận: biết cạnh -> tìm chu vi, diện tích, đường chéo
    in_loi_giai(HINH_VUONG, {a: 5}, goals=[p, S, d],
                tieu_de="HÌNH VUÔNG — biết cạnh a=5, tìm p, S, d")

    # Bài toán ngược: biết diện tích -> tìm cạnh, chu vi, đường chéo
    in_loi_giai(HINH_VUONG, {S: 36}, goals=[a, p, d],
                tieu_de="HÌNH VUÔNG — biết diện tích S=36, tìm a, p, d")

    # Biết đường chéo -> tìm cạnh, chu vi, diện tích
    in_loi_giai(HINH_VUONG, {d: 10}, goals=[a, p, S],
                tieu_de="HÌNH VUÔNG — biết đường chéo d=10, tìm a, p, S")
