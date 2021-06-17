from liquipediapy import liquipediapy


if __name__ == '__main__':
    api = liquipediapy('Oracle_of_GeT_RiGhT', 'counterstrike')
    soup, url = api.parse('GeT_RiGhT')
    print(soup)