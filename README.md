# Merge Customer Logs

This project demonstrates a basic merging technique (inspired by merge sort) to combine two company branches’ customer logs without duplicates. The logs are timestamps from two sources and are merged in order without using Python's built-in `sort()` function.

## 📌 Problem Statement

Given customer logs from Branch A and Branch B (in timestamp order), merge them into a single log while:
- Preserving timestamp order.
- Removing duplicate timestamps.

## 🧠 Key Concept

This approach manually performs a **merge** operation similar to the merge step in Merge Sort. It avoids duplicate entries and assumes each branch's logs are already sorted.

## 📂 Files

- `merge_customer_logs.py`: Main Python script containing the merge logic.
- `.gitignore`: Prevents `.pyc` and other unnecessary files from being committed.

## 🚀 How to Run

```bash
python merge_customer_logs.py
```

## 🔍 Sample Output

```
Branch A Logs:[1010, 1030, 1100, 1500, 1600]
Branch_B_Logs:[1000, 1030, 1500, 1130, 1700]

After Merge:
[1000, 1010, 1030, 1100, 1130, 1500, 1600, 1700]
```

## 📘 Topics Covered

- Manual merge logic
- De-duplication
- Merge sort inspiration

## 📜 License

This project is licensed under the MIT License.
