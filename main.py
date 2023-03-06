import os
import sys
import openai
import argparse
from dotenv import load_dotenv
sys.stdin.reconfigure(encoding='utf-8')  # 支持输入中文


def get_input(input_source):
    if input_source == "text":
        user_input = input(">>> You:\n\n")
        if user_input.lower() == "quit" or user_input.lower() == "exit":
            return None, True
    else:
        pass
    return user_input, False


def ask_davinci(message):
    response = openai.Completion.create(
        engine="davinci",
        prompt=message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )  # very likely to return a long long response
    return response.choices[0].text.strip()


def ask_chatgpt(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
    )
    return response['choices'][0]['message']['content']


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", action="store_true",
                        help="use text input instead of voice input",
                        default=False)
    parser.add_argument("--model_engine", type=str,
                        default="gpt-3.5-turbo")  # davinci or gpt-3.5-turbo
    args = parser.parse_args()

    # 加载环境变量 OPENAI_API_KEY
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    print("Welcome!\n"
          "Please enter your text to start chatting with chatgpt.\n"
          "This script is powered by the gpt-3.5-turbo engine by default.\n"
          "To exit, simply type 'quit' or 'exit'.\n")

    if args.model_engine == "davinci":
        user_input = input(">>> You:\n\n")
        response = ask_davinci(user_input)
        print("\n>>> AI: " + response + "\n")
    elif args.model_engine == "gpt-3.5-turbo":
        chat = []  # 保存完整对话
        while True:
            user_input, quit_flag = get_input("text" if args.text else "voice")
            if quit_flag:
                print("\nBye!\n")
                break

            chat.append({"role": "user", "content": user_input})
            try:
                result = ask_chatgpt(chat)
                chat.append({"role": "assistant", "content": result})
                print("\n>>> AI: " + result + "\n")
            except:
                print("Oops! Something went wrong. Please try again.\n")
                chat.pop()
    else:
        print("model_engine not supported")
