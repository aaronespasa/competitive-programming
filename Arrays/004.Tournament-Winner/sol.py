def normalize(result):
    return 1 if result == 0 else 0

def tournamentWinner(competitions, results):
    competitors = {}
    curr_winner = ""

    for i in range(len(competitions)):
        winner = competitions[i][normalize(results[i])]
        if winner in competitors:
            competitors[winner] += 1
        else:
            competitors[winner] = 1

        if curr_winner == "" or competitors[winner] > competitors[curr_winner]:
            curr_winner = winner

    return curr_winner