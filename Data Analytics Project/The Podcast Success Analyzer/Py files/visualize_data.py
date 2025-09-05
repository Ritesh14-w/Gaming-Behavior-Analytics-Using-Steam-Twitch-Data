import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_and_visualize():
    """
    Loads the cleaned data, performs analysis, and creates visualizations.
    """
    print("--- Starting Analysis and Visualization ---")

    try:
        publishers_df = pd.read_csv('cleaned_publishers.csv')
        podcasts_df = pd.read_csv('cleaned_podcasts.csv')
        print("Successfully loaded cleaned data files.")
    except FileNotFoundError:
        print("Error: Cleaned CSV files not found. Please run the clean_data.py script first.")
        return

    sns.set_style("whitegrid")

    print("\nAnalyzing: Top 10 Publishers by Monthly Audience...")
    top_10_audience = publishers_df.sort_values(by='MonthlyAudience', ascending=False).head(10)

    plt.figure(figsize=(12, 8))
    ax1 = sns.barplot(x='MonthlyAudience', y='Publisher', data=top_10_audience, palette='viridis')
    ax1.set_title('Top 10 Podcast Publishers by Monthly Audience', fontsize=16)
    ax1.set_xlabel('US Unique Monthly Audience (in tens of millions)', fontsize=12)
    ax1.set_ylabel('Publisher', fontsize=12)
    plt.tight_layout()
    plt.savefig('top_publishers_by_audience.png') 
    print("Saved chart: top_publishers_by_audience.png")

    print("\nAnalyzing: Publisher Efficiency (Downloads per Active Show)...")
    publishers_df['DownloadsPerShow'] = publishers_df['MonthlyDownloads'] / publishers_df['ActiveShows']
    top_10_efficiency = publishers_df.sort_values(by='DownloadsPerShow', ascending=False).head(10)

    plt.figure(figsize=(12, 8))
    ax2 = sns.barplot(x='DownloadsPerShow', y='Publisher', data=top_10_efficiency, palette='plasma')
    ax2.set_title('Top 10 Most Efficient Publishers (Downloads per Show)', fontsize=16)
    ax2.set_xlabel('Average Monthly Downloads per Active Show', fontsize=12)
    ax2.set_ylabel('Publisher', fontsize=12)
    plt.tight_layout()
    plt.savefig('top_publishers_by_efficiency.png')
    print("Saved chart: top_publishers_by_efficiency.png")

    print("\nAnalyzing: Market Share of Top 5 Publishers by Audience...")
    top_5_share = publishers_df.sort_values(by='MonthlyAudience', ascending=False).head(5).copy()
    top_5_share.loc['Other'] = publishers_df.iloc[5:]['MonthlyAudience'].sum()

    plt.figure(figsize=(10, 10))
    plt.pie(
        top_5_share['MonthlyAudience'],
        labels=top_5_share['Publisher'],
        autopct='%1.1f%%',
        startangle=140,
        pctdistance=0.85
    )
    plt.title('Market Share of Top 5 Publishers by Audience', fontsize=16)
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.tight_layout()
    plt.savefig('market_share_pie_chart.png')
    print("Saved chart: market_share_pie_chart.png")

    print("\n--- Analysis Complete! Check your folder for the saved .png chart files. ---")

if __name__ == "__main__":
    analyze_and_visualize()