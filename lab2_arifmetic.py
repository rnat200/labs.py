def is_diff_digits(num: int) -> bool:
    s = str(abs(num))
    return len(s) == len(set(s))

def is_simple_digit(num: int) -> bool:
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def is_sover_digit(num: int) -> bool:
    sum = 0
    for i in range(1,num):
        if num % i == 0:
           sum += i
    return sum == num

def print_sover_chisla(a:int, b:int) -> None:
    list = []
    for i in range(a,b+1):
        if is_sover_digit(i):
            list.append(i)
    print(list)

def is_a_mojet_bit_polycheno_iz_b (a: int, b: int) -> bool:
    s1,s2= str(a), str(b)
    it  = iter(s2)
    return all(char in it for char in s1)

num1 = 12345
num2 = 12245
print(f"   Цифры числа {num1} различны - {is_diff_digits(num1)}")
print(f"   Цифры числа {num2} различны - {is_diff_digits(num2)}")
a, b = 24, 12345
print(f"Можно ли получить {a} из {b} вычеркиванием цифр? {is_a_mojet_bit_polycheno_iz_b(a,b)}")
a = 1
b = 1000
print(f"Сов числа от 1 до 1000:")
print_sover_chisla(a,b)
