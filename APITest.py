from liquipediapy import liquipediapy, counterstrike

## 1. Tourniere, darin dann welche Teams, in den Teams die Spieler
## 2.

if __name__ == '__main__':
    api = liquipediapy('Oracle_of_GeT_RiGhT', 'counterstrike')
    soup, url = api.parse('GeT_RiGhT')
    # print(soup)

    cs_obj = counterstrike("Oracle_of_GeT_RiGhT")
    #tournaments = cs_obj.get_tournaments()
    #team_details = cs_obj.get_team_info('Team Liquid', True)
    player_details = cs_obj.get_player_info('GeT_RiGhT', True)
    print(player_details)

#    for i in tournaments:
 #       print(i)