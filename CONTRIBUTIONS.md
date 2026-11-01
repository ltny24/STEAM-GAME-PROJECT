# Bang Phan Cong & Tien Do Do An (CONTRIBUTIONS)
> **Du an**: STEAM GAME DATA ANALYSIS — CSC17104 Final Project (FIT@HCMUS)

---

## 1. Danh sach Thanh vien

| # | Ho va ten | MSSV | Vai tro chinh |
|:---:|---|:---:|:---:|---|
| 1 | **Le Thi Nhu Y** | **24127595** |  Business Strategy Lead & Slide Coordinator |
| 2 | **Ho Thi Nhu Ngoc** | **24127089** |  Deep Integration Lead & LLM Log Manager |
| 3 | **Vo Nguyen Van Anh** | **24127016** |  Machine Learning Lead & Conda Environment Admin |

---

## 2. Phan cong So Huu Cau Hoi (Question Ownership)


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

### Phase 1 — Thu thập & Khám phá Dữ liệu (EDA - Notebook 01)
*(Thời gian: 22/10 – 31/10)*
| Nhiệm vụ cụ thể | Người phụ trách | Branch | Trạng thái |
|---|:---:|:---:|:---:|
| Họp nhóm chốt chính thức 6 câu hỏi | Cả nhóm | `main` | Đã xong |
| **3.1 Thu thập dữ liệu (Data Collection)**: Viết 5 mục thu thập & bối cảnh dữ liệu | Nhu Ngoc | `Nhu-Ngoc` | Đã xong |
| **3.2.1 Tổng quan (Overview)**: Kiểm tra số dòng, cột, ý nghĩa và kiểu dữ liệu | Nhu Ngoc | `Nhu-Ngoc` | Đã xong |
| **3.2.2 Các cột dữ liệu số (Numerical Columns)**: Phân phối, min/max, outliers (IQR/z-score) | Van Anh | `Van-Anh` | Đã xong |
| **3.2.3 Các cột phân loại (Categorical Columns)**: Thống kê nhãn, genres, tags, languages | Nhu Ngoc | `Nhu-Ngoc` | Đã xong |
| **3.2.4 Dữ liệu bị thiếu (Missing Data)**: Thống kê % missing, vẽ ma trận `missingno` | Van Anh | `Van-Anh` | Đã xong |
| **3.2.5 Mối quan hệ (Relationships)**: Ma trận tương quan (Heatmap), phân tích chéo | Le Thi Nhu Y | `Nhu-Y` | Đã xong |
| **3.2.6 Tổng kết EDA**: Tóm tắt 3-5 quan sát chính & Preprocessing plan | Le Thi Nhu Y | `Nhu-Y` | Đã xong |
| **Ghép nối và hoàn thiện `01_collection_exploration.ipynb`** | Cả nhóm | `main` | Đã xong |

### Phase 2 — Phân tích Chuyên sâu & Machine Learning (Notebook 02 & 03)
*(Thời gian: 01/11 – 16/11)*
| Nhiệm vụ cụ thể | Người phụ trách | Nhánh Git | Trạng thái |
|---|:---:|:---:|:---:|
| Triển khai Q1 & Q2 | Ho Thi Nhu Ngoc | `Nhu-Ngoc` | Chưa bắt đầu |
| Triển khai Q3 (Machine Learning) & Q4 | Vo Nguyen Van Anh | `Van-Anh` | Chưa bắt đầu |
| Triển khai Q5 & Q6 | Le Thi Nhu Y | `Nhu-Y` | Chưa bắt đầu |
| Tải và ghép dữ liệu ngoại (CPI, Language) | Cả nhóm | Tùy câu hỏi | Chưa bắt đầu |
| Vẽ $\ge 2$ biểu đồ/câu, kiểm định D5, test D6 | Từng cá nhân | Tùy nhánh | Chưa bắt đầu |
| Ghép nối và hoàn thiện `02_analysis.ipynb` & `03_ml_question.ipynb` | Cả nhóm | `main` | Chưa bắt đầu |

### Phase 3 — Hoàn thiện Deliverables & Thuyết trình
*(Thời gian: 16/11 – 25/11)*
| Nhiệm vụ cụ thể | Người phụ trách | Hạn chót | Trạng thái |
|---|:---:|:---:|:---:|
| Viết Phase 3.5: Key findings & Limitations | Le Thi Nhu Y | 18/11 | Chưa bắt đầu |
| Viết Reflection cá nhân (từng người) | Tất cả | 18/11 | Chưa bắt đầu |
| Cập nhật nhật ký `LLM_USAGE.md` | Nhu Ngoc | 19/11 | Chưa bắt đầu |
| Kiểm tra đồng bộ môi trường Conda `environment.yml` | Van Anh | 19/11 | Chưa bắt đầu |
| Soạn nội dung slide các câu hỏi tương ứng | Từng cá nhân | 20/11 | Chưa bắt đầu |
| Mở Issue mời nhóm bạn review; đi review nhóm khác | Cả nhóm | 20/11 | Chưa bắt đầu |
| Thiết kế template & Ráp Master Slide xuất `slides.pdf` | Le Thi Nhu Y | 21/11 | Chưa bắt đầu |
| Chỉnh sửa feedback & nộp bài trên Moodle | Cả nhóm | 21/11 | Chưa bắt đầu |
| Báo cáo dự án và vấn đáp Q&A | Cả nhóm | 22/11 - 25/11 | Chưa bắt đầu |

---

## 4. Nhật ký các buổi họp nhóm (Meeting Log)

- **Buổi 1 (Khởi động dự án - 06/10)**:
  - Thống nhất chọn bộ dữ liệu Steam Games (March 2025).
  - Phân tích lại đề bài CSC17104 năm 2026: mở rộng lên 6 câu hỏi (2 câu 6D, 1 câu ML, 3 câu 4D).
  - Phân công vai trò chính và tạo các nhánh cá nhân trên GitHub.

- **Buổi 2 (Chốt câu hỏi & Lên Timeline - 21/10)**:
  - Chốt chính thức danh sách 6 câu hỏi phân tích.
  - Thống nhất quy trình làm Phase 3.1 và Phase 3.2.
  - Lên lịch các deadline nội bộ (Tuần 1, Tuần 2, Tuần 3, Tuần 4) để bám sát tiến độ đồ án.
