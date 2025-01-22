# Önce Seaborn kütüphanesini çağıralım.
import seaborn as sns
# Şimdi car_Crashes veri setini bir data frame'e atayalım.
df = sns.load_dataset("car_crashes")
df.columns

# List comprehension yapısı ile içinde "no" olmayan ifadelerin ismine "_FLAG" ekleyelim ve tüm değişkenlerin ismini büyütelim.

df.columns = [col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]
