# /newsletter
Scripts to find recent venture deals and send them out in emails. Scripts to score comapnies, and scrape early stage ones from seed-db.com. <bold> Currently only runs on Python 2.7 </bold>. You should use a web browser for best user experience for now. 

<h3>How to Run:</h3>
You can either manually execute ./run.sh while in the directory or set up crontab to do it regularly. </br>
Here are some helpful steps to setup crontab </br>
1) $ chmod +x run.sh  (this gives the permission to execute the bash script) </br>
2) $ crontab -e (for convenience, if you have editor like Nano, you can specify the editor by calling $ env EDITOR=nano crontab -e) </br>
3) 0 9 * * 1 path to bash script (this means to execute the script every Monday at 9am, see https://ole.michelsen.dk/blog/schedule-jobs-with-crontab-on-mac-osx.html for more information) </br>

</br></br>
`-scrape.py`: Runs all nessesary scripts to scrape and save data. The "Buzzy List" feature is currently commented out since it makes so many requets we are getting blocked. </br>
`-send.py`: sends content in `stories.txt` by email. The "to" email needs to be replaced with whoever the emails should be sent to.
</br>

<h3>Sources:</h3>
The following files scrape RSS feeds from various sources and store the headline, link, and short paragrph of each in `stories.txt`</br></br>
`-fortune.py`: "http://fortune.com/newsletter/termsheet" (new stories every day, not nessesarily unique)</br>
`-techcrunch.py`: "https://feeds.feedburner.com/TechCrunch/fundings-exits" (new unique stories every week)</br>
`-vcnewsdaily.py`: "https://feeds.feedburner.com/vcnewsdaily" (new unique stories every week)</br>
`-pehub.py`: "https://www.pehub.com/category/vc-deals/feed/" (new unique stories every week)</br>
`-seed-db.py`: gets lists of companies from seed-db's database of incubator batches. Calculates their buzz scores and saves the top n companies to `buzz.txt` and the top n fintech companies to `fintech_buzz.txt`. Usage: `getBuzzyCompanies(number of top companies, [accelerator id array], earliest year to a company can be founded, interest level threshold for fintech)` Accelerator ids can be found on seed-db.com
</br></br>

<h3>Scoring:</h3>
`-score.py`: contains methods to get information from an crunchbase url. Gets other info from `scraper_functions.py` such as number of twitter followers, search results, alexa rank, search ranking increase, etc. </br></br> It assembles the information into a single score. Creates a static score with position metrics (number of twitter followers, rank, etc) and a dynamic score with velocity metrics (rank increase, search increase). Combines the two.
</br></br>

<h3>Helpers</h3>
`-scraper_functions.py`: Contains a collection of functions used for scraping various data sources. </br></br>The functions used to obtain data are: `infoFromCrunchbase()`, `getAlexaRankings()`, `numberOfWebResults()`, and `numberOfTwitterFollowers()`</br></br>
`-helper_functions.py`: contains other functions to support `score.py`. `getCrunchbaseURL()` and `extractName()` are used to find the crunchbase URL if it wasn't provided in the story or database. `checkInterestLvl()` determines if an article is of interest to Arbor, by scanning thorugh it for words contained in `keywords.txt`, `geographies.txt`, or `vclist.txt`
</br></br>

<h3>Data</h3>
`-stories.txt`: stores new stories as their scraped by sources</br>
`-keywords.txt`: stores keywords we're interested in</br>
`-vclist.txt`: stores vc's we're interested in</br>
`-geographies.txt`: stores locations we're interested in </br>
`list.csv`: Primarily for debugging, buzz scores for each company are saved here as they are calculated
</br></br>

</br>
