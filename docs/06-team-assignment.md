# Phân chia Công việc — 4 Thành viên (Overlap Strategy v2)

## Thay đổi so với v1
- **2 người chuyên Forecasting** (ML + DL) thay vì 1
- Không giới hạn phương pháp: ML truyền thống (LightGBM, XGBoost, CatBoost) + Deep Learning (LSTM, N-BEATS, Transformer, TFT)
- EDA được dồn cho 2 người còn lại, nhưng ML team vẫn overlap review

---

## Nguyên tắc phân chia

- **Forecasting có 2 người**: 1 chuyên ML tabular, 1 chuyên DL time series → ensemble cả hai hướng
- **EDA có 2 người**: 1 chuyên phân tích số liệu, 1 chuyên visualization + storytelling
- **Mỗi output có ít nhất 2 người sign-off**
- **Cross-pollination**: ML team cung cấp insights cho EDA (feature importance → business insight), EDA team cung cấp domain knowledge cho ML (seasonality, promo patterns)

---

## Tổng quan phân công

| Thành viên | Vai trò chính | Vùng chính | Vùng overlap |
|------------|---------------|------------|-------------|
| **A — EDA Analyst** | Phân tích dữ liệu + MCQ | EDA Theme 1, 2, 3 · MCQ Q1–5 · Report Section 2 | Review features của B · Verify model numbers |
| **B — ML Engineer** | Forecasting (ML tabular) | Feature Engineering · LightGBM/XGBoost/CatBoost · Ensemble · SHAP | EDA Theme 1 Predictive · MCQ Q2, Q7 |
| **C — DL Engineer** | Forecasting (Deep Learning) | LSTM/N-BEATS/TFT · Advanced features · Stacking với B | Leakage check cho B · MCQ Q7 · Review EDA numbers |
| **D — Viz & Integrator** | EDA Storytelling + Report + QA | EDA Theme 4, 5 · MCQ Q6–10 · Report · GitHub · Submission | Review toàn bộ EDA · Review SHAP plots · Final QA |

---

## Chi tiết phân công theo Phase

### PHASE 0: Setup & Data Loading (Ngày 1, ~2 giờ)

| Công việc | Lead 🔴 | Support 🔵 |
|-----------|---------|------------|
| Project structure (folders, requirements.txt) | D | B |
| Load 15 CSV + data quality check | A | D |
| Config (seed=42, paths, constants) | B | C |
| Data dictionary / summary stats | A | D |
| GPU/DL environment setup (PyTorch/TF) | C | B |

**Overlap**: A + D cùng kiểm tra data quality. B + C cùng setup environment đảm bảo cả ML và DL đều chạy được.

---

### PHASE 1: Trắc nghiệm MCQ (Ngày 1, ~2 giờ)

| Câu | Lead 🔴 | Verify 🔵 | Lý do overlap |
|-----|---------|-----------|---------------|
| Q1 (inter-order gap) | A | D | A thạo pandas, D cross-check |
| Q2 (gross margin by segment) | A | B | B cần hiểu margin cho features |
| Q3 (return reason Streetwear) | A | D | D sẽ phân tích returns trong EDA Theme 4 |
| Q4 (bounce rate by source) | A | D | D phụ trách EDA Theme 5 |
| Q5 (promo usage rate) | A | D | D phụ trách EDA Theme 4 |
| Q6 (orders by age_group) | D | A | Cross-verify |
| Q7 (revenue by region) | D | B, C | B + C cần hiểu revenue distribution cho forecasting |
| Q8 (cancelled order payment) | D | A | Cross-verify |
| Q9 (return rate by size) | D | A | Cross-verify |
| Q10 (payment by installments) | D | A | Cross-verify |

**Mỗi câu 2 người tính độc lập → so kết quả → chốt đáp án.**

---

### PHASE 2: EDA & Data Storytelling (Ngày 2–6)

#### Phân chia Theme

| Theme | Lead 🔴 | Support 🔵 | Chi tiết overlap |
|-------|---------|------------|-----------------|
| **Theme 1: Revenue & Profitability** | A | B | A: Descriptive + Diagnostic. B bổ sung Predictive (trend decomposition, forecast fan chart từ model) |
| **Theme 2: Customer Behavior** | A | D | A: demographics + RFM + CLV. D: polish visualization + storytelling |
| **Theme 3: Product & Inventory** | A | C | A: product analysis + stockout impact. C: verify inventory numbers khớp với features |
| **Theme 4: Promotion Effectiveness** | D | B | D: promo ROI analysis. B: verify promo features khớp giữa EDA và model |
| **Theme 5: Digital & Operations** | D | C | D: traffic + delivery analysis. C: verify web_traffic features consistency |

