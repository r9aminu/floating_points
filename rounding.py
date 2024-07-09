from decimal import Decimal, getcontext, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_UP, ROUND_HALF_DOWN, ROUND_HALF_EVEN, ROUND_DOWN, ROUND_UP, ROUND_05UP

getcontext().prec = 10

def round_ceiling(value):
    getcontext().rounding = ROUND_CEILING
    return value.to_integral_value()

def round_floor(value):
    getcontext().rounding = ROUND_FLOOR
    return value.to_integral_value()

def round_half_up(value):
    getcontext().rounding = ROUND_HALF_UP
    return value.to_integral_value()

def round_half_down(value):
    getcontext().rounding = ROUND_HALF_DOWN
    return value.to_integral_value()

def round_half_even(value):
    getcontext().rounding = ROUND_HALF_EVEN
    return value.to_integral_value()

def round_down(value):
    getcontext().rounding = ROUND_DOWN
    return value.to_integral_value()

def round_up(value):
    getcontext().rounding = ROUND_UP
    return value.to_integral_value()

def round_05up(value):
    getcontext().rounding = ROUND_05UP
    return value.to_integral_value()

value = Decimal('2.5')
value_negative = Decimal('-2.5')

print(f"ROUND_CEILING: {value} -> {round_ceiling(value)}, {value_negative} -> {round_ceiling(value_negative)}")
print("Round towards positive infinity.\n")

print(f"ROUND_FLOOR: {value} -> {round_floor(value)}, {value_negative} -> {round_floor(value_negative)}")
print("Round towards negative infinity.\n")

print(f"ROUND_HALF_UP: {value} -> {round_half_up(value)}, {value_negative} -> {round_half_up(value_negative)}")
print("Round to nearest, away from zero if equidistant.\n")

print(f"ROUND_HALF_DOWN: {value} -> {round_half_down(value)}, {value_negative} -> {round_half_down(value_negative)}")
print("Round to nearest, towards zero if equidistant.\n")

print(f"ROUND_HALF_EVEN: {value} -> {round_half_even(value)}, {value_negative} -> {round_half_even(value_negative)}")
print("Round to nearest, to even if equidistant.\n")

print(f"ROUND_DOWN: {value} -> {round_down(value)}, {value_negative} -> {round_down(value_negative)}")
print("Round towards zero.\n")

print(f"ROUND_UP: {value} -> {round_up(value)}, {value_negative} -> {round_up(value_negative)}")
print("Round away from zero.\n")

print(f"ROUND_05UP: {value} -> {round_05up(value)}, {value_negative} -> {round_05up(value_negative)}")
print("Round away from zero if last digit is 0 or 5, otherwise round towards zero.\n")
