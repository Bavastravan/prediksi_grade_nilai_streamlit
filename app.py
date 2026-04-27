import streamlit as st
import pandas as pd

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Grade Master Pro", 
    page_icon="🚀", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- KONFIGURASI BOBOT MATA KULIAH ---
MAPEL_CONFIG = {
    "Algoritma Pemrograman": {"tugas": 0.20, "uts": 0.25, "uas": 0.40, "hadir": 0.15},
    "Basis Data": {"tugas": 0.30, "uts": 0.20, "uas": 0.40, "hadir": 0.10},
    "Pemrograman Web": {"tugas": 0.40, "uts": 0.20, "uas": 0.30, "hadir": 0.10},
    "Matematika Diskrit": {"tugas": 0.15, "uts": 0.35, "uas": 0.40, "hadir": 0.10}
}

# --- STYLE CSS ---
st.markdown("""
    <style>
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    .stExpander { border: none !important; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border-radius: 10px; }
    .stButton>button { border-radius: 8px; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

# --- DATABASE SESSION STATE ---
if 'user_db' not in st.session_state:
    st.session_state['user_db'] = {"admin": "12345"}
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'data_mahasiswa' not in st.session_state:
    st.session_state['data_mahasiswa'] = []
if 'editing_index' not in st.session_state:
    st.session_state['editing_index'] = None

# --- FUNGSI LOGIN & REGISTER ---
def login_page():
    _, col_mid, _ = st.columns([1, 2, 1])
    with col_mid:
        st.title("🔐 Grade Master")
        tab1, tab2 = st.tabs(["Masuk", "Daftar Akun"])
        with tab1:
            with st.form("login_form"):
                user = st.text_input("Username")
                pw = st.text_input("Password", type="password")
                if st.form_submit_button("LOGIN", use_container_width=True):
                    if user in st.session_state['user_db'] and st.session_state['user_db'][user] == pw:
                        st.session_state['logged_in'] = True
                        st.session_state['username'] = user
                        st.rerun()
                    else:
                        st.error("Username atau Password salah.")
        with tab2:
            with st.form("register_form"):
                new_user = st.text_input("Username Baru")
                new_pw = st.text_input("Password Baru", type="password")
                if st.form_submit_button("BUAT AKUN", use_container_width=True):
                    if new_user and new_pw:
                        st.session_state['user_db'][new_user] = new_pw
                        st.success("Akun berhasil dibuat! Silakan login.")

# --- HALAMAN UTAMA ---
def main_dashboard():
    with st.sidebar:
        st.title("🚀 Master Pro")
        st.markdown(f"User: **{st.session_state['username']}**")
        st.divider()
        menu = st.radio("MENU UTAMA", ["📊 Kalkulator & Input", "📂 Database Mahasiswa"], label_visibility="collapsed")
        st.divider()
        if st.button("🚪 Keluar", use_container_width=True):
            st.session_state['logged_in'] = False
            st.rerun()

    if menu == "📊 Kalkulator & Input":
        st.title("📊 Input Nilai & Kalkulator")
        
        with st.expander("📝 Form Data Akademik", expanded=True):
            c1, c2, c3 = st.columns([2, 1, 2])
            with c1:
                nama = st.text_input("Nama Lengkap")
            with c2:
                nim = st.text_input("NIM")
            with c3:
                matkul = st.selectbox("Mata Kuliah", list(MAPEL_CONFIG.keys()))

            st.divider()
            
            bobot = MAPEL_CONFIG[matkul]
            st.caption(f"💡 Bobot {matkul}: Tugas {bobot['tugas']*100:.0f}%, UTS {bobot['uts']*100:.0f}%, UAS {bobot['uas']*100:.0f}%, Kehadiran {bobot['hadir']*100:.0f}%")

            n1, n2, n3, n4 = st.columns(4)
            with n1:
                tugas = st.number_input("Tugas", 0, 100, 80)
            with n2:
                uts = st.number_input("UTS", 0, 100, 75)
            with n3:
                uas = st.number_input("UAS", 0, 100, 85)
            with n4:
                hadir_input = st.number_input("Kehadiran (0-14)", 0, 14, 14)
                skala_hadir = (hadir_input / 14) * 100

            nilai_akhir = (tugas * bobot['tugas']) + (uts * bobot['uts']) + (uas * bobot['uas']) + (skala_hadir * bobot['hadir'])
            
            if nilai_akhir >= 85: grade, warna, emo, pesan = "A", "green", "🏆", "Sangat Memuaskan! Pertahankan prestasimu."
            elif nilai_akhir >= 75: grade, warna, emo, pesan = "B", "blue", "🎈", "Kerja Bagus! Tingkatkan sedikit lagi untuk nilai A."
            elif nilai_akhir >= 60: grade, warna, emo, pesan = "C", "orange", "😕", "Cukup Baik. Jangan lupa belajar lebih giat lagi."
            elif nilai_akhir >= 45: grade, warna, emo, pesan = "D", "red", "😭", "Kurang Memuaskan. Segera perbaiki metode belajarmu."
            else: grade, warna, emo, pesan = "E", "red", "😱", "Gagal. Kamu harus mengulang mata kuliah ini."

            # Tampilan Hasil Utama
            st.markdown(f"### Hasil Perhitungan: :{warna}[Grade {grade}] ({nilai_akhir:.1f})")

            # --- FEEDBACK VISUAL (Selalu Muncul Setiap Perubahan) ---
            if grade == "A":
                st.success(f"**{emo} {pesan}**")
                st.balloons()
            elif grade == "B":
                st.info(f"**{emo} {pesan}**")
                st.balloons()
            elif grade == "C":
                st.warning(f"**{emo} {pesan}**")
            elif grade == "D":
                st.error(f"**{emo} {pesan}**")
            elif grade == "E":
                st.error(f"**{emo} {pesan}**")

            st.divider()
            
            if st.button("➕ SIMPAN DATA KE DATABASE", use_container_width=True, type="primary"):
                if nama and nim:
                    data = {
                        "NIM": nim, "Nama": nama, "Mata Kuliah": matkul,
                        "Tugas": tugas, "UTS": uts, "UAS": uas, "Hadir": hadir_input,
                        "Akhir": round(nilai_akhir, 2), "Grade": grade
                    }
                    st.session_state['data_mahasiswa'].append(data)
                    st.toast(f"Data {nama} berhasil disimpan!", icon="✅")
                else:
                    st.error("Nama dan NIM wajib diisi!")

    elif menu == "📂 Database Mahasiswa":
        st.title("📂 Database Mahasiswa")
        if not st.session_state['data_mahasiswa']:
            st.warning("Belum ada data mahasiswa yang tersimpan.")
        else:
            df = pd.DataFrame(st.session_state['data_mahasiswa'])
            st.dataframe(df, use_container_width=True, hide_index=True)
            
            st.divider()
            st.subheader("🛠️ Manajemen Data")
            list_data = [f"{d['NIM']} - {d['Nama']} ({d['Mata Kuliah']})" for d in st.session_state['data_mahasiswa']]
            target_idx = st.selectbox("Pilih Data Mahasiswa:", range(len(list_data)), format_func=lambda x: list_data[x])

            col_edit, col_del = st.columns(2)
            
            with col_edit:
                if st.button("📝 EDIT DATA", use_container_width=True):
                    st.session_state['editing_index'] = target_idx
            
            with col_del:
                if st.button("🗑️ HAPUS DATA", use_container_width=True, type="primary"):
                    st.session_state['data_mahasiswa'].pop(target_idx)
                    st.success("Data berhasil dihapus!")
                    st.rerun()

            if st.session_state['editing_index'] is not None:
                idx = st.session_state['editing_index']
                data_lama = st.session_state['data_mahasiswa'][idx]
                
                st.info(f"Sedang mengedit data: **{data_lama['Nama']}**")
                with st.form("edit_form"):
                    e_c1, e_c2 = st.columns(2)
                    e_nama = e_c1.text_input("Nama Lengkap", value=data_lama['Nama'])
                    e_nim = e_c2.text_input("NIM", value=data_lama['NIM'])
                    e_matkul = st.selectbox("Mata Kuliah", list(MAPEL_CONFIG.keys()), index=list(MAPEL_CONFIG.keys()).index(data_lama['Mata Kuliah']))
                    
                    e_n1, e_n2, e_n3, e_n4 = st.columns(4)
                    e_tugas = e_n1.number_input("Tugas", 0, 100, data_lama['Tugas'])
                    e_uts = e_n2.number_input("UTS", 0, 100, data_lama['UTS'])
                    e_uas = e_n3.number_input("UAS", 0, 100, data_lama['UAS'])
                    e_hadir = e_n4.number_input("Kehadiran (0-14)", 0, 14, data_lama['Hadir'])
                    
                    col_save, col_cancel = st.columns(2)
                    if col_save.form_submit_button("💾 UPDATE DATA", use_container_width=True):
                        b = MAPEL_CONFIG[e_matkul]
                        n_akhir = (e_tugas * b['tugas']) + (e_uts * b['uts']) + (e_uas * b['uas']) + ((e_hadir/14*100) * b['hadir'])
                        
                        n_grade = "A" if n_akhir >= 85 else "B" if n_akhir >= 75 else "C" if n_akhir >= 60 else "D" if n_akhir >= 45 else "E"
                        
                        st.session_state['data_mahasiswa'][idx] = {
                            "NIM": e_nim, "Nama": e_nama, "Mata Kuliah": e_matkul,
                            "Tugas": e_tugas, "UTS": e_uts, "UAS": e_uas, "Hadir": e_hadir,
                            "Akhir": round(n_akhir, 2), "Grade": n_grade
                        }
                        st.session_state['editing_index'] = None
                        st.success("Data berhasil diperbarui!")
                        st.rerun()
                    
                    if col_cancel.form_submit_button("❌ BATAL", use_container_width=True):
                        st.session_state['editing_index'] = None
                        st.rerun()

# --- ROUTING ---
if st.session_state['logged_in']:
    main_dashboard()
else:
    login_page()

st.markdown("---")
st.caption("🚀 Grade Master Pro v2.3 | CRUD & Instant Feedback System")