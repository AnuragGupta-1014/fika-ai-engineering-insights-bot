# # from langchain.chat_models import ChatOpenAI
# # from langchain.prompts import ChatPromptTemplate

# def narrate_insight(metrics):
#     prompt = ChatPromptTemplate.from_template("""
#     This week:
#     - {total_commits} commits
#     - {lines_added} lines added
#     - {lines_deleted} lines deleted
#     Generate a short DORA-based summary.
#     """)
#     # llm = ChatOpenAI()
#     llm = ChatOpenAI(openai_api_key="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")

#     chain = prompt | llm
#     return chain.invoke(metrics).content
import google.generativeai as genai

def narrate_insight(metrics):
    # Configure the API with your key
    genai.configure(api_key="AIzaSyAh3HsQtmBNRXUBYzSTDMcY-nK14w-NaFI")

    # Use a valid, supported Gemini model
    model = genai.GenerativeModel("models/gemini-1.5-flash")

    # Build the prompt with the provided metrics
    prompt = f"""
    This week:
    - {metrics['total_commits']} commits
    - {metrics['lines_added']} lines added
    - {metrics['lines_deleted']} lines deleted

    Please generate a short DORA-based engineering summary.
    """

    # Call Gemini
    response = model.generate_content(prompt)

    return response.text

