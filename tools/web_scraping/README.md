==== List Chapter Items ====

# Scripts


## list_atbs3e_chapter_topics.py

You’re welcome! Your ATBS scraping toolkit is becoming very solid and professional-looking now.

You now have a nice workflow:

1. Scrape TOC
2. Scrape chapter topics
3. Save JSON/CSV
4. Filter/list contents
5. Use outputs to generate directories/scripts/templates

A very good next improvement would be adding:

* `--export-txt`
* `--export-md`
* `--tree-view`
* colored terminal output
* topic statistics per chapter
* automatic chapter summary generation

For example:

```text
Chapter 10: Input Validation
========================================================================
* H2 Project: A Phone Number and Email Address Extractor
  * H3 Step 1: Create a Regex for Phone Numbers
  * H3 Step 2: Create a Regex for Email Addresses
```

That would make your tool feel like a professional CLI utility.


## show_atbs3e_chapter_topic_stats.py

## export_atbs3e_chapter_topics_txt.py

---

--export-txt √
--export-md
--tree-view √
--color
--stats √
--summary

1. --tree-view
2. --stats
3. --export-txt
4. --export-md
5. --color
6. --summary


```bash
python3 tools/web_scraping/list_atbs3e_chapter_topics.py
python3 tools/web_scraping/list_atbs3e_chapter_topics.py --chapter-number 10
python3 tools/web_scraping/list_atbs3e_chapter_topics.py --chapter-number 10 --tree-view
python3 tools/web_scraping/list_atbs3e_chapter_topics.py --stats
python3 tools/web_scraping/list_atbs3e_chapter_topics.py --summary
python3 tools/web_scraping/list_atbs3e_chapter_topics.py --export-md
python3 tools/web_scraping/list_atbs3e_chapter_topics.py --export-txt
python3 tools/web_scraping/list_atbs3e_chapter_topics.py --export-txt --output-file tools/web_scraping/out/chapter_topics_list_with_url.txt --show-url
```

main
 ├── add-tree-view
 ├── add-topic-stats
 ├── add-export-md
 ├── add-export-txt
 ├── add-color-output
 └── add-summary-generator