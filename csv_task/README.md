# CSV Task - Data Generation & CSV Operations

## Quick Navigation

| Section | Description | Files |
|---------|-------------|-------|
| [**Synthetic Data Generation**](#without_dataset-directory) | Generate fake user data from scratch | `without_dataset/` - `data_class.py`, `constants.py`, `write_csv.py` |
| [**Merge Existing Datasets**](#csv-task--building-a-dataset-with-existing-datasets) | Combine multiple CSV sources | `with_dataset/` - `main.py`, `social_media.csv`, `HREmails.csv`, `foods.csv` |
| [**Performance Tips**](#performance-considerations) | Multiprocessing considerations | Multiprocessing trade-offs & optimization |
| [**Usage Examples**](#usage) | How to run both approaches | Commands & examples |

---

## Overview

This project demonstrates two approaches to creating and handling CSV datasets in Python:
1. **Synthetic data generation**: Create random user data from predefined lists
2. **Data merging**: Combine multiple existing CSV files into one

---

## Project Structure

### `without_dataset/` Directory

This folder contains the core implementation for generating synthetic datasets and managing CSV operations.

#### Core Files

**`data_class.py`**
- Implements the `Data` class, which generates synthetic user datasets
- Constructor parameters:
  - `number`: Number of records to generate
  - `null_probability`: Probability of null values (default: 0.2)
  - `invalid_probability`: Probability of invalid values (default: 0.15)
  - `seed`: Optional random seed for reproducible results
- Key methods:
  - `get_data()`: Generates and returns the complete dataset with header row
  - `get_data_multiprocessing()`: Alternative implementation using multiprocessing
- Generated fields:
  - `user_id`, `name`, `age`, `email`, `city`, `signup_date`, `monthly_income`

**`read_csv.py`**
- Reads and displays records from the generated CSV file
- Uses Python's built-in `csv.DictReader` for easy record iteration
- Useful for validating generated data

**`write_csv.py`**
- Writes the generated dataset to `users_raw.csv`
- Uses the `Data` class to generate records
- Implements CSV writing using `csv.writer`

**`constants.py`**
- Stores predefined lists of constants used for random data generation:
  - `FIRST_NAMES`: List of Indian first names
  - `LAST_NAMES`: List of Indian surnames
  - `DOMAINS`: Email domain names
  - `INDIAN_CITIES`: List of Indian cities for location generation

**`users_raw.csv`**
- Output file containing the generated synthetic user data
- Created when `write_csv.py` is executed

## Performance Considerations

### Multiprocessing Challenge

The `get_data_multiprocessing()` method was implemented to leverage multiple processes for faster data generation. However, it currently **slows down the task** rather than speeding it up. This happens because:

- The generator functions used within processes are **not CPU-bound**
- The overhead of creating processes exceeds the performance gains
- Inter-process communication adds latency

### Optimization Recommendations

To achieve real performance improvements with multiprocessing:

1. **Use Global Generator Functions**: Create a global function that generates a complete row in a single call, rather than using multiple generator functions
2. **Implement Chunking Strategy**: Process data in chunks and distribute chunks across processes
3. **Reduce Process Overhead**: Batch multiple rows per process to amortize the initialization cost
4. **Consider Thread-based Approach**: For I/O-bound operations, multiprocessing with `ThreadPoolExecutor` might be more efficient

## Usage

### Generate and Write Data

```bash
python write_csv.py
```

This will:
- Create a `Data` object with 10,000 records
- Generate synthetic user data
- Write all records to `users_raw.csv`

### Read Generated Data

```bash
python read_csv.py
```

This will:
- Open and read records from `users_raw.csv`
- Display each record in dictionary format

## Customization

To generate data with custom parameters:

```python
from data_class import Data

# Generate 5000 records with 10% null probability and 5% invalid probability
data_obj = Data(number=5000, null_probability=0.1, invalid_probability=0.05)
dataset = data_obj.get_data()
```

## Key Learnings

- **Modular Design**: Separation of data generation, reading, and writing concerns
- **Random Data Generation**: Using random selection from predefined lists
- **CSV Operations**: Reading and writing CSV files efficiently in Python
- **Multiprocessing Trade-offs**: Understanding when multiprocessing is beneficial vs. counterproductive
- **Data Validation**: Handling null and invalid values in generated datasets 


## CSV Task – Building a dataset with existing datasets

## Overview

This section documents a utility script that **merges multiple CSV files** into a single consolidated dataset called `users_raw.csv`.

The script reads aligned records from:

* `social_media.csv`
* `HREmails.csv`
* `foods.csv`

…and combines selected fields into a unified schema.

---

## Input Files

### `social_media.csv`

Contains basic user information:

* `UserID`
* `Name`
* `DOB`
* `City`

---

### `HREmails.csv`

Contains email-related information:

* `Email`
  *(Note: This file contains a UTF-8 BOM and is opened using `encoding="utf-8-sig"`)*

---

### `foods.csv`

Contains demographic and income information:

* `Age`
* `Monthly Income`

---

## Output File

### `users_raw.csv`

The merged output file generated by the script.

### Output Schema

```text
["user_id", "name", "age", "email", "city", "signup_date", "monthly_income"]
```

### Column Mapping

| Output Column  | Source File      | Source Field   |
| -------------- | ---------------- | -------------- |
| user_id        | social_media.csv | UserID         |
| name           | social_media.csv | Name           |
| age            | foods.csv        | Age            |
| email          | HREmails.csv     | Email          |
| city           | social_media.csv | City           |
| signup_date    | social_media.csv | DOB            |
| monthly_income | foods.csv        | Monthly Income |

---

## Script Behavior

The script performs the following steps:

1. Opens three input CSV files and one output CSV file in a single context manager.
2. Uses `csv.DictReader` to read rows as dictionaries.
3. Iterates over all three CSVs in parallel using `zip()`.
4. Extracts and remaps required fields into a new row structure.
5. Writes the transformed rows into `users_raw.csv`.
6. Stops after writing **10,000 rows**.

---

## Row Limit Handling

The script enforces a hard limit:

```python
OUTPUT_ROWS = 10000
```

Only the first 10,000 aligned rows from the three input files are written.

⚠️ **Important**
`zip()` stops when the shortest file ends.
To guarantee 10,000 rows, **all three input files must contain at least 10,000 records**.

---

## BOM Handling for Email File

The email CSV is opened with:

```python
open("HREmails.csv", "r", encoding="utf-8-sig")
```

This automatically strips the UTF-8 Byte Order Mark (BOM), allowing safe access to:

```python
line2["Email"]
```

Without this, the column name would appear as:

```text
"\ufeffEmail"
```

---

## Usage

### Generate the Merged Dataset

```bash
python main.py
```

This will:

* Read records from:

  * `social_media.csv`
  * `HREmails.csv`
  * `foods.csv`
* Merge aligned rows
* Write 10,000 records to `users_raw.csv`

---

## Key Learnings

* **CSV Merging**: Combining multiple CSV sources using `zip()`
* **Schema Normalization**: Remapping disparate fields into a unified format
* **BOM Handling**: Using `utf-8-sig` to handle UTF-8 BOM characters
* **Context Managers**: Managing multiple files safely in a single `with` block
* **Row Limiting**: Enforcing record count constraints for controlled dataset size


