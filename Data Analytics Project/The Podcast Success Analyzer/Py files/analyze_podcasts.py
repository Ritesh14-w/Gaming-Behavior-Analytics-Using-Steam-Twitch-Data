import pandas as pd

def explore_podcast_data():
    """
    Loads and inspects the two podcast industry ranking datasets.
    """
    print("--- Loading and Exploring Podcast Data ---")

    try:
  
        podcasts_df = pd.read_csv('top_podcasts.csv', encoding='latin1')
        
        publishers_df = pd.read_csv('top_publishers.csv', encoding='latin1')
        
        print("\nSuccessfully loaded both CSV files!")

    except FileNotFoundError as e:
        print(f"Error: Could not find a file. Please make sure your CSV files are in the same folder as the script and named correctly.")
        print(f"Details: {e}")
        return 

    print("\n\n--- Inspecting the 'Top Podcasts' data ---")

    print("\nFirst 5 rows:")
    print(podcasts_df.head())

    print("\nData info (columns, data types, non-null values):")
    podcasts_df.info()

    print("\n\n--- Inspecting the 'Top Publishers' data ---")
    
    print("\nFirst 5 rows:")
    print(publishers_df.head())

    print("\nData info (columns, data types, non-null values):")
    publishers_df.info()

if __name__ == "__main__":
    explore_podcast_data()