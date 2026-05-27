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
