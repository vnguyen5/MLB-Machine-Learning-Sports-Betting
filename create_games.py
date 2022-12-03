import pandas as pd
from team import Team
from game import Game

GAME_DATA = ['GL2018.TXT', 'GL2019.TXT', 'GL2020.TXT', 'GL2021.TXT']

headers = ['date', 'number_of_game', 'day', 'away', 'away_league', 'away_game_number', 'home', 'home_league', 'home_game_number',
           'away_score', 'home_score', 'length_outs', 'day_night', 'completion_info', 'forfeit_info', 'protest_info', 'park_id',
           'attendance', 'length_min', 'away_line_score', 'home_line_score', 'ab_away', 'hits_away', 'doubles_away', 'triples_away',
           'homeruns_away', 'rbi_away', 'sac_hits_away', 'sac_fly_away', 'hbp_away', 'bb_away', 'ibb_away', 'ks_away', 'sb_away',
           'cs_away', 'hit_dp_away', 'cathers_interference_away', 'left_on_base_away', 'pitchers_away', 'earned_runs_away',
           'team_earned_runs_away', 'wild_pitches_away', 'balks_away', 'putouts_away', 'assist_away', 'errors_away', 'passed_balls_away',
           'dp_away', 'triple_play_away', 'ab_home', 'hits_home', 'doubles_home', 'triples_home', 'homeruns_home', 'rbi_home',
           'sac_hits_home', 'sac_fly_home', 'hbp_home', 'bb_home', 'ibb_home', 'ks_home', 'sb_home', 'cs_home', 'hit_dp_home',
           'cathers_interference_home', 'left_on_base_home', 'pitchers_home', 'earned_runs_home', 'team_earned_runs_home', 'wild_pitches_home',
           'balks_home', 'putouts_home', 'assist_home', 'errors_home', 'passed_balls_home', 'dp_home', 'triple_play_home', 'home_ump_id',
           'home_ump', '1b_ump_id', '1b_ump', '2b_ump_id', '2b_ump', '3b_ump_id', '3b_ump', 'lf_ump_id', 'lf_ump', 'rf_ump_id', 'rf_ump',
           'manager_id_away', 'manager_away', 'manager_id_home', 'manager_home', 'winning_p_id', 'winning_p', 'losing_p_id', 'losing_p',
           'saving_p_id', 'saving_p', 'gw_rbi_batter_id', 'gw_rb_batter', 'p_away_id', 'p_away', 'p_home_id', 'p_home', 'lineup_1_away_id',
           'lineup_1_away', 'lineup_1_pos_away', 'lineup_2_id_away', 'lineup_2_away', 'lineup_2_pos_away', 'lineup_3_id_away',
           'lineup_3_away', 'lineup_3_pos_away', 'lineup_4_id_away', 'lineup_4_away', 'lineup_4_pos_away', 'lineup_5_id_away',
           'lineup_5_away', 'lineup_5_pos_away', 'lineup_6_id_away', 'lineup_6_away', 'lineup_6_pos_away', 'lineup_7_id_away',
           'lineup_7_away', 'lineup_7_pos_away', 'lineup_8_id_away', 'lineup_8_away', 'lineup_8_pos_away', 'lineup_9_id_away',
           'lineup_9_away', 'lineup_9_pos_away', 'lineup_1_home_id', 'lineup_1_home', 'lineup_1_pos_home', 'lineup_2_id_home',
           'lineup_2_home', 'lineup_2_pos_home', 'lineup_3_id_home', 'lineup_3_home', 'lineup_3_pos_home', 'lineup_4_id_home',
           'lineup_4_home', 'lineup_4_pos_home', 'lineup_5_id_home', 'lineup_5_home', 'lineup_5_pos_home', 'lineup_6_id_home',
           'lineup_6_home', 'lineup_6_pos_home', 'lineup_7_id_home', 'lineup_7_home', 'lineup_7_pos_home', 'lineup_8_id_home',
           'lineup_8_home', 'lineup_8_pos_home', 'lineup_9_id_home', 'lineup_9_home', 'lineup_9_pos_home', 'notes', 'acquisition_info']

# drop_columns = ['day', 'length_outs', 'away_league', 'home_league','length_outs','completion_info', 'forfeit_info', 'protest_info',
#                  'attendance', 'length_min', 'away_line_score', 'home_line_score']

