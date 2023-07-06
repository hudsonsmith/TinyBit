# TinyBit.
A programming language.

Each line's first word defines an operation.
This makes it easy to parse.

For example:

```
SET X INT TO 3
```

`SET` is the clear operation, which the function handles.

SET calls the SET function with the whole line as a parameter.


# Note

Loop through every line in the text before starting.

Find all `-- POINT <x> NOENTER --` (noenter) is optional.

Add the line numbers to the thing and create function ranges.