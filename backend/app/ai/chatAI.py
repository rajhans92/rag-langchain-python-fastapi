from langchain_openai import ChatOpenAI
from app.helpers.config import OPENAI_API_KEY


llm =  ChatOpenAI(model="gpt-4.1")

def ragResponse(question: str, context: str)-> str:
    try:
        prompt = f"""
        Use ONLY the context below to answer the question.
        If the answer is not in context, say "I don't know".

        Context:
        {context}

        Question:
        {question}
        """

        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        print(f"Error generating RAG response: {str(e)}")
        return "I'm sorry, I couldn't process your request at this time."