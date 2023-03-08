import os
import io
import openai
import argparse
from dotenv import load_dotenv
from src.chat_with_GPT import ask_chatgpt
from src.audio_recorder import record
from src.speech_to_text import speech_to_text
from src.text_to_speech import text_to_speech


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", action="store_true",
                        help="use text input instead of voice input",
                        default=False)
    args = parser.parse_args()

    # 加载环境变量 OPENAI_API_KEY
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    print("Welcome!\n",
          "Please ",
          "enter your text" if args.text else "press space",
          " to start chatting with chatgpt.\n",
          "This script is powered by the gpt-3.5-turbo engine by default.\n",
          "To exit, simply ",
          "type" if args.text else "say",
          " '再见' or '退出' or 'quit' or 'exit'.\n",
          sep='')

    chat = []  # 保存完整对话
    while True:
        # 获取输入
        if args.text:
            user_input = input(">>> You:\n\n")
        else:
            target = io.BytesIO()
            target.name = 'audio.wav'
            record(target)
            user_input = speech_to_text(target)
            print("\n>>> You: \n\n" + user_input)
        if user_input in ["再見", "再见", "退出", "quit", "exit"]:
            print("\nBye!\n")
            break

        # 处理对话
        chat.append({"role": "user", "content": user_input})
        try:
            result = ask_chatgpt(chat)
            chat.append({"role": "assistant", "content": result})
            print("\n>>> AI: " + result + "\n")
            text_to_speech(result)
        except openai.error.APIConnectionError as e:
            print(e)
            print("Oops! Something went wrong with the chat completion. Please try again.\n")
            chat.pop()
