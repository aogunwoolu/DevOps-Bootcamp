## Regular Expressions

- template describing text of interest
- meta language of special characters
- supports extended regex

### regex in python

- import re
- can precompile regex
- Multi-line patterns are supported
- Substitution is supported
- regex are not **always** the answer, functions have lower overhead

### meta characters

**.** : match any single character 

**[a-zA-Z]** : match any char in the [...] set

**[^a-zA-Z]** : match any character _**not**_ in the [...] set

**^** : match begining of text

**$** : match end of text

x**?** : mach 0 or 1 occurances of x

x**+** : match 1 or more occurances of x

x**\*** : match 0 or more occurances of x

x**{m,n}** : match between <strong>m</strong> or <strong>n</strong> x's

abc : match _abc_

abc**|**xyz : match _abc_ or _xyz_

### regex objects

return of regex is match object or **none** if nothing is found

- Remember: in python **none** is **False**

**sub** : returns changed string

- re.sub(pattern, replacement, string[, count, flags])

**subn** : returns changed string and how many times it has replaced

## class shortcuts

**\B** : looking for non word boundaries

**\b**: looking for word boundaries

**\w**: word,  [a-zA-Z0-9_]

**\d**: digit [0-9]

**\s**: whitespace, [ \t\n\r\f]

**\W:** word,  [\^a-zA-Z0-9_]

**\D**: digit [\^0-9]

**\S**: whitespace, [\^ \t\n\r\f]

## flags

![Screenshot 2022-08-15 at 11.51.35 am](/Users/qol01/Documents/sky_devops_bootcamp/screenshots/Screenshot 2022-08-15 at 11.51.35 am.png)

## back referencing

```python
string_year = 'copyright 1998-2006'
print(re.sub(r'(19|20)[0-9]{2}-(19|20)[0-9]{2}', r'\1-' + currentyear))
```

with grouping 

## Reading and writing from files

r = open for read

w = write, create, overwrite

a = append

x = create file (fails if exists)

r+ = exostomg file read/write

w+ = create and truncate

**slurping**: opening and reading the whole file as string

**splitlines()**: splits input into lines of the file

**readlines()**: loads all file in memory to iterate

**open():** treats line by line

```python
output = open('myfile','w')
append = open('logfile', 'a')

num = output.write('hello\n')
output.writeline(list)
```



binary mode

```python
for line in open('lines.txt', 'rb'):
	print(line.decode(), end='')
  
fo = open('out.dat', 'wb')
fo.write('hello'.encode())
```



## standard streams

**standard input**, **standard output**, **standard error**

Errors and output are being written to the same place (the terminal window)

**rstrip()** removing whitespace



**using print to write to file**:

```python
output = open('myfile', 'w')
print('hello', file=output)
print('oops, error', file.sys.stderr)

# to flush the buffer
output.flush()

"""
tail: the end of the file. 

big log files you may only care about the end
"""
```

btye file **.tell()** says what position in the file the pointer is

```python
fh = open('country.txt', 'rb')

index = {}

while True:
  line = fh.readline()
  if not line: break
  print(line)
  fields = line.decode().splie(',')
  index[fields[0]] = fh.tell() - len(line)
  
key = input('enter a country')
fh.seek(index[key])
print(fh.readline().decode(), end='')
```

## pickle persistence

pickling converts python objects into stream of bytes

usually written to file or across. network

```python
import pickle

caps = {'Australia':'Canberra', 'Eire':'Dublin', 'UK':'London', 'US':'Washington'}

# pickling only works with binary files - b
outp = open('capitals.p', 'wb')
pickle.dump(caps, outp)
outp.close
```

and to read the pickled file

```python
import pickle

# pickling only works with binary files - b
inp = open('capitals.p', 'rb')
caps = pickle.load(inp)
inp.close()
```

other languages call this serialisation and deserialisation

**shelve**: a keyed pickle dumped to a database

looks like an ordinary dictionary

Methods: open(), sync(), close()

```python
import shelve

db = shelve.open('capitals')
db['UK'] = 'London'
...
db.close()
```

and to retrieve

```python
db = shelve.open('capitals')
print(db['UK'])
db.close()
```

 ## compression

gzip method for opening compressed files

```python
import pickle
import gzip

f_outp = gzip.open('capitals.pgz', 'wb')
pickle.dump(caps, f_outp)
f_outp.close()
```

and to retrieve

```python
import pickle 
import gzip

f_inp = gzip.open('capitals.pgz', 'rb')
caps = pickle.load(f_inp)
f_inp.close()
```

