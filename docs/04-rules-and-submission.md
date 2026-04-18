# Rules & Hướng dẫn Nộp bài

---

## Ràng buộc bắt buộc

1. **Không dùng dữ liệu ngoài** — Tất cả đặc trưng phải được tạo từ các file dữ liệu được cung cấp. Nghiêm cấm sử dụng nguồn dữ liệu bên ngoài.

2. **Tính tái lập (Reproducibility)** — Đính kèm toàn bộ mã nguồn trong GitHub repository. Đặt `random seed` khi cần thiết. Kết quả không thể tái lập sẽ bị loại.

3. **Khả năng giải thích (Explainability)** — Báo cáo phải có mục giải thích các yếu tố dẫn động doanh thu chính (feature importances, SHAP values, hoặc partial dependence plots) bằng ngôn ngữ kinh doanh.

---

## Điều kiện loại bài (Phần 3)

Bài nộp bị loại toàn bộ điểm Phần 3 nếu vi phạm bất kỳ điều nào sau:

- ❌ Sử dụng dữ liệu ngoài bộ dữ liệu được cung cấp
- ❌ Không đính kèm mã nguồn hoặc kết quả không thể tái lập
- ❌ Sử dụng `Revenue`/`COGS` từ tập test làm đặc trưng

---

## Checklist nộp bài

Mỗi đội cần hoàn thành và nộp đầy đủ các mục sau:

### 1. File `submission.csv` trên Kaggle

- Link: https://www.kaggle.com/competitions/datathon-2026-round-1
- Đảm bảo file `submission.csv` có đúng số lượng dòng và giữ nguyên thứ tự như `sample_submission.csv`
- File không đúng định dạng sẽ bị từ chối bởi hệ thống Kaggle

### 2. Báo cáo (Report — PDF)

- Sử dụng **template LaTeX NeurIPS**: https://neurips.cc/Conferences/2025/CallForPapers
- Giới hạn tối đa **4 trang** (không tính references và appendix)
- Bao gồm các nội dung:
  - Trực quan hoá và phân tích dữ liệu (Phần 2)
  - Phương pháp tiếp cận, pipeline mô hình và kết quả thực nghiệm (Phần 3)
  - Link GitHub repository của nhóm

### 3. GitHub Repository

- Chứa toàn bộ code, notebook, và file submission
- Đặt ở chế độ **public** hoặc cấp quyền truy cập cho ban tổ chức trước deadline
- Cần có `README.md` mô tả cấu trúc thư mục và hướng dẫn chạy lại kết quả

### 4. Form nộp bài chính thức

Điền đầy đủ thông tin trong form nộp bài (link sẽ được cung cấp). Form yêu cầu:

- ✅ Chọn đáp án đúng cho câu hỏi trắc nghiệm
- ✅ Upload file báo cáo (PDF)
- ✅ Link GitHub repository
- ✅ Link submission trên Kaggle
- ✅ Ảnh chụp thẻ sinh viên của tất cả thành viên trong đội
- ✅ Tickbox xác nhận: Nhóm thi cam kết có ít nhất 1 thành viên có thể tham gia trực tiếp Vòng Chung kết vào ngày **23/05/2026** tại Đại học VinUni, Hà Nội

> ⚠️ **Quan trọng**: Các đội không xác nhận khả năng tham gia trực tiếp Vòng Chung kết hoặc không cung cấp đầy đủ ảnh thẻ học sinh sẽ không đủ điều kiện để được xét vào vòng tiếp theo.

---

## Kaggle Competition Rules (Tóm tắt)

### Điều kiện tham gia
- Phải có tài khoản Kaggle đã đăng ký
- Từ 18 tuổi trở lên (hoặc tuổi trưởng thành tại nơi cư trú)
- Không cư trú tại các vùng bị cấm vận

### Quy định về Team
- Mỗi cá nhân chỉ được tham gia **1 team**
- Mỗi thành viên phải có tài khoản Kaggle riêng
- Cho phép merge team nếu không vượt quá giới hạn kích thước

### Quy định về Code
- **Không** chia sẻ code riêng tư giữa các team
- **Được phép** chia sẻ code công khai trên Kaggle forum/notebooks
- Nếu dùng open source, phải tuân thủ license OSI-approved

### Xác định người thắng
- Dựa trên **Private Leaderboard** (tập test ẩn)
- Trường hợp hoà: submission nộp trước sẽ thắng
- Giải thưởng: **Kudos** (không có Points hoặc Medals)
