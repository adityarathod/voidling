import logging


logging.basicConfig(level=logging.INFO)

from sanic import Sanic, text

from data_service.api.lore_qa import bp as lore_qa
from data_service.api.summoner_info import bp as summoner_info
from data_service.api.match_history import bp as match_history

app = Sanic("voidling-data-service")


@app.route("/")
async def hello(request):
    return text("Voidling Data Service")


app.blueprint(lore_qa)
app.blueprint(summoner_info)
app.blueprint(match_history)
app.config.REQUEST_TIMEOUT = 120
