from CSGOAPI import CSGOAPI

if __name__ == '__main__':
    api = CSGOAPI('Oracle_of_GeT_RiGhT, University Research Project, https://github.com/f4nz0/oracle_of_getright')
    all_tournaments = api.get_all_tournament_ids()

