# Klasifikasi Citra Slingbag dan Totebag Menggunakan HOG-SVM, MobileNetV2, dan EfficientNetB0

## Deskripsi

Proyek ini bertujuan untuk melakukan klasifikasi citra tas berdasarkan dua kategori:

- Slingbag
- Totebag

Penelitian membandingkan performa metode Machine Learning tradisional (HOG + SVM) dengan metode Deep Learning berbasis Transfer Learning menggunakan MobileNetV2 dan EfficientNetB0.

---

## Dataset

Dataset terdiri dari:

| Kelas    | Jumlah |
| -------- | -----: |
| Slingbag |    500 |
| Totebag  |    500 |
| Total    |   1000 |

Seluruh gambar diproses menjadi ukuran:

256 × 256 piksel

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

```
Train-Test: 0
Train-Validation: 0
Validation-Test: 0
```

---

## Metode

### 1. HOG + SVM

Tahapan:

- Image Resizing
- HOG Feature Extraction
- Support Vector Machine (SVM)

### 2. MobileNetV2

Transfer Learning menggunakan:

- ImageNet Pretrained Weights
- Data Augmentation
- GlobalAveragePooling2D
- Dense Layer

### 3. EfficientNetB0

Transfer Learning menggunakan:

- ImageNet Pretrained Weights
- Data Augmentation
- GlobalAveragePooling2D
- Dense Layer

---

## Hasil Eksperimen

| Model          | Accuracy |
| -------------- | -------: |
| HOG + SVM      |   92.00% |
| MobileNetV2    |  100.00% |
| EfficientNetB0 |   99.33% |

---

## Struktur Repository

```text
notebooks/

01_Dataset.ipynb
02_Preprocessing.ipynb
03_Data_Split.ipynb
04_HOG_SVM.ipynb
05_MobileNetV2_TransferLearning.ipynb
06_EfficientNetB0.ipynb
07_Model_Comparison.ipynb
08_Demo_Prediction.ipynb

results/

confusion-matrix-EfficientNetB0.png
confusion-matrix-mobilenetv2.png
EfficientNetB0-accuracy.png
EfficientNetB0-Loss.png
HOG+SVM-ConfusionMatrix.png
mobilenetv2-accuracy.png
mobilenetv2-loss.png
comparison_accuracy.png
```

---

## Dataset

Dataset tidak disertakan secara langsung pada repository karena ukuran file yang besar (±2.6 GB).

Dataset dapat diakses melalui Google Drive:

[https://drive.google.com/drive/folders/1mzHUwoo-mk3xkPJalf2zmxlBhSnieyWY?usp=drive_link]

Isi folder Google Drive:

- Dataset Slingbag & Totebag (dataset asli)
- Dataset_256_Preprocessing (hasil resize 256×256)
- Dataset_Split (train, validation, test)

Dataset terdiri dari:

- Slingbag : 500 gambar
- Totebag : 500 gambar

Total : 1000 gambar

---

## Cara Menjalankan

1. Clone repository

```bash
git clone https://github.com/username/repository.git
```

2. Install dependency

```bash
pip install -r requirements.txt
```

3. Jalankan notebook sesuai urutan.

---

## Author

Nama: Akmallullail Sya'ban

NIM: 2310817310010

Program Studi Teknologi Informasi

Universitas Lambung Mangkurat
