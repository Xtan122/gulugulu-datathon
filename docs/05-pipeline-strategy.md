# Pipeline Chiến lược — DATATHON 2026

## Phân tích chiến lược tổng thể

### Phân bổ effort theo ROI (Return on Investment)

| Phần | Điểm | Effort | Lý do |
|------|------|--------|-------|
| Phần 1 — MCQ | 20đ | 5% thời gian | 10 câu tính toán đơn giản, AI có thể giải gần như tự động → **easy 20 điểm** |
| Phần 2 — EDA | 60đ | 55% thời gian | Chiếm 60% tổng điểm, đánh giá chủ quan bởi giám khảo → **cần đầu tư nhiều nhất** |
| Phần 3 — Forecasting | 20đ | 30% thời gian | Kaggle leaderboard + báo cáo kỹ thuật, cần pipeline chắc chắn |
| Report + Submission | — | 10% thời gian | Tổng hợp, viết báo cáo NeurIPS, setup GitHub |

---

## PHASE 0: Setup & Data Loading (Ngày 1, ~2 giờ)

### Mục tiêu
Thiết lập môi trường, load toàn bộ 15 file CSV, kiểm tra data quality cơ bản.

### Các bước

| Bước | Công việc | 🤖 Vai trò AI |
|------|-----------|---------------|
| 0.1 | Tạo cấu trúc project (folders, requirements.txt) | AI **tự động tạo** scaffold project: `data/`, `notebooks/`, `src/`, `reports/`, `submissions/` |
| 0.2 | Load toàn bộ 15 CSV files | AI **sinh code** load data với pandas, kiểm tra dtypes, shape, memory usage |
| 0.3 | Data quality check | AI **sinh code** kiểm tra: missing values, duplicates, data types, value ranges, FK integrity |
| 0.4 | Tạo data dictionary tự động | AI **phân tích** và tạo summary statistics cho từng bảng |
| 0.5 | Setup random seed & reproducibility | AI **cấu hình** `SEED=42`, logging, version tracking |

### Output
- `notebooks/00_data_loading.ipynb` — Load & validate data
- `src/config.py` — Constants, paths, seed
- `src/data_loader.py` — Reusable data loading functions

---

## PHASE 1: Trắc nghiệm — MCQ (Ngày 1, ~2 giờ)

### Mục tiêu
Trả lời chính xác 10/10 câu → **20/20 điểm**.

### Các bước

| Câu | Bảng cần dùng | Phép tính | 🤖 Vai trò AI |
|-----|---------------|-----------|---------------|
| Q1 | `orders.csv` | Tính inter-order gap median cho khách hàng có >1 đơn | AI **sinh code** pandas: groupby customer_id, sort order_date, diff(), median() |
| Q2 | `products.csv` | Tính `(price-cogs)/price` trung bình theo segment | AI **sinh code** groupby segment, mean gross margin |
| Q3 | `returns.csv` + `products.csv` | Join → filter Streetwear → value_counts return_reason | AI **sinh code** merge + filter + value_counts |
| Q4 | `web_traffic.csv` | Groupby traffic_source → mean bounce_rate → min | AI **sinh code** groupby + mean + idxmin |
| Q5 | `order_items.csv` | Tỷ lệ promo_id not null | AI **sinh code** notna().mean() |
| Q6 | `customers.csv` + `orders.csv` | Join → groupby age_group → count orders / count customers | AI **sinh code** merge + groupby + agg |
| Q7 | `orders.csv` + `order_items.csv` + `geography.csv` | Join → groupby region → sum revenue | AI **sinh code** multi-table join + groupby sum |
| Q8 | `orders.csv` | Filter cancelled → value_counts payment_method | AI **sinh code** filter + value_counts |
| Q9 | `returns.csv` + `order_items.csv` + `products.csv` | Return rate by size | AI **sinh code** multi-join + ratio calculation |
| Q10 | `payments.csv` | Groupby installments → mean payment_value | AI **sinh code** groupby + mean |

### 🤖 AI Strategy cho Phase 1
- AI đóng vai **Data Analyst tự động**: sinh toàn bộ code tính toán cho 10 câu
- AI **cross-validate** kết quả bằng cách tính theo 2 cách khác nhau cho mỗi câu
- AI **giải thích** logic tính toán để người dùng verify trước khi chọn đáp án
- **Ước tính**: AI có thể giải 10/10 câu trong ~30 phút

