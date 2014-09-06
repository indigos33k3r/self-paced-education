import subprocess, sys

# gets the first link on any webpage
def get_next_target(page):
    copy = page
    repl = ['= ', ' =', ' = ']
    for i in range(0, len(repl)):
        copy = copy.replace(repl[i], "=")

    first_link_start = copy.find("<a")
	   
    if (first_link_start == -1):
        return None
    else:
        first_url_start = copy.find("href=", first_link_start) + len("href=") + 1

        if (copy[copy.find("href=", first_link_start) + len("href=")] == '"'):
            url = copy[first_url_start:copy.find('"', first_url_start)]
        else:
            url = copy[first_url_start:copy.find("'", first_url_start)]

        first_url_end = page.find(url) + len(url) + 1
        return url, first_url_end

# prints out all of the links on a webpage
def get_all_links(page):
    links = []
    while (get_next_target(page) != None):
        url, marker = get_next_target(page)
        links.append(url)
        page = page[marker:]
    return links

# joins two lists, ignoring shared items
def union(a, b):
    [a.append(x) for x in b if x not in a]

def get_page(url):
    try:
        return subprocess.check_output(['curl', '-s', url])
    except subprocess.CalledProcessError as failure:
        sys.exit('\n\033[91mfatal: %s\n\033[0m' % failure)
    
def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    return None

def add_to_index(index,keyword,url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)
    
# crawls the web for all links reachable by a seed page
def crawl_web(seed):
    to_crawl = [seed]
    crawled = []
    index = {}
    graph = {}
    while to_crawl:
        page = to_crawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(to_crawl, outlinks)
            crawled.append(page)
    return index, graph

def compute_ranks(graph):
    d = 0.8 # damping factor
    num_loops = 10 # arbitrary, but decent
    ranks = {}

    npages = len(graph) # nodes in the graph
    for page in graph:
        ranks[page] = 1.0 / npages

    for i in range(0, num_loops):
        new_ranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            newrank += sum([d *ranks[node] / len(graph[node]) for node in graph if page in graph[node]])
            new_ranks[page] = newrank
        ranks = new_ranks
    return ranks

index, graph = crawl_web('https://www.udacity.com/cs101x/urank/index.html')
ranks = compute_ranks(graph)
print ranks