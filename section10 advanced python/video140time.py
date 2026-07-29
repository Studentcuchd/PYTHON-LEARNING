import timeit

time = timeit.timeit(
    stmt="sum(range(1000))",
    number=1000
)

print(time)