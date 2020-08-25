
def editConfig(player_number):
    import pandas as pd
    df_config = pd.read_csv("config.csv")
    df_config = df_config.set_index("Player")
    config = df_config[player_number-1:player_number]
    print(config)
editConfig(1)