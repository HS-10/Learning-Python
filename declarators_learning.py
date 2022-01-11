#functional programming
#declarator a function that takes a function, modifies it and gives us back something
def announce(f):
    def wrapper():
        print("About to run the function....")
        f()
        print("Done with the function.")
    return wrapper

#declarator is added with the @ symbol
@announce
def hello():
    print("Hello, world!")

hello()