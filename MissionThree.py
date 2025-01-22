# Önce Seaborn kütüphanesini çağıralım.
import seaborn as sns
# Şimdi car_Crashes veri setini bir data frame'e atayalım.
df = sns.load_dataset("car_crashes")
df.columns

# Öncelikle istenmeyen sütunları bir listeye atayalım.
og_list = ["abbrev", "no_previous"]
# Şimdi istenmeyenler dışındaki sütunları yeni bir listeye atayalım.
new_cols = [col for col in df.columns if col not in og_list]
# Şimdi new_cols listesindeki sütunları kullanarak yeni bir DataFrame oluşturalım.
new_df = df[new_cols]