from langchain.prompts import PromptTemplate

def create_stuff_prompt() -> PromptTemplate:
    template =  """Use below provided context to generate summary out of it.

    Context:
    {context}

    Summary:"""

    return PromptTemplate(
        template=template, input_variables=["context"]
    )
