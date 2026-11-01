# Nhật ký sử dụng LLM — Võ Nguyễn Vân Anh

> Bản ghi cá nhân cho đồ án CSC17104. Trước khi nộp nhật ký chung của nhóm, cần bổ sung bản ghi của các thành viên còn lại theo mục 6 của đề bài.

Các mục dưới đây gộp những lượt trao đổi cùng một công việc. AI hỗ trợ giải thích, rà soát, biên tập và tích hợp notebook; các đề xuất được đối chiếu với đề bài, dữ liệu và kết quả chạy kiểm tra trước khi đưa vào bản làm việc.

| Thời điểm | Công cụ | Nội dung đã hỏi | Cách sử dụng và điều chỉnh câu trả lời |
|---|---|---|---|
| 27/10–01/11/2026 | ChatGPT/Codex | Đối chiếu `Final Project.pdf`, `CSC17104_2026_Final_Project.pdf` với các phần 3.1, 3.2.1 và cột phân loại trong notebook; xác định phạm vi và những điểm còn thiếu. | Dùng bản rà soát để chỉnh thứ tự mục, bổ sung giới hạn của dữ liệu và xác định các cột phân loại. Giữ những quyết định thuộc phạm vi cá nhân; không đưa các phần cột số, dữ liệu thiếu và mối quan hệ vào phần việc của mình. |
| 27/10–01/11/2026 | ChatGPT/Codex | Giải thích `pd.read_csv()`, việc các cell thống kê có thay đổi `df` hay không, cách đếm nhãn nhiều giá trị và nguyên nhân cell chạy chậm. | AI giải thích và hỗ trợ sửa các code cell để thống kê đúng cột phân loại, tách nhãn dạng danh sách và không đếm trực tiếp `packages` như nhãn đơn. Đối chiếu kết quả trên mẫu và toàn bộ 89.618 dòng; giữ lệnh đọc CSV theo quyết định của mình. |
| 01/11/2026 | ChatGPT/Codex | Rà soát diễn giải dữ liệu, số liệu trong bảng, văn phong Markdown và các output lỗi/cảnh báo trước khi bàn giao. | AI hỗ trợ biên tập các đoạn Markdown và chỉnh code liên quan. Số liệu được tính lại từ dữ liệu; các nhận định chưa đủ căn cứ được sửa hoặc bỏ, nhất là cách hiểu giá trị `0`, `packages` và các cột thời gian chơi hai tuần. Xóa output lỗi cũ và kiểm tra cấu trúc notebook. |
| 01/11/2026 | ChatGPT/Codex | Đồng bộ notebook lên nhánh `Van-Anh`, ghép phần EDA từ `Nhu-Ngoc`, `Nhu-Y` và `Van-Anh`, rồi kiểm tra thêm file ở `notebooks/` của nhánh `Nhu-Y`. | AI hỗ trợ thao tác Git, ghép và đánh số lại các mục, sửa chỗ phụ thuộc dữ liệu giữa các phần. Kiểm tra cấu trúc notebook, cú pháp code và chạy thử các bước chuẩn bị dữ liệu; bản ghép được lưu ở commit local `501d71f`. File thứ hai của `Nhu-Y` được xác nhận có cùng nội dung với file đã dùng. |
