import json


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