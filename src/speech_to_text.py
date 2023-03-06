import os
import openai
from dotenv import load_dotenv


def speech_to_text(audio):
    try:
        transcript = openai.Audio.transcribe("whisper-1", audio)
        return transcript['text']
    except:
        print("Something went wrong with the audio transcription.")
        return None


if __name__ == "__main__":
    # 加载环境变量 OPENAI_API_KEY
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    audio_file = open(r"record.wav", "rb")
    print(speech_to_text(audio_file))
