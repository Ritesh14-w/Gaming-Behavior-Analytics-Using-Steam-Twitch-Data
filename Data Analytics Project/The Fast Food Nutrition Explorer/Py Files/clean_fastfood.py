import pandas as pd

def clean_fastfood_data():
    """
    Loads the raw fast food data, cleans column names, converts data types,
    and saves a new, cleaned CSV file.
    """
    print("--- Starting Data Cleaning Process ---")

    try:
        df = pd.read_csv('fastfood.csv')
        print("Successfully loaded raw data.")
    except FileNotFoundError:
        print("Error: fastfood.csv not found.")
        return

    print("\n--- Cleaning Column Names ---")
    
    original_columns = df.columns
    
    df.columns = df.columns.str.lower().str.replace(' ', '').str.replace('\n', '').str.replace('(g)', '').str.replace('(mg)', '')
    
    print("Old column names:", original_columns)
    print("New column names:", df.columns)
    
    print("\n--- Converting Data Types ---")
  
    numeric_cols = ['calories', 'caloriesfromfat', 'totalfat', 'saturatedfat', 
                    'transfat', 'cholesterol', 'sodium', 'carbs', 'fiber', 
                    'sugars', 'protein', 'weightwatcherspnts']
 
    for col in numeric_cols:
    
        df[col] = pd.to_numeric(df[col], errors='coerce')

    print("\nConversion to numeric types complete. Checking new data info:")
    df.info()

    print("\n--- Creating 'Health Score' ---")

    df['health_score'] = (df['totalfat'].fillna(0) * 1.2) + \
                         (df['saturatedfat'].fillna(0) * 1.5) + \
                         (df['sugars'].fillna(0)) + \
                         (df['sodium'].fillna(0) * 0.05) - \
                         (df['protein'].fillna(0) * 1.5) - \
                         (df['fiber'].fillna(0) * 2)

    print("Health Score created. Here's a preview with the new column:")
    print(df[['company', 'item', 'protein', 'sugars', 'health_score']].head())

    try:
        df.to_csv('cleaned_fastfood.csv', index=False)
        print("\nSuccessfully saved 'cleaned_fastfood.csv' to your folder!")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    clean_fastfood_data()