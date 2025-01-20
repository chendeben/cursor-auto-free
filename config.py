from dotenv import load_dotenv
import os
import sys
from logger import logging
import uuid


class Config:
    def __init__(self):
        # 获取应用程序的根目录路径
        if getattr(sys, "frozen", False):
            # 如果是打包后的可执行文件
            application_path = os.path.dirname(sys.executable)
        else:
            # 如果是开发环境
            application_path = os.path.dirname(os.path.abspath(__file__))

        self.auth_token = str(uuid.uuid4()).replace('-', '')

    def get_temp_mail(self):
        # 返回临时邮箱地址
        return getattr(self, 'temp_mail', None)

    def set_temp_mail(self, mail):
        self.temp_mail = mail

    def get_auth_token(self):
        return self.auth_token

    def check_is_valid(self, str):
        return len(str.strip()) > 0

    def print_config(self):
        temp_mail = self.get_temp_mail()
        if temp_mail:
            logging.info(f"\033[32m临时邮箱: {temp_mail}\033[0m")


# 使用示例
if __name__ == "__main__":
    try:
        config = Config()
        print("配置初始化成功！")
        config.get_temp_mail()
    except Exception as e:
        print(f"错误: {e}")
