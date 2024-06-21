import openai
from pathlib import Path

# set your api key here
openai.api_key = 'sk-proj-xxx'

# function to call the assistant
def call_assistant(prompt):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Kamu adalah chatbot berbahasa Indonesia, yang mengetahui banyak soal BPJS Ketenagakerjaan. Jawabanmu pendek dan conversational, tanpa mempergunakan banyak simbol, kecuali titik dan koma."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.86
    )
    print(response)  # print the raw response for debugging
    return response

# function to convert text to speech using openai's tts api
def text_to_speech(text):
    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = openai.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    with open(speech_file_path, 'wb') as f:
        f.write(response.content)
    return speech_file_path

# example usage
if __name__ == "__main__":
    user_prompt = "Jelaskan Jaminan Hari Tua."
    response = call_assistant(user_prompt)
    print("assistant raw response:", response)
    
    # correctly accessing the message content
    text_response = response.choices[0].message.content
    audio_file_path = text_to_speech(text_response)
    print(f"audio response saved as '{audio_file_path}'")
  
