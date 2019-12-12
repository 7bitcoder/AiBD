# Lab 1 
Przez niepoprawne działanie i brak czasu na naprawę jupytera wyniki prezentuję w readme
```python
import pandas as pd

df = pd.read_csv("../Analysis Data/billboard.csv", encoding="mac_latin2")
# Melting
id_vars = ["year",
           "artist.inverted",
           "track",
           "time",
           "genre",
           "date.entered",
           "date.peaked"]
with pd.option_context('display.max_columns', None):
    print(df)
```
```
     year      artist.inverted                                  track  time  \
0    2000      Destiny's Child               Independent Women Part I  3:38   
1    2000              Santana                           Maria, Maria  4:18   
2    2000        Savage Garden                     I Knew I Loved You  4:07   
3    2000              Madonna                                  Music  3:45   
4    2000  Aguilera, Christina  Come On Over Baby (All I Want Is You)  3:38   
..    ...                  ...                                    ...   ...   
312  2000     Ghostface Killah                       Cherchez LaGhost  3:04   
313  2000          Smith, Will                            Freakin' It  3:58   
314  2000        Zombie Nation                          Kernkraft 400  3:30   
315  2000       Eastsidaz, The                               Got Beef  3:58   
316  2000               Fragma                         Toca's Miracle  3:22   

    genre date.entered date.peaked  x1st.week  x2nd.week  x3rd.week  \
0    Rock   2000-09-23  2000-11-18         78       63.0       49.0   
1    Rock   2000-02-12  2000-04-08         15        8.0        6.0   
2    Rock   1999-10-23  2000-01-29         71       48.0       43.0   
3    Rock   2000-08-12  2000-09-16         41       23.0       18.0   
4    Rock   2000-08-05  2000-10-14         57       47.0       45.0   
..    ...          ...         ...        ...        ...        ...   
312   R&B   2000-08-05  2000-08-05         98        NaN        NaN   
313   Rap   2000-02-12  2000-02-12         99       99.0       99.0   
314  Rock   2000-09-02  2000-09-02         99       99.0        NaN   
315   Rap   2000-07-01  2000-07-01         99       99.0        NaN   
316   R&B   2000-10-28  2000-10-28         99        NaN        NaN   

     x4th.week  x5th.week  x6th.week  x7th.week  x8th.week  x9th.week  \
0         33.0       23.0       15.0        7.0        5.0        1.0   
1          5.0        2.0        3.0        2.0        2.0        1.0   
2         31.0       20.0       13.0        7.0        6.0        4.0   
3         14.0        2.0        1.0        1.0        1.0        1.0   
4         29.0       23.0       18.0       11.0        9.0        9.0   
..         ...        ...        ...        ...        ...        ...   
312        NaN        NaN        NaN        NaN        NaN        NaN   
313       99.0        NaN        NaN        NaN        NaN        NaN   
314        NaN        NaN        NaN        NaN        NaN        NaN   
315        NaN        NaN        NaN        NaN        NaN        NaN   
316        NaN        NaN        NaN        NaN        NaN        NaN   

     x10th.week  x11th.week  x12th.week  x13th.week  x14th.week  x15th.week  \
0           1.0         1.0         1.0         1.0         1.0         1.0   
1           1.0         1.0         1.0         1.0         1.0         1.0   
2           4.0         4.0         6.0         4.0         2.0         1.0   
3           2.0         2.0         2.0         2.0         2.0         4.0   
4          11.0         1.0         1.0         1.0         1.0         4.0   
..          ...         ...         ...         ...         ...         ...   
312         NaN         NaN         NaN         NaN         NaN         NaN   
313         NaN         NaN         NaN         NaN         NaN         NaN   
314         NaN         NaN         NaN         NaN         NaN         NaN   
315         NaN         NaN         NaN         NaN         NaN         NaN   
316         NaN         NaN         NaN         NaN         NaN         NaN   

     x16th.week  x17th.week  x18th.week  x19th.week  x20th.week  x21st.week  \
0           1.0         1.0         1.0         1.0         2.0         3.0   
1           1.0         1.0         1.0         8.0        15.0        19.0   
2           1.0         1.0         2.0         1.0         2.0         4.0   
3           8.0        11.0        16.0        20.0        25.0        27.0   
4           8.0        12.0        22.0        23.0        43.0        44.0   
..          ...         ...         ...         ...         ...         ...   
312         NaN         NaN         NaN         NaN         NaN         NaN   
313         NaN         NaN         NaN         NaN         NaN         NaN   
314         NaN         NaN         NaN         NaN         NaN         NaN   
315         NaN         NaN         NaN         NaN         NaN         NaN   
316         NaN         NaN         NaN         NaN         NaN         NaN   

     x22nd.week  x23rd.week  x24th.week  x25th.week  x26th.week  x27th.week  \
0           7.0        10.0        12.0        15.0        22.0        29.0   
1          21.0        26.0        36.0        48.0        47.0         NaN   
2           8.0         8.0        12.0        14.0        17.0        21.0   
3          27.0        29.0        44.0         NaN         NaN         NaN   
4           NaN         NaN         NaN         NaN         NaN         NaN   
..          ...         ...         ...         ...         ...         ...   
312         NaN         NaN         NaN         NaN         NaN         NaN   
313         NaN         NaN         NaN         NaN         NaN         NaN   
314         NaN         NaN         NaN         NaN         NaN         NaN   
315         NaN         NaN         NaN         NaN         NaN         NaN   
316         NaN         NaN         NaN         NaN         NaN         NaN   

     x28th.week  x29th.week  x30th.week  x31st.week  x32nd.week  x33rd.week  \
0          31.0         NaN         NaN         NaN         NaN         NaN   
1           NaN         NaN         NaN         NaN         NaN         NaN   
2          24.0        30.0        34.0        37.0        46.0        47.0   
3           NaN         NaN         NaN         NaN         NaN         NaN   
4           NaN         NaN         NaN         NaN         NaN         NaN   
..          ...         ...         ...         ...         ...         ...   
312         NaN         NaN         NaN         NaN         NaN         NaN   
313         NaN         NaN         NaN         NaN         NaN         NaN   
314         NaN         NaN         NaN         NaN         NaN         NaN   
315         NaN         NaN         NaN         NaN         NaN         NaN   
316         NaN         NaN         NaN         NaN         NaN         NaN   

     x34th.week  x35th.week  x36th.week  x37th.week  x38th.week  x39th.week  \
0           NaN         NaN         NaN         NaN         NaN         NaN   
1           NaN         NaN         NaN         NaN         NaN         NaN   
2           NaN         NaN         NaN         NaN         NaN         NaN   
3           NaN         NaN         NaN         NaN         NaN         NaN   
4           NaN         NaN         NaN         NaN         NaN         NaN   
..          ...         ...         ...         ...         ...         ...   
312         NaN         NaN         NaN         NaN         NaN         NaN   
313         NaN         NaN         NaN         NaN         NaN         NaN   
314         NaN         NaN         NaN         NaN         NaN         NaN   
315         NaN         NaN         NaN         NaN         NaN         NaN   
316         NaN         NaN         NaN         NaN         NaN         NaN   

     x40th.week  x41st.week  x42nd.week  x43rd.week  x44th.week  x45th.week  \
0           NaN         NaN         NaN         NaN         NaN         NaN   
1           NaN         NaN         NaN         NaN         NaN         NaN   
2           NaN         NaN         NaN         NaN         NaN         NaN   
3           NaN         NaN         NaN         NaN         NaN         NaN   
4           NaN         NaN         NaN         NaN         NaN         NaN   
..          ...         ...         ...         ...         ...         ...   
312         NaN         NaN         NaN         NaN         NaN         NaN   
313         NaN         NaN         NaN         NaN         NaN         NaN   
314         NaN         NaN         NaN         NaN         NaN         NaN   
315         NaN         NaN         NaN         NaN         NaN         NaN   
316         NaN         NaN         NaN         NaN         NaN         NaN   

     x46th.week  x47th.week  x48th.week  x49th.week  x50th.week  x51st.week  \
0           NaN         NaN         NaN         NaN         NaN         NaN   
1           NaN         NaN         NaN         NaN         NaN         NaN   
2           NaN         NaN         NaN         NaN         NaN         NaN   
3           NaN         NaN         NaN         NaN         NaN         NaN   
4           NaN         NaN         NaN         NaN         NaN         NaN   
..          ...         ...         ...         ...         ...         ...   
312         NaN         NaN         NaN         NaN         NaN         NaN   
313         NaN         NaN         NaN         NaN         NaN         NaN   
314         NaN         NaN         NaN         NaN         NaN         NaN   
315         NaN         NaN         NaN         NaN         NaN         NaN   
316         NaN         NaN         NaN         NaN         NaN         NaN   

     x52nd.week  x53rd.week  x54th.week  x55th.week  x56th.week  x57th.week  \
0           NaN         NaN         NaN         NaN         NaN         NaN   
1           NaN         NaN         NaN         NaN         NaN         NaN   
2           NaN         NaN         NaN         NaN         NaN         NaN   
3           NaN         NaN         NaN         NaN         NaN         NaN   
4           NaN         NaN         NaN         NaN         NaN         NaN   
..          ...         ...         ...         ...         ...         ...   
312         NaN         NaN         NaN         NaN         NaN         NaN   
313         NaN         NaN         NaN         NaN         NaN         NaN   
314         NaN         NaN         NaN         NaN         NaN         NaN   
315         NaN         NaN         NaN         NaN         NaN         NaN   
316         NaN         NaN         NaN         NaN         NaN         NaN   

     x58th.week  x59th.week  x60th.week  x61st.week  x62nd.week  x63rd.week  \
0           NaN         NaN         NaN         NaN         NaN         NaN   
1           NaN         NaN         NaN         NaN         NaN         NaN   
2           NaN         NaN         NaN         NaN         NaN         NaN   
3           NaN         NaN         NaN         NaN         NaN         NaN   
4           NaN         NaN         NaN         NaN         NaN         NaN   
..          ...         ...         ...         ...         ...         ...   
312         NaN         NaN         NaN         NaN         NaN         NaN   
313         NaN         NaN         NaN         NaN         NaN         NaN   
314         NaN         NaN         NaN         NaN         NaN         NaN   
315         NaN         NaN         NaN         NaN         NaN         NaN   
316         NaN         NaN         NaN         NaN         NaN         NaN   

     x64th.week  x65th.week  x66th.week  x67th.week  x68th.week  x69th.week  \
0           NaN         NaN         NaN         NaN         NaN         NaN   
1           NaN         NaN         NaN         NaN         NaN         NaN   
2           NaN         NaN         NaN         NaN         NaN         NaN   
3           NaN         NaN         NaN         NaN         NaN         NaN   
4           NaN         NaN         NaN         NaN         NaN         NaN   
..          ...         ...         ...         ...         ...         ...   
312         NaN         NaN         NaN         NaN         NaN         NaN   
313         NaN         NaN         NaN         NaN         NaN         NaN   
314         NaN         NaN         NaN         NaN         NaN         NaN   
315         NaN         NaN         NaN         NaN         NaN         NaN   
316         NaN         NaN         NaN         NaN         NaN         NaN   

     x70th.week  x71st.week  x72nd.week  x73rd.week  x74th.week  x75th.week  \
0           NaN         NaN         NaN         NaN         NaN         NaN   
1           NaN         NaN         NaN         NaN         NaN         NaN   
2           NaN         NaN         NaN         NaN         NaN         NaN   
3           NaN         NaN         NaN         NaN         NaN         NaN   
4           NaN         NaN         NaN         NaN         NaN         NaN   
..          ...         ...         ...         ...         ...         ...   
312         NaN         NaN         NaN         NaN         NaN         NaN   
313         NaN         NaN         NaN         NaN         NaN         NaN   
314         NaN         NaN         NaN         NaN         NaN         NaN   
315         NaN         NaN         NaN         NaN         NaN         NaN   
316         NaN         NaN         NaN         NaN         NaN         NaN   

     x76th.week  
0           NaN  
1           NaN  
2           NaN  
3           NaN  
4           NaN  
..          ...  
312         NaN  
313         NaN  
314         NaN  
315         NaN  
316         NaN  
```
```python 
#normalizacja rankingu tygodni
df = pd.melt(frame=df, id_vars=id_vars, var_name="week", value_name="rank")

with pd.option_context('display.max_columns', None):
      print(df)
```
```
[317 rows x 83 columns]
       year      artist.inverted                                  track  time  \
0      2000      Destiny's Child               Independent Women Part I  3:38   
1      2000              Santana                           Maria, Maria  4:18   
2      2000        Savage Garden                     I Knew I Loved You  4:07   
3      2000              Madonna                                  Music  3:45   
4      2000  Aguilera, Christina  Come On Over Baby (All I Want Is You)  3:38   
...     ...                  ...                                    ...   ...   
24087  2000     Ghostface Killah                       Cherchez LaGhost  3:04   
24088  2000          Smith, Will                            Freakin' It  3:58   
24089  2000        Zombie Nation                          Kernkraft 400  3:30   
24090  2000       Eastsidaz, The                               Got Beef  3:58   
24091  2000               Fragma                         Toca's Miracle  3:22   

      genre date.entered date.peaked        week  rank  
0      Rock   2000-09-23  2000-11-18   x1st.week  78.0  
1      Rock   2000-02-12  2000-04-08   x1st.week  15.0  
2      Rock   1999-10-23  2000-01-29   x1st.week  71.0  
3      Rock   2000-08-12  2000-09-16   x1st.week  41.0  
4      Rock   2000-08-05  2000-10-14   x1st.week  57.0  
...     ...          ...         ...         ...   ...  
24087   R&B   2000-08-05  2000-08-05  x76th.week   NaN  
24088   Rap   2000-02-12  2000-02-12  x76th.week   NaN  
24089  Rock   2000-09-02  2000-09-02  x76th.week   NaN  
24090   Rap   2000-07-01  2000-07-01  x76th.week   NaN  
24091   R&B   2000-10-28  2000-10-28  x76th.week   NaN  

[24092 rows x 9 columns]
```
```python
    #znormalizowanie tygodni -> data -> liczba
df["week"] = df['week'].str.extract('(\d+)', expand=False).astype(int)
    df = df.dropna()
with pd.option_context('display.max_columns', None):
    print(df)
```
```
[24092 rows x 9 columns]
       year      artist.inverted                                  track  time  \
0      2000      Destiny's Child               Independent Women Part I  3:38   
1      2000              Santana                           Maria, Maria  4:18   
2      2000        Savage Garden                     I Knew I Loved You  4:07   
3      2000              Madonna                                  Music  3:45   
4      2000  Aguilera, Christina  Come On Over Baby (All I Want Is You)  3:38   
...     ...                  ...                                    ...   ...   
19663  2000             Lonestar                                 Amazed  4:25   
19700  2000                Creed                                 Higher  5:16   
19980  2000             Lonestar                                 Amazed  4:25   
20017  2000                Creed                                 Higher  5:16   
20334  2000                Creed                                 Higher  5:16   

         genre date.entered date.peaked  week  rank  
0         Rock   2000-09-23  2000-11-18     1  78.0  
1         Rock   2000-02-12  2000-04-08     1  15.0  
2         Rock   1999-10-23  2000-01-29     1  71.0  
3         Rock   2000-08-12  2000-09-16     1  41.0  
4         Rock   2000-08-05  2000-10-14     1  57.0  
...        ...          ...         ...   ...   ...  
19663  Country   1999-06-05  2000-03-04    63  45.0  
19700     Rock   1999-09-11  2000-07-22    63  50.0  
19980  Country   1999-06-05  2000-03-04    64  50.0  
20017     Rock   1999-09-11  2000-07-22    64  50.0  
20334     Rock   1999-09-11  2000-07-22    65  49.0  

[5307 rows x 9 columns]
```
```python 
#zamiana kolumny date na datę rzeczywistą
df['date'] = pd.to_datetime(df['date.entered']) + pd.to_timedelta(df['week'], unit='w') - pd.DateOffset(weeks=1)
with pd.option_context('display.max_columns', None):
    print(df)
```
```
[5307 rows x 9 columns]
       year      artist.inverted                                  track  time  \
0      2000      Destiny's Child               Independent Women Part I  3:38   
1      2000              Santana                           Maria, Maria  4:18   
2      2000        Savage Garden                     I Knew I Loved You  4:07   
3      2000              Madonna                                  Music  3:45   
4      2000  Aguilera, Christina  Come On Over Baby (All I Want Is You)  3:38   
...     ...                  ...                                    ...   ...   
19663  2000             Lonestar                                 Amazed  4:25   
19700  2000                Creed                                 Higher  5:16   
19980  2000             Lonestar                                 Amazed  4:25   
20017  2000                Creed                                 Higher  5:16   
20334  2000                Creed                                 Higher  5:16   

         genre date.entered date.peaked  week  rank       date  
0         Rock   2000-09-23  2000-11-18     1  78.0 2000-09-23  
1         Rock   2000-02-12  2000-04-08     1  15.0 2000-02-12  
2         Rock   1999-10-23  2000-01-29     1  71.0 1999-10-23  
3         Rock   2000-08-12  2000-09-16     1  41.0 2000-08-12  
4         Rock   2000-08-05  2000-10-14     1  57.0 2000-08-05  
...        ...          ...         ...   ...   ...        ...  
19663  Country   1999-06-05  2000-03-04    63  45.0 2000-08-12  
19700     Rock   1999-09-11  2000-07-22    63  50.0 2000-11-18  
19980  Country   1999-06-05  2000-03-04    64  50.0 2000-08-19  
20017     Rock   1999-09-11  2000-07-22    64  50.0 2000-11-25  
20334     Rock   1999-09-11  2000-07-22    65  49.0 2000-12-02  

[5307 rows x 10 columns]
```
```python
#pozbycie się zbędnnych kolumn
df = df[["year",
         "genre",
         "artist.inverted",
         "track",
         "time",
         "date",
         "rank"]]
with pd.option_context('display.max_columns', None):  # more options can be specified also
    print(df)
```
```
[5307 rows x 10 columns]
       year    genre      artist.inverted  \
0      2000     Rock      Destiny's Child   
1      2000     Rock              Santana   
2      2000     Rock        Savage Garden   
3      2000     Rock              Madonna   
4      2000     Rock  Aguilera, Christina   
...     ...      ...                  ...   
19663  2000  Country             Lonestar   
19700  2000     Rock                Creed   
19980  2000  Country             Lonestar   
20017  2000     Rock                Creed   
20334  2000     Rock                Creed   

                                       track  time       date  rank  
0                   Independent Women Part I  3:38 2000-09-23  78.0  
1                               Maria, Maria  4:18 2000-02-12  15.0  
2                         I Knew I Loved You  4:07 1999-10-23  71.0  
3                                      Music  3:45 2000-08-12  41.0  
4      Come On Over Baby (All I Want Is You)  3:38 2000-08-05  57.0  
...                                      ...   ...        ...   ...  
19663                                 Amazed  4:25 2000-08-12  45.0  
19700                                 Higher  5:16 2000-11-18  50.0  
19980                                 Amazed  4:25 2000-08-19  50.0  
20017                                 Higher  5:16 2000-11-25  50.0  
20334                                 Higher  5:16 2000-12-02  49.0  

[5307 rows x 7 columns]
```
```python
#podzielenie danych na 2 zbiory
    copy = df
    songs_cols = ["year", "artist.inverted", "track", "time", "genre"]
    songs = copy[songs_cols].drop_duplicates()
    songs = songs.reset_index(drop=True)
    songs["song_id"] = songs.index
    print(songs)
```
```
[5307 rows x 7 columns]
     year      artist.inverted                                  track  time  \
0    2000      Destiny's Child               Independent Women Part I  3:38   
1    2000              Santana                           Maria, Maria  4:18   
2    2000        Savage Garden                     I Knew I Loved You  4:07   
3    2000              Madonna                                  Music  3:45   
4    2000  Aguilera, Christina  Come On Over Baby (All I Want Is You)  3:38   
..    ...                  ...                                    ...   ...   
312  2000     Ghostface Killah                       Cherchez LaGhost  3:04   
313  2000          Smith, Will                            Freakin' It  3:58   
314  2000        Zombie Nation                          Kernkraft 400  3:30   
315  2000       Eastsidaz, The                               Got Beef  3:58   
316  2000               Fragma                         Toca's Miracle  3:22   

    genre  song_id  
0    Rock        0  
1    Rock        1  
2    Rock        2  
3    Rock        3  
4    Rock        4  
..    ...      ...  
312   R&B      312  
313   Rap      313  
314  Rock      314  
315   Rap      315  
316   R&B      316  

[317 rows x 6 columns]
```
```python 
with pd.option_context('display.max_columns', None):  # more options can be specified also

    ranks = pd.merge(copy, songs, on=["year", "artist.inverted", "track", "time", "genre"])
    ranks = ranks[["song_id", "date", "rank", "time"]]
    print(ranks)
    ranks.info()
    ranks.to_csv(r'../Analysis Data/ranks.csv')
songs.to_csv(r'../Analysis Data/songs.csv')
```
```
[317 rows x 6 columns]
      song_id       date  rank  time
0           0 2000-09-23  78.0  3:38
1           0 2000-09-30  63.0  3:38
2           0 2000-10-07  49.0  3:38
3           0 2000-10-14  33.0  3:38
4           0 2000-10-21  23.0  3:38
...       ...        ...   ...   ...
5302      314 2000-09-02  99.0  3:30
5303      314 2000-09-09  99.0  3:30
5304      315 2000-07-01  99.0  3:58
5305      315 2000-07-08  99.0  3:58
5306      316 2000-10-28  99.0  3:22

[5307 rows x 4 columns]
<class 'pandas.core.frame.DataFrame'>
Int64Index: 5307 entries, 0 to 5306
Data columns (total 4 columns):
song_id    5307 non-null int64
date       5307 non-null datetime64[ns]
rank       5307 non-null float64
time       5307 non-null object
dtypes: datetime64[ns](1), float64(1), int64(1), object(1)
memory usage: 207.3+ KB
```
