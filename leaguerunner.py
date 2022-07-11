from league import *

# txt Files
PREM_TXT = 'premteams.txt'
LALIGA_TXT = 'laligateams.txt'
SERIE_TXT = 'serieteams.txt'
BUNDESLIGA_TXT = 'bundesligateams.txt'

# Following is the sample code how you can use the league class methods

premierLeague, laLiga, serieA, bundesliga = League(), League(), League(), League()
leagueInit(premierLeague, PREM_TXT)
leagueInit(laLiga, LALIGA_TXT)
leagueInit(serieA, SERIE_TXT)
leagueInit(bundesliga, BUNDESLIGA_TXT)

# Simulate leagues

premierLeague.simulateSeason()
laLiga.simulateSeason()
serieA.simulateSeason()
bundesliga.simulateSeason()

# Display League tables

print(premierLeague)
print(laLiga)
print(serieA)
print(bundesliga)