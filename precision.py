import numpy as np
import matplotlib.pyplot as pp

def map_plot():
    large_numbers = np.logspace(1, 10, num=10)
    small_numbers = np.logspace(-1, -10, num=10)

    large_diff = large_numbers * 1.000001 - large_numbers
    small_diff = small_numbers - (small_numbers / 2)

    df_large = {
        'Numbers': large_numbers,
        'Difference': large_diff,
        'Type': ['Large Numbers'] * len(large_numbers)
    }
    
    df_small = {
        'Numbers': small_numbers,
        'Difference': small_diff,
        'Type': ['Small Numbers'] * len(small_numbers)
    }

    pp.figure(figsize=(12, 6))

    pp.plot(df_large['Numbers'], df_large['Difference'], label='Large Numbers', color='blue', marker='o')
    pp.plot(df_small['Numbers'], df_small['Difference'], label='Small Numbers', color='red', marker='o')

    pp.xscale('log')
    pp.yscale('log')

    pp.xlabel('Numbers')
    pp.ylabel('Precision loss')
    pp.title('Precision Loss large and small numbers')

    pp.legend()
    pp.tight_layout()
    pp.show()

map_plot()
