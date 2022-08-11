**pair programming**: split between <strong>driver</strong> and <strong>navigator </strong>

## python

**python 2 vs python 3**: in python 2, it is single byte strings, whereas python 3 (aka 3000 or py3k) uses multibyte strings

**PEPs**: python enhancement proposal

- most well known one is PEP8 (rules about formatting)

underscore based variable naming is called **snake case**

Conventions:

- names beginning with private models/classes _ before name: _private_var
- names beginning with 2 underscores are mangled (don't want any interactions): __private_to_class
- names beginning and ending with 2 underscores are special: __magical_var__
- character _ represents result of previous command

double underscore = dunderscore (or dunder)

for a tuple, the brackets are not the thing that make them. the comma makes the tuple

- mytuple = 3, 4
- mytuple = (3, 4)

**sequence**: data type that remembers the order of elements

- Bytes, strings, types, lists, bytearrays

in python the following are treated as **False**:

​	0, None, empty string, empty tuple, empty list, empty dictionary, empty set

everything else is **True**

**is**: are variables the same in term of address

**in**: is value in iterable

**all(...)**: all items in collection is true (none 0)

**any(...)**: at least 1 item is true (1 is none 0)

**pass**: empty placeholder (doing nothing)



**enumerate(...)**: around a for loop iterable, can return object and index

- Enumerate(itr, 1) → starts at 1

**sys.exit(output message)** best way to exit program