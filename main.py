"""
파일 및 폴더를 생성해주는 Python script
"""

import os


boj_python_template = '"""\nTitle : \nLink : \n"""'


def main() -> None:
    platform = input("platform (BOJ)\n").strip()
    platform_name = {
        "BOJ": "BAEKJOON",
    }
    current_dir = os.path.dirname(os.path.realpath(__file__))
    if platform == "BOJ":
        problem_num = int(input("problem number\n").strip())
        # 문제 제목 가져오기
        problem_dir = f"{problem_num // 1000 * 1000}/{problem_num // 100 * 100}"
        languages = input("languages (py go js)\n").strip().split()
        languages_name = {
            "py": "Python",
            "go": "Golang",
            "js": "JavaScript",
        }
        for language in languages:
            target_dir = f"{current_dir}/{platform_name[platform]}/{languages_name[language]}/{problem_dir}"
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            # 파일 생성
            # 파일에 탬플릿 적용


if __name__ == "__main__":
    main()
