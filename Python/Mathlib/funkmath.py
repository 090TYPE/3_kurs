# Функция prime_factors
def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

# Функция is_perfect
def is_perfect(n):
    if n <= 0:
        return False
    divisors_sum = sum([i for i in range(1, n) if n % i == 0])
    return divisors_sum == n

# Функция is_armstrong
def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == n

# Функция is_palindrome
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# Функция is_perfect_square
def is_perfect_square(n):
    sqrt = int(n ** 0.5)
    return sqrt * sqrt == n

# Функция factorial
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Функция fibonacci
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Функция gcd
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Функция lcm
def lcm(a, b):
    return a * b // gcd(a, b)

# Функция is_prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Функция is_power_of_two
def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

# Функция is_even
def is_even(n):
    return n % 2 == 0

# Функция is_odd
def is_odd(n):
    return n % 2 != 0

# Функция is_positive
def is_positive(n):
    return n > 0

# Функция is_negative
def is_negative(n):
    return n < 0

# Функция sqrt
def sqrt(n):
    return n ** 0.5

# Функция log
def log(n, base):
    if n <= 0 or base <= 0 or base == 1:
        return "Логарифм не определен"
    result = 0
    while n >= base:
        n /= base
        result += 1
    return result

# Функция sin
def sin(angle):
    if angle == 0:
        return 0
    elif angle == 3.14:
        return 0
    elif angle == 2 * 3.14:
        return 0
    elif angle == 3.14 / 2:
        return 1
    elif angle == 3 * 3.14 / 2:
        return -1
    else:
        return None

# Функция cos
def cos(angle):
    if angle == 0:
        return 1
    elif angle == 3.14:
        return -1
    elif angle == 2 * 3.14:
        return 1
    elif angle == 3.14 / 2:
        return 0
    elif angle == 3 * 3.14 / 2:
        return 0
    else:
        return None

# Функция tan
def tan(angle):
    sin_val = sin(angle)
    cos_val = cos(angle)
    if sin_val is not None and cos_val is not None and cos_val != 0:
        return sin_val / cos_val
    else:
        return None

# Функция to_radians
def to_radians(degrees):
    return degrees * (3.14 / 180)

# Функция to_degrees
def to_degrees(radians):
    return radians * (180 / 3.14)

# Функция add
def add(a, b):
    return a + b

# Функция subtract
def subtract(a, b):
    return a - b

# Функция multiply
def multiply(a, b):
    return a * b

# Функция divide
def divide(a, b):
    if b == 0:
        return "Деление на ноль невозможно"
    return a / b

# Функция exponentiate
def exponentiate(base, exponent):
    return base ** exponent

# Функция is_divisible
def is_divisible(a, b):
    return a % b == 0

# Функция is_multiple
def is_multiple(a, b):
    return b % a == 0

# Функция is_coprime
def is_coprime(a, b):
    return gcd(a, b) == 1

# Функция is_factorial
def is_factorial(n):
    fact = 1
    i = 1
    while fact < n:
        i += 1
        fact *= i
    return fact == n

# Функция is_fibonacci
def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

# Функция is_perfect_cube
def is_perfect_cube(n):
    cube_root = int(n ** (1/3))
    return cube_root ** 3 == n

# Функция is_power_of_three
def is_power_of_three(n):
    while n % 3 == 0 and n > 1:
        n /= 3
    return n == 1

# Функция is_power_of_ten
def is_power_of_ten(n):
    return n > 0 and (n & (n - 1)) == 0 and str(n).count('0') == len(str(n)) - 1

# Функция is_harshad
def is_harshad(n):
    sum_of_digits = sum(int(digit) for digit in str(n))
    return n % sum_of_digits == 0

# Функция is_abundant
def is_abundant(n):
    divisors_sum = sum([i for i in range(1, n) if n % i == 0])
    return divisors_sum > n

# Функция is_deficient
def is_deficient(n):
    divisors_sum = sum([i for i in range(1, n) if n % i == 0])
    return divisors_sum < n

# Функция is_pandigital
def is_pandigital(n):
    num_str = str(n)
    return '0' not in num_str and len(num_str) == 10 and len(set(num_str)) == 10

# Функция is_happy
def is_happy(n):
    def get_next(n):
        result = 0
        while n > 0:
            digit = n % 10
            result += digit ** 2
            n //= 10
        return result
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1

# Функция is_amicable
def is_amicable(a, b):
    def get_divisors_sum(n):
        return sum([i for i in range(1, n) if n % i == 0])
    sum_a = get_divisors_sum(a)
    sum_b = get_divisors_sum(b)
    return sum_a == b and sum_b == a

# Функция для нахождения суммы делителей числа n (включая 1, но не включая само n)
def sum_of_divisors(n):
    divisors_sum = 1  # Изначально добавляем 1, так как оно делитель для всех чисел.
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:  # Добавляем также парные делители, если они различны.
                divisors_sum += n // i
    return divisors_sum

# Функция is_abundant_number
def is_abundant_number(n):
    if n <= 0:
        return False
    return sum_of_divisors(n) > n

# Функция is_deficient_number
def is_deficient_number(n):
    if n <= 0:
        return False
    return sum_of_divisors(n) < n
