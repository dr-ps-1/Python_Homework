def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


year_2025 = is_year_leap(2025)
print(f"год 2025: {year_2025}")

year_2020 = is_year_leap(2020)
print(f"год 2020: {year_2020}")
