import time
import re
from config import Config
import requests


class EmailVerificationHandler:
    def __init__(self):
        self.config = Config()
        self.session = requests.Session()
        self.base_url = "https://tm.ss5.xyz"
        self.headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'dnt': '1',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://tm.ss5.xyz/index.html',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
        self.auth_token = self.config.get_auth_token()
        self.session.cookies.set('PHPSESSID', '967qb8iskkmkl2q56i554l5j3e')
        self.session.cookies.set('ysmail', self.auth_token)

    def get_verification_code(self, email=None):
        code = None

        try:
            print("正在处理...")
            # 使用传入的邮箱地址或从配置获取
            self.username = email if email else self.config.get_temp_mail()
            print("当前邮箱：", self.username)
            
            if self.username:
                # 使用邮箱地址获取验证码
                code = self._get_latest_mail_code()
            else:
                print("错误：未提供有效的邮箱地址")

        except Exception as e:
            print(f"获取验证码失败: {str(e)}")

        return code

    def _create_mailbox(self):
        url = f"{self.base_url}/user/user?a={self.auth_token}"
        response = self.session.get(url, headers=self.headers)
        if response.status_code != 200:
            raise Exception("创建邮箱失败")
        return response.json()

    def _get_email_list(self):
        url = f"{self.base_url}/user/lists?a={self.auth_token}"
        response = self.session.get(url, headers=self.headers)
        if response.status_code != 200:
            raise Exception("获取邮箱列表失败")
        data = response.json()
        return data.get('data', [])

    def _get_latest_mail_code(self):
        # 第一阶段：10次尝试，每次间隔3秒
        code = self._attempt_get_code(max_attempts=10, retry_interval=3)
        if code:
            return code
            
        print("第一阶段未获取到验证码，进入第二阶段重试...")
        # 第二阶段：100次尝试，每次间隔5秒
        return self._attempt_get_code(max_attempts=100, retry_interval=5)
        
    def _attempt_get_code(self, max_attempts, retry_interval):
        for attempt in range(max_attempts):
            url = f"{self.base_url}/mail/lists?u={self.username}&a={self.auth_token}"
            response = self.session.get(url, headers=self.headers)
            if response.status_code != 200:
                print(f"第 {attempt + 1} 次尝试获取邮件失败，{retry_interval} 秒后重试...")
                time.sleep(retry_interval)
                continue

            response_data = response.json()
            mail_list_data = response_data.get('data')
            
            # 检查返回的数据结构
            if not isinstance(mail_list_data, list) or not mail_list_data or response_data.get('code') != 0:
                print(f"第 {attempt + 1} 次尝试未收到邮件，{retry_interval} 秒后重试...")
                time.sleep(retry_interval)
                continue

            # 获取最新邮件内容
            try:
                latest_mail = mail_list_data[0]
                if not isinstance(latest_mail, dict):
                    print(f"第 {attempt + 1} 次尝试邮件格式错误，{retry_interval} 秒后重试...")
                    time.sleep(retry_interval)
                    continue
                    
                mail_text = latest_mail.get('content', '')
                
                # 移除所有 CSS 样式和 HTML 标签
                clean_text = re.sub(r'<style[^>]*>[^<]*</style>', '', mail_text)
                clean_text = re.sub(r'<[^>]+>', '', clean_text)
                # 移除多余的空白字符
                clean_text = re.sub(r'\s+', ' ', clean_text).strip()
                # print("过滤后的邮件内容：", clean_text)
                # 从纯文本中提取 6 位数字验证码
                pattern = r'\b(\d{6})\b'
                code_match = re.search(pattern, clean_text)

                # code_match = re.search(r'Your verification code is (\d{6})', clean_text)
                if code_match:
                    print("提取到验证码", code_match.group(0))
                    return code_match.group(0)
            except Exception as e:
                print(f"处理邮件内容时出错: {str(e)}")
                time.sleep(retry_interval)
                continue
            
            print(f"第 {attempt + 1} 次尝试未找到验证码，{retry_interval} 秒后重试...")
            time.sleep(retry_interval)

        print(f"已达到最大尝试次数 ({max_attempts})，获取验证码失败")
        return None


if __name__ == "__main__":
    email_handler = EmailVerificationHandler()
    code = email_handler.get_verification_code()
    print(code)