### Output
- `notebooks/01_mcq_answers.ipynb` — Code + đáp án + giải thích
- `answers.json` — Đáp án cuối cùng {Q1: "B", Q2: "A", ...}

---

## PHASE 2: EDA & Data Storytelling (Ngày 2–6, ~60% effort)

### Mục tiêu
Đạt **50–60/60 điểm** bằng cách cover đầy đủ 4 cấp độ phân tích với data storytelling xuất sắc.

### Chiến lược: 5 Chủ đề phân tích (Analysis Themes)

Mỗi chủ đề sẽ đi qua đầy đủ 4 cấp độ: Descriptive → Diagnostic → Predictive → Prescriptive.

---

### Theme 1: Revenue & Profitability Deep Dive

**Câu hỏi kinh doanh**: Doanh thu và lợi nhuận biến động như thế nào? Đâu là động lực tăng trưởng chính?

| Cấp độ | Phân tích | 🤖 Vai trò AI |
|--------|-----------|---------------|
| Descriptive | Revenue trend theo ngày/tháng/quý/năm; Revenue by category/segment; Gross margin distribution | AI **sinh code** time series plots, bar charts, distribution plots với matplotlib/seaborn/plotly |
| Diagnostic | Tại sao revenue tăng/giảm đột biến? Correlation với promotions, seasonality, web traffic | AI **phân tích** anomaly detection, correlation analysis, decomposition; **sinh narrative** giải thích |
| Predictive | Xu hướng revenue 2023–2024; Seasonal patterns; Leading indicators từ web_traffic | AI **chạy** seasonal decomposition (STL), trend extrapolation; **sinh biểu đồ** forecast fan charts |
| Prescriptive | Đề xuất: tập trung vào segment/category nào? Thời điểm nào cần đẩy mạnh? | AI **tổng hợp** insights → **viết** business recommendations với số liệu cụ thể |

### Theme 2: Customer Behavior & Segmentation

**Câu hỏi kinh doanh**: Khách hàng mua sắm như thế nào? Nhóm nào có giá trị cao nhất?

| Cấp độ | Phân tích | 🤖 Vai trò AI |
|--------|-----------|---------------|
| Descriptive | Customer demographics (age_group, gender, city); Order frequency distribution; AOV by segment | AI **sinh code** demographic charts, RFM metrics calculation |
| Diagnostic | Tại sao nhóm 55+ có order frequency cao? Kênh acquisition nào hiệu quả nhất? | AI **phân tích** cohort analysis, acquisition channel ROI; **sinh** comparison charts |
| Predictive | Customer lifetime value prediction; Churn risk indicators | AI **tính** CLV estimates, retention curves; **sinh** survival analysis plots |
| Prescriptive | Đề xuất: chiến lược retention cho từng segment; Kênh marketing nên đầu tư | AI **viết** actionable recommendations: "Tăng 15% budget cho email_campaign vì conversion rate cao hơn 2.3x so với social_media" |

### Theme 3: Product & Inventory Optimization

**Câu hỏi kinh doanh**: Sản phẩm nào bán chạy? Tồn kho có tối ưu không?

| Cấp độ | Phân tích | 🤖 Vai trò AI |
|--------|-----------|---------------|
| Descriptive | Top products by revenue/quantity; Category mix; Size/color distribution; Stockout frequency | AI **sinh code** Pareto charts, heatmaps, treemaps |
| Diagnostic | Tại sao một số sản phẩm có return rate cao? Stockout ảnh hưởng revenue thế nào? | AI **phân tích** return reasons by product attributes; stockout impact analysis |
| Predictive | Sản phẩm nào sẽ trending? Inventory needs dự báo | AI **chạy** demand forecasting by category; **sinh** inventory projection charts |
| Prescriptive | Đề xuất: reorder points, markdown strategy cho overstock, size optimization | AI **tính** optimal reorder quantities; **viết** "Giảm 20% tồn kho size XL vì sell-through rate chỉ 0.3x so với size M" |

### Theme 4: Promotion Effectiveness

**Câu hỏi kinh doanh**: Khuyến mãi có hiệu quả không? ROI của từng loại promotion?

