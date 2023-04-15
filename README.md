# voidling
*ml-powered league of legends discord bot*

## components
- bot core: handles user input and dispaches actions as needed. does not handle interfacing with user-visible surfaces.
- discord plugin: handles communication with discord (the only supported user-visible surface).
- data service: a unified interface for retrieval and persistence of champion lore as well as user profiles, along with scrapers for data.
- action server: intermediary REST-based service that holds custom logic to be dispatched by the bot core.

## running
1. clone the repo
2. `cp .env.example production.env` and fill out the appropriate fields in that file
3. `docker compose --env-file production.env build`
4. `docker compose --env-file production.env up`
5. invite the bot to your Discord server

## future work
- security enhancements
- efficiency enhancements
- builds/counters/jungle pathing/patch notes info