import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('Tugas LPK - Kelompok 8 (1C)')
st.header('Perhitungan Normalitas (N), %(b/b), %(b/v)')

# Buat Tabel BE
st.subheader ('Tabel Bobot Ekuivalen (mg/mgrek)')
st.markdown('''
|   Nama Senyawa  |Bobot Ekuivalen (mg/mgrek)|
|-----------------|--------------------------|
|   Asam Oksalat  |              63          |
|      Boraks     |             191          |
|   Asam Asetat   |              60          |
| Natrium Karbonat|              53          |
|       Besi      |              56          |
| Kalium Dikromat |              49          |
|      Klor       |             35,5         |
''')



#Menghitung Normalitas
st.subheader ('Menghitung Normalitas')
mgsampel = st.number_input ("Masukkan Nilai mg",0)
fp = st.number_input("Masukkan Nilai fp",0)
vsampel = st.number_input ("Masukkan Nilai V Sampel",0.000)
be = st.number_input ("Masukkan Nilai BE",0)
hitung = st.button ("Hitung Normalitas")

if hitung :
    Normalitas = mgsampel / (fp * vsampel * be)
    st.write ("Normalitas sampel = ", Normalitas)
    st.success(f"Normalitas sampel = {Normalitas}") 
    st.snow ()


# Perhitungan %b/b
st.subheader('Menghitung Kadar %(b/b)')
Normalitas=st.number_input("Masukkan Nilai Normalitas Titran (N)")
Volume=st.number_input("Masukkan Nilai Volume Titran (mL)")
be=st.number_input("Masukkan Nilai bobot ekuivalen(BE) Contoh (g)")
gram=st.number_input("Masukkan Nilai g Contoh")
fp=st.number_input("Masukkan Nilai FP")


tombol=st.button("Hitung Nilai Kadar (%(b/b))")

if tombol:
    nilai_persentase=Volume*Normalitas*be*fp*10**-3*100/(gram)
    st.success(f"Nilai Kadar (%(b/b)) adalah {nilai_persentase}")
    st.snow ()

# Perhitungan %b/v
st.subheader('Menghitung Kadar %(b/v)')
Normalitas=st.number_input("Masukkan Nilai N Titran")
volume=st.number_input("Masukkan Nilai V Titran (mL)")
be=st.number_input("Masukkan Nilai Berat Ekuivalen Contoh (g)")
v=st.number_input("Masukkan Nilai V Titrat")
FP=st.number_input("Masukkan Nilai fp")


tombol=st.button("Hitung Nilai Kadar (%(b/v))")

if tombol:
    nilai_persentase=volume*Normalitas*be*fp*10**-3*100/(v)
    st.success(f"Nilai Kadar (%(b/v)) adalah {nilai_persentase}")
    st.snow ()

#Gambar Tabel Periodik
st.subheader ('Tabel Periodik')
pilih = st.button ('Tampilkan')
if pilih :
    st.image ('tabel periodik.png')