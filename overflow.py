def demonstrate_overflow():
    large_number = 1.8e308
    overflow_factor = 10
    result = large_number * overflow_factor
    print("Large number:", large_number)
    print("Overflow:", result)

def demonstrate_underflow():
    small_number = 2.2e-308
    large_divisor = 1e308
    result = small_number / large_divisor
    print("Small number:", small_number)
    print("Underflow:", result)

demonstrate_overflow()
demonstrate_underflow()
