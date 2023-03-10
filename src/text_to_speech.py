import pyttsx3

# 创建 TTS 引擎
engine = pyttsx3.init()


def text_to_speech(text):
    # 将文本转换为语音并播放
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    # 设置要转换为语音的文本
    # text = "Hello, world!"
    text = "明天天气怎么样？"

    # 调用 text_to_speech 函数
    text_to_speech(text)
