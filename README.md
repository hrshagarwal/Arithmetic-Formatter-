# Arithmetic-Formatter-

A simple Python script that takes a list of arithmetic problems and formats them vertically and side-by-side, with optional result display.

## ✅ Features

- Supports addition and subtraction
- Input validation:
  - Max 5 problems
  - Numbers only
  - Max 4 digits per number
  - Operators: only '+' or '-'
- Optional answer output
- Clean and readable formatting

## 🧠 Example

```python
from arithmetic_arranger import arithmetic_arranger

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))

Output 
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
  730      3799      88      172

