import logging

logging.basicConfig(level=logging.INFO)

from flask import Flask

from data_service.api.lore_qa import bp as lore_qa_bp

app = Flask(__name__)
app.register_blueprint(lore_qa_bp, url_prefix="/lore_question")
