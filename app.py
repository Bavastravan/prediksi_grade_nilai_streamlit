import streamlit as st

st.set_page_config(page_title="Grade Master Pro", page_icon="🚀")

st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR INPUT ---
with st.sidebar:
    st.header("📥 Input Nilai")
    st.info("Geser slider atau ketik nilai di bawah ini.")
    
    tugas = st.slider("Nilai Tugas (20%)", 0, 100, 75)
    uts = st.slider("Nilai UTS (30%)", 0, 100, 70)
    uas = st.slider("Nilai UAS (50%)", 0, 100, 80)
    
    st.divider()
    calculate = st.button("🚀 Hitung Sekarang", use_container_width=True)

# --- LOGIKA PERHITUNGAN ---
# Rumus: (Tugas * 0.2) + (UTS * 0.3) + (UAS * 0.5)
nilai_akhir = (tugas * 0.2) + (uts * 0.3) + (uas * 0.5)

# --- DASHBOARD UTAMA ---
st.title("📊 Dashboard Evaluasi Mahasiswa")
st.write("Sistem otomatisasi penentuan grade berbasis bobot akademik.")

if calculate:
    # Penentuan Grade & Status dengan Logika If-Then
    if nilai_akhir >= 85:
        grade, status, pesan, warna = "A", "LULUS", "Sangat Memuaskan! Pertahankan.", "#28a745"
    elif nilai_akhir >= 75:
        grade, status, pesan, warna = "B", "LULUS", "Kerja bagus! Sedikit lagi menuju sempurna.", "#17a2b8"
    elif nilai_akhir >= 60:
        grade, status, pesan, warna = "C", "LULUS", "Cukup, tapi perlu ditingkatkan lagi.", "#ffc107"
    elif nilai_akhir >= 45:
        grade, status, pesan, warna = "D", "REMIDI", "Nilai di bawah standar, segera hubungi dosen.", "#fd7e14"
    else:
        grade, status, pesan, warna = "E", "GAGAL", "Wajib mengulang mata kuliah di semester depan.", "#dc3545"

    col1, col2, col3 = st.columns(3)
    col1.metric("Nilai Akhir", f"{nilai_akhir:.1f}")
    col2.metric("Grade", grade)
    col3.metric("Status", status)

    
    st.write(f"**Progress Nilai:** {nilai_akhir}%")
    st.progress(int(nilai_akhir))

   
    st.markdown(f"""
        <div style="background-color: {warna}; padding: 20px; border-radius: 10px; color: white;">
            <h3 style="margin: 0;">{status}</h3>
            <p style="margin: 5px 0 0 0;">{pesan}</p>
        </div>
        """, unsafe_allow_html=True)
    
    if grade in ["A", "B"]:
        st.balloons()
else:
    st.warning("Silakan atur nilai di sidebar dan klik 'Hitung Sekarang' untuk melihat hasil.")

# --- FOOTER ---
st.caption("Developed with ❤️ using Streamlit")