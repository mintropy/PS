"""
파일 및 폴더를 생성해주는 Python script
- 백준 문제 번호에 대하여 문제 제목과 함께 생성, Python, JS 가능
"""

import os

import requests
from bs4 import BeautifulSoup

boj_url = "https://www.acmicpc.net/problem/"


def main() -> None:
    platform = input("platform (BOJ)\n").strip()
    platform_name = {
        "BOJ": "BAEKJOON",
    }

    # Get Absolute Pate
    current_dir = os.path.dirname(os.path.realpath(__file__))
    if platform == "BOJ":
        # BOJ Problem Number
        problem_num = int(input("problem number\n").strip())
        # BOJ Problem Name
        url = boj_url + f"{problem_num}"
        headers = {"User_Agent": "Chrome/66.0.3359.181"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        res = soup.select_one("#problem_title").get_text()

        # Languages Templates
        python_template = (
            '"""\n'
            f"Title : {res}\n"
            f"Link : {url}\n"
            '"""\n\n'
            "from sys import stdin\n\n"
            "input = stdin.readline\n\n\n"
            "if __name__ == '__main__':\n"
            "    pass\n"
        )
        javascript_template = (
            "/*\n"
            f"Title : {res}\n"
            f"Link : {url}\n"
            "*/\n\n"
            'const fs = require("fs")\n'
            'const filepath = process.platform === "linux" ? "/dev/stdin" : __dirname+"/input.txt"\n'
            "const input = fs.readFileSync(filepath).toString().trim()\n\n"
        )
        kotlin_template = (
            "import java.io.BufferedReader\n"
            "import java.io.InputStreamReader\n\n"
            "func main() {\n"
            "        with(BufferedReader(InputStreamReader(System.`in`))) {\n\n"
            "        }"
        )

        languages = input("languages (py go js kt)\n").strip().split()
        # Make File
        problem_dir = f"{problem_num // 1000 * 1000}/{problem_num // 100 * 100}"
        languages_name = {
            "py": "Python",
            "go": "Golang",
            "js": "JavaScript",
            "kt": "Kotlin",
        }
        for language in languages:
            target_dir = f"{current_dir}/{platform_name[platform]}/{languages_name[language]}/{problem_dir}"
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            # 파일 생성
            # 파일에 탬플릿 적용
            if language == "py":
                template = python_template
            elif language == "js":
                template = javascript_template
            else:
                continue
            with open(os.path.join(target_dir, f"{problem_num}.{language}"), "w") as fp:
                fp.write(template)


if __name__ == "__main__":
    main()
