import pandas as pd
import os

path = 'names'
cols = ['Name', 'Gender', 'Count']


def count_top3(years):
    names_years = []

    for year in years:
        tmp_names = pd.read_csv(os.path.join(path, 'yob' + year + '.txt'),
                                names=cols)
        names_years.append(tmp_names)

    names = pd.DataFrame.sort_values(pd.concat(names_years), by=['Count'])
    names = pd.DataFrame.sort_values(names, by=['Count']).reset_index()
    top_names = [names['Name'][len(names) - 1], names['Name'][len(names) - 2], names['Name'][len(names) - 3]]
    return top_names


years = input('Введите года через пробел: ').split()
top3 = count_top3(years)
print(top3)
