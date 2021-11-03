def format_table(champion_pool):
    output = ''
    champions = ''
    kda = ''
    games = ''
    for champion in champion_pool:
        champions += champion.get_name() + '\n'
        kda += champion.get_kda_whole() + ' (' + champion.get_kda() + ')\n'
        games += champion.get_games_played() + ' ('+ champion.get_win_rate() + 'WR)\n'
    champions.rstrip('\n')
    kda.rstrip('\n')
    games.rstrip('\n')
    return [champions, kda, games]