#### Ma trận Overlap

```
              Theme 1    Theme 2    Theme 3    Theme 4    Theme 5
A (EDA)       🔴 Lead    🔴 Lead    🔴 Lead    ·          ·
B (ML)        🔵 Predict ·          ·          🔵 Verify  ·
C (DL)        ·          ·          🔵 Verify  ·          🔵 Verify
D (Viz+QA)    ·          🔵 Viz     ·          🔴 Lead    🔴 Lead
```

#### Cross-pollination EDA ↔ Forecasting

| Từ | Đến | Nội dung |
|----|-----|---------|
| A → B, C | Feature ideas | A phát hiện seasonality patterns, promo impact → B, C tạo features tương ứng |
| B → A | Predictive insights | B cung cấp feature importance → A dùng cho EDA Theme 1 Predictive + Prescriptive |
| C → A | Trend analysis | C cung cấp DL trend predictions → A dùng cho forecast fan charts trong EDA |
| B, C → D | Model results | B, C cung cấp SHAP plots → D đưa vào report |

---

### PHASE 3: Sales Forecasting (Ngày 2–8, song song EDA)

Đây là phase chính được tăng cường với 2 người. B và C chạy **2 track song song**, cuối cùng ensemble lại.

#### Track phân chia

```
┌─────────────────────────────────────────────────────────────────┐
│                    DUAL-TRACK FORECASTING                        │
│                                                                  │
│  TRACK B (ML Tabular)          TRACK C (Deep Learning)          │
│  ┌──────────────────┐          ┌──────────────────┐             │
│  │ Feature Eng.     │          │ Sequence Prep    │             │
│  │ (50-100 features)│          │ (windowed data)  │             │
│  └────────┬─────────┘          └────────┬─────────┘             │
│           ▼                             ▼                        │
│  ┌──────────────────┐          ┌──────────────────┐             │
│  │ LightGBM         │          │ LSTM / BiLSTM    │             │
│  │ XGBoost          │          │ N-BEATS          │             │
│  │ CatBoost         │          │ TFT (Temporal    │             │
│  │ Prophet          │          │   Fusion Trans.) │             │
│  │ SARIMAX          │          │ DeepAR           │             │
│  └────────┬─────────┘          └────────┬─────────┘             │
│           ▼                             ▼                        │
│  ┌──────────────────────────────────────────────────┐           │
│  │           ENSEMBLE (B + C cùng làm)              │           │
│  │  Weighted Average · Stacking · Blending          │           │
│  │  ML predictions + DL predictions → Final         │           │
│  └──────────────────────────────────────────────────┘           │
└─────────────────────────────────────────────────────────────────┘
```

#### Step 3.1: Feature Engineering

| Công việc | Lead 🔴 | Support 🔵 |
|-----------|---------|------------|
| **Calendar features** (day_of_week, month, quarter, holidays, Tet) | B | C |
| **Lag features** (lag 1,7,14,28,30,90,365 + rolling stats) | B | C |
| **Fourier seasonality** (sin/cos weekly, monthly, yearly) | B | C |
| **Promotion features** (active promos, avg discount, promo type) | B | A |
| **Web traffic features** (sessions, visitors, conversion — aggregated) | B | A |
| **Inventory features** (stock, stockout_days, fill_rate — monthly→daily) | B | A |
| **Order-derived features** (daily order count, AOV, category mix) | B | A |
| **Sequence/window preparation** cho DL | C | B |
| **Embedding features** (category, segment, day_of_week encodings) | C | B |
| **Leakage audit** — independent check | C | A |

**Overlap quan trọng**:
- A cung cấp domain knowledge từ EDA → B, C tạo features chính xác hơn
- C kiểm tra leakage độc lập (không tự tạo tabular features nên không bị bias)
- B và C chia sẻ base features, mỗi người transform khác nhau cho model type

#### Step 3.2: Model Training — Track B (ML Tabular)

