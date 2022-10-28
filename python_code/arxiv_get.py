import arxiv
import os
import time
import logging


now = str(time.ctime()).split(" ")
time_tag = "most recent update (" + now[0] + " " + now[1] + " " + now[2] + " " + now[4] + ")"
logging.basicConfig(level=logging.ERROR)

'''
def get_id(query: str):

    search = arxiv.Search(
    query = query,
    max_results = 1000,
    #sort_by = arxiv.SortCriterion.SubmittedDate,
    sort_by = arxiv.SortCriterion.SubmittedDate
    )
    id_list = []
    for result in search.results():
        id = str(result.entry_id).split("/")[-1]
        id_list.append(id)
    return id_list
'''



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
    if not os.path.exists("./new_article"):
        os.makedirs("./new_article")

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
        
        
        if ((year == year_limit) and month == month_limit) and (day_up_limit >= day >= day_down_limit) and (str(result.primary_category).split(".")[0] == "astro-ph"):
            logging.warning(result.title)
            count += 1
            fname = str(result.title) + ".md"
            fname = fname.replace(" ", "_")
            fname = fname.replace("/", "_")
            fname = fname.replace("\\", "_")
            fname = fname.replace("$", "_")
            script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
            rel_path = f"new_article/{fname}"
            abs_file_path = os.path.join(script_dir, rel_path)
            title = str(result.title).replace("\\", "\\\\")

            with open(abs_file_path, "w") as f:
                f.write(
                    f"---\ntitle: \"{title}\"\ndate: \"{year}-{month}-{day}\"\ntype: article\ntags:\n  - \"arxiv\"\n  - \"{time_tag}\"\ncategories:\n  - {query}\n  - {year}(year)\n  - {month}(month)\ndraft: false\n---\n\n> First author: {result.authors[0]}\n\n {result.summary}\n\n---\n[arxiv link]({result.entry_id})\n\n[pdf link]({result.pdf_url})")
                f.close()
        else:
            pass

    print(f"In {query}, add {count} papers")



# paremeter
query_list = [
    "cosmology", "early universe", "galaxies", 
    "high-redshift", "intergalactic medium", "Population III", 
    "supernovae", "radiative transfer", "nuclear reactions", 
    "hydrodynamics", "Active galactic nucleus", "AGN", 
    "galaxy merger", "dwarf galaxy", 
    "chemical evolution", "SMBH", "blackhole physics", 
    "galactic bugle", "galactic disk", "high redshift"
]

year_limit = 2022
month_limit = 10
day_up_limit = 28#21
day_down_limit = 22#14
NOW = time.ctime()
for query in query_list:
    #l = get_id(i)
    get_md(query, year_limit, month_limit, day_up_limit, day_down_limit)
print(f"For this update at {NOW}")
    

