def prime_numbers(*numbers):
    quantity_prime_num = 0
    for elem in numbers:
        count = 0
        if elem != 0:
            for divider in range(1, abs(elem) + 1):
                if abs(elem) % divider == 0:
                    count += 1
                if count == 3:
                    break
            if count < 3:
                quantity_prime_num += 1
    return quantity_prime_num


print(prime_numbers(1, 2, 3, 4, 5, 6, 7, 8))
