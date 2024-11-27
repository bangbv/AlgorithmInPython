def print_debug(f, title, value, log_debug = False):
    if log_debug : f(title, value)

def my_print(title, value):
    print(f"{title}: {value}")

log_debug = True
print_debug(my_print, "title", "value", log_debug)

