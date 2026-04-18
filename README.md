# 🏆 DATATHON 2026 — The Gridbreakers

> Team **gulugulu** | VinTelligence — VinUniversity Data Science & AI Club

Kaggle: [datathon-2026-round-1](https://www.kaggle.com/competitions/datathon-2026-round-1)

## Mô tả

Cuộc thi Khoa học Dữ liệu tại VinUniversity. Phân tích bộ dữ liệu mô phỏng hoạt
động của doanh nghiệp thời trang thương mại điện tử Việt Nam (2012–2022).

**3 phần thi**: MCQ (20đ) · EDA (60đ) · Sales Forecasting (20đ)

## Cấu trúc thư mục

```
├── data/
│   ├── raw/              ← 15 CSV gốc từ Kaggle
│   └── processed/        ← Features đã xử lý
├── notebooks/
│   ├── baseline_kaggle.ipynb
│   ├── 00_data_loading.ipynb
│   ├── 01_mcq_answers.ipynb
│   ├── 02_eda_*.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   ├── 03_ensemble.ipynb
│   └── 03_explainability.ipynb
├── src/
│   ├── config.py         ← Paths, constants, seed
│   ├── data_loader.py    ← Data loading utilities
│   ├── features.py       ← Feature engineering
│   ├── models.py         ← Model training
│   └── ensemble.py       ← Ensemble logic
├── reports/
│   ├── figures/          ← Exported charts
│   ├── report.tex        ← NeurIPS LaTeX report
│   └── report.pdf
├── submissions/
│   └── submission.csv    ← Kaggle submission
├── answers/
│   └── mcq_answers.json  ← Đáp án trắc nghiệm
├── docs/                 ← Tài liệu cuộc thi
├── requirements.txt
└── README.md
```

## Reproduce kết quả

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Download data từ Kaggle
kaggle competitions download -c datathon-2026-round-1 -p data/raw/
unzip data/raw/datathon-2026-round-1.zip -d data/raw/

# Chạy notebooks theo thứ tự 00 → 01 → 02 → 03
```

## Seed

Tất cả random operations sử dụng `SEED = 42`.
