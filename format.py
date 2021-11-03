def format_table(champion_pool):
    output = ''
    name = ''
    kda = ''
    kda_whole = ''
    cs = ''
    cs_min = ''
    win_rate = ''
    games_played = ''
    for champion in champion_pool:
        name += champion.get_name() + '\n'
        kda += champion.get_kda() + '\n'
        kda_whole += champion.get_kda_whole() + '\n'
        cs += champion.get_cs() + '\n'
        cs_min += champion.get_cs_min() + '\n'
        win_rate += champion.get_win_rate() + '\n'
        games_played += champion.get_games_played() + '\n'
    name.rstrip('\n')
    kda.rstrip('\n')
    kda_whole.rstrip('\n')
    cs.rstrip('\n')
    cs_min.rstrip('\n')
    win_rate.rstrip('\n')
    games_played.rstrip('\n')
    return [name, kda, kda_whole, cs, cs_min, win_rate, games_played]

