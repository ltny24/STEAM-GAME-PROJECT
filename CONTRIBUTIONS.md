# Bang Phan Cong & Tien Do Do An (CONTRIBUTIONS)
> **Du an**: STEAM GAME DATA ANALYSIS — CSC17104 Final Project (FIT@HCMUS)

---

## 1. Danh sach Thanh vien

| # | Ho va ten | MSSV | GitHub | Vai tro chinh |
|:---:|---|:---:|:---:|---|
| 1 | **Le Thi Nhu Y** | **24127595** | [@ltny24](https://github.com/ltny24) | Business Strategy Lead & Slide Coordinator |
| 2 | **Ho Thi Nhu Ngoc** | **24127089** | @... | Deep Integration Lead & LLM Log Manager |
| 3 | **Vo Nguyen Van Anh** | **24127016** | @... | Machine Learning Lead & Conda Environment Admin |

---

## 2. Phan cong So Huu Cau Hoi (Question Ownership)

*(Cap nhat sau khi nhom hop thong nhat 6 cau hoi. Moi thanh vien phu trach 2 cau).*

| STT | Cau hoi nghien cuu | Nguoi phu trach | Loai & Tieu chi do sau | File Notebook |
|:---:|---|:---:|:---:|:---:|
| **Q1** | **Mo rong Do phu & Quy mo Nguoi choi**:<br>Số lượng ngôn ngữ và hệ điều hành được hỗ trợ có mối liên hệ như thế nào với lượng người sở hữu ước tính, và mối liên hệ này thay đổi ra sao khi xét đến thể loại và tuổi đời game? | **Ho Thi Nhu Ngoc**<br>(24127089) | Non-ML (Kiem soat Confounders: The loai & Tuoi doi) | `02_analysis.ipynb` |
| **Q2** | **Phan hoa Thoi luong choi (Playtime Distribution)**:<br>Sự chênh lệch giữa thời gian chơi trung bình và trung vị phản ánh những đặc điểm khác biệt nào trong phân phối thời lượng chơi của các tựa game, và mức độ chênh lệch này có khác nhau giữa các thể loại game hay không? | **Ho Thi Nhu Ngoc**<br>(24127089) | Non-ML (Phan phoi lech phai & Heavy-tailed Distribution) | `02_analysis.ipynb` |
| **Q3** | **Du doan Hit Game truoc ngay phat hanh**:<br>Dựa trên các đặc điểm cấu hình ban đầu lúc phát hành như mức giá (price), thể loại (categories, genres, tags), số lượng ngôn ngữ hỗ trợ (supported_languages, full_audio_languages) và độ phủ nền tảng (windows, mac, linux), chúng ta có thể nhận diện/dự đoán khả năng một tựa game sẽ trở nên thành công (có estimated_owners thuộc top 20% cao nhất và pct_pos_total > 80%) hay không? | **Vo Nguyen Van Anh**<br>(24127016) | **Machine Learning**<br>(Classification Pipeline, Time-based Split, Error Analysis) | `03_ml_question.ipynb` |
| **Q4** | **Gia tri Noi dung Bo sung (DLC & Achievements)**:<br>Mật độ phân bổ thành tựu trên mỗi gói mở rộng (achievements/dlc_count) có chiều hướng tác động như thế nào đến tỷ lệ đánh giá tích cực gần đây của người chơi (pct_pos_recent), sau khi đã kiểm soát yếu tố chất lượng chuyên môn của trò chơi (metacritic_score)? | **Vo Nguyen Van Anh**<br>(24127016) | Non-ML (Feature Engineering & Quality Control) | `02_analysis.ipynb` |
| **Q5** | **Dong luc Tuong tac F2P vs Pay-to-Play**:<br>Động lực Tương tác Người chơi giữa Mô hình Free-to-Play và Pay-to-Play: Liệu Game Miễn phí có duy trì được mức độ tham gia tương đối (Relative Recent Activity) cao hơn Game Trả phí sau khi kiểm soát các tựa game Outlier ngoại lai (Top 1% Blockbuster)? | **Le Thi Nhu Y**<br>(24127595) | Non-ML (So sanh nhom & Kiem soat Outlier) | `02_analysis.ipynb` |
| **Q6** | **Nghich ly Thoi luong choi (The Playtime Paradox)**:<br>Nghịch lý thời lượng chơi (The Playtime Paradox): Game có thời lượng chơi càng dài có thực sự mang lại mức độ hài lòng cao hơn cho game thủ, hay việc cố tình kéo dài nội dung (Content Bloating) đang gây ra hiệu ứng mệt mỏi phản tác dụng? | **Le Thi Nhu Y**<br>(24127595) | Non-ML (Quan he phi tuyen & Saturation Threshold) | `02_analysis.ipynb` |

---

## 3. Phan cong chi tiet theo cac giai doan (Workflow)

### Phase 1 — Thu thap & Kham pha Du lieu (EDA - Notebook 01)
| Nhiem vu cu the | Nguoi phu trach | Nhanh Git | Trang thai |
|---|:---:|:---:|:---:|
| **3.1 Data Collection**: Viet 5 muc thu thap & boi canh du lieu | Nhu Ngoc | `Nhu-Ngoc` | Dang thuc hien |
| **3.2 Categorical Columns**: Thong ke nhan, genres, tags, languages | Nhu Ngoc | `Nhu-Ngoc` | Dang thuc hien |
| **3.2 Numerical Columns**: Phan phoi, min/max, outliers (IQR/z-score) | Van Anh | `Van-Anh` | Dang thuc hien |
| **3.2 Missing Data**: Thong ke % missing, ve ma tran `missingno` | Van Anh | `Van-Anh` | Dang thuc hien |
| **3.2 Relationships**: Ma tran tuong quan (Heatmap), phan tich cheo | Le Thi Nhu Y | `Nhu-Y` | Dang thuc hien |
| **3.2 Tong ket EDA**: Tom tat 3-5 quan sat chinh & Preprocessing plan | Le Thi Nhu Y | `Nhu-Y` | Dang thuc hien |
| **Hop nhom & Ghep noi vao `01_collection_exploration.ipynb`** | Ca nhom | `main` | Chua bat dau |

### Phase 2 — Phan tich Chuyen sau & Machine Learning (Notebook 02 & 03)
| Nhiem vu cu the | Nguoi phu trach | Nhanh Git | Trang thai |
|---|:---:|:---:|:---:|
| Trien khai Q1 & Q2 | Ho Thi Nhu Ngoc | `Nhu-Ngoc` | Chua bat dau |
| Trien khai Q3 (Machine Learning) & Q4 | Vo Nguyen Van Anh | `Van-Anh` | Chua bat dau |
| Trien khai Q5 & Q6 | Le Thi Nhu Y | `Nhu-Y` | Chua bat dau |
| Ghep noi va hoan thien `02_analysis.ipynb` & `03_ml_question.ipynb` | Ca nhom | `main` | Chua bat dau |

### Phase 3 — Hoan thien Deliverables & Thuyet trinh
| Nhiem vu cu the | Nguoi phu trach | Han chot | Trang thai |
|---|:---:|:---:|:---:|
| Viet phan Danh gia & Reflection ca nhan (tung nguoi) | Tat ca | *(Ngay...)* | Chua bat dau |
| Cap nhat day du nhat ky `LLM_USAGE.md` | Nhu Ngoc | *(Ngay...)* | Chua bat dau |
| Kiem tra dong bo moi truong Conda `environment.yml` | Van Anh | *(Ngay...)* | Chua bat dau |
| Soan noi dung slide cac cau hoi tuong ung | Tung ca nhan | *(Ngay...)* | Chua bat dau |
| Thiet ke template & Rap Master Slide xuat `slides.pdf` | Le Thi Nhu Y | *(Ngay...)* | Chua bat dau |
| Luyen tap thuyet trinh khop khung 15 phut + 10 phut Q&A | Ca nhom | *(Ngay...)* | Chua bat dau |

---

## 4. Nhat ky cac buoi hop nhom (Meeting Log)

* **Buoi 1 (Khoi dong du an)**:
  - Thong nhat chon bo du lieu Steam Games (March 2025).
  - Phan tich lai de bai CSC17104 nam 2026: mo rong len 6 cau hoi (2 cau 6D, 1 cau ML, 3 cau 4D).
  - Phan cong vai tro chinh va tao cac nhanh ca nhan tren GitHub.
