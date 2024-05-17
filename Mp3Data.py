import json


class Mp3Data:
    def __init__(self):
        self.title = ""
        self.url = ""
        self.duration = ""  # 时长
        self.published = ""  # 发布时间

    def __repr__(self):
        return f"Mp3Data(title={self.title}, url={self.url}, duration={self.duration}, published={self.published})"


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Mp3Data):
            return {
                'title': obj.title,
                'url': obj.url,
                'duration': obj.duration,
                'published': obj.published
            }
        # 对于不支持的类型，让基类来处理
        return super().default(obj)  # 使用super().default更简洁
