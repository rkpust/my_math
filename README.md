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
