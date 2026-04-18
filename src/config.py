"""
DATATHON 2026 — The Gridbreakers
Global configuration: paths, constants, random seed.
"""
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────
ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_RAW = ROOT_DIR / "data" / "raw"
DATA_PROCESSED = ROOT_DIR / "data" / "processed"
REPORTS_DIR = ROOT_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
SUBMISSIONS_DIR = ROOT_DIR / "submissions"
ANSWERS_DIR = ROOT_DIR / "answers"

# ── Raw CSV file paths ────────────────────────────────────
# Master tables
PRODUCTS_CSV = DATA_RAW / "products.csv"
CUSTOMERS_CSV = DATA_RAW / "customers.csv"
PROMOTIONS_CSV = DATA_RAW / "promotions.csv"
GEOGRAPHY_CSV = DATA_RAW / "geography.csv"

# Transaction tables
ORDERS_CSV = DATA_RAW / "orders.csv"
ORDER_ITEMS_CSV = DATA_RAW / "order_items.csv"
PAYMENTS_CSV = DATA_RAW / "payments.csv"
SHIPMENTS_CSV = DATA_RAW / "shipments.csv"
RETURNS_CSV = DATA_RAW / "returns.csv"
REVIEWS_CSV = DATA_RAW / "reviews.csv"

# Analytical tables
SALES_CSV = DATA_RAW / "sales.csv"
SAMPLE_SUBMISSION_CSV = DATA_RAW / "sample_submission.csv"

# Operational tables
INVENTORY_CSV = DATA_RAW / "inventory.csv"
WEB_TRAFFIC_CSV = DATA_RAW / "web_traffic.csv"

# ── Reproducibility ───────────────────────────────────────
SEED = 42

# ── Competition constants ─────────────────────────────────
TRAIN_START = "2012-07-04"
TRAIN_END = "2022-12-31"
TEST_START = "2023-01-01"
TEST_END = "2024-07-01"
TARGET_COL = "Revenue"
DATE_COL = "Date"
