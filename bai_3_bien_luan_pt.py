# -*- coding: utf-8 -*-
"""
BÀI 3: GIẢI VÀ BIỆN LUẬN PHƯƠNG TRÌNH THEO THAM SỐ m
a. Phương trình bậc nhất: A(m)*x + B(m) = 0
   Ví dụ: (m^2 - 4)*x + 2m - 4 = 0
b*. Phương trình bậc hai: A(m)*x^2 + B(m)*x + C(m) = 0
   Ví dụ: (m - 2)*x^2 - 2*(m + 2)*x + m + 2 = 0
"""

import sympy as sp

m, x = sp.symbols("m x")

def giai_va_bien_luan_bac_nhat(eq_expr):
    """
    Giải và biện luận phương trình bậc nhất theo tham số m:
    Dạng: A(m)*x + B(m) = 0
    """
    print("\n" + "-" * 70)
    print("3a. GIẢI VÀ BIỆN LUẬN PHƯƠNG TRÌNH BẬC NHẤT THEO THAM SỐ m")
    print(f"Phương trình xét: {eq_expr} = 0")
    print("-" * 70)
    
    poly = sp.Poly(eq_expr, x)
    coeffs = poly.all_coeffs()
    
    if len(coeffs) == 2:
        A, B = coeffs[0], coeffs[1]
    elif len(coeffs) == 1:
        if poly.degree() == 1:
            A, B = coeffs[0], sp.S.Zero
        else:
            A, B = sp.S.Zero, coeffs[0]
    else:
        A, B = sp.S.Zero, sp.S.Zero
        
    print(f"Đưa về dạng chuẩn: ({A}).x + ({B}) = 0   <=>  ({A}).x = -({B})")
    
    # Tìm các giá trị m làm triệt tiêu hệ số bậc nhất A(m) = 0
    roots_A = sp.solve(sp.Eq(A, 0), m)
    # Lọc nghiệm thực
    real_roots_A = [r for r in roots_A if r.is_real]
    
    # Xét từng giá trị m đặc biệt
    for r in real_roots_A:
        A_val = A.subs(m, r)
        B_val = B.subs(m, r)
        print(f"\n+ Nếu m = {r}:")
        print(f"  Phương trình có dạng: ({A_val}).x + ({B_val}) = 0")
        if B_val == 0:
            print("  => Phương trình có vô số nghiệm thuộc R.")
        else:
            print(f"  => Phương trình có dạng: 0.x = {-B_val}")
            print("  => Phương trình vô nghiệm.")
            
    # Điều kiện A != 0
    if real_roots_A:
        cond_str = " và ".join([f"m ≠ {r}" for r in real_roots_A])
        print(f"\n+ Nếu {cond_str}:")
    else:
        print("\n+ Với mọi m ∈ R:")
        
    sol = sp.cancel(-B / A)
    print("  Phương trình có nghiệm duy nhất:")
    print(f"  x = -({B}) / ({A}) = {sol}")

