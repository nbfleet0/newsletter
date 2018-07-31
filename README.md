# VentureDigest
Weekly newsletter with new venture capital deals
</br>
</br>
<h2>/newsletter</h2>
<h3>Sources:</h3>
-fortune.py: "http://fortune.com/newsletter/termsheet/?scrape=1" (new stories every day, not nessesarily unique)</br>
-techcrunch.py: "https://feeds.feedburner.com/TechCrunch/fundings-exits" (new unique stories every week)</br>
-vcnewsdaily.py: "https://feeds.feedburner.com/TechCrunch/fundings-exits" (new unique stories every week)</br>
-pehub.py: "https://feeds.feedburner.com/TechCrunch/fundings-exits" (new unique stories every week)</br>
</br></br>
<h3>Periodics:</h3>
-daily.py: runs sources that change daily (fortune.py)</br>
-weekly.py: runs sources that change weekly (techcrunch.py, vcnewsdaily.py, pehub.py)</br>
</br></br>
<h3>Other</h3>
-send.py: sends stories.txt by email</br>
-helper_functions.py: contains other functions (like calculating interest level of a story)</br>
</br></br>
<h3>Data</h3>
-stories.txt: stores new stories as their scraped by sources</br>
-keywords.txt: stores keywords we're interested in</br>
-vclist.txt: stores vc's we're interested in</br>
-geographies.txt: stores locations we're interested in
</br></br>
<h2>/scoring</h2>
-score.py: contains methods to get information from an angellist url, as well as number of twitter followers, search results, and twitter likes a company has</br>
-seed-db.py: gets lists of companies from seed-db's database of incubator batches including angellist url's, funding, and exit status