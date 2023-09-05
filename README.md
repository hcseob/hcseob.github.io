# Overview
Recently a co-worker posed the question to me as to whether an LLM can generate Wikipedia, given that it was trained on the source from Wikipedia articles. I decided to write a basic script to take a rudimentory crack at this. The output of this script starts at the root page [hcseob.github.io/pages/Philosophy.html](https://hcseob.github.io/pages/Philosophy.html). 

**Basic concept:**
1. Use OpenAI APIs for the LLM
2. Apply some basic prompt engineering to get the LLM to produce a Wikipedia-style page in markdown format, including generating links to other pages that it thinks should exist
3. Track the pages created as well as the deadlinks to non-existent pages (including the number of deadlinks) in a dictionary that gets saved as a json file between runs
4. Create pages in order of the maximum number of deadlinks pointing to uncreated pages
5. Start with Philosophy as the root page, since 97% of Wikipedia article links can reach the Philosophy page (see [Wikipedia:Getting to Philosophy](https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy))
6. Once a sufficient set of deadlinked pages is created, start creating the final pages without generating new links
7. Host the pages on my github.io [here](https://hcseob.github.io)

# How to use this repo
1. Create a file 'init.sh' with contents:
> #!/bin/sh <br>
> source venv/bin/activate <br>
> export OPENAI_API_KEY='sk-...'

2. Create a virtual env: `python -m venv venv`
3. Install `requirements.py`
4. Execute `source init.sh`
5. Reset the pages `python python/reset.py`
6. Create pages (e.g. 100 in this example) `python python/run.py --page_count 100 --new_links True`
7. Run `python python/status.py` to see how many deadlinks are remaining
8. Create pages with `--new_links False` until no deadlinks remain

