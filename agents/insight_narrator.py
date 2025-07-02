
import google.generativeai as genai

def narrate_insight(metrics):
    # Configure the API with your key
    genai.configure(api_key="AIzaSyAh3HsQtmBNRXUBYzSTDMcY-nK14w-NaFI")

   
    model = genai.GenerativeModel("models/gemini-1.5-flash")

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

