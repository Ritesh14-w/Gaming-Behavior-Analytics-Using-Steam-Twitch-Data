import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_and_visualize_fastfood():
    """
    Loads the cleaned fast food data, performs analysis, and creates visualizations.
    """
    print("--- Starting Analysis and Visualization ---")

    try:
        df = pd.read_csv('cleaned_fastfood.csv')
        print("Successfully loaded cleaned_fastfood.csv")
    except FileNotFoundError:
        print("Error: cleaned_fastfood.csv not found. Please run the clean_fastfood.py script first.")
        return

    sns.set_style("whitegrid")
    

    print("\nAnalyzing: Average Health Score by Restaurant...")
    avg_health_score = df.groupby('company')['health_score'].mean().sort_values(ascending=True)

    plt.figure(figsize=(12, 8))
    ax1 = sns.barplot(x=avg_health_score.values, y=avg_health_score.index, palette='coolwarm_r')
    ax1.set_title('Average Menu Health Score by Restaurant (Lower is Better)', fontsize=16)
    ax1.set_xlabel('Average Health Score', fontsize=12)
    ax1.set_ylabel('Restaurant', fontsize=12)
    plt.tight_layout()
    plt.savefig('average_health_score.png')
    print("Saved chart: average_health_score.png")

    print("\nAnalyzing: Distribution of Sugar Content by Restaurant...")
    
    plt.figure(figsize=(12, 8))
    ax2 = sns.boxplot(x='sugars', y='company', data=df, palette='pastel')
    ax2.set_title('Distribution of Sugar Content (g) by Restaurant', fontsize=16)
    ax2.set_xlabel('Sugar (g)', fontsize=12)
    ax2.set_ylabel('Restaurant', fontsize=12)

    plt.xlim(0, 150) 
    plt.tight_layout()
    plt.savefig('sugar_distribution_boxplot.png')
    print("Saved chart: sugar_distribution_boxplot.png")

    print("\nAnalyzing: Relationship between Protein and Calories...")
    
    plt.figure(figsize=(10, 10))

    ax3 = sns.scatterplot(x='protein', y='calories', data=df, hue='company', alpha=0.7)
    ax3.set_title('Calories vs. Protein Content', fontsize=16)
    ax3.set_xlabel('Protein (g)', fontsize=12)
    ax3.set_ylabel('Calories', fontsize=12)
    plt.tight_layout()
    plt.savefig('protein_vs_calories_scatterplot.png')
    print("Saved chart: protein_vs_calories_scatterplot.png")

    print("\n--- Analysis Complete! Check your folder for the saved .png chart files. ---")


if __name__ == "__main__":
    analyze_and_visualize_fastfood()