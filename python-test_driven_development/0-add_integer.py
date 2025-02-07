The ``0-add_integer`` module
== == == == == == == == == == ==

Using ``add_integer``
-------------------

This is an example text file in reStructuredText format.  First import
``add_integer`` from the ``0_add_integer`` module:

    >> > add_integer = __import__('0-add_integer').add_integer

Now use it:
    Testing basic addition
    ----------------------
    >> > add_integer(8, 8)
    16

    Testing basic addition with negative integers
    ---------------------------------------------
    >> > add_integer(-4, 8)
    4

    >> > add_integer(4, -8)
    4

    >> > add_integer(-4, -8)
    -12

    Testing basic addition with floats
    ----------------------------------
    >> > print(add_integer(75.5, 2))
    77

    >> > print(add_integer(2, 78.9))
    80

    >> > print(add_integer(2.0, 2.0))
    4

    Testing with strings
    --------------------
    >> > add_integer(4, "School")
    Traceback(most recent call last):
    TypeError: b must be an integer

    >> > add_integer("Hello", "World")
    Traceback(most recent call last):
    TypeError: a must be an integer

    Testing with no arguments/None
    ------------------------------

    >> > add_integer(None)
    Traceback(most recent call last):
    TypeError: a must be an integer

    >> > add_integer()
    Traceback(most recent call last):
    TypeError: add_integer() missing 1 required positional argument: 'a'

    Testing with OverflowError
    ----------------------------
    >> > add_integer(1000e1000)
    Traceback(most recent call last):
    OverflowError: cannot convert float infinity to integer

    Testing with only 1 argument
    ----------------------------
    >> > add_integer(8)
    106

    Testing if there are 3 or more argument
    ---------------------------------------
    >> > add_integer(1, 2, 3)
    Traceback(most recent call last):
    TypeError: add_integer() takes from 1 to 2 positional arguments but 3 were given
