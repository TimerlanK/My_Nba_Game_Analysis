import csv
import pprint
pp = pprint.PrettyPrinter(indent=4)


def analyse_nba_game(param_1):
    with open(param_1,'r') as file:
        reader = csv.reader(file,delimiter = '|')

        players_list_of_dict_home = []
        players_list_of_dict_away = []

        result_dict = {"home_team": {"name": '', "players_data": players_list_of_dict_home}, "away_team": {"name": '', "players_data": players_list_of_dict_away}}

        #FIND ALL NAMES
        for row in reader:
            result_dict["home_team"]["name"] = row[4]
            result_dict["away_team"]["name"] = row[3]
            player_description_list = row[7].split()
            # print(player_description_list)

            # 3 points makes home names
            if row[2] == row[4] and 'makes 3-pt' in row[7]:
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                bool_found = 0
                for item in result_dict["home_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["home_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            #3 points makes away names
            if row[2] == row[3] and 'makes 3-pt' in row[7]:
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                bool_found = 0
                for item in result_dict["away_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["away_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            # total assist home names
            if row[2] == row[4] and 'assist by' in row[7]:
                index_of_assist = player_description_list.index('(assist')
                player_name = player_description_list[index_of_assist+2] + ' ' + player_description_list[index_of_assist+3][:-1]
                bool_found = 0
                for item in result_dict["home_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["home_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            # total assist away names
            if row[2] == row[3] and 'assist by' in row[7]:
                index_of_assist = player_description_list.index('(assist')
                player_name = player_description_list[index_of_assist+2] + ' ' + player_description_list[index_of_assist+3][:-1]
                bool_found = 0
                for item in result_dict["away_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["away_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            #3 points misses home names
            if row[2] == row[4] and player_description_list[2] == 'misses' and player_description_list[3] == '3-pt':
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                bool_found = 0
                for item in result_dict["home_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["home_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            #3 points misses away names
            if row[2] == row[3] and player_description_list[2] == 'misses' and player_description_list[3] == '3-pt':
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                bool_found = 0
                for item in result_dict["away_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["away_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            #2 points makes home names
            if row[2] == row[4] and player_description_list[2] == 'makes' and player_description_list[3] == '2-pt':
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                bool_found = 0
                for item in result_dict["home_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["home_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            #2 points makes away names
            if row[2] == row[3] and player_description_list[2] == 'makes' and player_description_list[3] == '2-pt':
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                bool_found = 0
                for item in result_dict["away_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["away_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            #2 points misses home names
            if row[2] == row[4] and player_description_list[2] == 'misses' and player_description_list[3] == '2-pt':
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                bool_found = 0
                for item in result_dict["home_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["home_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            #2 points misses away names
            if row[2] == row[3] and player_description_list[2] == 'misses' and player_description_list[3] == '2-pt':
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                bool_found = 0
                for item in result_dict["away_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["away_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            #1p free throw makes home names
            if row[2] == row[4] and 'makes' in row[7]  and 'free throw' in row[7]:
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                bool_found = 0
                for item in result_dict["home_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["home_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            #1p free throw makes away names
            if row[2] == row[3] and 'makes' in row[7]  and 'free throw' in row[7]:
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                bool_found = 0
                for item in result_dict["away_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["away_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            #1p free throw misses home names
            if row[2] == row[4] and 'misses' in row[7] and 'free throw' in row[7]:
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                bool_found = 0
                for item in result_dict["home_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["home_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            #1p free throw misses away names
            if row[2] == row[3] and 'misses' in row[7] and 'free throw' in row[7]:
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                bool_found = 0
                for item in result_dict["away_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["away_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            #OFFENSIVE REBOUNDS home names
            if row[2] == row[4] and 'rebound' in row[7] and 'Offensive' in row[7] and 'Team' not in row[7]:
                index_of_by = player_description_list.index('by')
                player_name = player_description_list[index_of_by+1] + ' ' + player_description_list[index_of_by+2]
                bool_found = 0
                for item in result_dict["home_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["home_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            #OFFENSIVE REBOUNDS away names
            if row[2] == row[3] and 'rebound' in row[7] and 'Offensive' in row[7] and 'Team' not in row[7]:
                index_of_by = player_description_list.index('by')
                player_name = player_description_list[index_of_by+1] + ' ' + player_description_list[index_of_by+2]
                bool_found = 0
                for item in result_dict["away_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["away_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            #DEFENSIVE REBOUNDS home names
            if row[2] == row[4] and 'rebound' in row[7] and 'Defensive' in row[7] and 'Team' not in row[7]:
                index_of_by = player_description_list.index('by')
                player_name = player_description_list[index_of_by+1] + ' ' + player_description_list[index_of_by+2]
                bool_found = 0
                for item in result_dict["home_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["home_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            #DEFENSIVE REBOUNDS away names
            if row[2] == row[3] and 'rebound' in row[7] and 'Defensive' in row[7] and 'Team' not in row[7]:
                index_of_by = player_description_list.index('by')
                player_name = player_description_list[index_of_by+1] + ' ' + player_description_list[index_of_by+2]
                bool_found = 0
                for item in result_dict["away_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["away_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            #turnover home names
            if row[2] == row[4] and player_description_list[0] == 'Turnover' and player_description_list[2] != 'Team':
                player_name = player_description_list[2] + ' ' + player_description_list[3]
                bool_found = 0
                for item in result_dict["home_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["home_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            #turnover away names
            if row[2] == row[3] and player_description_list[0] == 'Turnover' and player_description_list[2] != 'Team':
                player_name = player_description_list[2] + ' ' + player_description_list[3]
                bool_found = 0
                for item in result_dict["away_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["away_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            #steal home names
            if row[2] == row[3] and player_description_list[0] == 'Turnover' and 'steal' in row[7]:
                index_of_by = player_description_list.index('by',4)
                player_name = player_description_list[index_of_by+1] + ' ' + player_description_list[index_of_by+2][:-1]
                bool_found = 0
                for item in result_dict["home_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["home_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})


            #steal away names
            if row[2] == row[4] and player_description_list[0] == 'Turnover' and 'steal' in row[7]:
                index_of_by = player_description_list.index('by',4)
                player_name = player_description_list[index_of_by+1] + ' ' + player_description_list[index_of_by+2][:-1]
                bool_found = 0
                for item in result_dict["away_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["away_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            #block home names
            if row[2] == row[3] and '(block by' in row[7]:
                index_of_by = player_description_list.index('by')
                player_name = player_description_list[index_of_by+1] + ' ' + player_description_list[index_of_by+2][:-1]
                bool_found = 0
                for item in result_dict["home_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["home_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            #block away names
            if row[2] == row[4] and '(block by' in row[7]:
                index_of_by = player_description_list.index('by')
                player_name = player_description_list[index_of_by+1] + ' ' + player_description_list[index_of_by+2][:-1]
                bool_found = 0
                for item in result_dict["away_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["away_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            # personal fouls  home names
            if row[2] == row[3] and 'Personal foul' in row[7]:
                index_of_by = player_description_list.index('by')
                player_name = player_description_list[index_of_by+1] + ' ' + player_description_list[index_of_by+2]
                bool_found = 0
                for item in result_dict["home_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["home_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})

            # personal fouls away names
            if row[2] == row[4] and 'Personal foul' in row[7]:
                index_of_by = player_description_list.index('by')
                player_name = player_description_list[index_of_by+1] + ' ' + player_description_list[index_of_by+2]
                bool_found = 0
                for item in result_dict["away_team"]["players_data"]:
                    try:
                        if item['player_name'] == player_name:
                            bool_found = 1
                    except:
                        continue
                if bool_found == 0:
                    result_dict["away_team"]["players_data"].append({"player_name": player_name, "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0})





        file.seek(0)
        #FILL IN THE DATA

        for row in reader:
            result_dict["home_team"]["name"] = row[4]
            result_dict["away_team"]["name"] = row[3]
            player_description_list = row[7].split()
            # print(player_description_list)

            # 3 points makes home
            if row[2] == row[4] and 'makes 3-pt' in row[7]:
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                for item in result_dict["home_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['FG'] += 1
                        item['FGA'] += 1
                        item['3P'] += 1
                        item['3PA'] += 1
                        item['PTS'] += 3

            #3 points makes away
            if row[2] == row[3] and 'makes 3-pt' in row[7]:
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                for item in result_dict["away_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['FG'] += 1
                        item['FGA'] += 1
                        item['3P'] += 1
                        item['3PA'] += 1
                        item['PTS'] += 3

            # total assist home
            if row[2] == row[4] and 'assist by' in row[7]:
                index_of_assist = player_description_list.index('(assist')
                player_name = player_description_list[index_of_assist+2] + ' ' + player_description_list[index_of_assist+3][:-1]
                for item in result_dict["home_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['AST'] += 1

            # total assist away
            if row[2] == row[3] and 'assist by' in row[7]:
                index_of_assist = player_description_list.index('(assist')
                player_name = player_description_list[index_of_assist+2] + ' ' + player_description_list[index_of_assist+3][:-1]
                bool_found = 0
                for item in result_dict["away_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['AST'] += 1

            #3 points misses home
            if row[2] == row[4] and player_description_list[2] == 'misses' and player_description_list[3] == '3-pt':
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                # print(player_name)
                for item in result_dict["home_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['FGA'] += 1
                        item['3PA'] += 1

            #3 points misses away
            if row[2] == row[3] and player_description_list[2] == 'misses' and player_description_list[3] == '3-pt':
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                for item in result_dict["away_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['FGA'] += 1
                        item['3PA'] += 1

            #2 points makes home
            if row[2] == row[4] and player_description_list[2] == 'makes' and player_description_list[3] == '2-pt':
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                for item in result_dict["home_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['FG'] += 1
                        item['FGA'] += 1
                        item['PTS'] += 2

            #2 points makes away
            if row[2] == row[3] and player_description_list[2] == 'makes' and player_description_list[3] == '2-pt':
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                for item in result_dict["away_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['FG'] += 1
                        item['FGA'] += 1
                        item['PTS'] += 2

            #2 points misses home
            if row[2] == row[4] and player_description_list[2] == 'misses' and player_description_list[3] == '2-pt':
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                for item in result_dict["home_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['FGA'] += 1

            #2 points misses away
            if row[2] == row[3] and player_description_list[2] == 'misses' and player_description_list[3] == '2-pt':
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                for item in result_dict["away_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['FGA'] += 1

            #1p free throw makes home
            if row[2] == row[4] and 'makes' in row[7]  and 'free throw' in row[7]:
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                for item in result_dict["home_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['FT'] += 1
                        item['FTA'] += 1
                        item['PTS'] += 1

            #1p free throw makes away
            if row[2] == row[3] and 'makes' in row[7]  and 'free throw' in row[7]:
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                for item in result_dict["away_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['FT'] += 1
                        item['FTA'] += 1
                        item['PTS'] += 1

            #1p free throw misses home
            if row[2] == row[4] and 'misses' in row[7] and 'free throw' in row[7]:
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                for item in result_dict["home_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['FTA'] += 1

            #1p free throw misses away
            if row[2] == row[3] and 'misses' in row[7] and 'free throw' in row[7]:
                player_name = player_description_list[0] + ' ' + player_description_list[1]
                for item in result_dict["away_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['FTA'] += 1

            #OFFENSIVE REBOUNDS home
            if row[2] == row[4] and 'rebound' in row[7] and 'Offensive' in row[7] and 'Team' not in row[7]:
                index_of_by = player_description_list.index('by')
                player_name = player_description_list[index_of_by+1] + ' ' + player_description_list[index_of_by+2]
                for item in result_dict["home_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['ORB'] += 1
                        item['TRB'] += 1

            #OFFENSIVE REBOUNDS away
            if row[2] == row[3] and 'rebound' in row[7] and 'Offensive' in row[7] and 'Team' not in row[7]:
                index_of_by = player_description_list.index('by')
                player_name = player_description_list[index_of_by+1] + ' ' + player_description_list[index_of_by+2]
                for item in result_dict["away_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['ORB'] += 1
                        item['TRB'] += 1

            #DEFENSIVE REBOUNDS home
            if row[2] == row[4] and 'rebound' in row[7] and 'Defensive' in row[7] and 'Team' not in row[7]:
                index_of_by = player_description_list.index('by')
                player_name = player_description_list[index_of_by+1] + ' ' + player_description_list[index_of_by+2]
                for item in result_dict["home_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['DRB'] += 1
                        item['TRB'] += 1

            #DEFENSIVE REBOUNDS away
            if row[2] == row[3] and 'rebound' in row[7] and 'Defensive' in row[7] and 'Team' not in row[7]:
                index_of_by = player_description_list.index('by')
                player_name = player_description_list[index_of_by+1] + ' ' + player_description_list[index_of_by+2]
                for item in result_dict["away_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['DRB'] += 1
                        item['TRB'] += 1

            #turnover home
            if row[2] == row[4] and player_description_list[0] == 'Turnover' and player_description_list[2] != 'Team':
                player_name = player_description_list[2] + ' ' + player_description_list[3]
                for item in result_dict["home_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['TOV'] += 1

            #turnover away
            if row[2] == row[3] and player_description_list[0] == 'Turnover' and player_description_list[2] != 'Team':
                player_name = player_description_list[2] + ' ' + player_description_list[3]
                for item in result_dict["away_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['TOV'] += 1

            #steal home
            if row[2] == row[3] and player_description_list[0] == 'Turnover' and 'steal' in row[7]:
                index_of_by = player_description_list.index('by',4)
                player_name = player_description_list[index_of_by+1] + ' ' + player_description_list[index_of_by+2][:-1]
                for item in result_dict["home_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['STL'] += 1

            #steal away
            if row[2] == row[4] and player_description_list[0] == 'Turnover' and 'steal' in row[7]:
                index_of_by = player_description_list.index('by',4)
                player_name = player_description_list[index_of_by+1] + ' ' + player_description_list[index_of_by+2][:-1]
                for item in result_dict["away_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['STL'] += 1

            #block home
            if row[2] == row[3] and '(block by' in row[7]:
                index_of_by = player_description_list.index('by')
                player_name = player_description_list[index_of_by+1] + ' ' + player_description_list[index_of_by+2][:-1]
                for item in result_dict["home_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['BLK'] += 1

            #block away
            if row[2] == row[4] and '(block by' in row[7]:
                index_of_by = player_description_list.index('by')
                player_name = player_description_list[index_of_by+1] + ' ' + player_description_list[index_of_by+2][:-1]
                for item in result_dict["away_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['BLK'] += 1

             # personal fouls  home
            if row[2] == row[3] and 'Personal foul' in row[7]:
                index_of_by = player_description_list.index('by')
                player_name = player_description_list[index_of_by+1] + ' ' + player_description_list[index_of_by+2]
                for item in result_dict["home_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['PF'] += 1

            # personal fouls away
            if row[2] == row[4] and 'Personal foul' in row[7]:
                index_of_by = player_description_list.index('by')
                player_name = player_description_list[index_of_by+1] + ' ' + player_description_list[index_of_by+2]
                for item in result_dict["away_team"]["players_data"]:
                    if item['player_name'] == player_name:
                        item['PF'] += 1

        for item in result_dict["home_team"]["players_data"]:
            try:
                item['FG%'] = "{:.2%}".format((item['FG'])/(item['FGA']))
            except:
                item['FG%'] = 0
            try:
                item["3P%"] = "{:.2%}".format((item['3P'])/(item['3PA']))
            except:
                item["3P%"] = 0
            try:
                item["FT%"] = "{:.2%}".format((item['FT'])/(item['FTA']))
            except:
                item["FT%"] = 0

        for item in result_dict["away_team"]["players_data"]:
            try:
                item['FG%'] = "{:.2%}".format((item['FG'])/(item['FGA']))
            except:
                item['FG%'] = 0
            try:
                item["3P%"] = "{:.2%}".format((item['3P'])/(item['3PA']))
            except:
                item["3P%"] = 0
            try:
                item["FT%"] = "{:.2%}".format((item['FT'])/(item['FTA']))
            except:
                item["FT%"] = 0


        print('-'*100)
        pp.pprint(result_dict)
        # print(result_dict)









# play_by_play_moves =  "nba_game_copy.csv"
# play_by_play_moves =  "nba_game.csv"
play_by_play_moves =  "nba_game_2.csv"
analyse_nba_game(play_by_play_moves)
