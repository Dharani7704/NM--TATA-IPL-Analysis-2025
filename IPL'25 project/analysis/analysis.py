import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set the working directory to the script's location
os.chdir(os.path.dirname(__file__))

# Ensure the images directory exists
images_dir = '../website/images/'
os.makedirs(images_dir, exist_ok=True)

# Use the absolute path for the dataset file
file_path = os.path.join(os.path.dirname(__file__), 'deliveries.csv')

# Debugging: Print the resolved file path
print(f"Resolved file path for deliveries.csv: {file_path}")

if not os.path.exists(file_path):
    raise FileNotFoundError("The dataset file 'deliveries.csv' is missing.")

# Define column names explicitly
column_names = [
    'match_id', 'date', 'stage', 'venue', 'team1', 'team2', 'innings', 'over_ball',
    'batsman', 'bowler', 'batsman_runs', 'extras', 'wides', 'noballs', 'byes', 'legbyes',
    'dismissal_kind', 'player_dismissed', 'fielder'
]
data = pd.read_csv(file_path, names=column_names, header=None)

# Ensure 'batsman_runs' is numeric
data['batsman_runs'] = pd.to_numeric(data['batsman_runs'], errors='coerce')

# Top 5 Batsmen
batsmen = data.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(5)
if batsmen.empty:
    raise ValueError("No data available to plot for top batsmen.")

batsmen.plot(kind='bar', color='skyblue')
plt.title('Top 5 Batsmen')
plt.ylabel('Total Runs')
plt.xlabel('Batsman')
plt.tight_layout()
plt.savefig(os.path.join(images_dir, 'top_batsmen.png'))
plt.close()

# Top 5 Bowlers
bowlers = data.groupby('bowler')['batsman_runs'].sum().sort_values(ascending=True).head(5)
bowlers.plot(kind='bar', color='orange')
plt.title('Top 5 Bowlers')
plt.ylabel('Runs Conceded')
plt.xlabel('Bowler')
plt.tight_layout()
plt.savefig(os.path.join(images_dir, 'top_bowlers.png'))
plt.close()

# Economy Rate
economy = data.groupby('bowler').agg({'batsman_runs': 'sum', 'over_ball': 'count'})
economy['economy_rate'] = economy['batsman_runs'] / (economy['over_ball'] / 6)
economy = economy.sort_values(by='economy_rate').head(5)
economy['economy_rate'].plot(kind='bar', color='green')
plt.title('Top 5 Economy Rate Bowlers')
plt.ylabel('Economy Rate')
plt.xlabel('Bowler')
plt.tight_layout()
plt.savefig(os.path.join(images_dir, 'economy_rate.png'))
plt.close()

# Partnership Analysis Heatmap Data Preparation
partnership_data = data.groupby(['batsman', 'bowler'])['batsman_runs'].sum().unstack(fill_value=0)
partnership_data.to_csv('../website/images/partnership_heatmap.csv')

# Partnership Analysis Heatmap Visualization
plt.figure(figsize=(10, 8))
sns.heatmap(partnership_data, annot=False, cmap='viridis', cbar=True)
plt.title('Partnership Analysis Heatmap')
plt.xlabel('Batsmen')
plt.ylabel('Partners')
plt.tight_layout()
plt.savefig(os.path.join(images_dir, 'partnership_heatmap.png'))
plt.close()