games_columns = ['team_away', 'games_away','runs_away', 'ops_away', 
                'runs_allowed_away','ops_allowed_away',

                'team_home', 'games_home', 'runs_home', 'ops_home', 
                'runs_allwoed_home','ops_allowed_home',

                'home_win'
                 ]
teams = []

# def cleanup(file):
#     file = file.drop(drop_columns, axis=1)
#     print(file.head())


def check_team(team_id):
    if not team_id in map(lambda x: x.id, teams):
        teams.append(Team(team_id))

def increment_row(row, games):
    check_team(row.away)
    check_team(row.home)

    away_team = next((x for x in teams if x.id == row.away), None)
    home_team = next((x for x in teams if x.id == row.home), None)

    away_team.games += 1

    away_team.offensive_stats.runs += row.away_score
    away_team.offensive_stats.ab += row.ab_away
    away_team.offensive_stats.hits += row.hits_away
    away_team.offensive_stats.doubles += row.doubles_away
    away_team.offensive_stats.triples += row.triples_away
    away_team.offensive_stats.homeruns += row.homeruns_away
    away_team.offensive_stats.hbp += row.hbp_away
    away_team.offensive_stats.bb += row.bb_away
    away_team.offensive_stats.ibb += row.ibb_away
    away_team.offensive_stats.ks += row.ks_away
    away_team.offensive_stats.sac_fly += row.sac_fly_away

    away_team.defensive_stats.runs += row.home_score
    away_team.defensive_stats.ab += row.ab_home
    away_team.defensive_stats.hits += row.hits_home
    away_team.defensive_stats.doubles += row.doubles_home
    away_team.defensive_stats.triples += row.triples_home
    away_team.defensive_stats.homeruns += row.homeruns_home
    away_team.defensive_stats.hbp += row.hbp_home
    away_team.defensive_stats.bb += row.bb_home
    away_team.defensive_stats.ibb += row.ibb_home
    away_team.defensive_stats.ks += row.ks_home
    away_team.defensive_stats.sac_fly += row.sac_fly_home

    home_team.games += 1

    home_team.offensive_stats.runs += row.home_score
    home_team.offensive_stats.ab += row.ab_home
    home_team.offensive_stats.hits += row.hits_home
    home_team.offensive_stats.doubles += row.doubles_home
    home_team.offensive_stats.triples += row.triples_home
    home_team.offensive_stats.homeruns += row.homeruns_home
    home_team.offensive_stats.hbp += row.hbp_home
    home_team.offensive_stats.bb += row.bb_home
    home_team.offensive_stats.ibb += row.ibb_home
    home_team.offensive_stats.ks += row.ks_home
    home_team.offensive_stats.sac_fly = row.sac_fly_home

    home_team.defensive_stats.runs += row.away_score
    home_team.defensive_stats.ab += row.ab_away
    home_team.defensive_stats.hits += row.hits_away
    home_team.defensive_stats.doubles += row.doubles_away
    home_team.defensive_stats.triples += row.triples_away
    home_team.defensive_stats.homeruns += row.homeruns_away
    home_team.defensive_stats.hbp += row.hbp_away
    home_team.defensive_stats.bb += row.bb_away
    home_team.defensive_stats.ibb += row.ibb_away
    home_team.defensive_stats.ks += row.ks_away
    home_team.defensive_stats.sac_fly = row.sac_fly_away


    game = Game(away_team, home_team, home_win=int(
        row.home_score) > int(row.away_score))

    games = games.append(game.series(), ignore_index= True)

    # games = pd.concat(games, game.series(), ignore_index=True)
    print(games)

    return games
#how to query every pitcher game 
#file[(file.p_away_id == 'hendk001') | (file.p_home_id == 'hendk001')]

def main():
    games = pd.DataFrame(columns=games_columns)
    for filename in GAME_DATA:

        file = pd.read_csv(f'./Game_Data/{filename}',
                            header=None, names=headers, delimiter=',')
        for row in file.itertuples():
            games = increment_row(row, games=games)

        games.to_excel('./Clean_Data/MLB_Games.xlsx')
        print(len(teams))


if __name__ == '__main__':
    main()
