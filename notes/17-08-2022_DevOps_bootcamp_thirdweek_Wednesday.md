zoom in

```bash 
cmd, shift, +
```

## Unit testing

testing is generally tiple A:

1. Arrange
2. Act
3. Assert

For 

```python
self.assertEqual(result, answer)
```

The first is <strong>test variable</strong> and the second is <strong>expected variable</strong>

__dir__ is __ls__ equivalent

the command to run unit tests using the unittest module:

```
python3 -m unittest calc_tests
```

testing the **output** in whitebox testing instead of the inner workings

**test driven development**: write/plan the tests first before creating the logic

normal syntax:

```python
class TestCalc(unittest.TestCase):
    """Test methods needed to start tests"""

    def test_add(self):
        # Triple A pattern:
        # 1. Arrange
        # 2. Act
        # 3. Assert

        result = calc.add(10, 5)
        self.assertEqual(result, 15)
```

compact syntax

```py
class TestCalc(unittest.TestCase):
    """Test methods needed to start tests"""

    def test_add(self):
        # Triple A pattern:
        # 1. Arrange
        # 2. Act, Assert

        self.assertEqual(calc.add(10, 5), 15)
```

if testing multiple assertions in a test, make them under one category (so it is easy to troubleshoot)

```python
def test_divide_by_0(self):
  self.assertRaises(ValueError, calc.divide, 10, 0)
  
def test_divide_by_0(self):
  with self.assertRaises(ValueError):
    calc.divide(10, 0)
```



## Flask

**pipenv**: 

```bash
pipenv shell
```

To have auto restart

```bash
export FLASK_ENV=development
```

