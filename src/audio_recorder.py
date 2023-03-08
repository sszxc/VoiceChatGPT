import io
import wave
import pyaudio
import keyboard


def record(target,
           CHUNK=1024,  # 每个音频块的大小
           FORMAT=pyaudio.paInt16,  # 音频格式
           CHANNELS=1,  # 声道数
           RATE=44100,  # 采样率
           ):
    frames = []  # 存储每个音频块
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    recording = False  # 是否正在录音

    keyboard.block_key(57)  # 捕获空格键

    # 录音
    while True:
        space_pressed = keyboard.is_pressed('space')
        if space_pressed and not recording:
            print("(Start recording)")
            recording = True
        elif not space_pressed and recording:
            print("(Stop recording)")
            recording = False
            break
        if recording:
            data = stream.read(CHUNK)
            frames.append(data)

    # 停止录音 释放资源
    stream.stop_stream()
    stream.close()
    p.terminate()

    # 将录音数据保存到文件中
    wf = wave.open(target, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    if isinstance(target, io.BytesIO):
        target.seek(0)  # 对于 io.BytesIO 将指针移动到文件开头

    keyboard.unblock_key(57)  # 停止捕获空格键


if __name__ == "__main__":
    target = "record.wav"
    # target = io.BytesIO()

    print("按下空格键开始录音，松开空格键结束录音并保存到文件中")
    record(target)
    print("录音完成")
