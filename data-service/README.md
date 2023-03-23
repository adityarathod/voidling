# voidling data service
scrapers and data stuff for the voidling bot :3

## runnable worker scripts
- lore scraper: scrapes lore and persists it to mongodb
  - run via `python -m data_service.scripts.lore_scraper`
- lore downloader: downloads lore from mongodb for offline analysis
  - run via `python -m data_service.scripts.lore_downloader -o <output_folder>`