# Internal
import os
import logging

# Installed
from langchain.chains import StuffDocumentsChain, LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI

# App code
from .prompts import create_stuff_prompt

logger = logging.Logger('logs')

OPENAI_MODEL_NAME = os.getenv('OPENAI_MODEL_NAME', 'gpt-3.5-turbo-1106')

def generate_summary(text):
    try:
        llm = ChatOpenAI(model_name=OPENAI_MODEL_NAME, temperature=0.2, max_retries=20)

        # Prepare summarization chain
        prompt = create_stuff_prompt()
        document_prompt = PromptTemplate(
            input_variables=["page_content"],
            template="{page_content}"
        )
        llm_chain = LLMChain(llm=llm, prompt=prompt)

        # TODO: implement Map Reduce chain, for larger text input
        chain = StuffDocumentsChain(
            llm_chain=llm_chain,
            document_prompt=document_prompt,
            document_variable_name="context"
        )

        # Generate summary
        docs = [
            Document(page_content=text),
        ]
        summary = chain.invoke({"input_documents": docs})

        return summary
    except Exception as err:
        print('Failed inside summary function, due to error:')
        logger.exception(err)
        return ""
