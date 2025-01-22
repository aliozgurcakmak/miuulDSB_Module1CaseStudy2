# Önce Seaborn kütüphanesini çağıralım.
import seaborn as sns
# Şimdi car_Crashes veri setini bir data frame'e atayalım.
df = sns.load_dataset("car_crashes")
df.columns

# List Comprehension yapısı ile numeric değişkenleri bulalım ve başına NUM ekleyip büyük harfe çevirelim.
df.columns = ["NUM_" + col.upper() if df[col].dtype != "O" else col  for col in df.columns]