| Cấp độ | Phân tích | 🤖 Vai trò AI |
|--------|-----------|---------------|
| Descriptive | Promotion usage rate; Discount distribution; Revenue with/without promo | AI **sinh code** promo analysis: usage %, avg discount, revenue lift |
| Diagnostic | Promo nào thực sự tăng revenue vs. cannibalize margin? Stackable promos có hiệu quả? | AI **phân tích** A/B style comparison (promo vs non-promo periods); margin impact |
| Predictive | Dự báo impact của promo lên revenue trong tương lai | AI **mô hình hoá** promo elasticity; **sinh** what-if scenarios |
| Prescriptive | Đề xuất: loại promo nào nên dùng, thời điểm nào, cho category nào | AI **viết** "Percentage discounts 10-15% trên Activewear tạo revenue lift 23% với margin erosion chỉ 8%" |

### Theme 5: Digital & Operations Performance

**Câu hỏi kinh doanh**: Website traffic chuyển đổi thành doanh thu hiệu quả thế nào? Logistics có bottleneck?

| Cấp độ | Phân tích | 🤖 Vai trò AI |
|--------|-----------|---------------|
| Descriptive | Traffic trends; Conversion funnel; Delivery time distribution; Shipping cost analysis | AI **sinh code** funnel charts, delivery time histograms, traffic source breakdown |
| Diagnostic | Tại sao bounce rate cao ở social_media? Delivery delay ảnh hưởng review rating? | AI **phân tích** correlation: delivery_time vs rating; bounce_rate by source |
| Predictive | Traffic → Revenue prediction; Delivery capacity planning | AI **chạy** regression: sessions → orders → revenue; **sinh** capacity charts |
| Prescriptive | Đề xuất: tối ưu traffic source mix; cải thiện delivery SLA | AI **viết** "Chuyển 30% budget từ social_media sang email_campaign sẽ tăng conversion 18%" |

---

### 🤖 AI Roles tổng hợp cho Phase 2

| Vai trò AI | Mô tả chi tiết |
|------------|-----------------|
| **Code Generator** | Sinh toàn bộ code Python cho data manipulation, visualization (matplotlib, seaborn, plotly) |
| **Statistical Analyst** | Chạy statistical tests, correlation analysis, decomposition, anomaly detection |
| **Visualization Designer** | Đề xuất loại biểu đồ phù hợp nhất cho từng insight; tối ưu aesthetics (color palette, layout) |
| **Business Narrator** | Viết narrative cho mỗi visualization: what it shows, why it matters, what to do about it |
| **Insight Synthesizer** | Kết nối insights across themes; tìm cross-table patterns mà single-table analysis bỏ lỡ |
| **Quality Reviewer** | Review biểu đồ: đủ title/labels/annotations chưa? Số liệu có consistent không? |

### Output
- `notebooks/02_eda_theme1_revenue.ipynb`
- `notebooks/02_eda_theme2_customer.ipynb`
- `notebooks/02_eda_theme3_product.ipynb`
- `notebooks/02_eda_theme4_promotion.ipynb`
- `notebooks/02_eda_theme5_digital_ops.ipynb`
- `figures/` — Tất cả biểu đồ export PNG/SVG cho report

---

## PHASE 3: Sales Forecasting Model (Ngày 3–8, song song với EDA)

### Mục tiêu
Đạt **top leaderboard** (MAE thấp, RMSE thấp, R² cao) + báo cáo kỹ thuật chất lượng → **16–20/20 điểm**.

