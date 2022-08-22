## functions

Reusable pieces of code

**lambda function**: nameless function

functions are objects

```python
def make_list(val, times):
  res = str(val) * times
  return result
```

**Blob class/function**: anti-pattern, class/function with too much functionality and too many lines in it 

**signiture**: name and parameter of a function

**argument**: literal/variable passed into function

**JSON**: Javscript Object Notation

**XML**: extensible markup language

```python
# unpacking values

def add(a, b, c):
  return a + b + c

mytup = 23, 45, 67
add(*mytup)
```

```python
# variadic functions

# passing in unnamed arguments
def filepath(dir, *files):
  print('dir:', dir, 'files:', files)
  
filepath('c:/stuff', 'f1.txt', 'f2.txt', 'f3.txt')
```



```python
# keyword parameters

def print_vat(**kwargs):
  print(kwargs)
  
print_vat(vatpc=15, gross=9.55, message='Summary')

argsdict = dict(vatpc=15, gross=9.55, message='Summary')
print_vat(**argsdict)
```



**lambda functions**:

- annonymous shorthand
- cannot contain branches + loops
- can contain conditional expressions
- cannot have a return statement or assigments
- last result of the function is the returned value

```python
compare = lambda a,b: -1 if a < b else (+1 if a > b else 0)

print("a > b", compare(42, 3))
```

- often used with map() and filter() built-ins

lambda as sort key

```python
countries.sort(key=lambda c: c[1])
```



## OOP

create object instances using **instantiation**

```python
from account import Account

some_account = Account(1000.00)
some_account.deposit(550.23)
some_account.deposite(100)
some_account.withdraw(50)
print(some_account.getbalance())

another = Account(0)

# static
print(Account.numCreated)
print("object another is class", another.__class__.__name__)
```

Check if object has an attribute:

```python
hasattr(x, '__str__')
```

Constructor:

```python
def __init__(self):
```

Destructor

```python
def __del__(self):
```

overload special methods:

```python
__add__				+
__sub__				-
__lt__				<
__gt__				>
```

Decorator

```python
# function that is extended with other functionality

@property
def description(self):
  return self._description

@description.setter
def description(self, description):
  self._description = description 
```

Class method

```python
# does not need instantiation to call

@classmethod
def get_count(cls):
  return Date._count
```

inheritance

```python
class DerivedClassName(base_classes):
  def __init__(self, args):
    base_class.__init__(self, arguments)
```

**Base/superclass**: parent class

**Derived/subclass**: child class

## Unit testing