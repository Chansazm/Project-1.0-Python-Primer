# This will result in an error
def some_function():
    word = "hello"

    print(word)
some_function()


# This works fine
def some_function():
    word = "hello"

def another_function():
    word = "goodbye"
