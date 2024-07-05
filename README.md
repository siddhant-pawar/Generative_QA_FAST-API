# Generative_QA_FAST-API
Develop an AI API that generates questions based on user-specified topics. Users provide answers to these questions, which are then evaluated for accuracy and relevance using generative AI technology, comparing them to model answers to assess correctness.

#Explanation:
- Imports and Initialization:

    - FastAPI, HTTPException: Imports from FastAPI for creating the web API and handling HTTP exceptions.
    - BaseModel: From Pydantic for defining data models.
    - List: From typing for defining lists.
    - uvicorn: Used to run the FastAPI application.
    - PromptTemplate, CTransformers: Imports from the langchain library ```(langchain.prompts, langchain.llms)``` for interacting with the language model ```(CTransformers)```.

- Language Model Initialization:

    - ```llm = CTransformers(...)```: Initializes a language model (```CTransformers```) with specific parameters ```(model, model_type, config)```. This model (llm) is used throughout the application to generate questions and validate answers.
      
- FastAPI Application Setup:
    - ```app = FastAPI()```: Creates a FastAPI instance.

- Data Models:
    - ```TopicRequest```: Defines a data model for requests to generate a question with a topic attribute.
    - ```ValidationRequest```: Defines a data model for requests to validate an answer with question and answer attributes.

- Functions:
  - ```generate_question_llama2(topic)```: Generates a question related to the specified topic using the language model (llm).
  - ```validate_answer_llama2(question, answer)```: Validates an answer to a given question using the language model (llm). It also retrieves a model's suggested correct answer for the question.

- Endpoints:
  - ```generate_question(topic_request: TopicRequest)```: Endpoint ```/generate-question``` that accepts POST requests with a JSON payload containing a topic. It returns a generated question as a string.
  - ```validate_answer(validation_request: ValidationRequest)```: Endpoint ```/validate-answer``` that accepts POST requests with a JSON payload containing question and answer. It validates the answer and returns a dictionary with ```validation_result``` (whether the answer is ```"Good"``` or ```"Bad"```) and ```model_answer``` (the model's suggested correct answer).

- Running the Application:
  - ```uvicorn.run(app, host="0.0.0.0", port=8000)```: Starts the FastAPI application using Uvicorn, making it accessible at ```http://localhost:8000```.
