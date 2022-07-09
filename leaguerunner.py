from league import League

# txt Files
PREM_TXT = 'premteams.txt'
LALIGA_TXT = 'premteams.txt'
SERIE_TXT = 'serieteams.txt'
BUNDESLIGA_TXT = 'bundesligateams.txt'

def addClubFromText(league: League, fileName: str):
    """
        Read the text file, add the teams and ratings into League object

        Args: 
            league: League object
            fileName: name of the file 
    """

    with open(fileName) as file_in:
        index, name, line = 1, str(), str()
        for line in file_in:
            if index % 2:
                name = line.replace('\n', '')
            else:
                league.addClub(name, int(line))
            index += 1

# Following is the sample code how you can use the league class methods

premierLeague, laLiga, serieA, bundesliga = League(), League(), League(), League()
addClubFromText(premierLeague, PREM_TXT)
addClubFromText(laLiga, LALIGA_TXT)
addClubFromText(serieA, SERIE_TXT)
addClubFromText(bundesliga, BUNDESLIGA_TXT)

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