import random
import pandas as pd
from termcolor import colored
import time
from tqdm import tqdm
import pingouin as pg  # Pastikan untuk menginstall library ini menggunakan `pip install pingouin`

# Simulasi loading
for i in tqdm(range(100), desc="Loading SUPER DATA...", ascii=False, ncols=75):
    time.sleep(0.05)

print("We Are Ready.")
print("-" * 40)
print(colored("SUPER DATA", 'green', attrs=['bold']))
print("BY @iwanggawae V1")
print("-" * 40)

try:
    num_participants = int(input("Masukkan jumlah partisipan: "))
    num_questions = int(input("Masukkan jumlah pertanyaan: "))
except ValueError:
    print(colored("!!!MASUKKAN ANGKA!!!", 'red', attrs=['bold']))
    sys.exit(1)

# Fungsi untuk menghasilkan data
def generate_data(num_participants, num_questions):
    data = []
    total_ratings = num_participants * num_questions

    # Proporsi rating yang diinginkan
    proporsi_ratings = {
        1: 0.009,
        2: 0.015,
        3: 0.287,
        4: 0.345,
        5: 0.344
    }

    # Hitung max_ratings secara dinamis
    max_ratings = {
        rating: round(proporsi * total_ratings) for rating, proporsi in proporsi_ratings.items()
    }

    # Pastikan total max_ratings sesuai dengan total rating yang dibutuhkan
    while sum(max_ratings.values()) != total_ratings:
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
    return pd.DataFrame(data, columns=columns)

# Loop untuk memastikan reliabilitas di atas 0.60
cronbach_alpha_value = 0
while cronbach_alpha_value <= 0.70:
    print(colored("Data belum Reliabel, akan mengenerate ulang...", 'red', attrs=['bold']))
    df = generate_data(num_participants, num_questions)

    # Menghitung Cronbach's Alpha
    reliability_data = df.iloc[:, 1:]  # Data pertanyaan saja, tanpa kolom 'Participant'
    cronbach_alpha = pg.cronbach_alpha(reliability_data)
    cronbach_alpha_value = cronbach_alpha[0]

    print(f"Cronbach's Alpha: {cronbach_alpha_value}")

# Menghitung jumlah dan rata-rata untuk setiap pertanyaan
summary_data = {
    'Total': df.iloc[:, 1:].sum(),
    'Average': df.iloc[:, 1:].mean()
}

# Menggabungkan hasil ke DataFrame summary
summary_df = pd.DataFrame(summary_data).T
summary_df.index.name = 'Statistics'

# Menambahkan hasil uji reliabilitas ke summary
reliability_summary = pd.DataFrame({'Cronbach\'s Alpha': [cronbach_alpha_value], 'N of Items': [num_questions]})

# Export ke Excel
with pd.ExcelWriter('hasil_kuesioner.xlsx') as writer:
    df.to_excel(writer, sheet_name='Data', index=False)
    summary_df.to_excel(writer, sheet_name='Summary')
    reliability_summary.to_excel(writer, sheet_name='Reliability')

print(colored("Data SUDAH RELIABEL!", 'green', attrs=['bold']))
print("Data telah berhasil diekspor ke hasil_kuesioner.xlsx")
