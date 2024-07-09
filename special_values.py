def special_values():
    positive_inf = float('inf')
    negative_inf = -float('inf')

    nan_value = positive_inf + negative_inf

    print('pos inf:', positive_inf)
    print('neg inf:', negative_inf)
    print('nan value:', nan_value)
    print(positive_inf > 1e308)
    print(negative_inf < -1e308)
    print(nan_value != nan_value)

special_values()

