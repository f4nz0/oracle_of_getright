import json
import networkx as nx


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


def network_from_json():
    esports_graph = nx.Graph()
    added_players = []
    esports_data = read_json()
    playerlabels = {}
    edge_weights = {}
    for tournamentid in esports_data['tournaments']:
        tournament = esports_data['tournaments'][tournamentid]
        # print(tournament)
        for team in tournament['tteams']:
            players = []
            for player in team['team_players']:
                if ".php" in (player['pid']):
                    playername = player['pname'].replace("$", "S")
                    if playername.lower() == "nikolinho":
                        print(tournament)
                else:
                    playername = player['pid'].replace("$", "S")
                    if playername.lower() == "nikolinho":
                        print(tournament)
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
