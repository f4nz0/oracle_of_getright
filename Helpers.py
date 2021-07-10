import json
import networkx as nx
import datetime

def write_results_to_json(results):
    with open('database.json') as json_file:
        data = json.load(json_file)
        if data['tournaments'] is None:
            data['tournaments'] = results
        else:
            print(results)
            for tournament in results:
                all_tournaments = data['tournaments']
                all_tournaments[tournament] = results[tournament]
        with open('database.json', 'w') as outfile:
            json.dump(data, outfile)


def get_saved_tournament_ids():
    with open('database.json') as json_file:
        data = json.load(json_file)
        if data['tournaments'] is not None:
            tournament_ids = []
            for tournament in data['tournaments']:
                tournament_ids.append(tournament)
            return tournament_ids
    return None


def clear_json():
    with open('database.json', 'w') as outfile:
        empty = {}
        empty['tournaments'] = {}
        json.dump(empty, outfile)


def read_json():
    with open('database.json') as json_file:
        data = json.load(json_file)
        return data


def write_json(data):
    with open('database.json', 'w') as outfile:
        json.dump(data, outfile)


def network_from_json(start_date='2000-01-01', end_date='2030-12-31', tier='s', coaches=False, dnp=False):
    esports_graph = nx.Graph()
    added_players = []
    esports_data = read_json()
    playerlabels = {}
    edge_weights = {}
    for tournamentid in esports_data['tournaments']:
        tournament = esports_data['tournaments'][tournamentid]

        valid_tournament = True
        cutoff_end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        cutoff_start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        try:
            tournament_date = datetime.datetime.strptime(tournament['date_start'].replace('?', '1'), '%Y-%m-%d')
        except KeyError:
            valid_tournament = False
            continue
        except ValueError:
            valid_tournament = False
            continue
        tournament_tier = tournament['tier']
        if cutoff_end_date < tournament_date or cutoff_start_date > tournament_date:
            valid_tournament = False

        elif tournament_tier == 'A-Tier ' and tier == 's':
            valid_tournament = False
        elif tournament_tier == 'B-Tier ' and (tier == 's' or tier == 'a'):
            valid_tournament = False
        if valid_tournament:
            # print(tournament['tname'] + ' is a valid tournament!')
            for team in tournament['tteams']:
                players = []
                for player in team['team_players']:
                    eligible = True
                    if 'p_dnp' in player and not dnp:
                        eligible = False
                    elif 'pcoach' in player and player['pcoach'] == True and not coaches:
                        eligible = False
                    if eligible:
                        if ".php" in (player['pid']):
                            playername = player['pname'].replace("$", "S")
                        else:
                            playername = player['pid'].replace("$", "S")
                        if 'rid' in player and int(player['rid']) > 0:
                            real_id = player['rid']
                            players.append(real_id)
                            if not added_players.__contains__(real_id):
                                added_players.append(real_id)
                                playerlabels[real_id] = playername
                                esports_graph.add_node(real_id)
                for player in players:
                    for player2 in players:
                        if player != player2:
                            esports_graph.add_edge(player, player2)
                            if (player, player2) in edge_weights:
                                edge_weights[(player, player2)].append(tournament['tname'])
                            else:
                                edge_weights[(player, player2)] = [tournament['tname']]
    return esports_graph, playerlabels, edge_weights


def get_player_id_from_json(name):
    es_data = read_json()
    if name in es_data['players']:
        return es_data['players'][name]
    else:
        return '-1'
