import pandas as pd

def clean_podcast_data():
    """
    Loads the raw podcast data, cleans it, and saves the cleaned versions.
    """
    print("--- Starting Data Cleaning Process ---")

    try:
        publishers_df = pd.read_csv('top_publishers.csv', encoding='latin1')
        podcasts_df = pd.read_csv('top_podcasts.csv', encoding='latin1')
        print("Successfully loaded raw data.")
    except FileNotFoundError:
        print("Error: Raw CSV files not found. Please ensure they are in the folder.")
        return

    print("\n--- Cleaning the 'Publishers' DataFrame ---")
    
    publishers_df.dropna(subset=['Rank'], inplace=True)

    publishers_df.drop(columns=['Unnamed: 6'], inplace=True)

    publishers_df.rename(columns={
        'Podcast Publisher': 'Publisher',
        'US Unique Monthly Audience': 'MonthlyAudience',
        'US Downloads & Streams': 'MonthlyDownloads',
        'Active Shows': 'ActiveShows'
    }, inplace=True)

    columns_to_clean = ['Publisher', 'MonthlyAudience', 'MonthlyDownloads', 'ActiveShows']
    for col in columns_to_clean:

        publishers_df[col] = publishers_df[col].astype(str).str.replace(',', '')
        publishers_df[col] = publishers_df[col].str.replace('*', '', regex=False)

    publishers_df['MonthlyAudience'] = pd.to_numeric(publishers_df['MonthlyAudience'], errors='coerce')
    publishers_df['MonthlyDownloads'] = pd.to_numeric(publishers_df['MonthlyDownloads'], errors='coerce')
    publishers_df['ActiveShows'] = pd.to_numeric(publishers_df['ActiveShows'], errors='coerce')
    publishers_df['Rank'] = publishers_df['Rank'].astype(int)
    print("\nCleaning complete! Here is a preview of the cleaned data:")
    print(publishers_df.head())

    print("\nAnd here is the new data info. Note the change in Dtype for our numeric columns!")
    publishers_df.info()

    try:
        publishers_df.to_csv('cleaned_publishers.csv', index=False)
        podcasts_df.to_csv('cleaned_podcasts.csv', index=False)
        
        print("\nSuccessfully saved 'cleaned_publishers.csv' and 'cleaned_podcasts.csv' to your folder!")
    except Exception as e:
        print(f"Error saving files: {e}")

if __name__ == "__main__":
    clean_podcast_data()