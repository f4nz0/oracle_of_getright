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


def network_from_json():
    esports_graph = nx.Graph()
    added_players = []
    esports_data = read_json()
    for tournamentid in esports_data['tournaments']:
        tournament = esports_data['tournaments'][tournamentid]
        # print(tournament)
        for team in tournament['tteams']:
            players = []
            for player in team['team_players']:
                if ".php" in (player['pid']):
                    playerid = player['pname'].replace("$", "S")
                    if playerid.lower() == "nikolinho":
                        print(tournament)
                else:
                    playerid = player['pid'].replace("$", "S")
                    if playerid.lower() == "nikolinho":
                        print(tournament)
                if not added_players.__contains__(playerid):
                    #print(playerid)
                    players.append(playerid)
                    esports_graph.add_node(playerid)
            for player in players:
                for player2 in players:
                    if player != player2:
                        esports_graph.add_edge(player, player2)
    return esports_graph
