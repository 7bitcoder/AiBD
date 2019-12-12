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
#normalizacja rankingu tygodni
df = pd.melt(frame=df, id_vars=id_vars, var_name="week", value_name="rank")

with pd.option_context('display.max_columns', None):
    print(df)
    #znormalizowanie tygodni ->pseudo data -> liczba
    df["week"] = df['week'].str.extract('(\d+)', expand=False).astype(int)
    df = df.dropna()
with pd.option_context('display.max_columns', None):
    print(df)
    #zamiana kolumny data na datę rzeczywistą
df['date'] = pd.to_datetime(df['date.entered']) + pd.to_timedelta(df['week'], unit='w') - pd.DateOffset(weeks=1)
with pd.option_context('display.max_columns', None):
    print(df)
#pozbycie się zbędnnych kolumn
df = df[["year",
         "genre",
         "artist.inverted",
         "track",
         "time",
         "date",
         "rank"]]
with pd.option_context('display.max_columns', None):
    print(df)
    #podzielenie danych na 2 zbiory
    copy = df
    songs_cols = ["year", "artist.inverted", "track", "time", "genre"]
    songs = copy[songs_cols].drop_duplicates()
    songs = songs.reset_index(drop=True)
    songs["song_id"] = songs.index
    print(songs)

with pd.option_context('display.max_columns', None):

    ranks = pd.merge(copy, songs, on=["year", "artist.inverted", "track", "time", "genre"])
    ranks = ranks[["song_id", "date", "rank", "time"]]
    print(ranks)
    ranks.info()
    ranks.to_csv(r'../Analysis Data/ranks.csv')
songs.to_csv(r'../Analysis Data/songs.csv')
