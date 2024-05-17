import uuid
import os
from moviepy.editor import VideoFileClip
from pytube import YouTube


# 下载视频
def download_video(url, output_path):
    try:
        name = str(uuid.uuid4()) + ".mp4"
        print("开始下载：" + url)
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if streams:
            video = streams
            filename = os.path.basename(name)  # 使用视频的文件名
            video.download(output_path, filename=filename)  # 保存视频时指定文件名
            print("下载完成！")
            print("文件名称:", filename)
            return str(filename)
        else:
            print("视频没有可用的流。")
    except Exception as e:
        print("下载出错:", e)


# 视频转音频
def toMp3(mp4FileName):
    try:
        print("开始视频转音频")
        video = VideoFileClip(mp4FileName)
        audio = video.audio
        mp3Name = str(uuid.uuid4()) + ".mp3"
        # 写入MP3文件并设置比特率
        audio.write_audiofile("./data/"+mp3Name, codec='libmp3lame', bitrate='64K')

        # 关闭视频和音频的读取器，释放资源
        video.reader.close()
        audio.reader.close_proc()  # 注意这里使用close_proc()来确保子进程被关闭

        print("视频转音频结束，开始删除视频")
        os.remove(mp4FileName)
        return mp3Name
        print("视频删除成功")
    except Exception as e:
        print("视频转音频出现异常:", e)


def mp4Time(mp4FileName):
    print("获取视频时长")
    clip = VideoFileClip(mp4FileName)
    duration = clip.duration
    duration = int(duration)
    minutes = duration // 60  # 使用整数除法得到完整的分钟数
    remaining_seconds = duration % 60  # 使用模运算符得到剩余的秒数
    durationStr = str(minutes) + "分" + str(remaining_seconds) + "秒"
    print("视频时长：" + durationStr)
    return durationStr


#toMp3("./data/126e5de0-c1bd-4638-8286-71bdb1c08162.mp4")