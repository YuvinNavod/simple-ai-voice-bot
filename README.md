# Simple AI Voice Bot

This project is an AI-powered voice bot that listens to customer queries via speech, recognizes the spoken words, and responds with product recommendations. It uses `SpeechRecognition` for converting speech to text and `pyttsx3` for converting text to speech. The bot is based on keyword matching and suggests products based on the user's spoken request.

## Features

- **Speech-to-Text**: Converts user speech into text using the Google Web Speech API.
- **Text-to-Speech**: Responds to the user by converting text back into speech using `pyttsx3`.
- **Product Recommendations**: Provides product suggestions based on predefined keywords.

## Prerequisites

Before you begin, ensure you have the following software installed:

- Python 3.x
- A working microphone

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YuvinNavod/simple-ai-voice-bot.git

2. Navigate into the project directory:
   ```bash
   cd ai-voice-bot
   
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate

4. Install the required packages:
   ```bash
   pip install -r requirements.txt


## How to Run the Voice Bot
- **Connect a microphone to your computer.**
- **Run the following command to start the bot:**
  
   ```bash
   python main.py

The bot will listen for your speech, recognize the keywords, and provide product recommendations based on your request.

## Example Interaction
- **You say:** "Can you recommend a good laptop?"
- **Bot response (text and speech):** "I recommend the Dell XPS 13 for performance and portability."

