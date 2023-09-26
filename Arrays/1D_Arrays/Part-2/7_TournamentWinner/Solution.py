def updateScores(team, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += 3

def tournamentWinner(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}
    for index, competition in enumerate(competitions):
        result = results[index]
        homeTeam, awayTeam = competition

        winningTeam = homeTeam if result == 1 else awayTeam
        updateScores(winningTeam, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam
    return currentBestTeam

competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]
results = [0, 0, 1]

print(tournamentWinner(competitions, results))
