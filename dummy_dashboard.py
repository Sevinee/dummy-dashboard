# -*- coding: utf-8 -*-
"""dummy dashboard.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AbQfdJ0Tfx-oMv469XHzVLJ1p-IS1XUe
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Forecast USD/IDR", layout="centered")
st.title("📈 Prediksi Nilai Tukar USD ke IDR")
st.subheader("Model: LSTM + Variabel Makroekonomi")

df = pd.read_excel("hasil_prediksi.xlsx")

st.write("📄 Data Hasil Prediksi vs Aktual:")
st.dataframe(df[['Tanggal', 'Actual', 'Predicted']])

st.write("📊 Grafik Perbandingan:")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df['Tanggal'], df['Actual'], label='Actual', marker='o')
ax.plot(df['Tanggal'], df['Predicted'], label='Predicted', marker='x')
ax.set_title('Prediksi vs Aktual USD/IDR')
ax.set_ylabel('Kurs IDR')
ax.set_xlabel('Tanggal')
plt.xticks(rotation=45)
ax.legend()
st.pyplot(fig)

st.caption("Data diproses dan diprediksi secara otomatis oleh model LSTM harian.")