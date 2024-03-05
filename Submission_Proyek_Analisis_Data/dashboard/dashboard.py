import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

bike_day_df = pd.read_csv(r"D:\Bangkit\tugas\Submission_Proyek_Analisis_Data\dataset\day.csv")

# Judul Dashboard
st.title("Dashboard: Analisis Data Bike Sharing")

# Menampilkan Data
st.subheader("Data Bike Sharing")
st.write(bike_day_df.head())

# Tampilan Sidebar
st.sidebar.title("Proyek Analisis Data")
st.sidebar.markdown("---")
st.sidebar.markdown("ML-79 | Muhammad Kusyairi Ihsan")

# Visualization Penyewaan sepeda berdasarkan kondisi cuaca
st.subheader("Penyewaan Sepeda berdasarkan Kondisi Cuaca")
fig, ax = plt.subplots(figsize=(8,4))
sns.barplot(
    x='weathersit',
    y='cnt',
    data=bike_day_df,
    hue='weathersit',
    palette='plasma',
    legend=False)

plt.title('Jumlah Penyewa Sepeda berdasarkan Kondisi Cuaca')
plt.xlabel('Keterangan: 1 = Cerah, 2 = Mendung, 3 = Hujan')
plt.ylabel('Jumlah Penyewa Sepeda')
st.pyplot(fig)

# Visualization pattern penggunaan sepeda dari waktu ke waktu
dtedayPD = pd.to_datetime(bike_day_df['dteday'])

st.subheader("pattern penggunaan sepeda dari waktu ke waktu")
fig, ax = plt.subplots(figsize=(8, 4))
bike_day_df['dteday'] = pd.to_datetime(bike_day_df['dteday'])
plt.plot(
    bike_day_df['dteday'], 
    bike_day_df['cnt'], 
    marker='o', 
    linestyle='-')

plt.title('pattern penggunaan sepeda berubah dari waktu ke waktu')
plt.xlabel('Waktu')
plt.ylabel('Jumlah Peminjaman Sepeda')
plt.xticks(rotation=45)
st.pyplot(fig)

# CopyRight
st.markdown("---")
st.markdown("CopyRight © 2024 | Muhammad Kusyairi Ihsan")