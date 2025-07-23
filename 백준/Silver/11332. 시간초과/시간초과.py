import math


def func_n(n, t, l):
    operation_per_test_case = n
    total_operations = operation_per_test_case * t
    elapsed_time = total_operations / operations_per_second

    return elapsed_time <= l

def func_n_squared(n, t, l):
    operation_per_test_case = n ** 2
    total_operations = operation_per_test_case * t
    elapsed_time = total_operations / operations_per_second

    return elapsed_time <= l

def func_n_cubed(n, t, l):
    operation_per_test_case = n ** 3
    total_operations = operation_per_test_case * t
    elapsed_time = total_operations / operations_per_second

    return elapsed_time <= l

def func_power_two(n, t, l):
    if n > 30:
        return False

    operation_per_test_case = 2 ** n
    total_operations = operation_per_test_case * t
    elapsed_time = total_operations / operations_per_second

    return elapsed_time <= l

def func_n_factorial(n, t, l):
    if n > 20:
        return False

    operation_per_test_case = math.factorial(n)
    total_operations = operation_per_test_case * t
    elapsed_time = total_operations / operations_per_second

    return elapsed_time <= l

dict_func ={
    'O(N)': func_n,
    'O(N^2)': func_n_squared,
    'O(N^3)': func_n_cubed,
    'O(2^N)': func_power_two,
    'O(N!)': func_n_factorial
}

operations_per_second = 100_000_000
c = int(input())
for _ in range(c):
    S, N, T, L = input().split()

    result = dict_func[S](int(N), int(T), int(L))

    if result:
        print('May Pass.')
    else:
        print('TLE!')