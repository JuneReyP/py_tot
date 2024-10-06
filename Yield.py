def generate():
    yield 1
    yield 2
    yield 3

gen =generate()

print(next(gen))
print(next(gen))
print(next(gen))