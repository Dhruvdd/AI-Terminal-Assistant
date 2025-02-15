import openai

openai.api_key = "OPENAI_API_KEY"

def interpret_command(user_input):
    """Uses OpenAI API to convert natural language into a terminal command."""
    prompt = f"Convert this natural language request into a terminal command:\n\n{user_input}"

    try:
        client = openai.Client()  # Updated API format
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI that translates human language into valid shell commands."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=50
        )
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        return f"Error in NLP processing: {str(e)}"