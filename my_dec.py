def around_decorator(fff):
    def arounder():
        print("Before")
        fff()
        print("After")
    return arounder

def dec_with_params(f):
    def w(*args):
        return f(*args)
    return w