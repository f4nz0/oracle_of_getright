from liquipediapy import liquipediapy, counterstrike
from CSGOAPI import CSGOAPI
import Helpers
import time


if __name__ == '__main__':
    api = CSGOAPI('Oracle_of_GeT_RiGhT, University Research Project, https://github.com/f4nz0/oracle_of_getright')

    # Helpers.clear_json()
    # info = api.get_tournament_info("Cs_summit/8")
    # print(info)

    all_tournament_ids = api.get_all_tournament_ids("A-Tier_Tournaments/2015-2013")
    time.sleep(35)
    all_tournaments = api.get_all_tournaments_from_ids(all_tournament_ids, 0, 56)
    Helpers.write_results_to_json(all_tournaments)

