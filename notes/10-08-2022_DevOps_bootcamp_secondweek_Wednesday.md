## Strings

strings are **immutable**, so if assigning in a for loop this makes a lot of unused variables. instead of string1 += string2, string1.join(string2) is preferred 

**repr**: gets reference (representation) on string

**count**: returns number of occurances in string

**endswith**: returns boolean,

**isalnum**: returns boolean, are all characters alphanumerical

**isalpha**: returns boolean, are all characters alphabetical 

**isdigit**: returns boolean, are all characters digits

**islower**: returns boolean, is string lower case

**isspace**: returns boolean, is string whitespace (tab, space etc.)

**isupper**: returns boolean, is string upper case

**startswith**: returns boolean,



**capitalize**: 

**upper**: 

**ljust**: fills specific length string with spaces on the right

**rjust**: fills specific length string with spaces on the left

**zfill**: fills specific length string with 0s

### string formatting

<value>:<zero fill><total width>.<number of items after decimal><floating point>

value:06.2f 

## unpacking iterables:

this will give you an error:

```python
My tuple = 'eggs', 'bacon', 'grits', 'sausage'
x, y, z = mytuple

# !ERROR
```

this will make the last unpacked variable a list (always)

```python
My tuple = 'eggs', 'bacon', 'grits', 'sausage'
x, y, z* = mytuple

# x = 'eggs', y = 'bacon', z = ['grits', 'sausage']
```

adding items to a list

```python
cheese[:0] = ['brie', 'cheddar']
cheese += ['Oke', 'Devon Blue']
cheese.extend(['Oke', 'Devon Blue'])
cheese.append('Oke')
cheese.insert(2, 'Cornish Brie')
cheese[2:2] = ['Cornish Brie']
```

deleting from list

```python
cheese.pop(1)
cheese.pop() # pops last item every time
del cheese[1:3]
```

sorting

```python
cheese = ['Cornish Yarg', 'Oke', 'Edam', 'Stilton']
cheese.sort(key=len) # sorts based on string length
cheese.sort(reverse=True) # sorts alphabetically in reverse
cheese.sort() # sorts in alphabetical order
print(cheese)

nums = ['1001', '34', '3', '11', '24']
sortednums = sorted(nums, key=int) # sorts nums, comparing them by converting to int
print(sortednums)
```

**sets**

set is _mutatable_, frozenset is _immutable_

set items are unqiue

```python
s1 = {5, 6, 7, 8, 5} # {5, 6, 7, 8}
s2 = frozenset([9, 10, 11, 12, 9]) # {9, 10, 11, 12}

s1.add(9) # {5, 6, 7, 8, 9}
s2.remove(10) # {9, 11, 12}
```

exploiting sets

```python
cheese = ['Cornish Yarg', 'Stilton', 'Oke', 'Edam', 'Stilton']
cheese = list(set(cheese)) # removes duplicates from lists

cheese = ['Cornish Yarg', 'Stilton', 'Oke', 'Edam', 'Stilton']
cheese = list(set(cheese) - {'Stilton', 'Oke', 'Brie'}) #difference
```

**set operators**

& - intersection - each item in both sets

| - union - each item in both sets

~ - difference

**dictionaries**

creating dictioaries

```python
mydictone = {1: 'one', 2: 'two'}
mydicttwo = dict(1 = 'one', 2 = 'two')
```

