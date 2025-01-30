# my_math
**my_math** is a simple Python package designed to provide various mathematical operations and utilities. It offers basic arithmetic, comparison, and bitwise operations, making it easy to perform essential calculations.
<br/>

| | |
| --- | --- |
| Testing | [![CI - Test](https://github.com/pandas-dev/pandas/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/rkpust/my_math/blob/master/test.py)
| Package | [![v0.1](https://img.shields.io/badge/v-0.1-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](https://github.com/rkpust/my_math)
| Meta | [![Powered by rkpust](https://img.shields.io/badge/powered%20by-rkpust-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](https://sites.google.com/view/rkpust) |


## Features
  - Basic arithmetic operations: addition, subtraction, multiplication, division etc.
  - Bitwise Operations: AND, OR, NOT, XOR etc.
  - Comparison Operations: equal, less than, greater than etc.
  - More utilities to be added soon!

## Installations
To install the my_math package, you must be installed Python. Python Version >= 3.0 (Recommended)

### Using Python, Git
You can install the my_math package directly from GitHub using pip (git must be installed):
  ```bash
  pip install git+https://github.com/rkpust/my_math
  ```

### Using Python
First, you need to download this repository as a .zip, then extract it. Now open CLI and navigate to the setup.py file path. Then run two commands one after the other.

You can install the my_math package by following the command:

  **i.**
  ```bash
  python setup.py sdist bdist_wheel
  ```
After executing the above command, you will see three folders build, dist, my_math.egg-info. You will also see my_math-0.1.tar.gz, my_math-0.1-py3-none-any.whl in the dist folder.

  **ii.**
  ```bash
  pip install dist\my_math-0.1.tar.gz
  ```
  or 

  ```bash
  pip install dist\my_math-0.1-py3-none-any.whl
  ```

### Checking Installation
You can check whether the **my_math** package is installed correctly by using the following command.
 ```bash
  pip show my_math
  ```
  or 

  ```bash
  pip list | findstr my_math
  ```

You will get output like below:
<pre>
Name: my_math
Version: 0.1
Summary: A simple python package for math
Home-page: https://github.com/rkpust/my_math
Author: Md. Rezaul Karim
Author-email: rezaul.cse.pust17@gmail.com
License: MIT
Location: C:\Users\hp\AppData\Local\Programs\Python\Python311\Lib\site-packages
Requires:
Required-by:
</pre>
<hr>
<pre>my_math                0.1</pre>

*Congratulations!* You have successfully installed the **my_math** package.

## Usage With Examples
Here, some of usage are given below:
### Constant
```python
from my_math import mm

#pi
print(mm.PI) # 3.141592653589793
```

### Arithmetic
```python
from my_math import mm

#addition
print(mm.add(1, 5, -4, 8)) # 10

#subtraction
print(mm.sub(5, -2)) # 7

#multiplication
print(mm.mul(1, 5, 0, 8)) # 0

#division
print(mm.div(5, 2)) # 2.5

#modulus
print(mm.mod(20, 3)) # 2

#floor division
print(mm.flr_div(20, 3)) # 6

#exponentiation
print(mm.exp(2, 5)) # 32
```

### Comparison
```python
from my_math import mm

#equal
print(mm.eq(0, 0)) # True

#not equal
print(mm.ne(2, 5)) # True

#greater than
print(mm.gt(-1, 0)) # False

#less than
print(mm.lt(-3, -3)) # False

#greater than or equal to
print(mm.ge(12, 5)) # True

#less than or equal to
print(mm.le(12, 5)) # False
```

### Bitwise
```python
from my_math import mm

#and
print(mm.band(6, 3)) # 2

#or
print(mm.bor(1, 1)) # 1

#xor
print(mm.bxor(12, 5)) # 9

#not
print(mm.bnot(3)) # -4

#zero fill left shift
print(mm.bls(6, 3)) # 48

#signed right shift
print(mm.brs(6, 3)) # 0
```

## Contributing
*Contributions are welcome!* If you'd like to improve or add new features to the **my_math** package, please fork the repository and submit a pull request. Be sure to include tests for new features, and ensure the code adheres to the project’s style.

## License
This project is licensed under the **MIT License** – see the LICENSE file for details.

## Author
**Md. Rezaul Karim**
<br>
GitHub: [@rkpust](https://github.com/rkpust)
<br>
Portfolio: [https://sites.google.com/view/rkpust](https://sites.google.com/view/rkpust)
