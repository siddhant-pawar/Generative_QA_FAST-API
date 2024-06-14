from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

llm = CTransformers(
    model='models/llama-2-7b-chat.ggmlv3.q2_K.bin',
    model_type='llama',
    config={'max_new_tokens': 20, 'temperature': 0.1}
)

app = FastAPI()

class TopicRequest(BaseModel):
    topic: str

class ValidationRequest(BaseModel):
    question: str
    answer: str

def generate_question_llama2(topic):
    template = """
                Generate a {topic}-related question.
                """
    prompt = PromptTemplate(input_variables=["topic"], template=template)
    response = llm(prompt.format(topic=topic))
    return response

def validate_answer_llama2(question, answer):
    template = """
            Question: {question}
            Answer: {answer}
            Validate the answer in "Good" or "Bad" only
            """
    prompt = PromptTemplate(input_variables=["question", "answer"], template=template)
    response = llm(prompt.format(question=question, answer=answer))

    model_answer_template = """
                                Question: {question}
                                Give Correct answer.
                            """

    model_answer_prompt = PromptTemplate(input_variables=["question"], template=model_answer_template)

    model_answer_response = llm(model_answer_prompt.format(question=question))

    return response, model_answer_response

@app.post("/generate-question", response_model=str)
def generate_question(topic_request: TopicRequest):
    topic = topic_request.topic
    question = generate_question_llama2(topic)
    return question

@app.post("/validate-answer", response_model=dict)
def validate_answer(validation_request: ValidationRequest):
    question = validation_request.question
    answer = validation_request.answer
    validation_result, model_answer = validate_answer_llama2(question, answer)
    return {
        "validation_result": validation_result,
        "model_answer": model_answer
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
