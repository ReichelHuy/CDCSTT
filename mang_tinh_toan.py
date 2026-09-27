# -*- coding: utf-8 -*-
"""
mang_tinh_toan.py
Engine MẠNG TÍNH TOÁN (Computation Network) dùng chung cho Bài 1, 2, 3.

Mô hình tri thức:  (M, F)
  - M : tập THUỘC TÍNH (biến), mỗi biến là một sympy Symbol.
  - F : tập LUẬT, mỗi luật là một PHƯƠNG TRÌNH (sympy Eq) nối một số biến.

Bài toán:  cho GIẢ THIẾT (biến đã biết giá trị) và MỤC TIÊU (biến cần tìm),
tìm LỜI GIẢI = dãy luật áp dụng theo thứ tự (suy diễn tiến / forward chaining).
Nguyên tắc: một luật "kích hoạt" được khi trong nó chỉ còn ĐÚNG 1 biến chưa biết
-> giải phương trình để suy ra biến đó.
"""
import sympy as sp


class Rule:
    """Một luật = một phương trình giữa các biến."""
    def __init__(self, equation, name=""):
        self.eq = equation
        self.vars = set(equation.free_symbols)
        self.name = name or str(equation)

    def unknowns(self, known):
        return self.vars - set(known)

    def can_fire(self, known):
        # Kích hoạt được khi còn đúng 1 ẩn số
        return len(self.unknowns(known)) == 1

    def fire(self, values):
        """values: {symbol: number}. Trả về (biến_suy_ra, giá_trị)."""
        target = self.unknowns(values.keys()).pop()
        expr = self.eq.subs(values)
        sols = sp.solve(expr, target)

        real = []
        for s in sols:
            try:
                c = complex(sp.N(s))
            except (TypeError, ValueError):
                continue
            if abs(c.imag) < 1e-9:
                real.append(c.real)
        if not real:
            return target, None
        pos = [x for x in real if x > 1e-12]        # ưu tiên nghiệm dương
        return target, (pos[0] if pos else real[0])


class ComputationNetwork:
    def __init__(self, variables, rules):
        self.M = list(variables)
        self.F = list(rules)

    def solve(self, gt, goals=None):
        """
        gt    : dict giả thiết  {symbol: value}
        goals : list biến mục tiêu (None = suy ra tất cả những gì có thể)
        Trả về: (solvable, values, trace)
                trace = [(Rule, biến, giá_trị), ...]  chính là lời giải.
        """
        values = dict(gt)
        goal_set = set(goals) if goals else set(self.M)
        trace = []
        progress = True
        while not goal_set <= set(values) and progress:
            progress = False
            for f in self.F:
                if f.can_fire(values):
                    target, val = f.fire(values)
                    if val is not None and target not in values:
                        values[target] = val
                        trace.append((f, target, val))
                        progress = True
        return (goal_set <= set(values)), values, trace


def in_loi_giai(cn, gt, goals=None, don_vi=None, tieu_de=""):
    """In gọn: giả thiết -> các bước -> kết quả mục tiêu."""
    don_vi = don_vi or {}
    if tieu_de:
        print("=" * 60)
        print(tieu_de)
        print("=" * 60)
    gt_txt = ", ".join(f"{k}={v:g}{don_vi.get(k,'')}" for k, v in gt.items())
    print(f"Giả thiết : {gt_txt}")
    print(f"Mục tiêu  : {', '.join(map(str, goals)) if goals else 'tất cả'}")

    ok, values, trace = cn.solve(gt, goals)
    print("\nLời giải (dãy luật suy diễn):")
    if not trace:
        print("  (không suy ra thêm được biến nào)")
    for i, (f, sym, val) in enumerate(trace, 1):
        print(f"  {i}. [{f.name}]  =>  {sym} = {val:.4g}{don_vi.get(sym,'')}")

    if goals:
        print("\nKết quả:")
        for g in goals:
            if g in values:
                print(f"  {g} = {values[g]:.6g}{don_vi.get(g,'')}")
            else:
                print(f"  {g} = KHÔNG suy ra được")
    print("=> " + ("GIẢI ĐƯỢC\n" if ok else "KHÔNG đủ dữ kiện\n"))
    return values
