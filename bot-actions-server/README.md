# voidling bot actions server
an intermediary REST-based service that is compliant with the Rasa Action Server protocol. Holds custom logic to populate "slots" (localized user profile information) based on previous conversations with the bot (retrieved from the data service). It also holds validation logic, as well as dispatching logic for the Q&A pipeline (described below).
