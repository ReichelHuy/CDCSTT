# -*- coding: utf-8 -*-
"""
BÀI 2*: LOGIC BẬC NHẤT NÂNG CAO VÀ CHỨNG MINH SUY LUẬN
Vị từ:
  L(x): "x là một nhà logic"
  C(x): "x uống café"
  W(x): "x làm việc chăm chỉ"
  T(x): "x phát biểu định lý"
  f(x): Hàm trả ra người bạn duy nhất của x.
"""

def print_bai_2_part1():
    print("=" * 75)
    print("BÀI 2* - PHẦN 1: BIỂU DIỄN LOGIC BẬC NHẤT (CÓ SỬ DỤNG DẤU =)")
    print("=" * 75)
    
    cau_a = (
        "a. Không nhà logic nào uống café:\n"
        "   - Biểu diễn chuẩn:  ∀x (L(x) → ¬C(x))  hoặc  ¬∃x (L(x) ∧ C(x))\n"
        "   - Dùng dấu =:       ∀x ∀y ((y = x ∧ L(x)) → ¬C(y))"
    )
    
    cau_b = (
        "b. Bất kỳ ai là một nhà logic cũng đều là bạn của ai đó:\n"
        "   - Diễn giải: Nếu x là nhà logic thì tồn tại người y sao cho bạn của y là x (x = f(y)).\n"
        "   - Biểu diễn:        ∀x (L(x) → ∃y (x = f(y)))"
    )
    
    cau_c = (
        "c. Không người nào phát biểu được định lý lại có một người bạn uống café:\n"
        "   - Diễn giải: Không có ai phát biểu định lý mà bạn của họ lại uống café.\n"
        "   - Biểu diễn chuẩn:  ∀x (T(x) → ¬C(f(x)))  hoặc  ¬∃x (T(x) ∧ C(f(x)))\n"
        "   - Dùng dấu =:       ∀x ∀y ((y = f(x) ∧ T(x)) → ¬C(y))"
    )
    
    cau_d = (
        "d. Ai có một người bạn làm việc chăm chỉ thì hoặc là một nhà logic hoặc cũng là một người làm việc chăm chỉ:\n"
        "   - Diễn giải: Với mọi x, nếu bạn của x (f(x)) làm việc chăm chỉ thì x là nhà logic hoặc x chăm chỉ.\n"
        "   - Biểu diễn chuẩn:  ∀x (W(f(x)) → (L(x) ∨ W(x)))\n"
        "   - Dùng dấu =:       ∀x ∀y ((y = f(x) ∧ W(y)) → (L(x) ∨ W(x)))"
    )
    
    cau_e = (
        "e. Mọi người bạn là một nhà logic:\n"
        "   - Diễn giải: Bất kỳ ai là bạn của một ai đó (tức tồn tại y sao cho x = f(y)) thì người đó là nhà logic.\n"
        "   - Biểu diễn với =:  ∀x (∃y (x = f(y)) → L(x))\n"
        "   - Tương đương:      ∀y L(f(y)) (Bạn của bất kỳ ai cũng là nhà logic)."
    )
    
    print(cau_a)
    print("\n" + cau_b)
    print("\n" + cau_c)
    print("\n" + cau_d)
    print("\n" + cau_e)

def print_bai_2_part2():
    print("\n" + "=" * 75)
    print("BÀI 2* - PHẦN 2: CHỨNG MINH HÌNH THỨC BẰNG CÁC LUẬT SUY DIỄN")
    print("=" * 75)
    print("TIỀN ĐỀ (PREMISES):")
    print("  (1) Tất cả nhà logic đều uống café:                 ∀x (L(x) → C(x))")
    print("  (2) Ai không phát biểu được định lý thì không café: ∀x (¬T(x) → ¬C(x))")
    print("  (3) Có một số người mà bạn của họ là nhà logic:     ∃x L(f(x))")
    print("\nKẾT LUẬN CẦN CHỨNG MINH:")
    print("  Có một nhà logic uống café và phát biểu được định lý: ∃x (L(x) ∧ C(x) ∧ T(x))")
    print("\nCÁC BƯỚC CHỨNG MINH HÌNH THỨC (FORMAL PROOF):")
    
    steps = [
        ("Bước 1", "∃x L(f(x))", "Tiền đề (3)"),
        ("Bước 2", "L(f(c))", "Đặc tả tồn tại (Existential Instantiation - EI) từ Bước 1, với c là một cá thể cụ thể trong miền biến."),
        ("Bước 3", "Đặt y_0 = f(c)", "Gọi y_0 là người bạn của c (do f(c) là một phần tử xác định thuộc miền biến). Ta có: L(y_0)."),
        ("Bước 4", "∀x (L(x) → C(x))", "Tiền đề (1)"),
        ("Bước 5", "L(y_0) → C(y_0)", "Đặc tả phổ dụng (Universal Instantiation - UI) từ Bước 4 thay x bằng y_0."),
        ("Bước 6", "C(y_0)", "Luật Khẳng định (Modus Ponens) từ Bước 3 và Bước 5."),
        ("Bước 7", "∀x (¬T(x) → ¬C(x))", "Tiền đề (2)"),
        ("Bước 8", "∀x (C(x) → T(x))", "Luật phản đảo (Contrapositive) tương đương logic từ Bước 7."),
        ("Bước 9", "C(y_0) → T(y_0)", "Đặc tả phổ dụng (UI) từ Bước 8 thay x bằng y_0."),
        ("Bước 10", "T(y_0)", "Luật Khẳng định (Modus Ponens) từ Bước 6 và Bước 9."),
        ("Bước 11", "L(y_0) ∧ C(y_0) ∧ T(y_0)", "Luật hội (Conjunction) kết hợp Bước 3, Bước 6 và Bước 10."),
        ("Bước 12", "∃x (L(x) ∧ C(x) ∧ T(x))", "Khái quát hóa tồn tại (Existential Generalization - EG) từ Bước 11.")
    ]
    
    for st, fml, reason in steps:
        print(f"  {st:<8} | {fml:<26} | Lý do: {reason}")
    print("\n=> ĐIỀU PHẢI CHỨNG MINH (Q.E.D.)")
    print("=" * 75)

if __name__ == "__main__":
    print_bai_2_part1()
    print_bai_2_part2()