def giai_va_bien_luan_bac_hai(eq_expr):
    """
    Giải và biện luận phương trình bậc hai theo tham số m:
    Dạng: A(m)*x^2 + B(m)*x + C(m) = 0
    """
    print("\n" + "-" * 70)
    print("3b*. GIẢI VÀ BIỆN LUẬN PHƯƠNG TRÌNH BẬC HAI THEO THAM SỐ m")
    print(f"Phương trình xét: {eq_expr} = 0")
    print("-" * 70)
    
    poly = sp.Poly(eq_expr, x)
    coeffs = poly.all_coeffs()
    
    # Đảm bảo có đủ 3 hệ số A, B, C
    deg = poly.degree()
    if deg == 2:
        A, B, C = coeffs[0], coeffs[1], coeffs[2]
    elif deg == 1:
        A, B, C = sp.S.Zero, coeffs[0], coeffs[1]
    else:
        A, B, C = sp.S.Zero, sp.S.Zero, coeffs[0] if coeffs else sp.S.Zero
        
    print(f"Hệ số A(m) = {A}")
    print(f"Hệ số B(m) = {B}")
    print(f"Hệ số C(m) = {C}")
    
    # 1. Trường hợp A(m) = 0: phương trình suy biến thành bậc nhất
    roots_A = [r for r in sp.solve(sp.Eq(A, 0), m) if r.is_real]
    if roots_A:
        print("\n[Trường hợp 1]: Xét hệ số A(m) = 0")
        for r in roots_A:
            B_sub = B.subs(m, r)
            C_sub = C.subs(m, r)
            print(f"  + Với m = {r}:")
            print(f"    Phương trình trở thành: ({B_sub}).x + ({C_sub}) = 0")
            if B_sub != 0:
                sol_linear = sp.cancel(-C_sub / B_sub)
                print(f"    => Phương trình bậc nhất có nghiệm duy nhất: x = {sol_linear}")
            else:
                if C_sub == 0:
                    print("    => Phương trình có vô số nghiệm thuộc R.")
                else:
                    print("    => Phương trình vô nghiệm.")
                    
    # 2. Trường hợp A(m) != 0: phương trình thực sự là bậc hai
    cond_A = " và ".join([f"m ≠ {r}" for r in roots_A]) if roots_A else "m bất kỳ"
    print(f"\n[Trường hợp 2]: Xét A(m) ≠ 0 ({cond_A})")
    print("  Phương trình là phương trình bậc hai.")
    
    # Kiểm tra B có chia hết cho 2 để dùng Delta' không
    B_simplified = sp.simplify(B)
    b_half = sp.simplify(B_simplified / 2)
    use_delta_prime = b_half.is_polynomial() or not b_half.has(sp.Rational(1, 2))
    
    if use_delta_prime:
        delta_prime = sp.factor(sp.simplify(b_half**2 - A * C))
        print(f"  Sử dụng biệt thức thu gọn Δ' = (B')^2 - A*C với B' = {b_half}:")
        print(f"  Δ' = ({b_half})^2 - ({A})*({C}) = {delta_prime}")
        roots_delta = [r for r in sp.solve(sp.Eq(delta_prime, 0), m) if r.is_real]
        
        # Biện luận theo delta'
        print(f"  - Nghiệm của Δ' = 0: m = {roots_delta}")
        print("  Biện luận các trường hợp:")
        
        # Ví dụ cụ thể với delta_prime = 4*(m + 2)
        print("  + Nếu Δ' < 0: Phương trình vô nghiệm thực.")
        print(f"    (Tức {delta_prime} < 0)")
        
        for r in roots_delta:
            print(f"  + Nếu m = {r} (Δ' = 0):")
            double_root = sp.cancel(-b_half.subs(m, r) / A.subs(m, r))
            print(f"    Phương trình có nghiệm kép: x = -B'/A = {double_root}")
            
        print("  + Nếu Δ' > 0 (và thỏa điều kiện A ≠ 0):")
        print(f"    (Tức {delta_prime} > 0)")
        print("    Phương trình có hai nghiệm phân biệt:")
        print("    x1 = (-B' - √Δ') / A")
        print("    x2 = (-B' + √Δ') / A")
        print(f"    Với x1,2 = [ -({b_half}) ± √({delta_prime}) ] / ({A})")
    else:
        delta = sp.factor(sp.simplify(B**2 - 4 * A * C))
        print(f"  Biệt thức Δ = B^2 - 4*A*C = {delta}")
        roots_delta = [r for r in sp.solve(sp.Eq(delta, 0), m) if r.is_real]
        print(f"  - Nghiệm của Δ = 0: m = {roots_delta}")
        print("  + Nếu Δ < 0: Phương trình vô nghiệm thực.")
        for r in roots_delta:
            print(f"  + Nếu m = {r} (Δ = 0):")
            double_root = sp.cancel(-B.subs(m, r) / (2 * A.subs(m, r)))
            print(f"    Phương trình có nghiệm kép: x = -B/(2A) = {double_root}")
        print("  + Nếu Δ > 0 (và A ≠ 0):")
        print(f"    Phương trình có 2 nghiệm phân biệt: x1,2 = [ -({B}) ± √({delta}) ] / [ 2*({A}) ]")

def chay_vi_du_de_bai():
    # Ví dụ câu a: (m^2 - 4)*x + 2*m - 4 = 0
    eq_a = (m**2 - 4)*x + 2*m - 4
    giai_va_bien_luan_bac_nhat(eq_a)
    
    # Ví dụ câu b*: (m - 2)*x^2 - 2*(m + 2)*x + m + 2 = 0
    eq_b = (m - 2)*x**2 - 2*(m + 2)*x + m + 2
    giai_va_bien_luan_bac_hai(eq_b)

if __name__ == "__main__":
    chay_vi_du_de_bai()
