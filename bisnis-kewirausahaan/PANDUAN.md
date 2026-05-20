# 📖 PANDUAN LENGKAP — BisnisKu Tools
### Aplikasi Simulasi Keuangan & Business Plan Checker
### Prodi S1 Kewirausahaan — UM Metro

---

## ✅ LANGKAH 1 — Install Library (Lakukan Sekali Saja)

Buka **Terminal / Command Prompt**, ketik:

```
pip install streamlit pandas plotly
```

Tunggu sampai selesai (butuh internet).

---

## ✅ LANGKAH 2 — Jalankan di Laptop

1. Buka **Terminal / Command Prompt**
2. Masuk ke folder project:
   ```
   cd bisnis-kewirausahaan
   ```
3. Jalankan aplikasi:
   ```
   streamlit run app.py
   ```
4. Browser akan otomatis terbuka di: **http://localhost:8501**

---

## ✅ LANGKAH 3 — Upload ke GitHub (Agar Bisa Online)

### A. Buat Akun GitHub
- Buka: https://github.com
- Daftar gratis

### B. Buat Repository Baru
- Klik tombol **"New"** (tombol hijau)
- Nama repo: `bisnis-kewirausahaan`
- Pilih **Public**
- Klik **Create repository**

### C. Upload File
- Klik **"uploading an existing file"**
- Drag & drop semua file dari folder `bisnis-kewirausahaan`
- Klik **Commit changes**

---

## ✅ LANGKAH 4 — Deploy ke Streamlit Cloud (GRATIS, Jadi Online!)

1. Buka: https://streamlit.io
2. Klik **"Sign up"** → Login dengan akun GitHub
3. Klik **"New app"**
4. Pilih repository: `bisnis-kewirausahaan`
5. Main file path: `app.py`
6. Klik **"Deploy!"**
7. Tunggu 2-3 menit...
8. 🎉 Aplikasi Anda ONLINE di URL seperti:
   **https://bisnis-kewirausahaan.streamlit.app**

---

## 📁 STRUKTUR FILE

```
bisnis-kewirausahaan/
│
├── app.py                          ← Halaman utama (beranda)
├── requirements.txt                ← Daftar library (wajib ada)
├── PANDUAN.md                      ← File ini
└── pages/
    ├── 1_📊_Simulasi_Keuangan.py   ← Fitur simulasi keuangan
    └── 2_📝_Business_Plan_Checker.py ← Fitur business plan
```

---

## ❓ TROUBLESHOOTING

**"streamlit not found"**
→ Jalankan: `pip install streamlit`

**"ModuleNotFoundError: plotly"**
→ Jalankan: `pip install plotly`

**Browser tidak terbuka otomatis**
→ Buka manual: http://localhost:8501

---

## 📞 BANTUAN
Jika ada kendala, screenshot error-nya dan konsultasikan dengan
tim IT kampus atau dosen mata kuliah Teknologi Informasi.
