# Image Data Analysis & Anomaly Detection Framework

## 📊 Project Overview
This project focuses on the **statistical analysis and detection of hidden anomalies** (steganography) within unstructured image datasets. By analyzing pixel-value distributions and extracting high-dimensional features, this framework distinguishes between "Clean" (unaltered) and "Stego" (hidden data) images.

## 🎯 Key Objectives
* **Data Analysis:** Conducted statistical distribution checks on 10,000+ images to identify pixel-level variances.
* **Pattern Recognition:** Utilized Deep Learning feature extraction to detect non-visual anomalies.
* **Performance Evaluation:** Implemented rigorous metric evaluation using Confusion Matrices and ROC Curves.

## 📈 Analysis & Results
We processed a balanced dataset of cover and steganographic images. The analysis focused on:
### 📊 Analysis Visualizations

**1. Pixel Intensity Distribution**
*Statistical analysis revealing the variance between clean and steganographic pixel data.*
![Pixel Distribution Chart](distribution_chart.png)

**2. Model Performance (Confusion Matrix)**
*Classification accuracy showing the model's ability to distinguish anomalies.*
![Confusion Matrix](confusion_matrix.png)

### 1. Pixel Intensity Distribution
We analyzed the histogram of pixel intensities to find slight deviations caused by data embedding.
*(See `analysis_visualization.ipynb` for the distribution charts)*

### 2. Classification Metrics
The model performance was evaluated using standard classification metrics:
* **Accuracy:** [Insert Your Accuracy]%
* **Precision/Recall:** Optimized for minimizing false negatives in security checks.
  
### 🧠 Deep Learning Architecture
*The model utilizes a Convolutional Neural Network (CNN) with custom layers for feature extraction and binary classification. Below is the successful initialization of the model architecture:*
![Model Architecture Summary](model_architecture.png)

## 🛠️ Tech Stack
* **Language:** Python 3.9
* **Data Processing:** NumPy, Pandas, OpenCV
* **Visualization:** Matplotlib, Seaborn
* **Modeling:** TensorFlow/PyTorch
