# Đề Bài — Chi tiết 3 phần thi

---

## Phần 1 — Câu hỏi Trắc nghiệm (20 điểm)

Chọn **một đáp án đúng nhất** cho mỗi câu hỏi. Các câu hỏi yêu cầu tính toán trực tiếp từ dữ liệu được cung cấp.

### Q1
Trong số các khách hàng có nhiều hơn một đơn hàng, trung vị số ngày giữa hai lần mua liên tiếp (inter-order gap) xấp xỉ là bao nhiêu? *(Tính từ `orders.csv`)*

- A) 30 ngày
- B) 90 ngày
- C) 180 ngày
- D) 365 ngày

### Q2
Phân khúc sản phẩm (`segment`) nào trong `products.csv` có tỷ suất lợi nhuận gộp trung bình cao nhất, với công thức `(price − cogs) / price`?

- A) Premium
- B) Performance
- C) Activewear
- D) Standard

### Q3
Trong các bản ghi trả hàng liên kết với sản phẩm thuộc danh mục **Streetwear** (join `returns` với `products` theo `product_id`), lý do trả hàng nào xuất hiện nhiều nhất?

- A) defective
- B) wrong_size
- C) changed_mind
- D) not_as_described

### Q4
Trong `web_traffic.csv`, nguồn truy cập (`traffic_source`) nào có tỷ lệ thoát trung bình (`bounce_rate`) thấp nhất trên tất cả các ngày xuất hiện nguồn đó?

- A) organic_search
- B) paid_search
- C) email_campaign
- D) social_media

### Q5
Tỷ lệ phần trăm các dòng trong `order_items.csv` có áp dụng khuyến mãi (tức là `promo_id` không null) xấp xỉ là bao nhiêu?

- A) 12%
- B) 25%
- C) 39%
- D) 54%

### Q6
Trong `customers.csv`, xét các khách hàng có `age_group` khác null, nhóm tuổi nào có số đơn hàng trung bình trên mỗi khách hàng cao nhất? *(tổng số đơn / số khách hàng trong nhóm)*

- A) 55+
- B) 25–34
- C) 35–44
- D) 45–54

### Q7
Vùng (`region`) nào trong `geography.csv` tạo ra tổng doanh thu cao nhất trong `sales_train.csv`?

- A) West
- B) Central
- C) East
- D) Cả ba vùng có doanh thu xấp xỉ bằng nhau

### Q8
Trong các đơn hàng có `order_status = 'cancelled'` trong `orders.csv`, phương thức thanh toán nào được sử dụng nhiều nhất?

- A) credit_card
- B) cod
- C) paypal
- D) bank_transfer

### Q9
Trong bốn kích thước sản phẩm (S, M, L, XL), kích thước nào có tỷ lệ trả hàng cao nhất, được định nghĩa là số bản ghi trong `returns` chia cho số dòng trong `order_items` (join với `products` theo `product_id`)?

- A) S
- B) M
- C) L
- D) XL

### Q10
Trong `payments.csv`, kế hoạch trả góp nào có giá trị thanh toán trung bình trên mỗi đơn hàng cao nhất?

- A) 1 kỳ (trả một lần)
- B) 3 kỳ
- C) 6 kỳ
- D) 12 kỳ

---

## Phần 2 — Trực quan hoá và Phân tích Dữ liệu (60 điểm)

Khám phá bộ dữ liệu để tìm ra các insight có ý nghĩa kinh doanh. Phần này được đánh giá dựa trên **tính sáng tạo**, **chiều sâu phân tích** và **chất lượng trình bày**. Không có đáp án đúng duy nhất — ban giám khảo đánh giá khả năng **kể chuyện bằng dữ liệu** (data storytelling).

### Yêu cầu

Các đội thi tự do lựa chọn góc nhìn phân tích. Bài nộp cần bao gồm:

1. **Trực quan hoá (Visualizations)**: Tạo các biểu đồ, đồ thị, bản đồ hoặc dashboard trực quan để thể hiện các pattern, xu hướng và mối quan hệ trong dữ liệu. Mỗi hình ảnh cần có tiêu đề, nhãn trục rõ ràng và chú thích phù hợp.

