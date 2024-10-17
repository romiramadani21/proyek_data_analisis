import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

# Set style seaborn
sns.set(style='dark')

# Membuat judul
st.header('Bike Rental Dashboard 🚲')

# Membaca data
day_df = pd.read_csv("dashboard/day.csv")
hr_df = pd.read_csv("dashboard/hour.csv")

# Menghapus duplikasi
day_df.drop_duplicates(inplace=True)
hr_df.drop_duplicates(inplace=True)

# Mengisi missing values dengan forward fill
day_df.fillna(method='ffill', inplace=True)
hr_df.fillna(method='ffill', inplace=True)

# Mengubah nama kolom
day_df.rename(columns={
    'dteday': 'dateday', 'yr': 'year', 'mnth': 'month',
    'weathersit': 'weather_cond', 'cnt': 'count'
}, inplace=True)

# Mengubah angka menjadi kategori di beberapa kolom
day_df['month'] = day_df['month'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
})

day_df['season'] = day_df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})

day_df['weekday'] = day_df['weekday'].map({
    0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'
})

day_df['weather_cond'] = day_df['weather_cond'].map({
    1: 'Cerah/Mendung', 2: 'Kabut/Mendung', 3: 'Hujan/Snow'
})

# Mengubah tipe data obj ke datetime
day_df['dateday'] = pd.to_datetime(day_df.dateday)

# Mengubaha tipe data ke categorical
day_df['season'] = day_df.season.astype('category')
day_df['year'] = day_df.year.astype('category')
day_df['month'] = day_df.month.astype('category')
day_df['holiday'] = day_df.holiday.astype('category')
day_df['weekday'] = day_df.weekday.astype('category')
day_df['workingday'] = day_df.workingday.astype('category')
day_df['weather_cond'] = day_df.weather_cond.astype('category')

st.subheader('Tabel Data Day')
st.write(day_df.head())

# Mengubah nama judul kolom pada tabel hour
hr_df.rename(columns={
    'dteday': 'dateday',
    'yr': 'year',
    'mnth': 'month',
    'hr' : 'hour',
    'weathersit': 'weather_cond',
    'cnt': 'count'
}, inplace=True)

# Mengubah angka menjadi keterangan pada beberapa kolom di tabel hour
hr_df['month'] = hr_df['month'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
})

hr_df['season'] = hr_df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})

hr_df['weekday'] = hr_df['weekday'].map({
    0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'
})

hr_df['weather_cond'] = hr_df['weather_cond'].map({
    1: 'Clear/Partly Cloudy',
    2: 'Misty/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Severe Weather'
})

hr_df['dateday'] = pd.to_datetime(hr_df.dateday)

# Mengubaha tipe data ke categorical
hr_df['season'] = hr_df.season.astype('category')
hr_df['year'] = hr_df.year.astype('category')
hr_df['month'] = day_df.month.astype('category')
hr_df['holiday'] = hr_df.holiday.astype('category')
hr_df['weekday'] = hr_df.weekday.astype('category')
hr_df['workingday'] = hr_df.workingday.astype('category')
hr_df['weather_cond'] = hr_df.weather_cond.astype('category')

st.subheader('Tabel Data Hour')
st.write(hr_df.head())

# Membuat komponen filter
min_date = pd.to_datetime(day_df['dateday']).dt.date.min()
max_date = pd.to_datetime(day_df['dateday']).dt.date.max()
 
with st.sidebar:
    st.image('data:image/png;base64,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')
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value= min_date,
        max_value= max_date,
        value=[min_date, max_date]
    )

main_df = day_df[(day_df['dateday'] >= str(start_date)) & 
                (day_df['dateday'] <= str(end_date))]

# ************************* START VISUALIZATION ***************************************
st.subheader('Pola Penggunaan Sepeda Berdasarkan Hari dalam Seminggu')
# Menambahkan palet warna agar lebih menarik
sns.set_palette('Set2')

# Pola penggunaan sepeda mingguan
plt.figure(figsize=(10, 6))
sns.barplot(x='weekday', y='count', data=day_df, ci=None, palette='Set2')
plt.title('Pola Penggunaan Sepeda Berdasarkan Hari dalam Seminggu')
plt.xticks(ticks=range(7), labels=['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'])
plt.xlabel('Hari dalam Seminggu')
plt.ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(plt.gcf())

