import numpy as np
import pandas as pd
import os

# ==========================================
# DATA-CENTRIC FEATURE ENGINEERING
# ==========================================
# This script demonstrates "Analyst" skills:
# 1. Transforming unstructured images -> Structured Data (CSV)
# 2. Running SQL-style GroupBy and Aggregations
# 3. Checking for Data Quality (Missing values, Outliers)

def generate_mock_dataset(num_samples=1000):
    """
    Simulates extracting features from 10,000 images.
    In a real scenario, this would loop through image files and calculate:
    - Mean Pixel Intensity
    - Standard Deviation (Contrast)
    - Entropy (Complexity)
    """
    print("Extracting features from raw images...")
    
    data = {
        'image_id': [f'img_{i:04d}' for i in range(num_samples)],
        'label': np.random.choice(['clean', 'stego'], num_samples),
        'mean_intensity': np.random.normal(120, 15, num_samples),  # Simulated pixel mean
        'std_deviation': np.random.normal(45, 5, num_samples),     # Simulated contrast
        'file_size_kb': np.random.normal(25, 2, num_samples)       # Simulated file size
    }
    
    # Introduce some "dirty data" for us to clean (Analyst mindset!)
    df = pd.DataFrame(data)
    
    # Add a few outliers manually
    df.loc[0, 'mean_intensity'] = None  # Missing value
    df.loc[1, 'mean_intensity'] = 300   # Impossible pixel value (Outlier)
    
    return df

def run_data_analysis(df):
    print("\n--- 1. DATA QUALITY CHECKS ---")
    
    # Check for missing values
    missing = df.isnull().sum()
    print(f"Missing Values:\n{missing[missing > 0]}")
    
    # Fill missing values (Data Cleaning)
    df['mean_intensity'] = df['mean_intensity'].fillna(df['mean_intensity'].mean())
    print("-> Filled missing values with mean.")

    # Outlier Detection
    outliers = df[df['mean_intensity'] > 255]
    print(f"Outliers Detected (Pixel > 255): {len(outliers)}")
    
    # Remove outliers
    df = df[df['mean_intensity'] <= 255]
    print("-> Removed outliers.")

    print("\n--- 2. FEATURE-LEVEL INSIGHTS (SQL-Style) ---")
    # SQL Equivalent: SELECT label, AVG(mean_intensity), AVG(std_deviation) FROM table GROUP BY label;
    
    group_stats = df.groupby('label').agg({
        'mean_intensity': 'mean',
        'std_deviation': 'mean',
        'file_size_kb': 'count'
    }).rename(columns={'file_size_kb': 'image_count'})
    
    print("Aggregated Statistics by Class:")
    print(group_stats)
    
    return df

if __name__ == "__main__":
    # 1. Create Dataset
    df = generate_mock_dataset()
    
    # 2. Analyze Dataset
    clean_df = run_data_analysis(df)
    
    # 3. Export to CSV (Structured Data)
    clean_df.to_csv('image_features_structured.csv', index=False)
    print("\n[SUCCESS] Structured features saved to 'image_features_structured.csv'")
