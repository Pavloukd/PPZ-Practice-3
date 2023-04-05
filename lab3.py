from collections import Counter
import requests


def main():
    get_text_info("demo.txt")
    download_csv("https://support.staffbase.com/hc/en-us/article_attachments/360009197031/username.csv")


def get_text_info(path):
    file = open(path)
    parts = file.read().lower().split()
    words_pair = Counter(parts)

    for word, count in words_pair.items():
        print(f"{word.lower()} - {count}")


def download_csv(url_path):
    response = requests.get(url_path)

    result_content = [part for part in response.text.split("\n") if part != ""]
    result_content = result_content[:-1]

    open("source_data/article.txt", "wb").write("\n".join(result_content).encode("utf-8"))
    print("Complete!")


if __name__ == '__main__':
    main()
