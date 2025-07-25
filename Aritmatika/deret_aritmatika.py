import streamlit as st
import time
import pandas as pd # Menambahkan import pandas untuk visualisasi tabel

def calculate_arithmetic_series(a, b, n_terms):
    """Menghitung dan mengembalikan deret aritmatika."""
    series = [a + (i * b) for i in range(n_terms)]
    return series

st.set_page_config(
    page_title="Kalkulator Deret Aritmatika Interaktif",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Kalkulator Deret Aritmatika Interaktif")
st.markdown("""
Aplikasi ini dirancang untuk membantu Anda *memahami dan menemukan rumus deret aritmatika ($U_n = a + (n-1)b$)* secara interaktif.
Coba ubah nilai-nilai di sidebar dan perhatikan bagaimana deret terbentuk!
""")

st.markdown("---")

# --- Sidebar untuk Input ---
st.sidebar.header("Pengaturan Deret Aritmatika")
initial_term = st.sidebar.number_input("Suku Pertama (a):", value=5, step=1)
common_difference = st.sidebar.number_input("Beda (b):", value=3, step=1)
num_terms = st.sidebar.slider("Jumlah Suku (n):", min_value=1, max_value=15, value=5)
animation_speed = st.sidebar.slider("Kecepatan Animasi (detik/suku):", min_value=0.1, max_value=2.0, value=0.5, step=0.1)

st.sidebar.markdown("---")
st.sidebar.markdown("""
*Aplikasi ini sangat cocok digunakan untuk:*
- Pelajar sekolah menengah
- Mahasiswa tingkat dasar
- Guru sebagai media bantu pembelajaran interaktif
""")

# --- Bagian Utama Aplikasi ---
st.header("Pembentukan Deret Aritmatika")
st.write(f"*Suku Pertama (a):* {initial_term}")
st.write(f"*Beda (b):* {common_difference}")
st.write(f"*Jumlah Suku (n):* {num_terms}")

placeholder_series = st.empty()
placeholder_un_formula = st.empty()

# Animasi Pembentukan Deret
current_series_display = []
series_values = []
un_value = 0

for i in range(num_terms):
    current_term = initial_term + (i * common_difference)
    series_values.append(current_term)
    current_series_display.append(f"$U_{i+1} = {current_term}$")

    with placeholder_series.container():
        st.write("Deret yang Terbentuk:")
        st.markdown(f"*{' | '.join(current_series_display)}*")

    # Update Un formula explanation step-by-step
    with placeholder_un_formula.container():
        st.markdown("---")
        st.subheader("Menemukan Rumus $U_n$")
        if i == 0:
            st.write(f"Suku pertama $U_1 = a = {initial_term}$")
        else:
            st.write(f"Suku $U_2 = a + b = {initial_term} + {common_difference} = {initial_term + common_difference}$")
            st.write(f"Suku $U_3 = a + b + b = a + 2b = {initial_term} + 2 \\times {common_difference} = {initial_term + 2 * common_difference}$")
            st.write(f"...")
            st.markdown(f"*Suku ke-$n$ ($U_n$) dapat dirumuskan sebagai:*")
            st.markdown(f"$$U_n = a + (n-1)b$$")
            st.markdown(f"Untuk suku ke-$U_{i+1}$, maka $U_{i+1} = a + ({i+1}-1)b = a + {i}b$")
            st.write(f"$U_{i+1} = {initial_term} + {i} \\times {common_difference} = {current_term}$")

    time.sleep(animation_speed)

# Menampilkan hasil akhir
st.markdown("---")
st.subheader("Hasil Akhir Perhitungan")
final_series = calculate_arithmetic_series(initial_term, common_difference, num_terms)
st.write(f"*Deret yang terbentuk:* {', '.join(map(str, final_series))}")

# Hitung dan tampilkan suku ke-n terakhir
final_un_value = initial_term + ((num_terms - 1) * common_difference)
st.markdown(f"*Suku ke-$n$ (yaitu suku ke-{num_terms}) adalah:*")
st.markdown(f"$$U_{num_terms} = a + ({num_terms}-1)b = {initial_term} + ({num_terms}-1){common_difference} = {final_un_value}$$")

st.markdown("---")
st.info("Dengan melihat bagaimana setiap suku terbentuk dan perbedaannya selalu konstan, Anda bisa memahami mengapa rumus $U_n = a + (n-1)b$ bekerja!")
