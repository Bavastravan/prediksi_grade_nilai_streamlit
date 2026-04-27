# 🎓 Grade Master Pro v2.3
> **Sistem Manajemen Nilai Akademik Berbasis Web dengan Streamlit**

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🌟 Deskripsi Proyek
**Grade Master Pro** adalah solusi digital modern yang dirancang untuk membantu tenaga pengajar mengelola nilai mahasiswa secara efisien. Menggunakan logika **Sistem Cerdas** untuk kalkulasi dinamis, aplikasi ini menawarkan pengalaman pengguna yang interaktif dan responsif.

---

## 🚀 Fitur Unggulan

### 🔐 1. Otentikasi Pengguna
Sistem Login dan Registrasi yang aman menggunakan manajemen sesi (`st.session_state`).
### 📊 2. Kalkulator Berbobot Dinamis
Perhitungan otomatis yang menyesuaikan bobot nilai berdasarkan mata kuliah yang dipilih:
* **Sistem Cerdas**: Fokus pada akurasi logika dan kehadiran.
* **Algoritma & Basis Data**: Kombinasi UTS, UAS, dan Tugas.
### 🛠️ 3. Manajemen Data CRUD (Full)
* **Create**: Input data mahasiswa & nilai secara instan.
* **Read**: Visualisasi database dalam tabel interaktif (Pandas).
* **Update**: Fitur **Edit** data tanpa perlu menghapus inputan lama.
* **Delete**: Hapus data mahasiswa secara spesifik.
### ✨ 4. Feedback Visual Interaktif
Aplikasi memberikan respon psikologis melalui animasi:
* **Balloons** 🎈 untuk perayaan prestasi (Grade A & B).
* **Snow** ❄️ untuk peringatan nilai rendah (Grade D & E).

---

## 🧠 Logika Keputusan (Decision Logic)

Sistem menggunakan alur percabangan **If-Then-Else** untuk menentukan Grade:

| Rentang Nilai | Grade | Status | Feedback |
| :--- | :---: | :--- | :--- |
| 85.0 - 100.0 | **A** | Lulus (Istimewa) | 🏆 Balloons |
| 75.0 - 84.9 | **B** | Lulus (Baik) | 🎈 Balloons |
| 60.0 - 74.9 | **C** | Lulus (Cukup) | 😕 Info Box |
| 45.0 - 59.9 | **D** | Remidi (Kurang) | 😭 Snow |
| < 45.0 | **E** | Gagal | 😱 Snow |

---

## 🛠️ Instalasi & Penggunaan

### 1. Prasyarat
Pastikan Anda memiliki Python 3.8+ terinstal di perangkat Anda.

### 2. Instalasi Library
Buka terminal/CMD dan jalankan perintah:
```bash
pip install streamlit pandas