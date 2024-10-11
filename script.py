import pandas as pd

top5_players = pd.read_csv('/mnt/data/top5-players (1).csv')

top5_players.rename(columns={
    'Rk': 'Rank',
    'Player': 'Player_Name',
    'Nation': 'Nationality',
    'Pos': 'Position',
    'Squad': 'Team',
    'Comp': 'Competition',
    'Born': 'Birth_Year',
    'MP': 'Matches_Played',
    'Starts': 'Starts',
    'Min': 'Minutes_Played',
    '90s': 'Games_90_Min',
    'Gls': 'Goals',
    'Ast': 'Assists',
    'G+A': 'Goals_Assists_Total',
    'G-PK': 'Goals_No_Penalty',
    'PK': 'Penalties_Scored',
    'PKatt': 'Penalties_Attempted',
    'CrdY': 'Yellow_Cards',
    'CrdR': 'Red_Cards',
    'xG': 'Expected_Goals',
    'npxG': 'Non_Penalty_Expected_Goals',
    'xAG': 'Expected_Assists',
    'npxG+xAG': 'Non_Penalty_xG_xA',
    'PrgC': 'Progressive_Carries',
    'PrgP': 'Progressive_Passes',
    'PrgR': 'Progressive_Receives',
    'Gls_90': 'Goals_per_90',
    'Ast_90': 'Assists_per_90',
    'G+A_90': 'Goals_Assists_per_90',
    'G-PK_90': 'Goals_No_Penalty_per_90',
    'G+A-PK_90': 'Goals_Assists_No_Penalty_per_90',
    'xG_90': 'Expected_Goals_per_90',
    'xAG_90': 'Expected_Assists_per_90',
    'xG+xAG_90': 'Expected_Goals_Assists_per_90',
    'npxG_90': 'Non_Penalty_xG_per_90',
    'npxG+xAG_90': 'Non_Penalty_xG_xA_per_90'
}, inplace=True)

columns_to_drop = [
    'Age', 'Min', '90s', 'G+A', 'G-PK', 'PKatt', 'CrdY', 'CrdR', 'xG',
    'npxG', 'xAG', 'npxG+xAG', 'PrgC', 'PrgP', 'PrgR'
]
top5_players.drop(columns=[col for col in columns_to_drop if col in top5_players.columns], inplace=True)

additional_columns = [
    'Minutes_Played', 'Games_90_Min', 'Goals_Assists_Total', 'Goals_No_Penalty',
    'Penalties_Scored', 'Penalties_Attempted', 'Yellow_Cards', 'Red_Cards',
    'Expected_Goals', 'Non_Penalty_Expected_Goals', 'Expected_Assists',
    'Non_Penalty_xG_xA', 'Progressive_Carries', 'Progressive_Passes',
    'Progressive_Receives'
]
for col in additional_columns:
    if col not in top5_players.columns:
        if 'Progressive' in col or 'Expected' in col or 'Penalties' in col:
            top5_players[col] = 0
        else:
            top5_players[col] = pd.NA


top5_players.fillna({'Goals': 0, 'Assists': 0, 'Goals_Assists_Total': 0, 'Goals_No_Penalty': 0,
                     'Penalties_Scored': 0, 'Penalties_Attempted': 0, 'Yellow_Cards': 0,
                     'Red_Cards': 0, 'Expected_Goals': 0, 'Non_Penalty_Expected_Goals': 0,
                     'Expected_Assists': 0, 'Non_Penalty_xG_xA': 0, 'Progressive_Carries': 0,
                     'Progressive_Passes': 0, 'Progressive_Receives': 0}, inplace=True)

final_columns = [
    'Rank', 'Player_Name', 'Nationality', 'Position', 'Team', 'Competition',
    'Birth_Year', 'Matches_Played', 'Starts', 'Minutes_Played', 'Games_90_Min',
    'Goals', 'Assists', 'Goals_Assists_Total', 'Goals_No_Penalty',
    'Penalties_Scored', 'Penalties_Attempted', 'Yellow_Cards', 'Red_Cards',
    'Expected_Goals', 'Non_Penalty_Expected_Goals', 'Expected_Assists',
    'Non_Penalty_xG_xA', 'Progressive_Carries', 'Progressive_Passes',
    'Progressive_Receives', 'Goals_per_90', 'Assists_per_90', 'Goals_Assists_per_90',
    'Goals_No_Penalty_per_90', 'Goals_Assists_No_Penalty_per_90',
    'Expected_Goals_per_90', 'Expected_Assists_per_90',
    'Expected_Goals_Assists_per_90', 'Non_Penalty_xG_per_90',
    'Non_Penalty_xG_xA_per_90'
]
cleaned_df = top5_players[final_columns]

cleaned_df.to_csv('LeFoot_cleaned.csv', index=False)

print("CSV nettoyé créé avec succès : LeFoot_cleaned.csv")