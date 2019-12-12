# Lab 3
Przez niepoprawne działanie i brak czasu na naprawę jupytera wyniki prezentuję w readme
```python
import pandas as pd
from tqdm import tqdm as tk

df = pd.read_csv("../Original Data/billboard.csv", encoding="mac_latin2")
# Melting
with pd.option_context('display.max_columns', None):  # more options can be specified also
    #df.info()
    # df().count(axis='columns')
    # with pd.option_context('display.max_columns', None):  # more options can be specified also
    #grupowanie po rodzaju muzyki
    grouped = df.groupby('genre')
    result = pd.DataFrame(columns=("genre"
                                   , "topTen", "tracks number"))
    # print(grouped)
    t = tk(total=len(grouped))  # Initialise
    for name, group in grouped:
        t.update()
        #liczenie ile razy utwory z danego rodzaju muzyki były top 10
        res = group[group.iloc[:, 7:] <= 10].count()
        res.rename(name)
        #suma
        final = res.sum()
        #dodatnie wiersza do result z nazwą grupy wynikiem oraz liczbą tracków
        result.loc[len(result)] = [name, final, len(group)]
        # print(group)

    t.close()
    print(result)
    print("*********Gatunek muzyki z najczęstszym top 10*********")
    print(result[result.topTen == result.topTen.max()])
    #rock był 428 razy w top 10
```
```
100%|██████████| 10/10 [00:39<00:00,  3.95s/it]
         genre topTen tracks number
0      Country     12            74
1  Electronica      4             4
2       Gospel      0             1
3         Jazz      2             1
4        Latin     16             9
5          Pop      9             9
6          R&B      0            23
7          Rap     53            58
8       Reggae      0             1
9         Rock    428           137
*********Gatunek muzyki z najczęstszym top 10*********
  genre topTen tracks number
9  Rock    428           137
```
```python
 #grupowanie po czasie utworów
    grouped = df.groupby('time')
    result = pd.DataFrame(columns=("time"
                                   , "topTen", "tracks number"))
    # print(grouped)
    #analogicznie do poprzedniego kodu
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
    #najcześciej top 10 były utworu z czasem trwania 3:52 
    #najrzadszych  w top 10 było 124

```
```
100%|██████████| 126/126 [00:12<00:00, 10.21it/s]
     time topTen tracks number
0    2:36      0             1
1    2:38      0             1
2    2:52      5             1
3    2:53      0             2
4    2:55      0             2
..    ...    ...           ...
121  6:22      0             1
122  6:50      0             1
123  7:10      0             1
124  7:35      0             1
125  7:50      2             1

[126 rows x 3 columns]
*********Grupa z najczęstszym top 10*********
    time topTen tracks number
49  3:52     40             6
*********Grupa z najrzadszym top 10*********
     time topTen tracks number
0    2:36      0             1
1    2:38      0             1
3    2:53      0             2
4    2:55      0             2
5    2:56      0             2
..    ...    ...           ...
120  6:20      0             1
121  6:22      0             1
122  6:50      0             1
123  7:10      0             1
124  7:35      0             1

[81 rows x 3 columns]
```

