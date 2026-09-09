# BÀI TẬP 1 - CƠ SỞ LOGIC VÀ ĐẠI SỐ MÁY TÍNH

Dự án hoàn thiện lời giải và mã nguồn chương trình cho **BÀI TẬP 1**, bao gồm:
1. **Bài 1**: Biểu diễn các phát biểu trong logic vị từ $C(x), D(x), F(x)$.
2. **Bài 2\***:
   - Phần 1: Biểu diễn logic bậc nhất có sử dụng hàm quan hệ $f(x)$ và dấu đẳng thức $=$.
   - Phần 2: Chứng minh hình thức suy luận logic từ các tiền đề bằng hệ thống luật suy diễn.
3. **Bài 3**: Chương trình giải và biện luận phương trình tham số $m$:
   - Câu a: Phương trình bậc nhất $(m^2 - 4)x + 2m - 4 = 0$.
   - Câu b\*: Phương trình bậc hai $(m - 2)x^2 - 2(m + 2)x + m + 2 = 0$.
4. **Bài 4**: Chương trình giải từng bước phân tích đa thức thành nhân tử theo phương pháp suy luận ngược từ `factor` và hỗ trợ đệ quy.
5. **Báo cáo LaTeX**: File `Bao_Cao_Bai_Tap_1.tex` định dạng chuẩn khoa học, sẵn sàng nộp hoặc biên dịch ra PDF trên Overleaf/TeXLive.

---

## Cấu trúc thư mục

```
CDCSTT/
├── Bao_Cao_Bai_Tap_1.tex         # Báo cáo học thuật LaTeX chi tiết
├── Danh_sach_nhom.csv            # Danh sách nhóm học viên
├── bai_1_logic.py                # Lời giải và kiểm chứng Bài 1
├── bai_2_logic_chung_minh.py     # Lời giải và suy diễn chứng minh Bài 2*
├── bai_3_bien_luan_pt.py         # Giải & biện luận PT bậc 1, bậc 2 theo m
├── bai_4_phan_tich_nhan_tu.py    # Phân tích đa thức thành nhân tử từng bước
├── main.py                       # Menu điều khiển chạy tổng hợp
├── requirements.txt              # Thư viện phụ thuộc
└── README.md                     # Tài liệu hướng dẫn
```

---

## Hướng dẫn cài đặt và chạy chương trình

### 1. Cài đặt thư viện
Yêu cầu Python >= 3.8 và thư viện `sympy`:
```bash
pip install -r requirements.txt
```

### 2. Chạy toàn bộ bài tập cùng một lúc
```bash
python main.py --all
```

### 3. Chạy giao diện tương tác lựa chọn
```bash
python main.py
```

### 4. Chạy riêng lẻ từng bài
- **Bài 1 (Logic vị từ):**
  ```bash
  python bai_1_logic.py
  ```
- **Bài 2 (Logic có dấu = và chứng minh suy luận):**
  ```bash
  python bai_2_logic_chung_minh.py
  ```
- **Bài 3 (Giải và biện luận phương trình bậc 1 & bậc 2):**
  ```bash
  python bai_3_bien_luan_pt.py
  ```
- **Bài 4 (Phân tích đa thức thành nhân tử từng bước):**
  ```bash
  python bai_4_phan_tich_nhan_tu.py
  ```

---

## Báo cáo LaTeX
File `Bao_Cao_Bai_Tap_1.tex` được thiết kế tương thích hoàn toàn với:
- [Overleaf](https://www.overleaf.com): Tạo New Project -> Upload file `Bao_Cao_Bai_Tap_1.tex` và Recompile (chọn pdfLaTeX hoặc XeLaTeX).
- VS Code với extension LaTeX Workshop hoặc TeXmaker / MiKTeX / MacTeX.
