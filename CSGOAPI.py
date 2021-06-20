from liquipediapy import liquipediapy
import Helpers
import time

class CSGOAPI():
    def __init__(self, appname):
        self.appname = appname
        self.liquipedia = liquipediapy(appname, 'counterstrike')
        self.__image_base_url = 'https://liquipedia.net'

    def get_tournament_info(self, tournament="StarLadder/2019/Major"):
        try:
            soup, __ = self.liquipedia.parse(tournament)
            tournament_info = {}
            tournament_info['tid'] = tournament
            tournament_info['tname'] = soup.find_all('div', class_='infobox-header')[0].contents[1]
            tournament_info['tteams'] = []
            all_teams = soup.find_all('div', class_='teamcard')
            for team in all_teams:
                team_info = {}
                team_info['team_name'] = team.find('a').get_text()
                team_info['team_players'] = []
                if team.find('a').get('href') is not None:
                    team_info['team_id'] = team.find('a').get('href')[15:]
                else:
                    team_info['team_id'] = ''
                tournament_info['tteams'].append(team_info)
                for player in team.find_all('tr'):
                    player_info = {}
                    if player.find('th') is not None:
                        if len(player.find_all('a')) > 1:
                            player_info['pname'] = player.find_all('a')[1].get_text()
                            player_info['pid'] = player.find_all('a')[1].get('href')[15:]
                            player_info['pcoach'] = False
                            player_info['psub'] = False
                            if player.find('abbr') is not None:
                                annotations = player.find_all('abbr')
                                for ann in annotations:
                                    if ann.get_text() == 'DNP':
                                        player_info['p_dnp'] = True
                                    elif ann.get_text() == 'C':
                                        player_info['pcoach'] = True
                            team_info['team_players'].append(player_info)
            divs = soup.find_all('div', class_='infobox-cell-2')
            for i in range (0, len(divs)):
                if divs[i].get_text() == 'Start Date:':
                    tournament_info['date_start'] = divs[i+1].get_text()
                elif divs[i].get_text() == 'End Date:':
                    tournament_info['date_end'] = divs[i + 1].get_text()
                elif divs[i].get_text() == 'Liquipedia Tier:':
                    tournament_info['tier'] = divs[i + 1].get_text()

            return tournament_info
        except TypeError:
            print("OOPSIE")
            return None
        except  AttributeError:
            print("OOPSIE")
            return None

    def get_all_tournament_ids(self, ttype="Valve_Tournaments"):
        all_tournaments = []
        soup, __ = self.liquipedia.parse(ttype)
        tables = soup.find_all('div', class_='divTable')
        for table in tables:
            rows = table.find_all('div', class_='divRow')
            for row in rows:
                tournament = {}
                tournament_cell = row.find('div', class_='Tournament')
                tournament['tournament'] = tournament_cell.find('b').get_text()
                link = tournament_cell.find('b').find('a').get('href')[15:]
                tournament['link'] = link
                #print(tournament['link'])
                all_tournaments.append(link)
        print("Getting Information from " + str(len(all_tournaments)) + " tournaments")
        return all_tournaments

    def get_all_tournaments_from_ids(self, t_ids, start, finish):
        all_tournaments = {}
        existing_tournaments = Helpers.get_saved_tournament_ids()
        for t_id in t_ids[start:finish]:
            if t_id not in existing_tournaments:
                tournament_info = self.get_tournament_info(t_id)
                if tournament_info is not None:
                    all_tournaments[tournament_info['tid']] = tournament_info
                    print(tournament_info)
                    time.sleep(35)
        return all_tournaments