| Model | Người | Ghi chú |
|-------|-------|---------|
| **LightGBM** | B 🔴 | Strong baseline, Optuna tuning |
| **XGBoost** | B 🔴 | So sánh với LightGBM |
| **CatBoost** | B 🔴 | Leverage categorical features |
| **Prophet** | B 🔴 | Custom seasonalities (Tet, promo periods) |
| **SARIMAX** | B 🔴 | Classical time series baseline |
| **Ridge/ElasticNet** | B 🔴 | Linear baseline + meta-learner cho stacking |

**C review**: C kiểm tra CV strategy của B, verify không random split.

#### Step 3.3: Model Training — Track C (Deep Learning)

| Model | Người | Ghi chú |
|-------|-------|---------|
| **LSTM / BiLSTM** | C 🔴 | Sequence model, window size tuning |
| **N-BEATS** | C 🔴 | Neural basis expansion, interpretable mode |
| **Temporal Fusion Transformer (TFT)** | C 🔴 | Attention-based, handles multiple inputs |
| **DeepAR** | C 🔴 | Probabilistic forecasting |
| **WaveNet / TCN** | C 🔴 | Dilated causal convolutions (nếu có thời gian) |

**B review**: B kiểm tra data pipeline của C, verify train/val split đúng temporal order.

#### Step 3.4: Validation Strategy (B + C cùng thống nhất)

| Validation | Lead 🔴 | Support 🔵 |
|------------|---------|------------|
| Expanding window CV (5 folds) | B | C |
| Holdout 2022 | B, C | cùng dùng |
| Metrics tracking (MAE, RMSE, R²) | B | C |
| Overfitting monitoring | B, C | cross-check |

**Quy tắc bắt buộc**: B và C dùng **cùng validation splits** → so sánh công bằng → chọn models tốt nhất cho ensemble.

#### Step 3.5: Ensemble (B + C cùng làm)

| Phương pháp | Lead 🔴 | Support 🔵 |
|-------------|---------|------------|
| **Weighted average** (ML models) | B | C |
| **Weighted average** (DL models) | C | B |
| **Cross-track ensemble** (ML + DL) | B + C | D (validate format) |
| **Stacking** (meta-learner trên OOF predictions) | B | C |
| **Blending** (holdout-based weights) | C | B |
| **Post-processing** (clip negatives, smooth outliers) | B | C |

**Quy trình ensemble**:
1. B ensemble top ML models → ML_pred
2. C ensemble top DL models → DL_pred
3. B + C cùng tìm optimal weight: `final = w × ML_pred + (1-w) × DL_pred`
4. So sánh: pure ML vs pure DL vs hybrid → chọn best
5. D validate submission format

#### Step 3.6: Explainability (cho báo cáo — 8 điểm)

| Phân tích | Lead 🔴 | Support 🔵 |
|-----------|---------|------------|
| SHAP values (LightGBM/XGBoost) | B | D |
| Feature importance bar chart | B | D |
| Partial Dependence Plots | B | A |
| Attention weights visualization (TFT) | C | D |
| Business interpretation | B + C | A |

**Overlap**: D review tất cả plots cho report quality. A verify business interpretation hợp lý.

---

### PHASE 4: Report & Submission (Ngày 9–11)

| Section báo cáo | Lead 🔴 | Support 🔵 |
|-----------------|---------|------------|
| **1. Introduction** (~0.3 trang) | D | A |
| **2. EDA & Insights** (~1.5 trang) | A | D |
| **3. Forecasting Pipeline** (~1.2 trang) | B | C, D |
| **4. DL Approach & Ensemble** (~0.3 trang) | C | B |
| **5. Model Explainability** (~0.5 trang) | B | C, D |
| **LaTeX formatting toàn bộ** | D | — |
| **Figure curation (chọn + resize)** | D | A, C |
| **GitHub README + repo structure** | D | B |

**Overlap**:
- Section 3 + 4: B viết ML pipeline, C viết DL pipeline → D merge + format thành 1 narrative liền mạch
- A verify mọi con số trong report khớp với EDA notebooks
- D đảm bảo tổng ≤ 4 trang

---

### PHASE 5: Final Review & Submit (Ngày 12–13)

| Công việc | Lead 🔴 | Support 🔵 |
|-----------|---------|------------|
| Validate submission.csv format | D | B, C |
| Re-run ML pipeline từ đầu | B | D |
| Re-run DL pipeline từ đầu | C | D |
| Verify ensemble reproducibility | B + C | D |
| Proofread report | D | A |
| MCQ final answers consensus | A | D |
| Submit Kaggle | D | B |
| Nộp form chính thức | D | tất cả |

