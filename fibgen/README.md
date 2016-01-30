#fibgen

###Description
simple python module to calculate fibonacci sequence to nth number. returns a list.

###Requirements
nose

###Installation

```
$ python setup.py install
```

###Usage

```python
from fibgen import fibgen
fibgen.gen(10)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

###Test
unit tests are currently in place.

to run:

```
$ nosetests
```

output should produce something like:

```
$ nosetests
```
.......
----------------------------------------------------------------------
Ran 7 tests in 0.003s

OK
```
