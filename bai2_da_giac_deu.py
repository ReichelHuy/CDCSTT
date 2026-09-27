# -*- coding: utf-8 -*-
"""
bai2_da_giac_deu.py
Mạng tính toán trên miền tri thức ĐA GIÁC ĐỀU n cạnh.

Thuộc tính (M): n, a, S, P, R, alpha, h
    n     : số cạnh
    a     : độ dài cạnh
    R     : bán kính đường tròn ngoại tiếp
    alpha : góc ở tâm chắn một cạnh
    h     : trung đoạn (khoảng cách từ tâm tới cạnh = bán kính nội tiếp)
    P     : chu vi
    S     : diện tích
Luật (F):
    (1) alpha = 2*pi/n
    (2) a = 2*R*sin(alpha/2)
    (3) h = R*cos(alpha/2)
    (4) P = n*a
    (5) S = (n*a*h)/2   ( = P*h/2 )
"""
import sympy as sp
from mang_tinh_toan import Rule, ComputationNetwork, in_loi_giai

n, a, S, P, R, alpha, h = sp.symbols('n a S P R alpha h', positive=True)

M = [n, a, S, P, R, alpha, h]
F = [
    Rule(sp.Eq(alpha, 2 * sp.pi / n),        "alpha = 2*pi/n"),
    Rule(sp.Eq(a, 2 * R * sp.sin(alpha / 2)), "a = 2R*sin(alpha/2)"),
    Rule(sp.Eq(h, R * sp.cos(alpha / 2)),     "h = R*cos(alpha/2)"),
    Rule(sp.Eq(P, n * a),                     "P = n*a"),
    Rule(sp.Eq(S, n * a * h / 2),             "S = n*a*h/2"),
]
DA_GIAC_DEU = ComputationNetwork(M, F)

DV = {"alpha": " rad"}

if __name__ == "__main__":
    # Biết n và R -> tìm cạnh, trung đoạn, chu vi, diện tích
    in_loi_giai(DA_GIAC_DEU, {n: 6, R: 4}, goals=[alpha, a, h, P, S], don_vi=DV,
                tieu_de="ĐA GIÁC ĐỀU — lục giác n=6, R=4; tìm a, h, P, S")

    # Bát giác đều n=8, R=5
    in_loi_giai(DA_GIAC_DEU, {n: 8, R: 5}, goals=[a, P, S], don_vi=DV,
                tieu_de="ĐA GIÁC ĐỀU — bát giác n=8, R=5; tìm a, P, S")

    # Biết n và cạnh a -> tìm R, trung đoạn, chu vi, diện tích
    in_loi_giai(DA_GIAC_DEU, {n: 6, a: 4}, goals=[R, h, P, S], don_vi=DV,
                tieu_de="ĐA GIÁC ĐỀU — biết n=6, a=4; tìm R, h, P, S")
