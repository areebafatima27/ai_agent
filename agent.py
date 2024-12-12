import google.generativeai as genai

# Set your API key directly here
API_KEY = "AIzaSyATGXWqRERgnmJp_EZsB22MAnv0SgspzMg"

# Load the API key
genai.configure(api_key=API_KEY)

# Define the model to use
model = genai.GenerativeModel("gemini-1.5-flash")

def gemini_ai_agent(prompt):
    if not prompt.strip():
        return "Prompt cannot be empty. Please provide a valid input."
    
    # Generate the AI response
    response = model.generate_content(prompt)
    return response.text

# Main loop for interaction
print("Welcome to the Gemini AI Agent!")

while True:
    user_input = input("You: ")
    
    # Check for exit condition
    if user_input.lower() == "exit":
        print("Goodbye!")
        break  # This will exit the loop
    
    if not user_input.strip():
        print("AI: Please enter a valid question or input.")
        continue
    
    # Get AI response
    ai_response = gemini_ai_agent(user_input)
    print(f"AI: {ai_response}")
