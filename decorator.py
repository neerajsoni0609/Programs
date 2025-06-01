def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorated function")
        func(*args, **kwargs)

    return wrapper

@decorator_func
def demo(arg1, arg2):
    print(f"Demo Function with {arg1}, {arg2}")

demo("arg1", arg2="arg2")