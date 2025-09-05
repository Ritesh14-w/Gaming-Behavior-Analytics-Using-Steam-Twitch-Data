import pandas as pd

def explore_fastfood_data():
    """
    Loads and performs an initial exploration of the Fast Food Nutrition dataset.
    """
    print("--- Loading and Exploring Fast Food Nutrition Data ---")

    try:
    
        df = pd.read_csv('fastfood.csv')
        print("Successfully loaded fastfood.csv")
    except FileNotFoundError:
        print("Error: fastfood.csv not found. Please make sure it's in the project folder.")
        return

    print("\n--- Initial Data Exploration ---")

    print(f"\nThe dataset has {df.shape[0]} rows and {df.shape[1]} columns.")
    
    print("\nFirst 5 rows of the dataset:")
    print(df.head())
   
    print("\nData info (columns, data types, non-null values):")
    df.info()

    print("\nStatistical summary of the nutritional columns:")

    print(df[['calories', 'total_fat', 'sat_fat', 'sugar', 'protein']].describe())

    print("\nRestaurants included in this dataset:")
    print(df['restaurant'].unique())

if __name__ == "__main__":
    explore_fastfood_data()