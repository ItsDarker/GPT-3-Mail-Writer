import openai

# Configure OpenAI API
openai.api_key = 'YOUR_OPENAI_API_KEY'

def generate_email(prompt):
    # Make a request to the OpenAI API
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=500,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

def save_as_text_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)

# Example usage
user_prompt = input("Enter the prompt for the email: ")
email_content = generate_email(user_prompt)
output_filename = 'email.txt'

save_as_text_file(email_content, output_filename)
print(f"Email generated and saved as '{output_filename}'.")