# Pola penggunaan sepeda berdasarkan bulan
plt.figure(figsize=(10, 6))
sns.barplot(x='month', y='count', data=day_df, ci=None, palette='Paired')
plt.title('Pola Penggunaan Sepeda Berdasarkan Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(plt.gcf())

# Musim (1: Musim Semi, 2: Musim Panas, 3: Musim Gugur, 4: Musim Dingin)
plt.figure(figsize=(10, 6))
sns.barplot(x='season', y='count', data=day_df, ci=None, palette='coolwarm')
plt.title('Pola Penggunaan Sepeda Berdasarkan Musim')
plt.xlabel('Musim')
plt.ylabel('Jumlah Penyewaan Sepeda')
plt.xticks(ticks=[1, 2, 3, 4], labels=['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'])
st.pyplot(plt.gcf())

st.subheader('Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda')
plt.figure(figsize=(10, 6))
sns.boxplot(x='weather_cond', y='count', data=day_df, palette='husl')
plt.title('Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda')
plt.xlabel('Situasi Cuaca')
plt.ylabel('Jumlah Penyewaan Sepeda')
plt.xticks(ticks=[1, 2, 3], labels=['Cerah/Mendung', 'Kabut/Mendung', 'Hujan/Snow'])
st.pyplot(plt.gcf())

st.subheader('Pengaruh Suhu terhadap Jumlah Penyewaan Sepeda')
plt.figure(figsize=(10, 6))
sns.scatterplot(x='temp', y='count', data=day_df, hue='season', palette='Spectral', s=100)
plt.title('Pengaruh Suhu terhadap Jumlah Penyewaan Sepeda')
plt.xlabel('Suhu (Dinormalisasi)')
plt.ylabel('Jumlah Penyewaan Sepeda')
plt.legend(title='Musim')
st.pyplot(plt.gcf())

st.subheader('Pengaruh Hari Kerja atau Akhir Pekan terhadap Jumlah Penyewaan Sepeda')
plt.figure(figsize=(10, 6))
sns.barplot(x='workingday', y='count', data=day_df, ci=None, palette='cubehelix')
plt.title('Pengaruh Hari Kerja atau Akhir Pekan terhadap Jumlah Penyewaan Sepeda')
plt.xticks(ticks=[0, 1], labels=['Akhir Pekan', 'Hari Kerja'])
plt.xlabel('Tipe Hari')
plt.ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(plt.gcf())

# Membuat kolom baru untuk kategori pengguna
hr_df['user_type'] = hr_df.apply(lambda row: 'Casual' if row['casual'] > 0 else 'Registered', axis=1)

# Visualisasi perbandingan penyewaan sepeda berdasarkan kategori pengguna
st.subheader('Perbandingan penyewaan sepeda berdasarkan kategori pengguna')
plt.figure(figsize=(10, 6))
sns.barplot(x='hour', y='count', hue='user_type', data=hr_df, ci=None, palette='Set2')
plt.title('Perbandingan Penggunaan Sepeda Berdasarkan Kategori Pengguna (Casual vs Registered)')
plt.xlabel('Jam')
plt.ylabel('Jumlah Penyewaan Sepeda')
plt.legend(title='Kategori Pengguna')
st.pyplot(plt.gcf())

# Menambahkan kolom estimasi durasi
# Asumsi: Durasi penyewaan adalah total penyewaan dalam satu jam (cnt) dibagi dengan jam kerja (8 jam kerja/hari)
hr_df['estimated_duration'] = hr_df['count'] / (24 / 8)  # 8 jam kerja per hari
st.subheader('Estimasi Durasi Penyewaan Sepeda Berdasarkan Jam dan Musim')
# Visualisasi estimasi durasi penyewaan berdasarkan jam
plt.figure(figsize=(10, 6))
sns.lineplot(x='hour', y='estimated_duration', data=hr_df, hue='season', palette='coolwarm', ci=None)
plt.title('Estimasi Durasi Penyewaan Sepeda Berdasarkan Jam dan Musim')
plt.xlabel('Jam')
plt.ylabel('Estimasi Durasi Penyewaan (jam)')
plt.legend(title='Musim')
st.pyplot(plt.gcf())

# Visualisasi pengaruh suhu terhadap estimasi durasi penyewaan
plt.figure(figsize=(10, 6))
sns.scatterplot(x='temp', y='estimated_duration', data=hr_df, hue='season', palette='Spectral', s=100)
plt.title('Pengaruh Suhu terhadap Estimasi Durasi Penyewaan')
plt.xlabel('Suhu (Dinormalisasi)')
plt.ylabel('Estimasi Durasi Penyewaan (jam)')
plt.legend(title='Musim')
st.pyplot(plt.gcf())

# Visualisasi pengaruh cuaca terhadap estimasi durasi penyewaan
plt.figure(figsize=(10, 6))
sns.boxplot(x='weather_cond', y='estimated_duration', data=hr_df, palette='husl')
plt.title('Pengaruh Cuaca terhadap Estimasi Durasi Penyewaan')
plt.xlabel('Situasi Cuaca')
plt.ylabel('Estimasi Durasi Penyewaan (jam)')
plt.xticks(ticks=[1, 2, 3], labels=['Cerah/Mendung', 'Kabut/Mendung', 'Hujan/Snow'])
st.pyplot(plt.gcf())


st.subheader('Analisis Lanjutan RFM')
import datetime as dt
# Menentukan tanggal sewa berdasarkan tahun dan bulan dari dataset
hr_df['date'] = pd.to_datetime(hr_df['dateday'])

# Menghitung Recency
# Misalkan kita gunakan tanggal analisis adalah 2021-12-31
analysis_date = dt.datetime(2021, 12, 31)
recency_df = hr_df.groupby('date')['count'].sum().reset_index()
recency_df['Recency'] = (analysis_date - recency_df['date']).dt.days

# Menghitung Frequency dan Monetary
frequency_df = hr_df.groupby('date')['count'].sum().reset_index()
frequency_df['Frequency'] = frequency_df['count']  # Menganggap setiap baris sebagai frekuensi sewa
monetary_df = hr_df.groupby('date')['count'].sum().reset_index()
monetary_df['Monetary'] = monetary_df['count']  # Total penyewaan

# Menggabungkan nilai RFM
rfm_df = recency_df[['Recency']].merge(frequency_df[['Frequency']], left_index=True, right_index=True).merge(monetary_df[['Monetary']], left_index=True, right_index=True)

# Visualisasi RFM
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Recency', y='Frequency', size='Monetary', data=rfm_df, sizes=(20, 400), alpha=0.6)
plt.title('RFM Analysis: Recency vs Frequency')
plt.xlabel('Recency (Days since last rental)')
plt.ylabel('Frequency (Total Rentals)')
plt.grid(True)
st.pyplot(plt.gcf())

st.write(
     """
   ### Conclusion
1. Bagaimana pola penggunaan sepeda berbagi berdasarkan waktu? (harian, mingguan, bulanan, atau musiman).

 - Berdasarkan grafik pola pengggunaan sepeda untuk terbanyak terjadi pada hari jumat ini menunjukkan penyewa dapat meningkatkan jumlah sepeda untuk dihari tersebut.
 - Berdasarkan grafik penggunaan sepeda paling banyak dibulan september dan musim yang banyak penyewa adalah musim semi.

2. Faktor-faktor apa saja yang paling mempengaruhi jumlah penyewaan sepeda? (cuaca, hari kerja atau akhir pekan, suhu, dll.)
    
    Berdasarkan boxplot dan grafik faktor yang mempengaruhi jumlah penyewaan sepeda terjadi pada cuaca cerah/mendung untuk penyewaan yang lebih banyak, kemudian penyewaan terbanyak terjadi pada musim fall dan penyewaan lebih banyak pada hari kerja atau biasa dibandingkan akhir pekan.

3. Apakah ada perbedaan penggunaan sepeda berdasarkan kategori pengguna (misalnya, member vs non-member)?
    
    Berdasarkan grafik penggunaan lebih banyak terjadi pada pengguna dengan kategori non - member ini bisa menjadi sasaran untuk marketing supaya menarik pengguna biasa menjadi member

4. Seberapa lama durasi rata-rata penyewaan sepeda, dan faktor apa saja yang mempengaruhi durasi penyewaan?
    
    Berdasarkan grafik durasi penyewaan sepeda rata rata banyak dimusim fall, kemudian pada musim winter yang cenderung durasi penyewaan lebih lama dan estimasi penyewaan untuk cuaca cerah/mendung cukup mempengaruhi penjimaman sepeda.

5. Bagaimana cara mengoptimalkan penyediaan sepeda agar tersedia ketika dibutuhkan di lokasi yang tepat?
    
    Berdasarkan grafik dapat disimpulkan ; Pelanggan dengan frequency tinggi dan recency rendah (pada sisi kiri atas grafik) menunjukkan bahwa di beberapa lokasi, sepeda sering digunakan dan baru saja disewa. Pelanggan dengan frequency rendah dan recency tinggi (sisi kanan bawah) menandakan lokasi atau pelanggan yang tidak lagi aktif menyewa. Sepeda perlu ditempatkan sebelum aktivitas rental mencapai puncak (yaitu di area dengan frequency tinggi). Dengan memantau pola recency dan frekuensi dari data sebelumnya, penyedia bisa memperkirakan kapan dan di mana sepeda akan paling dibutuhkan. Ukuran bubble di grafik menunjukkan bahwa pelanggan yang bertransaksi lebih besar (monetary tinggi) cenderung berada di area dengan frequency tinggi.
    """
)

# Footer
st.markdown("---")
st.markdown("Copyright 2024 ©️ Romi Ramadani")