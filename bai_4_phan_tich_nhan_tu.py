# -*- coding: utf-8 -*-
"""
BÀI 4: PHÂN TÍCH ĐA THỨC THÀNH NHÂN TỬ TỪNG BƯỚC
Ý tưởng thuật toán:
- Sử dụng hàm factor() của Sympy để tìm kết quả phân tích.
- Từ kết quả đó, suy luận ngược ra các bước giải:
  + Tách các hạng tử của thừa số thứ nhất.
  + Nhân từng hạng tử đó với thừa số còn lại.
  + Khai triển từng nhóm tích thành các hạng tử tương ứng.
  + Đặt nhân tử chung cho từng nhóm.
  + Rút nhân tử chung cuối cùng ra ngoài.
- Hỗ trợ đệ quy cho các đa thức có nhiều hơn 2 thừa số.
"""

import sympy as sp

def format_poly(expr):
    """Định dạng biểu thức đẹp mắt"""
    return str(expr).replace("**", "^")

def phan_tich_tung_buoc_2_thua_so(f1, f2):
    """
    Thực hiện phân tích từng bước cho tích f1 * f2
    với f1 là thừa số thứ nhất, f2 là thừa số thứ hai.
    """
    # Tách các hạng tử của thừa số thứ nhất
    terms_f1 = sp.Add.make_args(f1)
    
    # Bước 1: Khai triển từng nhóm (hạng tử của f1 * f2)
    # Ví dụ: (x^2 - xy) + (xy - y^2)
    expanded_groups = [sp.expand(t * f2) for t in terms_f1]
    
    # Chuỗi bước 1
    step1_parts = []
    for g in expanded_groups:
        step1_parts.append(f"({format_poly(g)})")
    step1_str = " + ".join(step1_parts)
    
    # Bước 2: Đặt nhân tử chung từng nhóm
    # Ví dụ: x(x - y) + y(x - y)
    step2_parts = []
    for t in terms_f1:
        step2_parts.append(f"{format_poly(t)}({format_poly(f2)})")
    step2_str = " + ".join(step2_parts)
    
    # Bước 3: Đưa về dạng tích cuối cùng
    # Ví dụ: (x + y)(x - y)
    step3_str = f"({format_poly(f1)})({format_poly(f2)})"
    
    return step1_str, step2_str, step3_str

def phan_tich_da_thuc_tung_buoc(expr, depth=0):
    """
    Phân tích đa thức thành nhân tử từng bước theo phương pháp suy luận ngược.
    Hỗ trợ đệ quy.
    """
    indent = "  " * depth
    print(f"\n{indent}Phân tích đa thức: {format_poly(expr)}")
    
    fact = sp.factor(expr)
    if fact == expr or not fact.is_Mul:
        print(f"{indent}Đa thức không thể phân tích thành nhân tử tiếp (tối giản hoặc đơn thức): {format_poly(fact)}")
        return fact
        
    coeff, factors = fact.as_coeff_mul()
    factors = list(factors)
    
    # Nếu có hệ số tự do khác 1, nhân vào thừa số đầu hoặc giữ riêng
    if coeff != 1:
        print(f"{indent}Rút hệ số chung ra ngoài: {coeff}")
        expr_inner = sp.simplify(expr / coeff)
        print(f"{indent}= {coeff} * [{format_poly(expr_inner)}]")
        # Phân tích phần bên trong
        inner_fact = phan_tich_da_thuc_tung_buoc(expr_inner, depth + 1)
        res = f"{coeff} * ({format_poly(inner_fact)})"
        return res
        
    if len(factors) == 2:
        f1, f2 = factors[0], factors[1]
        step1, step2, step3 = phan_tich_tung_buoc_2_thua_so(f1, f2)
        print(f"{indent}= {step1}")
        print(f"{indent}= {step2}")
        print(f"{indent}= {step3}")
        return fact
    elif len(factors) > 2:
        # Trường hợp đệ quy cho nhiều hơn 2 thừa số
        f1 = factors[0]
        f_rest = sp.Mul(*factors[1:])
        step1, step2, step3 = phan_tich_tung_buoc_2_thua_so(f1, f_rest)
        print(f"{indent}= {step1}")
        print(f"{indent}= {step2}")
        print(f"{indent}= {step3}")
        print(f"{indent}[Tiếp tục phân tích đệ quy cho thừa số phức tạp: ({format_poly(f_rest)})]:")
        phan_tich_da_thuc_tung_buoc(f_rest, depth + 1)
        return fact
    else:
        print(f"{indent}= {format_poly(fact)}")
        return fact

def chay_vi_du():
    print("=" * 70)
    print("BÀI 4: CHƯƠNG TRÌNH GIẢI TỪNG BƯỚC PHÂN TÍCH ĐA THỨC THÀNH NHÂN TỬ")
    print("=" * 70)
    
    x, y, z = sp.symbols("x y z")
    
    # 1. Ví dụ mẫu của đề bài: x^2 - y^2
    print("\n[VÍ DỤ 1 - MẪU TRONG ĐỀ BÀI]")
    expr1 = x**2 - y**2
    phan_tich_da_thuc_tung_buoc(expr1)
    
    # 2. Ví dụ mở rộng 2: x^2 - 5x + 6
    print("\n" + "-" * 70)
    print("[VÍ DỤ 2 - TAM THỨC BẬC HAI: x^2 - 5x + 6]")
    expr2 = x**2 - 5*x + 6
    phan_tich_da_thuc_tung_buoc(expr2)
    
    # 3. Ví dụ mở rộng 3 (Đệ quy 3 nhân tử): (x^2 - y^2)*(x + 1)
    print("\n" + "-" * 70)
    print("[VÍ DỤ 3 - ĐỆ QUY VỚI 3 THỪA SỐ: (x^2 - y^2)(x + 1)]")
    expr3 = sp.expand((x**2 - y**2) * (x + 1))
    phan_tich_da_thuc_tung_buoc(expr3)
    
    print("=" * 70)

if __name__ == "__main__":
    chay_vi_du()
