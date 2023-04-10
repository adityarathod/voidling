from flask import Blueprint, request

from data_service.database.lore_store import get_lore_by_id
from data_service.doc_qa import get_answer_with_rephrase
from data_service.doc_ranking import rank_vector, vectorize_query

bp = Blueprint("lore_qa", __name__)


@bp.route("/", methods=["POST"])
def answer_lore_qa():
    query = request.json["question"]
    # vectorize query and get top doc
    vect = vectorize_query(query)
    top_lore_doc_id = rank_vector(vect, 1)[0]

    # get lore from database
    lore = get_lore_by_id(top_lore_doc_id).lore

    # get answer with rephrase
    answer = get_answer_with_rephrase(query, lore)

    # return answer as json
    return answer.dict()
