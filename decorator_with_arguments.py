def decorator_func(arg):
    print(f"Argument taken from {arg}")
    def inner(func):
        print("function modified")
        def wrapper(*arg, **kwargs):
            result = func(*arg, **kwargs)
            return result
        return wrapper
    return inner

@decorator_func("Decorator Arg")
def demo(arg1):
    return(f"Demo function with arg {arg1}")

print(demo("Hello"))