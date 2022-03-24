def tournamentWinner(competitions, results):
    l = len(results)
    mem = {}
    max_score = 0
    finalwinner = None
    for i in range(l):
        home, away = competitions[i]
        winner = home if results[i] == 1 else away
        if winner not in mem:
            mem[winner] = 0
        mem[winner] += 3
        if mem[winner] > max_score:
            finalwinner = winner
            max_score = mem[winner]

    return finalwinner
