import pandas as pd
import os

path = 'names'
cols = ['Name', 'Gender', 'Count']


def count_dynamics(years):
    names_years = []
    dynamics = dict()
    male = []
    female = []
    for year in years:
        tmp_names = pd.read_csv(os.path.join(path, 'yob' + year + '.txt'),
                                names=cols)
        names_years.append(tmp_names)

    for names in names_years:
        f = 0
        m = 0
        genders = names['Gender']
        counts = names['Count']

        for num, count in enumerate(counts):
            if genders[num] == 'F':
                f += count
            elif genders[num] == 'M':
                m += count

        male.append(m)
        female.append(f)

    dynamics['F'] = female
    dynamics['M'] = male

    return dynamics


years = input('Введите года через пробел: ').split()
print(count_dynamics(years))
