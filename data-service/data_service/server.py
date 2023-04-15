import logging

logging.basicConfig(level=logging.INFO)

from sanic import Sanic, text

from data_service.api.lore_qa import bp as lore_qa

app = Sanic("voidling-data-service")


@app.route("/")
async def hello(request):
    return text("Voidling Data Service")


app.blueprint(lore_qa)
app.config.REQUEST_TIMEOUT = 120
