# Klasifikasi Citra Slingbag dan Totebag Menggunakan HOG-SVM dan MobileNetV2

## Deskripsi

Proyek ini bertujuan untuk melakukan klasifikasi citra tas berdasarkan dua kategori:

- Slingbag
- Totebag

Penelitian membandingkan performa metode Machine Learning tradisional (HOG + SVM) dengan metode Deep Learning berbasis Transfer Learning menggunakan MobileNetV2.

---

## Dataset

Dataset terdiri dari:

| Kelas    | Jumlah |
| -------- | -----: |
| Slingbag |    500 |
| Totebag  |    500 |
| Total    |   1000 |

Seluruh gambar diproses menjadi ukuran:

**256 × 256 piksel**

---

## Pembagian Dataset

Dataset dibagi menggunakan rasio:

- Train : 70%
- Validation : 15%
- Test : 15%

Hasil pembagian:

| Dataset    | Jumlah |
| ---------- | -----: |
| Train      |    700 |
| Validation |    150 |
| Test       |    150 |

Verifikasi dilakukan untuk memastikan tidak terjadi data leakage.

```text
Train-Test: 0
Train-Validation: 0
Validation-Test: 0
```

---

## Metode

### 1. HOG + SVM

Tahapan:

- Image Resizing
- Data Augmentation
- HOG Feature Extraction
- Feature Scaling
- Support Vector Machine (SVM)

Kernel yang diuji:

- RBF
- Polynomial
- Linear

### 2. MobileNetV2

Transfer Learning menggunakan:

- ImageNet Pretrained Weights
- Data Augmentation
- GlobalAveragePooling2D
- Dropout
- Dense Output Layer
- Early Stopping
- Model Checkpoint

---

## Hasil Eksperimen

| Model           | Accuracy |
| --------------- | -------: |
| HOG + SVM (RBF) |   97.33% |
| MobileNetV2     |  100.00% |

---

## Struktur Repository

```text
notebooks/

UAS_Slingbag_Totebag.ipynb

results/

HOG_SVM_RBF_ConfusionMatrix.png
MobileNetV2_Accuracy.png
MobileNetV2_Loss.png
MobileNetV2_ConfusionMatrix.png
Model_Comparison.png

README.md
requirements.txt
```

---

## Dataset

Dataset tidak disertakan secara langsung pada repository karena ukuran file yang besar (±2.6 GB).

Dataset dapat diakses melalui Google Drive:

https://drive.google.com/drive/folders/1mzHUwoo-mk3xkPJalf2zmxlBhSnieyWY?usp=drive_link

Isi folder Google Drive:

- Dataset Slingbag & Totebag (dataset asli)
- Dataset_256_Preprocessing
- Dataset_Split_UAS

Dataset terdiri dari:

- Slingbag : 500 gambar
- Totebag : 500 gambar

Total : 1000 gambar

---

## Cara Menjalankan

### 1. Clone Repository

```bash
git clone https://github.com/username/repository.git
```

### 2. Masuk ke Folder Repository

```bash
cd repository
```

### 3. Install Dependency

```bash
pip install -r requirements.txt
```

### 4. Jalankan Notebook

Buka Jupyter Notebook atau Google Colab kemudian jalankan notebook:

```text
UAS_Slingbag_Totebag.ipynb
```

---

## Kesimpulan

Berdasarkan hasil eksperimen, model MobileNetV2 memperoleh performa terbaik dengan akurasi sebesar 100.00%, sedangkan model HOG + SVM dengan kernel RBF memperoleh akurasi sebesar 97.33%.

Hasil tersebut menunjukkan bahwa pendekatan Deep Learning berbasis Transfer Learning mampu menghasilkan performa klasifikasi yang lebih tinggi dibandingkan metode Machine Learning berbasis fitur handcrafted HOG pada dataset Slingbag dan Totebag.

---

## Author

**Akmallullail Sya'ban**

NIM: 2310817310010

Program Studi Teknologi Informasi

Universitas Lambung Mangkurat