### Pipeline Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    FORECASTING PIPELINE                      │
│                                                              │
│  ┌──────────┐   ┌──────────────┐   ┌───────────────┐       │
│  │ Feature  │──▶│   Model      │──▶│  Ensemble &   │       │
│  │ Engine   │   │   Training   │   │  Post-process │       │
│  └──────────┘   └──────────────┘   └───────────────┘       │
│       │               │                    │                 │
│       ▼               ▼                    ▼                 │
│  Time features   Multiple models    Weighted average         │
│  Lag features    Time-series CV     Clipping/smoothing       │
│  External feat   Hyperparameter     submission.csv           │
│  (from 15 CSVs) tuning                                      │
└─────────────────────────────────────────────────────────────┘
```

### Step 3.1: Feature Engineering

| Feature Group | Chi tiết | 🤖 Vai trò AI |
|---------------|----------|---------------|
| **Time features** | day_of_week, month, quarter, year, day_of_year, week_of_year, is_weekend, is_month_start/end | AI **sinh code** tự động extract tất cả calendar features |
| **Lag features** | Revenue lag 1, 7, 14, 28, 30, 90, 365 ngày; Rolling mean/std 7, 14, 30, 90 ngày | AI **sinh code** shift() + rolling(); **cảnh báo** leakage nếu dùng future data |
| **Trend features** | Linear trend, exponential smoothing trend | AI **tính** trend decomposition |
| **Seasonality** | Fourier terms (sin/cos) cho weekly, monthly, yearly cycles | AI **sinh code** Fourier features với các period phù hợp |
| **Promotion features** | Số promo active theo ngày, avg discount_value, promo_type distribution | AI **sinh code** aggregate promotions.csv theo date range |
| **Web traffic features** | sessions, unique_visitors, page_views, conversion_rate (aggregate by date) | AI **sinh code** merge web_traffic.csv (aggregate across traffic_source) |
| **Inventory features** | Monthly: total stock_on_hand, stockout_days, fill_rate (forward-fill to daily) | AI **sinh code** resample monthly → daily; **cảnh báo** granularity mismatch |
| **Order features** | Daily: order count, avg order value, unique customers, category mix | AI **sinh code** aggregate orders + order_items by date |
| **Holiday/Event** | Vietnamese holidays, Tet, Black Friday, 11.11, 12.12 (derived from data patterns) | AI **phát hiện** spike patterns trong historical data → tạo binary flags |

### 🤖 AI Role — Feature Engineering Specialist
- **Tự động sinh** 50–100 features từ 15 bảng dữ liệu
- **Kiểm tra leakage**: đảm bảo không feature nào dùng thông tin từ tương lai
- **Feature selection**: chạy correlation analysis, mutual information, SHAP-based selection
- **Đề xuất** feature interactions và polynomial features

### Step 3.2: Model Training

| Model | Mô tả | 🤖 Vai trò AI |
|-------|--------|---------------|
| **LightGBM** | Gradient boosting — strong baseline cho tabular data | AI **sinh code** training + hyperparameter tuning với Optuna |
| **XGBoost** | Alternative gradient boosting | AI **sinh code** + compare với LightGBM |
| **CatBoost** | Handles categorical features natively | AI **sinh code** + leverage categorical columns |
| **Prophet** | Facebook's time series model — captures seasonality well | AI **sinh code** Prophet với custom seasonalities (Tet, promotions) |
| **ARIMA/SARIMAX** | Classical time series — good for trend + seasonality | AI **sinh code** auto_arima hoặc manual SARIMAX |
| **Neural Network** | LSTM hoặc N-BEATS nếu data đủ lớn | AI **đánh giá** có nên dùng không (10 năm daily data ≈ 3800 rows — có thể đủ) |

### 🤖 AI Role — ML Engineer
- **Sinh code** training pipeline cho mỗi model
- **Implement** Time Series Cross-Validation (expanding window, KHÔNG random split)
- **Tune** hyperparameters với Optuna/Bayesian optimization
- **Monitor** overfitting: train vs validation metrics
- **Đảm bảo** reproducibility: set seed, log all parameters

### Step 3.3: Validation Strategy

```
Time Series Cross-Validation (Expanding Window):
                                                              
Fold 1: [====TRAIN====][VAL]                                  
Fold 2: [======TRAIN======][VAL]                              
Fold 3: [========TRAIN========][VAL]                          
Fold 4: [==========TRAIN==========][VAL]                      
Fold 5: [============TRAIN============][VAL]                  
                                                              
