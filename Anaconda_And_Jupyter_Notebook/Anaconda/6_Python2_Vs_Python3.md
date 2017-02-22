#Why Should Use Python 3 Over Python 2

- Jupyter is switching to Python 3 only
- Python 2.7 is being retired
- Python 3.6 has great features such as formatted strings

At this point, there are enough new features in Python 3 that it doesn't make much sense to stick with Python 2 unless you're working with old code. All new Python code should be written for version 3.

###The main breakage between Python 2 and 3

For the most part, Python 2 code will work with Python 3. Of course, most new features introduced with Python 3 versions won't be backwards compatible. The place where your Python 2 code will fail most often is the print statement.

For most of Python's history including Python 2, printing was done like so:

```
print "Hello", "world!"
> Hello world!
```

This was changed in Python 3 to a function.

```
print("Hello", "world!")
> Hello world!
```

The print function was back-ported to Python 2 in version 2.6 through the __future__ module:

```
# In Python 2.6+
from __future__ import print_function
print("Hello", "world!")
> Hello world!
```

The print statement doesn't work in Python 3. If you want to print something and have it work in both Python versions, you'll need to import print_function in your Python 2 code.
