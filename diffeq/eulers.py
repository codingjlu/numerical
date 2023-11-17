def eulers(find, fn, initial_value, h):
    t, y = initial_value
    while t < find:
        v = fn(t, y)
        t += h
        y += h * v
    return y

print(eulers(10, lambda t, y: -2 * y, (0, 2), 5))
