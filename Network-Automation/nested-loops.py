# Nested loops - it can help generate co-ordinates such (0,0), (0,1)

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for y in range(x_count):
        output += 'x'
    print(output)