**Full-team review**: Ngày 12 cả 4 người cùng ngồi review toàn bộ deliverables.

---

## Timeline theo người (13 ngày)

```
         Ngày 1      Ngày 2-3     Ngày 4-6     Ngày 7-8     Ngày 9-11    Ngày 12-13
         ──────      ────────     ────────     ────────     ─────────    ──────────
A        Setup       EDA T1,T2    EDA T3       Review       Report       MCQ final
(EDA)    MCQ Q1-5    ──────→      Polish T1-3  Features     Sec 2        Report review
                                               → B,C        Verify #s    

B        Setup       Features     Models ML    Ensemble     Report       Re-run ML
(ML)     Config      ──────→      LGB/XGB/CB   ML+DL        Sec 3,5      Verify
         MCQ Q2,7    Prophet      Optuna       combine      SHAP         Submit

C        GPU setup   Features     Models DL    Ensemble     Report       Re-run DL
(DL)     ──────→     Sequence     LSTM/NBEATS  ML+DL        Sec 4        Verify
                     prep         TFT          combine      Attn viz     

D        Setup       MCQ Q6-10   EDA T4,T5    Review       Report       FULL QA
(Viz+QA) Structure   ──────→     ──────→      Reproduce    Format       Submit
                                              Submission   GitHub       Form
```

---

## Ma trận Overlap tổng hợp

```
              Phase 0   Phase 1    Phase 2         Phase 3           Phase 4    Phase 5
              Setup     MCQ        EDA             Forecasting       Report     Review
──────────────────────────────────────────────────────────────────────────────────────────
A (EDA)       🔵 Data   🔴 Q1-5    🔴 T1,T2,T3    🔵 Feature ideas  🔴 Sec 2   🔵 MCQ
              quality              🔵→B,C insights  🔵 Leakage help   🔵 Verify  Report

B (ML)        🔵 Config 🔵 Q2,Q7   🔵 T1 Predict  🔴 Features       🔴 Sec 3,5 🔴 Re-run
                                   🔵 T4 Verify    🔴 ML models      🔵 Sec 4   ML pipe
                                                   🔴 Ensemble                  

C (DL)        🔵 GPU    🔵 Q7      🔵 T3 Verify   🔴 DL models      🔴 Sec 4   🔴 Re-run
              setup                🔵 T5 Verify    🔴 Ensemble       🔵 Sec 5   DL pipe
                                                   🔵 Leakage check             

D (Viz+QA)    🔴 Struct 🔴 Q6-10   🔴 T4,T5       🔵 Reproduce      🔴 Format  🔴 FULL
                                   🔵 Review all   🔵 Submission      🔴 GitHub  QA+Submit
```

---

## Điểm mạnh của cách chia này

| Lợi ích | Chi tiết |
|---------|---------|
| **Forecasting mạnh hơn** | 2 track ML + DL → ensemble đa dạng hơn → score Kaggle cao hơn |
| **Không bỏ sót model type** | B cover tabular (LightGBM, XGBoost), C cover sequence (LSTM, TFT) → best of both worlds |
| **Leakage double-check** | C kiểm tra features của B, B kiểm tra pipeline của C |
| **EDA vẫn đủ sâu** | A chuyên phân tích 3 themes chính, D bổ sung 2 themes + polish storytelling |
| **Report coherent** | D là single point of integration → narrative liền mạch |
| **Reproducibility** | B re-run ML, C re-run DL, D verify cả hai → triple check |

---

## Quy tắc làm việc

### 1. Shared validation splits
B và C **bắt buộc** dùng cùng train/val/test splits → so sánh công bằng khi ensemble.

### 2. Feature sharing
B tạo tabular features → C có thể dùng subset làm exogenous variables cho DL models.
C tạo embeddings → B có thể dùng làm features cho tree models.

### 3. Daily sync (15 phút)
- Sáng: ai làm gì hôm nay
- Tối: kết quả, blockers, cần review gì
- B + C sync riêng về model performance → quyết định ensemble strategy

### 4. Ensemble decision
- Ngày 7: B + C cùng so sánh tất cả models trên holdout 2022
- Chọn top 3-5 models (mix ML + DL) cho final ensemble
- Nếu DL không cải thiện → fallback pure ML ensemble (không lãng phí)

### 5. Conflict resolution
- Kết quả khác nhau → cả 2 debug → chọn đúng
- Không đồng thuận → D quyết định cuối cùng