⚠️ KHÔNG dùng random KFold — sẽ gây data leakage!            
```

| Validation | Chi tiết | 🤖 Vai trò AI |
|------------|----------|---------------|
| Expanding window CV | 5 folds, mỗi fold validation = 6 tháng cuối | AI **implement** custom TimeSeriesSplit |
| Holdout set | Giữ 2022 làm final validation (gần nhất với test period) | AI **tách** data đúng cách |
| Metrics tracking | MAE, RMSE, R² cho mỗi fold | AI **log** metrics, **sinh** comparison table |

### Step 3.4: Ensemble & Post-processing

| Bước | Chi tiết | 🤖 Vai trò AI |
|------|----------|---------------|
| Weighted ensemble | Combine top 3–5 models bằng weighted average (weights from CV) | AI **tối ưu** weights bằng scipy.optimize |
| Stacking | Train meta-learner (Ridge/Linear) trên out-of-fold predictions | AI **implement** stacking pipeline |
| Post-processing | Clip negative values → 0; Smooth outlier predictions | AI **sinh code** post-processing rules |
| Submission format | Đảm bảo đúng format sample_submission.csv | AI **validate** submission file trước khi nộp |

### Step 3.5: Explainability (cho báo cáo — 8 điểm)

| Phân tích | 🤖 Vai trò AI |
|-----------|---------------|
| SHAP values | AI **sinh code** SHAP summary plot, dependence plots cho top features |
| Feature importance | AI **sinh** bar chart feature importance từ LightGBM/XGBoost |
| Partial Dependence Plots | AI **sinh** PDP cho top 5 features |
| Business interpretation | AI **viết** giải thích: "Web traffic sessions là feature quan trọng nhất, cho thấy demand online là driver chính của revenue" |

### Output
- `notebooks/03_feature_engineering.ipynb`
- `notebooks/03_model_training.ipynb`
- `notebooks/03_ensemble.ipynb`
- `notebooks/03_explainability.ipynb`
- `src/features.py` — Feature engineering functions
- `src/models.py` — Model training & prediction
- `src/ensemble.py` — Ensemble logic
- `submissions/submission.csv` — Final submission

---

## PHASE 4: Report & Submission (Ngày 9–11)

### Mục tiêu
Tổng hợp tất cả thành báo cáo NeurIPS 4 trang + nộp bài đầy đủ.

### Report Structure (NeurIPS Template, max 4 trang)

| Section | Nội dung | 🤖 Vai trò AI |
|---------|----------|---------------|
| **1. Introduction** (~0.3 trang) | Bối cảnh bài toán, approach overview | AI **viết draft** introduction dựa trên competition description |
| **2. EDA & Insights** (~1.5 trang) | Top 5–8 visualizations + analysis từ Phase 2 | AI **chọn** best visualizations; **viết** concise narratives; **format** cho LaTeX |
| **3. Forecasting Pipeline** (~1.5 trang) | Feature engineering, model selection, CV strategy, ensemble, results | AI **viết** technical description; **sinh** pipeline diagram; **format** metrics table |
| **4. Model Explainability** (~0.5 trang) | SHAP plots, feature importance, business interpretation | AI **chọn** most impactful SHAP plots; **viết** business-language explanation |
| **References** | Libraries, methods | AI **sinh** BibTeX references |
| **Appendix** | Additional charts, full feature list | AI **compile** supplementary materials |

### 🤖 AI Roles cho Phase 4

| Vai trò AI | Mô tả |
|------------|--------|
| **Technical Writer** | Viết draft báo cáo bằng tiếng Việt/Anh, academic style phù hợp NeurIPS |
| **LaTeX Formatter** | Sinh LaTeX code cho tables, figures, equations |
| **Figure Curator** | Chọn và resize figures phù hợp 4-page limit |
| **Proofreader** | Review consistency: số liệu trong text khớp với biểu đồ |

### GitHub Repository Structure

```
datathon-2026/
├── README.md                    ← AI sinh: project overview + hướng dẫn reproduce
├── requirements.txt             ← AI sinh: pinned versions
├── data/                        ← Raw CSV files (gitignore nếu quá lớn)
├── notebooks/
│   ├── 00_data_loading.ipynb
│   ├── 01_mcq_answers.ipynb
│   ├── 02_eda_theme1_revenue.ipynb
│   ├── 02_eda_theme2_customer.ipynb
│   ├── 02_eda_theme3_product.ipynb
│   ├── 02_eda_theme4_promotion.ipynb
│   ├── 02_eda_theme5_digital_ops.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   ├── 03_ensemble.ipynb
│   └── 03_explainability.ipynb
├── src/
│   ├── config.py
│   ├── data_loader.py
│   ├── features.py
│   ├── models.py
│   └── ensemble.py
├── reports/
│   ├── report.tex
│   ├── report.pdf
│   └── figures/
├── submissions/
│   └── submission.csv
└── answers/
    └── mcq_answers.json
