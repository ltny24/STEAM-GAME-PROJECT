# Steam Game Data Analysis — Final Project
> **FIT@HCMUS · Introduction to Data Science 4.0**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)](https://jupyter.org/)
[![License](https://img.shields.io/badge/Data%20License-Kaggle-20BEFF?logo=kaggle)](https://www.kaggle.com/)
[![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)]()

---

## Gioi thieu du an

Du an phan tich bo du lieu **Steam Games (March 2025)** thu thap tu Kaggle — nen tang phan phoi game lon nhat the gioi voi hon 50,000 tua game.

Muc tieu chinh:
- Kham pha cac yeu to anh huong den su thanh cong cua mot tua game tren Steam
- Tra loi cac cau hoi co gia tri thuc tien tu du lieu
- Thuc hanh quy trinh Data Science hoan chinh: Thu thap → EDA → Tien xu ly → Phan tich → Ket luan

---

## Cau truc thu muc

```
STEAM-GAME-PROJECT/
│
├── data/
│   ├── raw/                  # Du lieu goc (khong chinh sua)
│   │   └── games_march2025_cleaned.csv   (ignored by git)
│   └── processed/            # Du lieu sau khi tien xu ly
│
├── notebooks/
│   ├── individual/           # Notebook rieng cua tung thanh vien (moi nguoi mot branch)
│   └── group/                # Notebook nhom (phien ban chinh thuc, merge ve main)
│       ├── 00_skeleton.ipynb
│       ├── 01_collecting_data.ipynb
│       ├── 02_eda.ipynb
│       ├── 03_questions.ipynb
│       └── 04_reflection.ipynb
│
├── src/                      # Code Python tai su dung
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   └── visualization.py
│
├── reports/
│   └── figures/              # Hinh anh / bieu do da xuat
│
├── docs/
│   └── project_brief.pdf
│
├── .gitignore
├── requirements.txt
├── README.md
└── CONTRIBUTIONS.md
```

---

## Du lieu

| Thuoc tinh | Thong tin |
|---|---|
| **Nguon** | [Kaggle — Steam Games Dataset (March 2025)](https://www.kaggle.com/) |
| **Ten file** | `games_march2025_cleaned.csv` |
| **Kich thuoc** | ~450 MB |
| **Ghi chu** | File CSV qua lon, khong dua len Git — tai ve va dat vao `data/raw/` |

> **Luu y:** File du lieu goc duoc them vao `.gitignore` do kich thuoc lon (~450MB).
> De chay duoc notebook, tai file CSV ve tu Kaggle va dat vao thu muc `data/raw/`.

---

## Cac cau hoi phan tich

*(Cap nhat khi nhom thong nhat)*

---

## Thanh vien nhom & Phan cong

*(Cap nhat khi nhom thong nhat)*

---

## Quy trinh Git (theo yeu cau de)

```
main
 └── (chi chua skeleton va phien ban nhom da merge)

Moi thanh vien lam viec tren branch ca nhan:
 ├── member1/eda
 ├── member2/eda
 └── member3/eda
```

**Workflow:**
1. Mot thanh vien tao `notebooks/group/00_skeleton.ipynb` → push len `main`
2. Moi thanh vien tao branch rieng: `git checkout -b memberX/eda`
3. Moi nguoi lam viec doc lap tren branch ca nhan → commit len branch rieng
4. Hop nhom → hieu notebook cua nhau → merge tat ca ve `main`
5. Upload phien ban cuoi len GitHub + Moodle truoc deadline

---

## Cai dat moi truong

```bash
# Clone repo
git clone https://github.com/ltny24/STEAM-GAME-PROJECT.git
cd STEAM-GAME-PROJECT

# Cai thu vien
pip install -r requirements.txt

# Mo Jupyter
jupyter lab
```

---

## Tai lieu tham khao

- De bai: `docs/project_brief.pdf`
- Dataset: [Steam Games on Kaggle](https://www.kaggle.com/)
- *(Cap nhat them trong qua trinh lam)*

---

<p align="center">
  <sub>FIT@HCMUS · Khoa hoc Du lieu 4.0 · 2025</sub>
</p>
