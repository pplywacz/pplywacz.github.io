def announce(f):
    def wrapper():
        print("aboout to run the function..")
        f()
        print("Done with the functjion.")
    return wrapper

@announce
def hello():
    print("hello, world!")

hello()