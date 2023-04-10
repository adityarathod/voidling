import logging
import nltk

from data_service.doc_qa import QAAnswer

stopwords = nltk.corpus.stopwords.words("english")

log = logging.getLogger(__name__)

from transformers import pipeline

question_answerer = pipeline(
    "question-answering", model="distilbert-base-cased-distilled-squad"
)
summarizer = pipeline("summarization", model="yasminesarraj/flan-t5-small-samsum")


def get_answer_with_rephrase(question: str, lore: str) -> QAAnswer:
    global question_answerer, summarizer
    # remove stop words from question
    # question = "".join([word for word in question.split() if word not in stopwords])
    result = question_answerer(question=question, context=lore)
    log.info(f"Extraction model returned {str(result)}")
    extracted_context = result["answer"]
    qa_result = QAAnswer(confidence=result["score"])
    phrased_convo = f"""User: {question}\nWe: \"{extracted_context}\""""
    summary = summarizer(
        phrased_convo,
        min_length=min(10, len(question)),
        max_length=len(phrased_convo) // 2,
    )
    qa_result.answer = summary[0]["summary_text"]
    return qa_result
