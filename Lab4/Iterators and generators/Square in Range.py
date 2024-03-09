def squares(a, b):
    start = a
    stop = b
    while start <= stop:
        yield start ** 2
        start += 1

a=int(input())
squares1 = list(squares(1, a))

print(', '.join(map(str, squares1)))
    
