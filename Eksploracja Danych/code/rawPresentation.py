import pandas as pd
from tqdm import tqdm as tk

df = pd.read_csv("Raw_Data/billboard.csv", encoding="mac_latin2")
# Melting
with pd.option_context('display.max_columns', None):  # more options can be specified also
    #df.info()
    # df().count(axis='columns')
    # with pd.option_context('display.max_columns', None):  # more options can be specified also
    grouped = df.groupby('genre')
    result = pd.DataFrame(columns=("genre"
                                   , "topTen", "tracks number"))
    # print(grouped)
    print(len(grouped))
    t = tk(total=len(grouped))  # Initialise
    for name, group in grouped:
        t.update()
        res = group[group.iloc[:, 7:] <= 10].count()
        res.rename(name)
        final = res.sum()
        result.loc[len(result)] = [name, final, len(group)]
        # print(group)

    t.close()
    print(result)
    print("*********Gatunek muzyki z najczęstszym top 10*********")
    print(result[result.topTen == result.topTen.max()])

    grouped = df.groupby('time')
    result = pd.DataFrame(columns=("time"
                                   , "topTen", "tracks number"))
    # print(grouped)
    t = tk(total=len(grouped))  # Initialise
    for name, group in grouped:
        t.update()
        res = group[group.iloc[:, 7:] <= 10].count()
        res.rename(name)
        final = res.sum()
        result.loc[len(result)] = [name, final, len(group)]
        # print(group)
    t.close()
    print(result)
    print("*********Grupa z najczęstszym top 10*********")
    print(result[result.topTen == result.topTen.max()])
    print("*********Grupa z najrzadszym top 10*********")
    print(result[result.topTen == result.topTen.min()])
