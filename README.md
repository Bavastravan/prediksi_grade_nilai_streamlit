# 🎓 Grade Master Pro

**Grade Master Pro** adalah aplikasi berbasis web sederhana yang dibangun menggunakan framework **Streamlit**. Aplikasi ini berfungsi sebagai alat bantu dosen atau mahasiswa untuk menghitung nilai akhir secara otomatis berdasarkan bobot akademik dan logika keputusan yang sistematis.

---

## 🚀 Fitur Utama

* **Sistem Otentikasi (Login)**: Keamanan dasar untuk membatasi akses pengguna.
* **Perhitungan Berbobot Otomatis**: Kalkulasi presisi berdasarkan bobot:
    * Tugas: **20%**
    * UTS: **30%**
    * UAS: **50%**
* **Sistem Klasifikasi Grade**: Penentuan grade otomatis menggunakan logika percabangan.
* **UI/UX Modern**: Menggunakan sidebar, progress bar, dan kartu status dinamis.
* **Efek Interaktif**: Animasi selebrasi (balloons) untuk hasil memuaskan.

---

## 🧠 Logika Percabangan (If-Then Logic)

Proyek ini menerapkan struktur kontrol **If-Then-Else** di bagian utama:

### Logika Penentuan Grade & Status
Setelah nilai akhir dihitung, sistem menjalankan logika bertingkat:
- **IF** Nilai $\ge 85$: **Grade A** (Lulus - Istimewa)
- **ELIF** Nilai $\ge 75$: **Grade B** (Lulus - Sangat Baik)
- **ELIF** Nilai $\ge 60$: **Grade C** (Lulus - Cukup)
- **ELIF** Nilai $\ge 45$: **Grade D** (Remidi - Kurang)
- **ELSE**: **Grade E** (Gagal - Wajib Mengulang)

---

## 🛠️ Persyaratan Sistem

Pastikan perangkat Anda sudah terpasang perangkat lunak berikut:
* **Python**: Versi 3.7 atau yang lebih baru.
* **Streamlit**: Framework utama aplikasi.

### Instalasi Library
```bash
pip install streamlit