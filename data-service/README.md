# voidling data service
scrapers and data stuff for the voidling bot :3

the brains of the entire bot, and the most intensive and complex part of the bot architecture. a unified interface for retrieval and persistence of champion lore as well as user profiles. also home to a fairly novel and advanced hybrid extractive/abstractive question answering pipeline used in the bot. 


## runnable worker scripts
- lore scraper: scrapes lore and persists it to mongodb
  - run via `python -m data_service.scripts.lore_scraper`
- lore downloader: downloads lore from mongodb for offline analysis
  - run via `python -m data_service.scripts.lore_downloader`
- lore vectorizer: vectorizes lore and creates pipeline for processing queries in the future
  - run via `python -m data_service.scripts.vectorizer`
- lore q&a test suite: tests q&a performance for manual review
  - run via `python -m data_service.scripts.lore_qa_test_suite` 