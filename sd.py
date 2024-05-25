import random
import pandas as pd
from termcolor import colored
import time
from tqdm import tqdm

for i in tqdm(range(100), desc="Loading SUPER DATA...", ascii=False, ncols=75):
    time.sleep(0.05)  # Simulasi proses, 0.02 detik per iterasi (total 2 detik)

print("We Are Ready.")
print("-" * 40)
print(colored("SUPER DATA", 'red', attrs=['bold']))
print("BY @iwanggawae V1")
print("-" * 40)

try:
    num_participants = int(input("Masukkan jumlah partisipan: "))
    num_questions = int(input("Masukkan jumlah pertanyaan: "))
except ValueError:
    print("Input tidak valid. Masukkan angka.")
    sys.exit(1)

# Animasi Loading
for i in tqdm(range(100), desc="Preparing Data...", ascii=False, ncols=75):
    time.sleep(0.03)  # Simulasi proses, 0.02 detik per iterasi (total 2 detik)

for i in tqdm(range(100), desc="Getting Panda Ready...", ascii=False, ncols=75):
    time.sleep(0.02)

data = []
total_ratings = num_participants * num_questions

# Proporsi rating yang diinginkan
proporsi_ratings = {
    1: 0.009,
    2: 0.015,
    3: 0.287,
    4: 0.391,
    5: 0.298
}

# Hitung max_ratings secara dinamis
max_ratings = {
    rating: round(proporsi * total_ratings) for rating, proporsi in proporsi_ratings.items()
}

# Pastikan total max_ratings sesuai dengan total rating yang dibutuhkan
while sum(max_ratings.values()) != total_ratings:
    # Jika tidak sesuai, sesuaikan rating dengan frekuensi terbanyak
    most_frequent_rating = max(max_ratings, key=max_ratings.get)
    max_ratings[most_frequent_rating] += 1

count_ratings = {rating: 0 for rating in range(1, 6)}

for participant in range(1, num_participants + 1):
    row = [participant]
    for _ in range(num_questions):
        while True:
            rating = random.randint(1, 5)
            if count_ratings[rating] < max_ratings[rating]:
                break
        row.append(rating)
        count_ratings[rating] += 1
    data.append(row)

columns = ['Participant'] + [f'Q{i+1}' for i in range(num_questions)]
df = pd.DataFrame(data, columns=columns)

# Export ke Excel
with pd.ExcelWriter('hasil_kuesioner.xlsx') as writer:
    df.to_excel(writer, sheet_name='Data', index=False)

print("Data telah berhasil diekspor ke hasil_kuesioner.xlsx")
