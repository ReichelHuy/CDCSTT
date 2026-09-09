# -*- coding: utf-8 -*-
"""
CHƯƠNG TRÌNH CHÍNH - BÀI TẬP 1
Môn học: Cơ sở Logic và Toán rời rạc / Đại số máy tính
Hỗ trợ chạy và kiểm tra tất cả các bài:
  - Bài 1: Logic vị từ cơ bản (C(x), D(x), F(x))
  - Bài 2*: Logic bậc nhất nâng cao & Chứng minh hình thức
  - Bài 3: Giải và biện luận phương trình bậc 1 & bậc 2 theo tham số m
  - Bài 4: Phân tích đa thức thành nhân tử từng bước (có đệ quy)
"""

import sys
from bai_1_logic import print_bai_1
from bai_2_logic_chung_minh import print_bai_2_part1, print_bai_2_part2
from bai_3_bien_luan_pt import chay_vi_du_de_bai
from bai_4_phan_tich_nhan_tu import chay_vi_du

def menu():
    print("\n" + "=" * 60)
    print("           BÀI TẬP 1 - CHƯƠNG TRÌNH CHẠY TỔNG HỢP")
    print("=" * 60)
    print("1. Chạy Bài 1 (Logic vị từ C(x), D(x), F(x))")
    print("2. Chạy Bài 2* (Biểu diễn logic dấu = & Chứng minh suy luận)")
    print("3. Chạy Bài 3 (Giải và biện luận PT bậc 1, bậc 2 theo m)")
    print("4. Chạy Bài 4 (Phân tích đa thức thành nhân tử từng bước)")
    print("5. Chạy TẤT CẢ các bài (1, 2, 3, 4)")
    print("0. Thoát")
    print("=" * 60)

def main():
    # Nếu truyền cờ dòng lệnh --all thì chạy tất cả không cần chọn
    if len(sys.argv) > 1 and sys.argv[1] == "--all":
        print("\n>>> CHẠY TOÀN BỘ BÀI TẬP 1 <<<")
        print_bai_1()
        print_bai_2_part1()
        print_bai_2_part2()
        chay_vi_du_de_bai()
        chay_vi_du()
        return

    while True:
        menu()
        choice = input("Vui lòng nhập lựa chọn (0-5) [Mặc định 5]: ").strip()
        if choice == "" or choice == "5":
            print_bai_1()
            print_bai_2_part1()
            print_bai_2_part2()
            chay_vi_du_de_bai()
            chay_vi_du()
        elif choice == "1":
            print_bai_1()
        elif choice == "2":
            print_bai_2_part1()
            print_bai_2_part2()
        elif choice == "3":
            chay_vi_du_de_bai()
        elif choice == "4":
            chay_vi_du()
        elif choice == "0":
            print("Đã thoát chương trình. Chúc bạn học tốt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()
