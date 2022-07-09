# SoccerLeagueSimulator
Simulating 21/22 European soccer (football) leagues using **Python**<br/>**Available Leagues:** Premier League, La Liga, Bundesliga, and Serie A

Updated: 22/23 Leagues are now available

Example:

    newLeague.txt
    >>> Toronto FC
        92
        LA Galaxy
        90
        LA FC
        85
        Vancouver Whitecaps
        83
        Montreal Impact
        82
    
    leaguerunner.py
    >>> from league import League
    >>> newLeague = League()
    >>> addClubFromText(newLeague, "newLeague.txt")
    >>> newLeague.simulateSeason()
    >>> print(newLeague)

        
        