2. **Phân tích (Analysis)**: Viết phần giải thích đi kèm mỗi trực quan hoá, bao gồm:
   - Mô tả những gì biểu đồ thể hiện và tại sao góc nhìn này quan trọng
   - Các phát hiện chính (key findings) được hỗ trợ bởi số liệu cụ thể
   - Ý nghĩa kinh doanh (business implications) hoặc đề xuất hành động (actionable recommendations)

### Bốn cấp độ phân tích (Rubric)

| Cấp độ | Câu hỏi | Ban giám khảo đánh giá |
|--------|---------|------------------------|
| **Descriptive** | What happened? | Thống kê tổng hợp chính xác, biểu đồ có nhãn rõ ràng, tổng hợp dữ liệu đúng |
| **Diagnostic** | Why did it happen? | Giả thuyết nhân quả, so sánh phân khúc, xác định bất thường có bằng chứng hỗ trợ |
| **Predictive** | What is likely to happen? | Ngoại suy xu hướng, phân tích tính mùa vụ, phân tích chỉ số dẫn xuất |
| **Prescriptive** | What should we do? | Đề xuất hành động kinh doanh được hỗ trợ bởi dữ liệu; đánh đổi được định lượng |

> Các đội đạt cấp độ **Prescriptive** nhất quán trên nhiều phân tích sẽ đạt điểm cao nhất.

---

## Phần 3 — Mô hình Dự báo Doanh thu (20 điểm)

### Bối cảnh kinh doanh

Bạn là nhà khoa học dữ liệu tại một công ty thương mại điện tử thời trang Việt Nam. Doanh nghiệp cần dự báo nhu cầu chính xác ở mức chi tiết để:
- Tối ưu hoá phân bổ tồn kho
- Lập kế hoạch khuyến mãi
- Quản lý logistics trên toàn quốc

### Định nghĩa bài toán

Dự báo cột **`Revenue`** (doanh thu thuần hàng ngày) cho giai đoạn **01/01/2023 – 01/07/2024**.

Mỗi dòng trong tập test là một bộ `(Date, Revenue, COGS)` duy nhất.

### Chỉ số đánh giá

Bài nộp được đánh giá bằng **3 chỉ số** đồng thời:

**1. Mean Absolute Error (MAE)**
```
MAE = (1/n) × Σ|Fᵢ − Aᵢ|
```
Đo độ lệch tuyệt đối trung bình. Càng thấp càng tốt.

**2. Root Mean Squared Error (RMSE)**
```
RMSE = √[(1/n) × Σ(Fᵢ − Aᵢ)²]
```
Phạt nặng hơn các sai số lớn so với MAE. Càng thấp càng tốt.

**3. R² (Coefficient of Determination)**
```
R² = 1 − [Σ(Aᵢ − Fᵢ)² / Σ(Aᵢ − Ā)²]
```
Tỷ lệ phương sai được giải thích bởi mô hình. Càng cao càng tốt (lý tưởng gần 1).

Trong đó: `Fᵢ` = giá trị dự báo, `Aᵢ` = giá trị thực, `Ā` = trung bình giá trị thực.

### Định dạng file nộp

Nộp file `submission.csv` với cấu trúc:

```csv
Date,Revenue,COGS
2023-01-01,26607.2,2585.15
2023-01-02,1007.89,163.0
2023-01-03,1089.51,821.12
...
```

> ⚠️ Các dòng phải giữ **đúng thứ tự** như `sample_submission.csv`. Không sắp xếp lại hoặc xáo trộn.

### Ràng buộc

1. **Không dùng dữ liệu ngoài**: Tất cả đặc trưng phải được tạo từ các file dữ liệu được cung cấp.
2. **Tính tái lập (Reproducibility)**: Đính kèm toàn bộ mã nguồn. Đặt `random seed` khi cần thiết.
3. **Khả năng giải thích (Explainability)**: Trong report, bao gồm mục giải thích các yếu tố dẫn động doanh thu chính (feature importances, SHAP values, hoặc partial dependence plots). Giải thích bằng ngôn ngữ kinh doanh.
