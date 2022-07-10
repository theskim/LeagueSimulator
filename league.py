from configparser import NoSectionError
from random import randint

class League:
    def __init__(self) -> None:
        """
            Initialize a league
        """
        self.clubs = []
    
    def reset(self) -> None:
        """
            Reset a league
        """
        self.clubs.clear()
        
    def addClub(self, name:str, rating:int) -> None:
        """
            Append a club to the league

            Args:
                name: the name of the team
                rating: the rating of the club

            Example:
                >>> addClub("Manchester City", 85)
        """
        self.clubs.append([name, rating, 0])

    def addPoints(self, index:int, points:int) -> None:
        """
            Append points to the team

            Args:
                index: the index of the team
                points: amount of points being added to the club
        """
        self.clubs[index][2] += points

    def matchEngine(self, first:int, second:int) -> None:
        """
            Responsible for predicting the result between two clubs
            Difference factor is the scaling factor for the difference between two clubs
            
            Draw factor determines the maximum difference between the simulated result and club rating difference

            Args:
                first: first club's index 
                second: second club's index
        """
        
        DIFFERENCE_FACTOR = 1.6
        DRAW_FACTOR = 13
        posibility = 50 + (self.clubs[first][1] - self.clubs[second][1]) * DIFFERENCE_FACTOR
        result = randint(0, 100)
        if abs(result - posibility) < DRAW_FACTOR:
            self.addPoints(first, 1)
            self.addPoints(second, 1)
        elif result > posibility:
            self.addPoints(second, 3)
        else:
            self.addPoints(first, 3)

    def simulateSeason(self) -> NoSectionError:
        """
            Simulate the season
        """
        
        for i in range (0, len(self.clubs)):
            for j in range (i, len(self.clubs)):
                if (i != j):
                    self.matchEngine(i, j)
                    self.matchEngine(i, j)

    def __str__(self) -> str:
        """
            Sort and Display the current league table
            
            Return:
                table: Current League table

            Examples:
                >>> print(premierLeague)

                ------- Table --------
                1. Liverpool- 86
                2. Manchester City - 84
                3. Chelsea- 79
                4. Tottenham Hotspur- 75
                5. Manchester United- 65
                6. Arsenal- 59
                7. West Ham United- 54
                8. Newcastle United- 54
                9. Aston Villa- 52
                10. Leicester City- 50
                11. Brighton & Hove Albion- 50
                12. Everton- 47
                13. Wolverhampton- 42
                14. A.F.C Bournemouth- 41
                15. Leeds United- 39
                16. Brentford- 38
                17. Fulham- 38
                18. Southampton- 33
                19. Crystal Palace- 32
                20. Nottingham Forest- 32
        """
        
        self.clubs.sort(key=lambda row: (row[2]), reverse=True)
        table = "\n------- Table --------\n"
        for i in range(len(self.clubs)):
            table += str(i + 1) + ". " + str(self.clubs[i][0]) + "- " + str(self.clubs[i][2]) + "\n"
        return table