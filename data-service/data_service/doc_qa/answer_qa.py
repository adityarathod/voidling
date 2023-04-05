import logging

log = logging.getLogger(__name__)

from transformers import pipeline

question_answerer = pipeline(
    "question-answering", model="distilbert-base-cased-distilled-squad"
)
summarizer = pipeline("summarization", model="yasminesarraj/flan-t5-small-samsum")


def get_answer_with_rephrase(question: str, lore: str) -> str:
    global question_answerer, summarizer
    result = question_answerer(question=question, context=lore)
    log.info(f"Extraction model returned {str(result)}")
    phrased_convo = f"""User: {question}\nSummarizer: {result['answer']}"""
    summary = summarizer(
        phrased_convo, min_length=0, max_length=len(phrased_convo) // 2
    )
    return summary[0]["summary_text"]
