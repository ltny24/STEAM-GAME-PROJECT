# Nhật ký Sử dụng Công cụ LLM (LLM USAGE LOG)
> Theo quy định tại **Mục 6 – Academic integrity and use of LLMs** (FIT@HCMUS – CSC17104).

Nhóm cam kết sử dụng công cụ AI (ChatGPT, Claude, Copilot, Gemini...) với vai trò **trợ giảng / gia sư học tập (tutor)**: giải thích khái niệm, gỡ lỗi cú pháp, gợi ý thư viện. Không dùng công cụ để tự động viết kết quả phân tích hoặc viết thay phần reflection.

---

## Bảng ghi nhận sử dụng

| Ngày | Thành viên | Công cụ | Câu lệnh / Vấn đề cần hỏi (Prompt) | Kết quả & Cách nhóm đã tiếp thu / chỉnh sửa |
|---|---|---|---|---|
| 21/10/2026 | Lê Thị Như Ý | Gemini | Cách viết hàm Bootstrap 95% Confidence Interval bằng scipy | Tham khảo cú pháp `scipy.stats.bootstrap` và viết lại hàm áp dụng cho cột `pct_pos_total` của Steam |
| 22/10/2026 | Võ Nguyễn Vân Anh | Claude | Giải thích lỗi Data Leakage khi chia tập dữ liệu thời gian | Hiểu nguyên lý và chuyển sang Time-based split trước năm 2022 |
| 26/10/2026 | Lê Thị Như Ý | Gemini | Hướng dẫn cú pháp vẽ biểu đồ Heatmap tương quan Spearman, mask tam giác trên và kỹ thuật hexbin xử lý overplotting | Hiểu cách dùng `np.triu`, `sns.heatmap` và áp dụng phân tích các biến định lượng trên dataset Steam |
| 26/10/2026 | Lê Thị Như Ý | Gemini | Hướng dẫn gỡ lỗi môi trường `ModuleNotFoundError: pandas` và gỡ lỗi cú pháp `SyntaxError` do thiếu dấu ngoặc tròn | Biết cách đăng ký kernel conda `min_ds-env` vào Jupyter và sửa các lỗi cú pháp Python trong notebook |
| 26/10/2026 | Lê Thị Như Ý | Gemini | Phân tích phản biện về câu hỏi nghiên cứu F2P và sự khác biệt giữa Engagement vs Retention | Hiểu giới hạn của tập dữ liệu snapshot, loại bỏ thuật ngữ thiên kiến và chuẩn hóa câu hỏi nghiên cứu |
| 26/10/2026 | Hồ Thị Như Ngọc | Copilot | Hướng dẫn phân tích thống kê mô tả và phân phối các thuộc tính định lượng | Tham khảo gợi ý về cách tính các chỉ số thống kê và chọn biểu đồ phù hợp, sau đó áp dụng cho dữ liệu Steam |
| 27/10/2026 | Hồ Thị Như Ngọc | Copilot | Giải thích cách phát hiện giá trị ngoại lai bằng IQR và Z-score | Hiểu sự khác nhau giữa hai phương pháp và áp dụng để so sánh các thuộc tính định lượng |
| 31/10/2026 | Hồ Thị Như Ngọc | Copilot | Hướng dẫn kiểm tra dữ liệu thiếu và các giá trị thiếu được mã hóa trong dataset | Tham khảo cách tổng hợp, trực quan hóa và nhận diện mẫu hình dữ liệu thiếu để phục vụ phân tích |
| 05/11/2026 | Hồ Thị Như Ngọc | Copilot | Cách kết hợp dữ liệu giữa file CSV và Parquet theo appid, xử lý cột danh sách hệ điều hành và tính khoảng tin cậy | Hiểu cách dùng `pd.merge` với left join để giữ toàn bộ tập CSV gốc, kiểm tra độ phủ nối và viết hàm bootstrap ước lượng sai số chuẩn trong Q1 |
| 07/11/2026 | Hồ Thị Như Ngọc | Copilot | Cách phân tách chuỗi thể loại genres. Dùng hàm như thế nào để tạo bảng phụ mà không làm lặp game trong mẫu chính | Hiểu cách xử lý cột chuỗi chứa danh sách, tạo DataFrame phụ để phân tích tương quan theo thể loại mà không làm ảnh hưởng dữ liệu gốc ở Q1 |
| 12/11/2026 | Hồ Thị Như Ngọc | Copilot | Cú pháp thực hiện hồi quy tuyến tính và kiểm định Wald cho hệ số tương tác thể loại | Hiểu nguyên lý biến đổi để xử lý biến phân phối lệch, cách tính Wald chi2 test kiểm tra sự khác biệt độ dốc giữa các thể loại trong Q2 |
| 15/11/2026 | Hồ Thị Như Ngọc | Gemini | Hướng dẫn kỹ thuật kiểm tra độ bền loại bỏ 1% game có lượt đánh giá cao nhất và vẽ biểu đồ | Biết cách dùng những gì để lọc ngoại lai cực đại và vẽ thanh sai số trực quan hóa độ dốc các thể loại trong Q2 |
| *(Tiếp tục cập nhật)* | ... | ... | ... | ... |
