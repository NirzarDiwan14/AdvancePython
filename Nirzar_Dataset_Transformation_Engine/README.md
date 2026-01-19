# Dataset Transformation Engine

This project implements a modular data transformation pipeline that loads raw transaction data, engineers features, encodes categorical variables, and exports an ML-ready dataset.

---

## 📦 Project Structure

```
<name>_project/
├── loader.py                # Step 1: Load + validate + clean data
├── feature_engineering.py  # Step 2 & 3: Time + aggregation features
├── encoder.py              # Step 4: Encoding logic
├── scaler.py               # (Optional) Scaling numeric features
├── pipeline.py             # Orchestrates everything end-to-end
├── features_dataset.csv    # Final ML-ready dataset (output)
├── README.md               # Project documentation
```

---

## 🧠 What This Pipeline Does

1. **Loads raw CSV data**
2. **Validates schema and datatypes**
3. **Handles missing values**
4. **Creates time-based features**
5. **Generates user-level aggregation features**
6. **Encodes categorical variables**
7. **Exports a clean ML-ready dataset**

---

## 📄 Input Data Requirements

Your input CSV should contain at least the following columns:

* `user_id`
* `order_id`
* `order_date`
* `order_amount`
* `city`
* `payment_mode`

> Column names must match exactly. Adjust the code if your dataset uses different names.

---

## ⚙️ Setup Instructions

1. Clone or download this project
2. Install required dependencies:

```bash
pip install pandas
```

3. Place your dataset file (e.g., `dataset.csv`) in the project directory

---

## 🚀 How to Run the Pipeline

From the project folder:

```bash
python pipeline.py
```

This will:

* Load the raw dataset
* Apply feature engineering
* Encode categorical features
* Save the final dataset as:

```
features_dataset.csv
```

---

## 🛠️ Pipeline Steps Explained

### Step 1 — Data Loader (`loader.py`)

* Loads the CSV using pandas
* Validates required columns
* Converts datatypes (dates and numeric fields)
* Handles missing values

---

### Step 2 — Time-Based Features (`feature_engineering.py`)

Creates:

* `order_month`
* `order_day`
* `order_weekday`
* `is_weekend`

---

### Step 3 — Aggregation Features (`feature_engineering.py`)

Generates per-user features:

* `total_orders`
* `total_spend`
* `avg_order_value`
* `max_order_value`
* `days_since_last_order`

---

### Step 4 — Encoding Engine (`encoder.py`)

* One-hot encoding for:

  * `city`
  * `payment_mode`

* Frequency encoding for:

  * `city`

---

### Step 6 — Export ML-Ready Dataset (`pipeline.py`)

* Orchestrates all steps
* Saves the final dataset to `features_dataset.csv`

---

## 📌 Notes

* The pipeline is modular and extensible
* Designed for real-world ML preprocessing workflows
* Frequency encoding is computed on the full dataset (for internship demo purposes)



## ✅ Final Output

After running the pipeline, you will get:

```
features_dataset.csv
```

Which is a clean, ML-ready dataset containing:

* Original numeric features
* Engineered time features
* User-level aggregation features
* Encoded categorical features
