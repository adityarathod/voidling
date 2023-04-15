# voidling bot core
the core of the bot based on Rasa, extracting entities and classifying intents, and calling the appropriate services to make things happen. Exposed to the bot service via a simple REST endpoint.

## how it works
Rasa processes input as follows:

1. **NLU Pipeline**: Tokenization, featurization, intent classification, and entity extraction occurs at the base level, using a mix of heuristics and neural network-based methods.
2. **Next-Action Prediction**: Using rules (which are hard-coded action sequences) and stories (probabilistic/ML-based action sequences), the engine predicts the next action to take based on the detected intent and entity, taking into context the previous intents and entities. This allows the bot to do things like loop until all values in a form are provided by the user.
3. **Action Dispatching**: In some cases, custom actions need to be dispatched by the bot core – either manually specified as part of a rule or inferred as a validation action for a form. A component of Rasa performs these actions via HTTP to the action server (described below).

This is a pretty heavy component and can probably do a lot more, but I relied on my own code for any functionality not described in the pipeline above.