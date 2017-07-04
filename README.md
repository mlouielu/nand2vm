[![Build Status](https://travis-ci.org/mlouielu/nand2vm.svg?branch=master)](https://travis-ci.org/mlouielu/nand2vm)
[![Coverage Status](https://coveralls.io/repos/github/mlouielu/nand2vm/badge.svg?branch=master)](https://coveralls.io/github/mlouielu/nand2vm?branch=master)

![nand2vm logo](https://raw.githubusercontent.com/mlouielu/nand2vm/master/logo/nand2vm.png)

nand2vm - pure Python implement nand2tetris
-------------------------------------------

The goal of this project is to create a Python version of nand2tetris,
nand2vm include the full test suite of nand2tetris, and assembler with python version.

Fundamental Elements
--------------------

### BitArray

BitArray is used when manipulate bit data, using BitArray API,
we can quickly create a small endian bit array:

```python
>>> import nand2vm
# Init from list using big endian
>>> b = nand2vm.BitArray([True, True, False, True])
>>> b
1101
>>> b[0]
True
>>> b[1]    # Internal using small endian
False
>>> b.data
[True, False, True, True]

# Init from integer, default using 16 bits
>>> b = nand2vm.BitArray(-1)
>>> b        # 16 bits 2's complement
1111111111111111

# Init from string
>>> b = nand2vm.BitArray('1101')
>>> b
1101
```

### Nand gate

The only gate using python operator to construct

```python
>>> def Nand(a: bool, b: bool) -> bool:
...     return not (a and b)

>>> nand2vm.Nand(True, True)
False
>>> nand2vm.Nand(True, False)
True
>>>
```