```

### Output
- `reports/report.pdf` — Báo cáo NeurIPS 4 trang
- GitHub repository hoàn chỉnh với README.md

---

## PHASE 5: Final Review & Submit (Ngày 12–13)

| Bước | Công việc | 🤖 Vai trò AI |
|------|-----------|---------------|
| 5.1 | Verify submission.csv format | AI **validate**: đúng số dòng, đúng thứ tự, không NaN |
| 5.2 | Re-run toàn bộ pipeline từ đầu | AI **kiểm tra** reproducibility: kết quả có giống không? |
| 5.3 | Review report | AI **proofread**: typos, consistency, figure quality |
| 5.4 | Submit lên Kaggle | Người dùng submit; AI **verify** submission accepted |
| 5.5 | Nộp form chính thức | Người dùng điền form; AI **checklist** đầy đủ items |

---

## Timeline tổng hợp (13 ngày)

```
Ngày  1  ████░░░░░░░░░  Phase 0 (Setup) + Phase 1 (MCQ)
Ngày  2  ░░████████░░░  Phase 2 (EDA Theme 1-2)
Ngày  3  ░░████████░░░  Phase 2 (EDA Theme 3-4) + Phase 3 bắt đầu
Ngày  4  ░░████████░░░  Phase 2 (EDA Theme 5) + Phase 3 (Features)
Ngày  5  ░░████████░░░  Phase 2 (Polish) + Phase 3 (Models)
Ngày  6  ░░████████░░░  Phase 2 (Finalize) + Phase 3 (Models)
Ngày  7  ░░░░░░████░░░  Phase 3 (Ensemble + Tuning)
Ngày  8  ░░░░░░████░░░  Phase 3 (Explainability + Final model)
Ngày  9  ░░░░░░░░████░  Phase 4 (Report writing)
Ngày 10  ░░░░░░░░████░  Phase 4 (Report + GitHub)
Ngày 11  ░░░░░░░░████░  Phase 4 (Finalize report)
Ngày 12  ░░░░░░░░░░███  Phase 5 (Review + Submit)
Ngày 13  ░░░░░░░░░░░██  Phase 5 (Final submit + Buffer)
```

---

## Tổng hợp vai trò AI theo Phase

| Phase | Vai trò AI chính | Mức độ tự động |
|-------|-----------------|----------------|
| **Phase 0** | Project Scaffolder, Data Engineer | 🟢 90% tự động |
| **Phase 1** | Data Analyst, Calculator | 🟢 95% tự động — AI giải 10 câu, người verify |
| **Phase 2** | Code Generator, Viz Designer, Business Narrator, Insight Synthesizer | 🟡 70% tự động — AI sinh code + narrative, người chọn góc nhìn + review |
| **Phase 3** | ML Engineer, Feature Engineer, Hyperparameter Tuner | 🟡 75% tự động — AI build pipeline, người quyết định model strategy |
| **Phase 4** | Technical Writer, LaTeX Formatter, Proofreader | 🟡 60% tự động — AI viết draft, người review + polish |
| **Phase 5** | QA Engineer, Checklist Validator | 🟢 80% tự động — AI validate, người submit |

---

## Risk & Mitigation

| Risk | Impact | Mitigation | 🤖 AI giúp gì |
|------|--------|------------|---------------|
| Data leakage trong forecasting | Bị loại bài | Time-series CV, không dùng future features | AI **kiểm tra** mọi feature không dùng data sau cutoff date |
| EDA thiếu chiều sâu (chỉ Descriptive) | Mất 30+ điểm | Bắt buộc mỗi theme phải có Prescriptive | AI **review** mỗi theme đã cover đủ 4 cấp độ chưa |
| Report vượt 4 trang | Bị trừ điểm | Strict page budget per section | AI **đếm** pages, **cắt** nội dung thừa |
| Submission sai format | 0 điểm Phần 3 | Validate trước khi nộp | AI **so sánh** submission vs sample_submission structure |
| Không reproducible | Bị loại | Set seed everywhere, pin library versions | AI **audit** code cho reproducibility |
