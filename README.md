# Steam Game Data Analysis — Final Project
> **FIT@HCMUS · CSC17104 – Programming for Data Science**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Conda](https://img.shields.io/badge/Environment-Conda-green)](https://docs.conda.io/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Lab-orange)](https://jupyter.org/)
[![License](https://img.shields.io/badge/Data%20License-Kaggle%20Open-blue)](https://www.kaggle.com/)

---

## 1. Thanh vien nhom & Phan cong nhiem vu (Team & Task Breakdown)

| # | Ho va ten | MSSV | GitHub | Vai tro & Quyen so huu cau hoi |
|:---:|---|:---:|:---:|---|
| 1 | **Le Thi Nhu Y** | **24127595** | [@ltny24](https://github.com/ltny24) | **Business Strategy Lead**<br>• Phu trach **Q5** & **Q6**<br>• Phan tich Tuong quan & Tong ket EDA (Notebook 01)<br>• Dieu phoi slide thuyet trinh `slides.pdf` |
| 2 | **Ho Thi Nhu Ngoc** | **24127089** | @... | **Deep Integration Lead**<br>• Phu trach **Q1** & **Q2**<br>• Viet Muc 3.1 (Thu thap du lieu) & Categorical EDA (Notebook 01)<br>• Quan ly nhat ky `LLM_USAGE.md` |
| 3 | **Vo Nguyen Van Anh** | **24127016** | @... | **Machine Learning Lead**<br>• Phu trach **Q3 (Machine Learning)** & **Q4**<br>• Phan tich Numerical EDA & Missing Data (Notebook 01)<br>• Quan tri moi truong Conda `environment.yml` |

> *Chi tiet lich trinh va phan chia cong viec tung giai doan xem tai [CONTRIBUTIONS.md](CONTRIBUTIONS.md).*

---

## 2. Cau truc thu muc (Repository Structure)

Cau truc du an tuan thu Muc 4 (Deliverables and repository structure) cua de bai CSC17104:

```text
STEAM-GAME-PROJECT/
├── README.md                           # Gioi thieu do an, thanh vien, cau hoi & huong dan
├── environment.yml                     # Cau hinh moi truong Conda chuan
├── requirements.txt                    # Danh sach thu vien phu tro (pip)
├── LLM_USAGE.md                        # Nhat ky minh bach su dung cong cu AI (Muc 6)
├── CONTRIBUTIONS.md                    # Bang phan cong chi tiet va tien do lam viec
├── .gitignore                          # Chan cac file rac, file tam va du lieu lon (>100MB)
├── data/
│   ├── raw/                            # Chua file du lieu goc (khong commit len Git)
│   │   └── games_march2025_cleaned.csv # (~468 MB, tai tu Kaggle)
│   └── processed/                      # Chua du lieu da tien xu ly / lam sach
├── src/                                # Cac Python modules tai su dung
│   ├── __init__.py
│   ├── data_loader.py                  # Ham tien ich load & validate du lieu
│   └── preprocessing.py                # Pipeline tien xu ly va loc cot
├── notebooks/
│   ├── 01_collection_exploration.ipynb # Phase 3.1 (Thu thap) & Phase 3.2 (EDA chi tiet)
│   ├── 02_analysis.ipynb               # Phase 3.4 (5 cau hoi phan tich Non-ML)
│   └── 03_ml_question.ipynb            # Phase 3.4 (1 bai toan Machine Learning hoan chinh)
└── slides.pdf                          # Slide bao cao thuyet trinh (15 phut)
```

---

## 3. Mo ta Bo Du Lieu & Nghien Cuu Lien Quan (Dataset & Existing Work)

### 3.1 Thong tin bo du lieu chinh
* **Bo du lieu**: Steam Games Dataset (Thang 03/2025).
* **Nguon thu thap**: [Kaggle — Steam Games Dataset (March 2025)](https://www.kaggle.com/).
* **Kich thuoc**: Hon **50,000 dong** va **47 cot** (Dung luong: ~468 MB o dang file CSV).
* **Ban quyen (License)**: Du lieu cong khai phuc vu muc dich nghien cuu va giao duc theo dieu khoan cua Kaggle Open Data.
* **Phuong thuc thu thap goc**: Tac gia thu thap tu dong thong qua Steam Store API va SteamSpy API.

### 3.2 Khai bao nghien cuu co san tren Kaggle (Declaration of Existing Work)
*(Cap nhat danh sach cac public notebook tren Kaggle lien quan den dataset nay va giai thich diem khac biet cua de tai nhom de tranh dao van theo Muc 2 cua de bai).*

---

## 4. Danh Sach Cau Hoi Nghien Cuu (Research Questions)

Theo quy dinh de bai CSC17104, nhom 3 thanh vien thuc hien 6 cau hoi nghien cuu: moi thanh vien chiu trach nhiem chinh 2 cau, gom 1 bai toan Machine Learning hoan chinh va 5 cau hoi phan tich Non-ML phu cac tieu chi da chieu (D1 - D6).

### Bang phan cong 6 cau hoi nghien cuu:

| STT | Cau hoi nghien cuu | Nguoi phu trach | Dinh huong & Loai phan tich | File Notebook |
|:---:|---|:---:|:---:|:---:|
| **Q1** | **Mo rong Do phu & Quy mo Nguoi choi**:<br>Số lượng ngôn ngữ và hệ điều hành được hỗ trợ có mối liên hệ như thế nào với lượng người sở hữu ước tính, và mối liên hệ này thay đổi ra sao khi xét đến thể loại và tuổi đời game? | **Ho Thi Nhu Ngoc**<br>(24127089) | Non-ML (Kiem soat Confounders: The loai & Tuoi doi) | `02_analysis.ipynb` |
| **Q2** | **Phan hoa Thoi luong choi (Playtime Distribution)**:<br>Sự chênh lệch giữa thời gian chơi trung bình và trung vị phản ánh những đặc điểm khác biệt nào trong phân phối thời lượng chơi của các tựa game, và mức độ chênh lệch này có khác nhau giữa các thể loại game hay không? | **Ho Thi Nhu Ngoc**<br>(24127089) | Non-ML (Phan phoi lech phai & Heavy-tailed Distribution) | `02_analysis.ipynb` |
| **Q3** | **Du doan Hit Game truoc ngay phat hanh**:<br>Dựa trên các đặc điểm cấu hình ban đầu lúc phát hành như mức giá (price), thể loại (categories, genres, tags), số lượng ngôn ngữ hỗ trợ (supported_languages, full_audio_languages) và độ phủ nền tảng (windows, mac, linux), chúng ta có thể nhận diện/dự đoán khả năng một tựa game sẽ trở nên thành công (có estimated_owners thuộc top 20% cao nhất và pct_pos_total > 80%) hay không? | **Vo Nguyen Van Anh**<br>(24127016) | **Machine Learning**<br>(Classification Pipeline, Time-based Split, Error Analysis) | `03_ml_question.ipynb` |
| **Q4** | **Gia tri Noi dung Bo sung (DLC & Achievements)**:<br>Mật độ phân bổ thành tựu trên mỗi gói mở rộng (achievements/dlc_count) có chiều hướng tác động như thế nào đến tỷ lệ đánh giá tích cực gần đây của người chơi (pct_pos_recent), sau khi đã kiểm soát yếu tố chất lượng chuyên môn của trò chơi (metacritic_score)? | **Vo Nguyen Van Anh**<br>(24127016) | Non-ML (Feature Engineering & Quality Control) | `02_analysis.ipynb` |
| **Q5** | **Dong luc Tuong tac F2P vs Pay-to-Play**:<br>Động lực Tương tác Người chơi giữa Mô hình Free-to-Play và Pay-to-Play: Liệu Game Miễn phí có duy trì được mức độ tham gia tương đối (Relative Recent Activity) cao hơn Game Trả phí sau khi kiểm soát các tựa game Outlier ngoại lai (Top 1% Blockbuster)? | **Le Thi Nhu Y**<br>(24127595) | Non-ML (So sanh nhom & Kiem soat Outlier) | `02_analysis.ipynb` |
| **Q6** | **Nghich ly Thoi luong choi (The Playtime Paradox)**:<br>Nghịch lý thời lượng chơi (The Playtime Paradox): Game có thời lượng chơi càng dài có thực sự mang lại mức độ hài lòng cao hơn cho game thủ, hay việc cố tình kéo dài nội dung (Content Bloating) đang gây ra hiệu ứng mệt mỏi phản tác dụng? | **Le Thi Nhu Y**<br>(24127595) | Non-ML (Quan he phi tuyen & Saturation Threshold) | `02_analysis.ipynb` |

---

## 5. Cac Phat Hien Chinh (Key Findings)

*(Cap nhat sau khi hoan tat phan tich du lieu — tom tat 3-5 phat hien quan trong nhat kem phat hien bat ngo nhat).*

---

## 6. Huong Dan Cai Dat & Chay Do An (How to Run)

### Buoc 1: Clone kho luu tru
```bash
git clone https://github.com/ltny24/STEAM-GAME-PROJECT.git
cd STEAM-GAME-PROJECT
```

### Buoc 2: Thiet lap moi truong Conda
```bash
# Tao moi truong tu file environment.yml
conda env create -f environment.yml

# Kich hoat moi truong
conda activate steam_project
```
*(Neu su dung pip: `pip install -r requirements.txt`)*

### Buoc 3: Chuan bi du lieu
1. Tai file `games_march2025_cleaned.csv` tu Kaggle.
2. Dat file vao thu muc: `data/raw/games_march2025_cleaned.csv`.

### Buoc 4: Chay cac Notebook theo thu tu
Khoi dong Jupyter Lab:
```bash
jupyter lab
```
Chay lan luot cac notebook:
1. `notebooks/01_collection_exploration.ipynb`
2. `notebooks/02_analysis.ipynb`
3. `notebooks/03_ml_question.ipynb`

---

## 7. Liem Chinh Hoc Thuat & Su Dung AI (Academic Integrity)

* Du an tuan thu nghiem ngat chuan muc liem chinh hoc thuat cua FIT@HCMUS.
* Moi truong hop tham khao tai lieu hoac ho tro tu cong cu AI deu duoc ghi nhan tai **[LLM_USAGE.md](LLM_USAGE.md)**.
* Cac thanh vien deu co kha nang giai thich chi tiet tung dong ma nguon trong buoi van dap Q&A.

---
<p align="center">
  <sub>FIT@HCMUS · Khoa hoc Du lieu 4.0 · Hoc ky II (2025–2026)</sub>
</p>
