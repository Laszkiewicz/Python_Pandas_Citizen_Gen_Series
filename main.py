from faker import Faker
from pandas import pandas
import pandas as pd
import random, time, datetime, choice
from random import randrange
from datetime import timedelta, date, datetime
import time
import timeit


fake_data = Faker("pl_PL")


def generate_ssns(how_many):
    pesels=[]
    for i in range(how_many):
        pesels.append(fake_data.pesel())
    pesel_series = pd.Series(pesels)
    return pesel_series


def generate_unique_ssns(how_many, gender, date_start, date_end):
    year_start, month_start, day_start = [int(v) for v in date_start.split("-")]
    year_end, month_end, day_end = [int(v) for v in date_end.split("-")]
    pesels = []
    while len(pesels) < how_many:
        date_birth = fake_data.date_between_dates(date_start=datetime(year_start,month_start,day_start), date_end = datetime(year_end,month_end,day_end))
        new_pesel = fake_data.pesel(sex = gender, date_of_birth = date_birth)
        if new_pesel not in pesels:
            pesels.append(new_pesel)
    series_unique = pd.Series(pesels)

result_1000_generic = timeit.timeit(stmt="generate_ssns(1000)", globals=globals(), number=1)
print(f"This is the result of 1000 parses of generic function {result_1000_generic}")
result_1000_unique = timeit.timeit(stmt="generate_unique_ssns(1000,'F','1990-01-01','1990-01-19')", globals=globals(), number=1)
print(f"This is the result of 1000 parses of unique function {result_1000_unique}")

result_10k_generic = timeit.timeit(stmt="generate_ssns(10000)", globals=globals(), number=1)
print(f"This is the result of 10k parses of generic function {result_10k_generic}")
result_10k_unique = timeit.timeit(stmt="generate_unique_ssns(10000,'F','1990-01-01','1990-01-19')", globals=globals(), number=1)
print(f"This is the result of 10k parses of unique function {result_10k_unique}")

result_100k_generic = timeit.timeit(stmt="generate_ssns(100000)", globals=globals(), number=1)
print(f"This is the result of 100k parses of generic function {result_100k_generic}")
result_100k_unique = timeit.timeit(stmt="generate_unique_ssns(100000,'F','1990-01-01','1990-01-19')", globals=globals(), number=1)
print(f"This is the result of 100k parses of unique function {result_100k_unique}")