import arxiv
import os
import time
import logging



# set tag for md file
# `now` length will be different depend on day like below:
# ['Sun', 'Dec', '', '4', '09:44:35', '2022']
# ['Sun', 'Dec', '11', '01:29:52', '2022']
# so I use [length-n] to get correct indexing value.
now = str(time.ctime()).split(" ")
length = len(now)
time_tag = "most recent update (" + now[0] + " " + now[1] + " " + now[length-3] + " " + now[length-1]  + ")"
logging.basicConfig(level=logging.ERROR)

def get_md(query: str, year_limit: int, month_limit: int, day_up_limit: int, day_down_limit: int):
    '''
    [function]
    This function use arXiv API to get papers information
    including summary, author and links in .md format based on the query.
    save .md files in "./article" folder.
    
    [parameter]
    query: search query, such as "cosmology"
    month_limit: find articles published in that month
    day_up_limit: find articles published <= day_up_limit
    day_down_limit: find articles published >= day_down_limit
    '''


    search = arxiv.Search(
    query = query,
    max_results = 1000,
    sort_by = arxiv.SortCriterion.SubmittedDate,
    #sort_by = arxiv.SortCriterion.Relevance,
    sort_order = arxiv.SortOrder.Descending
    )
    count = 0
    for result in search.results():
        ptime = str(result.published).split("-")
        year = int(ptime[0])
        month = int(ptime[1])
        day = int(ptime[2].split(" ")[0])
        
        
        if ((year == year_limit) and month == month_limit) and (day_up_limit >= day >= day_down_limit) and \
            (str(result.primary_category).split(".")[0] == "astro-ph"):
            logging.warning(result.title)
            count += 1
            fname = str(result.title) + ".md"
            fname = fname.replace(" ", "_")
            fname = fname.replace("/", "_")
            fname = fname.replace("\\", "_")
            fname = fname.replace("$", "_")

            if not os.path.exists(f'./new_article/{query}'):
                os.makedirs(f'./new_article/{query}')
            script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
            rel_path = f"new_article/{query}/{fname}"
            abs_file_path = os.path.join(script_dir, rel_path)
            title = str(result.title).replace("\\", "\\\\")
            title = title.replace("\"", "\\\"")

            with open(abs_file_path, "w") as f:
                f.write(
                    f"---\ntitle: \"{title}\"\ndate: \"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}\"\ntype: article\ntags:\n  - \"arxiv\"\n  - \"{time_tag}\"\ncategories:\n  - {query}\n  - {year}(year)\n  - {month}(month)\ndraft: false\n---\n\n> First author: {result.authors[0]}\n\n {result.summary}\n\n---\n[arxiv link]({result.entry_id})\n\n[pdf link]({result.pdf_url})")
                f.close()
        else:
            pass

    print(f"In {query}, add {count} papers")



# paremeter
query_list = [
    "cosmology", "early universe", "galaxies", 
    "high-redshift", "intergalactic", "Population III", 
    "supernovae", "radiative transfer", "nuclear reactions", 
    "hydrodynamics", "AGN", 
    "galaxy merger", "dwarf galaxy", 
    "chemical evolution", "SMBH", "blackhole", 
    "galactic bugle", "galactic disk", "chemical",
    "globular cluster", "cluster simulation", "HII region simulation"
]


'''
 "early universe"
 "Population III"
 "radiative transfer"
 "nuclear reactions", 
 "galaxy merger", 
 "dwarf galaxy", 
 "chemical evolution"
 "galactic bugle", 
 "galactic disk"
 "globular cluster", 
 "cluster simulation", 
 "HII region simulation"
'''
query_list = [
    "cosmology", "galaxies", "high-redshift", 
    "intergalactic", "supernovae", "hydrodynamics", 
    "AGN", "SMBH", "blackhole",
    "chemical"   
]

year_limit = 2023#2022
month_limit = 1#12#11
day_up_limit = 10#4#31#26#18#10#3#25#19#11#28#21 most recent update (Thu Jan 5 2023)
day_down_limit = 5#1#27#19#10#4#1#12#1#22#14 
NOW = time.ctime()
for query in query_list:
    get_md(query, year_limit, month_limit, day_up_limit, day_down_limit)
print(f"For this update at {NOW}")






# sed -i 's/"most recent update (Sun Dec 4 2022)"/""/g' `ls`
# find ~/Hugo_site/explosion/python_code/new_article/ -type f -print0 | xargs -0 mv -t ~/Hugo_site/explosion/content/article/

# note: l copy newArtile to article, so next week no need co copy, only nedd to detete them
# in newArticle and replace tag in article.


    
