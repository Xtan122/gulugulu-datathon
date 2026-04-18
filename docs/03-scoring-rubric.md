# Thang điểm Chấm thi

Tổng điểm tối đa: **100 điểm**. Điểm thành phần không làm tròn cho đến khi tính tổng cuối cùng.

---

## Phân bổ điểm tổng quan

| Phần | Nội dung | Điểm | Tỷ trọng |
|------|----------|------|----------|
| 1 | Câu hỏi Trắc nghiệm (MCQ) | 20 | 20% |
| 2 | Trực quan hoá & Phân tích (EDA) | 60 | 60% |
| 3 | Mô hình Dự báo Doanh thu (Forecasting) | 20 | 20% |
| **Tổng** | | **100** | **100%** |

---

## Phần 1 — Câu hỏi Trắc nghiệm (20 điểm)

Mỗi câu đúng được **2 điểm**. Không trừ điểm cho câu trả lời sai.

| Thành phần | Số câu | Điểm |
|------------|--------|------|
| Câu trả lời đúng | 10 câu | 2 điểm / câu |
| Câu trả lời sai | — | 0 điểm |
| Không trả lời | — | 0 điểm |
| **Tổng tối đa** | | **20 điểm** |

---

## Phần 2 — Trực quan hoá & Phân tích EDA (60 điểm)

Chấm theo **4 tiêu chí** độc lập:

| Tiêu chí | Mô tả | Điểm tối đa |
|-----------|-------|-------------|
| **Chất lượng trực quan hoá** | Biểu đồ có tiêu đề, nhãn trục, chú thích đầy đủ; lựa chọn loại biểu đồ phù hợp; thẩm mỹ trình bày rõ ràng | 15 |
| **Chiều sâu phân tích** | Bao phủ đầy đủ 4 cấp độ Descriptive → Diagnostic → Predictive → Prescriptive; lập luận logic, có số liệu cụ thể hỗ trợ | 25 |
| **Insight kinh doanh** | Phát hiện có giá trị thực tiễn; đề xuất hành động khả thi; liên kết rõ ràng giữa dữ liệu và quyết định kinh doanh | 15 |
| **Tính sáng tạo & kể chuyện** | Góc nhìn độc đáo, không lặp lại các phân tích hiển nhiên; mạch trình bày coherent; kết nối nhiều bảng dữ liệu một cách có chủ đích | 5 |
| **Tổng tối đa** | | **60 điểm** |

### Chi tiết thang điểm từng tiêu chí

#### Chất lượng trực quan hoá (15 điểm)

| Mức điểm | Mô tả |
|----------|-------|
| 13–15 | Tất cả biểu đồ đều đạt chuẩn, lựa chọn loại biểu đồ tối ưu cho từng insight |
| 8–12 | Phần lớn biểu đồ đạt yêu cầu, một số thiếu nhãn hoặc chú thích |
| 0–7 | Biểu đồ thiếu thông tin, khó đọc hoặc không phù hợp với dữ liệu |

#### Chiều sâu phân tích (25 điểm)

| Mức điểm | Mô tả |
|----------|-------|
| 21–25 | Đạt cả 4 cấp độ Descriptive, Diagnostic, Predictive, Prescriptive một cách nhất quán |
| 14–20 | Đạt 3 cấp độ, cấp độ Prescriptive còn hời hợt |
| 7–13 | Chủ yếu ở cấp Descriptive và Diagnostic |
| 0–6 | Chỉ mô tả bề mặt, thiếu phân tích |

#### Insight kinh doanh (15 điểm)

| Mức điểm | Mô tả |
|----------|-------|
| 13–15 | Đề xuất cụ thể, định lượng được, áp dụng được ngay |
| 8–12 | Có đề xuất nhưng còn chung chung |
| 0–7 | Thiếu kết nối với bối cảnh kinh doanh |

#### Tính sáng tạo & kể chuyện (5 điểm)

| Mức điểm | Mô tả |
|----------|-------|
| 4–5 | Góc nhìn độc đáo, kết hợp nhiều nguồn dữ liệu, mạch trình bày thuyết phục |
| 2–3 | Có điểm sáng tạo nhưng chưa nhất quán |
| 0–1 | Phân tích dự đoán được, không có điểm nổi bật |

---

## Phần 3 — Mô hình Dự báo Doanh thu (20 điểm)

Điểm được tính từ **2 thành phần**:

| Thành phần | Mô tả | Điểm tối đa |
|------------|-------|-------------|
| **Hiệu suất mô hình** | Dựa trên điểm MAE, RMSE, R² trên tập test (Kaggle leaderboard); xếp hạng tương đối so với các đội khác | 12 |
| **Báo cáo kỹ thuật** | Chất lượng pipeline (feature engineering, cross-validation, xử lý leakage); giải thích mô hình bằng SHAP / feature importance; tuân thủ các ràng buộc | 8 |
| **Tổng tối đa** | | **20 điểm** |

### Chi tiết thang điểm

#### Hiệu suất mô hình (12 điểm)

| Mức điểm | Mô tả |
|----------|-------|
| 10–12 | Xếp hạng top leaderboard; MAE và RMSE thấp, R² cao |
| 5–9 | Hiệu suất trung bình; mô hình hoạt động nhưng chưa tối ưu |
| 3–4 | Bài nộp hợp lệ nhưng hiệu suất thấp; mức điểm sàn |

#### Báo cáo kỹ thuật (8 điểm)

| Mức điểm | Mô tả |
|----------|-------|
| 7–8 | Pipeline rõ ràng, cross-validation đúng chiều thời gian, giải thích mô hình cụ thể bằng SHAP hoặc tương đương, tuân thủ đầy đủ ràng buộc |
| 4–6 | Pipeline đủ dùng, giải thích còn định tính, một số ràng buộc chưa được xử lý tường minh |
| 0–3 | Thiếu giải thích, không kiểm soát leakage, hoặc không thể tái lập kết quả |

### Điều kiện loại bài (Phần 3)

Bài nộp bị **loại toàn bộ điểm Phần 3** nếu vi phạm bất kỳ điều nào sau:

- ❌ Sử dụng `Revenue`/`COGS` từ tập test làm đặc trưng
- ❌ Sử dụng dữ liệu ngoài bộ dữ liệu được cung cấp
- ❌ Không đính kèm mã nguồn hoặc kết quả không thể tái lập
