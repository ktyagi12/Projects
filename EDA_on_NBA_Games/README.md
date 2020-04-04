**EXPLORATORY DATA ANALYSIS: NBA GAMES**

![NBA](https://user-images.githubusercontent.com/38240162/78450744-ba2ebe00-7678-11ea-9400-2c4f7611c0a3.png)

**TECHNOLOGY USED:** Python

**IDE:** Jupyter

**AIM:** Collect a dataset from one or more open web APIs, and use Python to prepare and analyse the collected data.

**TASKS:**

1. Data identification:
 
      •  Choose at least one open web API as your data source (i.e. not a static or pre-collected dataset). 
    
      **API Chosen:** The NBA Game API: https://rapidapi.com/theapiguy/api/free-nba

       The NBA data is fetched using two following endpoints:

        1. https://free-nba.p.rapidapi.com/games?page={}

        2. https://free-nba.p.rapidapi.com/stats?page={}
        
        The NBA Games data consists of detailed information of NBA games played. 
        Initially the NBA Games data is collected from the API for around 100 days.

        A game is identified with the following features:

        1.Date on which Game is played,
        2. Home team
        3. Visitor Team
        4. Scores of both teams
        5. Status of the game
        6. Season
        7. Quarters played

        The NBA Statistics is the detailed information about all the players belonging to NBA irreespective of the team they play for.           
        The NBA statistics is collected from the API for about 100 days.

        NBA Statistics has a number of parameters like:
        1. Points(include all points with free throw): 'pts'
        2. Field goal made(include all points excluding free throw): 'fgm'
        3. Field goal attempt(include all points excluding free throw):'fga'
        4. Field goal percentage:'fg_pct'
        5. Assist: 'ast',
        6. Block:'blk',
        7. Rebounds: 'reb',
        8. Three point field goals made: 'fg3m'
        9. Three point field goals attempted: 'fg3a'
        10. Three point field percentage:'fg3_pct'
        11. Free throw made:'ftm'
        12. Free throw attempt: 'fta'
        13. Free throw percentage: 'ft_pct'
        14. Steals: 'stl'
        15. Personal fouls: 'pf'
        16. Turnover: 'turnover'
        17. Total time: 'min' and many more.....
        NBA games played throughout 2 decades ranging from 1990 till 2019 is collected using the given APIs.

2. Data collection:
  
      • Collect data from your API(s) using Python.

      • Store the collected data in an appropriate file format for subsequent analysis (e.g. JSON, XML, CSV).

      *Limitation:* Only 25 records or only a single page data of the NBA Games data as well as the statistics of all the players can be                     fetched, So, a iteration through number of pages from 1 till 100 is performed and the data of all 100 days is stored                     in a csv file format.

      *Requirement:* To fetch the data from the API, authentication was needed. Authentication consists of two things:
                    
                    1. API key
                    
                    2. Host name
      
      *Storage:* Further to perform any analysis on the collected data, the data is being read from the csv file in a storage data                       structure pandas "DataFrame" which makes it easier to pre-process and analyse the data.

3. Data preparation and analysis:

      • Load and represent the data using an appropriate data structure (i.e. records/items as rows, described by features as columns).
              
      • Apply any preprocessing steps that might be required to clean or filter the data before analysis. 
  
      • Analyse, characterise, and summarise the cleaned dataset, using tables and plots where appropriate. Clearly explain and interpret any analysis results which are produced.
      
      ![image](https://user-images.githubusercontent.com/38240162/78451081-33c7ab80-767b-11ea-9d4c-1aedc3fc45bc.png)
  
      • Summarise any insights which you gained from your analysis of the data. 
      
      ![image](https://user-images.githubusercontent.com/38240162/78450975-6c1aba00-767a-11ea-8669-84454fa5436c.png)


[Click here for the code](https://github.com/ktyagi12/Projects/tree/master/EDA_on_NBA_Games/code)

[Click here for the Input](https://github.com/ktyagi12/Projects/tree/master/EDA_on_NBA_Games/input)

[Click here for the Output](https://github.com/ktyagi12/Projects/tree/master/EDA_on_NBA_Games/output)
