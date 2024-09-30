import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to recognize speech from the microphone
def recognize_speech():
    """Convert speech to text."""
    with sr.Microphone() as source:
        print("Listening for your query...")
        audio_text = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio_text)
            print(f"You said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return None
        except sr.RequestError:
            print("Sorry, there seems to be an issue with the speech recognition service.")
            return None

# Function to convert text to speech
def speak_text(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

# Product recommendation based on keywords in the user's query
product_recommendations = {
    "laptop": "I recommend the Dell XPS 13 for performance and portability.",
    "phone": "I suggest the latest iPhone for a premium experience or a Google Pixel for great camera features.",
    "headphones": "The Sony WH-1000XM4 offers excellent sound quality and noise cancellation.",
    "smartwatch": "I recommend the Apple Watch Series 7 for fitness tracking and connectivity.",
}

# Response generator based on the user's query
def generate_response(user_query):
    """Generate a response based on the user's query."""
    for keyword in product_recommendations:
        if keyword in user_query.lower():
            return product_recommendations[keyword]
    return "Sorry, I don't have a recommendation for that product right now."

# Main function to run the voice bot
def run_voice_bot():
    """Run the AI voice call bot for product recommendations."""
    print("Welcome to the product recommendation system!")
    
    # Get user query through speech-to-text
    user_query = recognize_speech()
    
    if user_query:
        # Generate response based on user query
        response = generate_response(user_query)
        
        # Print and convert the response to speech
        print(f"Bot response: {response}")
        speak_text(response)

# Run the AI voice call bot
if __name__ == "__main__":
    run_voice_bot()
    