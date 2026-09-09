# -*- coding: utf-8 -*-
"""
BÀI 4: PHÂN TÍCH ĐA THỨC THÀNH NHÂN TỬ TỪNG BƯỚC
Ý tưởng thuật toán:
- Dùng factor_list của Sympy để lấy danh sách nhân tử bất khả quy.
- Từ danh sách đó, suy luận ngược ra các bước giải:
  + Rút nhân tử chung (hệ số hằng và các đơn thức) ra ngoài trước.
  + Tách các hạng tử của thừa số thứ nhất.
  + Nhân từng hạng tử đó với thừa số còn lại rồi khai triển.
  + Đặt nhân tử chung cho từng nhóm.
  + Gom lại thành dạng tích.
- Đệ quy cho thừa số còn lại khi nó vẫn tách được tiếp.
"""

import sympy as sp


def format_poly(expr):
    """Đổi ký hiệu luỹ thừa ** của sympy thành ^ cho dễ đọc."""
    return str(expr).replace("**", "^")


def lay_nhan_tu_bat_kha_quy(expr):
    """
    Trả về (hệ số hằng, danh sách nhân tử bất khả quy).
    Luỹ thừa được trải thành nhiều bản: (x + 1)**2 cho [x + 1, x + 1].

    Dùng factor_list thay cho factor vì factor trả về chính biểu thức cũ khi
    đầu vào đã ở dạng tích, khiến không phân biệt được "đã phân tích rồi" với
    "bất khả quy". factor_list luôn cho biết số nhân tử thật sự.
    """
    he_so, cac_cap = sp.factor_list(expr)
    nhan_tu = []
    for co_so, so_mu in cac_cap:
        nhan_tu.extend([co_so] * so_mu)
    return he_so, nhan_tu


def dem_hang_tu(expr):
    """Số hạng tử của một biểu thức: x + 1 có 2, còn 3*x^2 có 1."""
    return len(sp.Add.make_args(expr))


def co_hang_tu_am(expr):
    """Đa thức có hạng tử mang dấu trừ hay không."""
    return any(t.could_extract_minus_sign() for t in sp.Add.make_args(expr))


def noi_tong(cac_phan):
    """Nối các hạng tử thành một tổng, đổi '+ -a' thành '- a'."""
    ket_qua = cac_phan[0]
    for phan in cac_phan[1:]:
        if phan.startswith("-"):
            ket_qua += " - " + phan[1:]
        else:
            ket_qua += " + " + phan
    return ket_qua


def viet_tich(hang_tu, f2_str):
    """Viết tích hang_tu * (f2), bỏ hệ số 1 thừa cho đúng lối viết tay."""
    if hang_tu == 1:
        return f"({f2_str})"
    if hang_tu == -1:
        return f"-({f2_str})"
    return f"{format_poly(hang_tu)}({f2_str})"


def dung_ba_buoc(f1, f2):
    """
    Dựng ba dòng biến đổi cho tích f1 * f2, với f1 có từ hai hạng tử trở lên.
    Đây là phần suy luận ngược mà đề bài yêu cầu.
    """
    hang_tu_f1 = sp.Add.make_args(f1)
    f2_str = format_poly(f2)

    # Bước 1: nhân từng hạng tử của f1 với f2 rồi khai triển
    nhom = [sp.expand(t * f2) for t in hang_tu_f1]
    buoc_1 = " + ".join(f"({format_poly(g)})" for g in nhom)

    # Bước 2: đặt nhân tử chung f2 cho từng nhóm
    buoc_2 = noi_tong([viet_tich(t, f2_str) for t in hang_tu_f1])

    # Bước 3: gom lại thành tích
    buoc_3 = f"({format_poly(f1)})({f2_str})"

    return buoc_1, buoc_2, buoc_3


def phan_tich_da_thuc_tung_buoc(expr, do_sau=0):
    """
    In lời giải từng bước cho bài toán phân tích expr thành nhân tử.
    Trả về dạng tích cuối cùng dưới kiểu biểu thức sympy.
    """
    thut = "  " * do_sau
    print(f"\n{thut}Phân tích đa thức: {format_poly(expr)}")

    he_so, nhan_tu = lay_nhan_tu_bat_kha_quy(expr)

    if len(nhan_tu) <= 1 and he_so == 1:
        print(f"{thut}Đa thức bất khả quy, không phân tích được tiếp.")
        return expr

    don_thuc = [f for f in nhan_tu if dem_hang_tu(f) == 1]
    da_thuc = [f for f in nhan_tu if dem_hang_tu(f) > 1]

    if not da_thuc:
        print(f"{thut}= {format_poly(sp.factor(expr))}   [đơn thức, chỉ viết lại dạng tích]")
        return sp.factor(expr)

    # Nhân tử chung gồm hệ số hằng và các đơn thức, rút ra trước cho gọn
    chung = he_so * sp.Mul(*don_thuc)
    if chung != 1:
        con_lai = sp.expand(sp.Mul(*da_thuc))
        print(f"{thut}= {viet_tich(chung, format_poly(con_lai))}   [đặt nhân tử chung]")
        if len(da_thuc) >= 2:
            phan_tich_da_thuc_tung_buoc(con_lai, do_sau + 1)
        return sp.factor(expr)

    # Tới đây mọi nhân tử đều có từ hai hạng tử trở lên.
    # Ưu tiên thừa số toàn dấu cộng làm f1 để chuỗi biến đổi ít dấu trừ nhất,
    # nhờ vậy ví dụ x^2 - y^2 ra đúng lời giải mẫu trong đề bài.
    da_thuc.sort(key=co_hang_tu_am)

    f1 = da_thuc[0]
    f2 = sp.Mul(*da_thuc[1:])
    buoc_1, buoc_2, buoc_3 = dung_ba_buoc(f1, f2)
    print(f"{thut}= {buoc_1}")
    print(f"{thut}= {buoc_2}")
    print(f"{thut}= {buoc_3}")

    # Từ ba nhân tử trở lên thì thừa số thứ hai vẫn còn tách được
    if len(da_thuc) >= 3:
        print(f"{thut}Phân tích tiếp thừa số ({format_poly(f2)}):")
        phan_tich_da_thuc_tung_buoc(sp.expand(f2), do_sau + 1)

    return sp.factor(expr)


def chay_vi_du():
    print("=" * 70)
    print("BÀI 4: CHƯƠNG TRÌNH GIẢI TỪNG BƯỚC PHÂN TÍCH ĐA THỨC THÀNH NHÂN TỬ")
    print("=" * 70)

    x, y = sp.symbols("x y")

    print("\n[VÍ DỤ 1 - MẪU TRONG ĐỀ BÀI]")
    phan_tich_da_thuc_tung_buoc(x**2 - y**2)

    print("\n" + "-" * 70)
    print("[VÍ DỤ 2 - TAM THỨC BẬC HAI: x^2 - 5x + 6]")
    phan_tich_da_thuc_tung_buoc(x**2 - 5*x + 6)

    print("\n" + "-" * 70)
    print("[VÍ DỤ 3 - ĐỆ QUY VỚI 3 THỪA SỐ: (x^2 - y^2)(x + 1)]")
    phan_tich_da_thuc_tung_buoc(sp.expand((x**2 - y**2) * (x + 1)))

    print("\n" + "-" * 70)
    print("[VÍ DỤ 4 - NHÂN TỬ CHUNG VÀ LUỸ THỪA: x^3 + 2x^2 + x]")
    phan_tich_da_thuc_tung_buoc(x**3 + 2*x**2 + x)

    print("=" * 70)


if __name__ == "__main__":
    chay_vi_du()
