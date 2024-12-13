
class DBConfig:
    def __init__(self, name, remarks, url):
        self.name = name
        self.remarks = remarks
        self.url = url

    def __str__(self):
        return f'name: {self.name}\nremarks: {self.remarks}\nurl: {self.url}'
