from langchain_core.prompts import PromptTemplate


template = PromptTemplate(
    input_variables=["user_input", "style_input", "length_input"],
    template="""
        Answer the following research question:

        {user_input}

        Explain in this style: {style_input}
        Length: {length_input}
    """
    )
template.save("First Project/Prompt/prompt_template.json")