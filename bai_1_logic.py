# -*- coding: utf-8 -*-
"""
BÀI 1: BIỂU DIỄN LOGIC VỊ TỪ
Không gian biến (Domain): Tất cả sinh viên trong lớp.
Vị từ:
  C(x): "x có một con mèo"
  D(x): "x có một con chó"
  F(x): "x có một con chồn"
"""

class LogicProposition:
    def __init__(self, cau, bieu_thuc_logic, giai_thich):
        self.cau = cau
        self.bieu_thuc_logic = bieu_thuc_logic
        self.giai_thich = giai_thich

def get_bai_1_solutions():
    solutions = [
        LogicProposition(
            cau="a) Một sinh viên trong lớp có một con mèo, một con chó hay một con chồn.",
            bieu_thuc_logic="∃x (C(x) ∨ D(x) ∨ F(x))",
            giai_thich="Tồn tại ít nhất một sinh viên x trong lớp mà x có mèo, hoặc có chó, hoặc có chồn."
        ),
        LogicProposition(
            cau="b) Tất cả sinh viên trong lớp có một con mèo, một con chó hay một con chồn.",
            bieu_thuc_logic="∀x (C(x) ∨ D(x) ∨ F(x))",
            giai_thich="Với mọi sinh viên x trong lớp, x đều sở hữu ít nhất một trong ba loại thú nuôi (mèo, chó hoặc chồn)."
        ),
        LogicProposition(
            cau="c) Một sinh viên nào đó có một con mèo và một con chồn nhưng không có chó.",
            bieu_thuc_logic="∃x (C(x) ∧ F(x) ∧ ¬D(x))",
            giai_thich="Tồn tại sinh viên x đồng thời có mèo, có chồn và không nuôi chó."
        ),
        LogicProposition(
            cau="d) Không có sinh viên nào trong lớp có một con mèo, một con chó và một con chồn.",
            bieu_thuc_logic="¬∃x (C(x) ∧ D(x) ∧ F(x))   [tương đương: ∀x ¬(C(x) ∧ D(x) ∧ F(x))]",
            giai_thich="Phủ định của mệnh đề tồn tại một sinh viên có cả 3 con vật. Theo luật De Morgan cho lượng từ, tương đương với mọi sinh viên đều không sở hữu đồng thời cả 3 loài."
        ),
        LogicProposition(
            cau="e) Với mỗi loại con vật trên, có một sinh viên trong lớp có một con.",
            bieu_thuc_logic="(∃x C(x)) ∧ (∃y D(y)) ∧ (∃z F(z))",
            giai_thich="Có 3 loại vật nuôi (mèo, chó, chồn). Mỗi loài đều có ít nhất một sinh viên nuôi loài đó (không bắt buộc cùng một sinh viên)."
        )
    ]
    return solutions

def simulate_validation():
    """Mô phỏng kiểm chứng logic trên một tập sinh viên mẫu"""
    # Sinh viên mẫu: dict id -> {'C': bool, 'D': bool, 'F': bool}
    students = {
        "SV1": {"C": True,  "D": False, "F": False},
        "SV2": {"C": False, "D": True,  "F": False},
        "SV3": {"C": False, "D": False, "F": True},
        "SV4": {"C": True,  "D": False, "F": True},
    }
    
    # a) Tồn tại x có C hoặc D hoặc F
    res_a = any(s["C"] or s["D"] or s["F"] for s in students.values())
    # b) Mọi x có C hoặc D hoặc F
    res_b = all(s["C"] or s["D"] or s["F"] for s in students.values())
    # c) Tồn tại x có C, F và không D
    res_c = any(s["C"] and s["F"] and not s["D"] for s in students.values())
    # d) Không có x nào có cả C, D và F
    res_d = not any(s["C"] and s["D"] and s["F"] for s in students.values())
    # e) Tồn tại có C, tồn tại có D, tồn tại có F
    res_e = (any(s["C"] for s in students.values()) and 
             any(s["D"] for s in students.values()) and 
             any(s["F"] for s in students.values()))
    
    return {
        "a": res_a,
        "b": res_b,
        "c": res_c,
        "d": res_d,
        "e": res_e
    }

def print_bai_1():
    print("=" * 70)
    print("BÀI 1: BIỂU DIỄN MỆNH ĐỀ THEO C(x), D(x), F(x)")
    print("=" * 70)
    sols = get_bai_1_solutions()
    for sol in sols:
        print(f"\n{sol.cau}")
        print(f"  Biểu diễn logic: {sol.bieu_thuc_logic}")
        print(f"  Giải thích:      {sol.giai_thich}")
    
    print("\n--- Mô phỏng kiểm chứng chân trị trên mô hình mẫu ---")
    sim = simulate_validation()
    for k, v in sim.items():
        print(f"  Câu {k}: Giá trị chân trị = {v}")
    print("=" * 70)

if __name__ == "__main__":
    print_bai_1()
