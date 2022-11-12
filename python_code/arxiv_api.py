import urllib.request
import time
import feedparser
import os
now = str(time.ctime()).split(" ")
time_tag = "most recent update (" + now[0] + " " + now[1] + now[2] + " " + now[3] + " " + now[5] + ")"


# Base api query url
base_url = 'http://export.arxiv.org/api/query?';

# Search parameters
search_query = urllib.parse.quote("ti:supernova")
i = 0
results_per_iteration = 1
wait_time = 0.001
papers = []

year_lim = 2022
year = year_lim

month_lim = 10
month = month_lim

day_L = 1
day = 31

print('Searching arXiv for %s' % search_query)
condition = (year == year_lim) & (month <= month_lim) & (day_L <= day)

while ((year == year_lim) & (month >= month_lim) & (day_L < day)): #stop requesting when papers date reach 2018

    print(condition)
    print("Results %i - %i" % (i,i+results_per_iteration))
    
    query = 'search_query=%s&start=%i&max_results=%i&sortBy=submittedDate&sortOrder=descending' % (search_query,
                                                         i,
                                                         results_per_iteration)

    # perform a GET request using the base_url and query
    response = urllib.request.urlopen(base_url+query).read()

    # parse the response using feedparser
    feed = feedparser.parse(response)
    # Run through each entry, and print out information
    for entry in feed.entries:
        #print('arxiv-id: %s' % entry.id.split('/abs/')[-1])
        #print('Title:  %s' % entry.title)
        #feedparser v4.1 only grabs the first author
        #print('First Author:  %s' % entry.author)
        paper = {}
        paper["date"] = entry.published
        year = int(paper["date"][0:4])
        month = int(paper["date"][5:7])
        day = int(paper["date"][8:10])



        paper["title"] = entry.title
        paper["first_author"] = entry.author
        paper["summary"] = entry.summary
        paper["id"] = entry.id
        papers.append(paper)
        print(f'year{year} month{month} day{day}')
        #print(paper["id"])
        #print(type(paper["title"]))

        if not os.path.exists("./new_article"):
            os.makedirs("./new_article")

        fname = str(paper["id"]).split("/")[-1]


        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = f"new_article/{fname}.md"
        abs_file_path = os.path.join(script_dir, rel_path)

        with open(abs_file_path, "w", encoding='UTF-8') as f:
            f.write(f'---\ntitle: \"{paper["title"]}\"\ndate: \"{year}-{month}-{day}\"\ntype: article\ntags:\n  - \"arxiv\"\n  - \"{time_tag}\"\ncategories:\n  - {search_query[3:]}\n  - {year}(year)\n  - {month}(month)\ndraft: false\n---\n\n> First author:{paper["first_author"]}\n\n{paper["summary"]}\n---\n[arxiv link]({paper["id"]})\n\n[pdf link](https://arxiv.org/pdf/{fname}.pdf)')
            f.close 
# \n\n {result.summary}\n\n---\n[arxiv link]({result.entry_id})\n\n[pdf link]({result.pdf_url})")
        
    # Sleep a bit before calling the API again
    print('Bulk: %i' % 1)
    i += results_per_iteration
    time.sleep(wait_time)