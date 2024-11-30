import requests
import datetime
import os
from decouple import config

start_tag = '<pre><code>'
end_tag = '</code></pre>'


def get_code_position(text):
    start = text.rfind(start_tag) + len(start_tag)
    end = text.rfind(end_tag)

    return start, end


def download_input(day, year=2023):
    base_url = f"https://adventofcode.com/{year}/day/{day}"
    session_cookie = config('SESSION_COOKIE')

    headers = {
        "Cookie": f"session={session_cookie}",
    }

    response = requests.get(base_url + '/input', headers=headers)

    # Download input
    if response.status_code == 200:
        input_text = response.text.strip()
        save_path = f"inputs/real/input_day_{day}.txt"
        with open(save_path, "w") as file:
            file.write(input_text)
        print(f"Input file for Day {day} saved as {save_path}")
    else:
        raise Exception(f"Failed to download input for Day {day}. Status code: {response.status_code}")

    # Download sample
    response = requests.get(base_url, headers=headers)
    start, end = get_code_position(response.text)

    if start == len(start_tag) - 1 or end == -1:
        raise Exception(f"Failed to download sample input for Day {day}. Sample code not found")
    else:
        save_path = f"inputs/sample/sample_input_day_{day}.txt"
        with open(save_path, "w") as file:
            file.write(response.text[start:end-1])
        print(f"Sample input file for Day {day} saved as {save_path}")


def create_day(day):
    save_path = f"day_{day}/part_1.py"
    save_path_2 = f"day_{day}/part_2.py"

    python_file = f"""import tokenize
from io import BytesIO

import pandas as pd
from functools import reduce


def tokens(text):
    tok = tokenize.tokenize(text.readline)
    name_tuples = [
        (tokenize.tok_name[token.type],
         (int(token.string) if token.type == tokenize.NUMBER else token.string))
        for token in tok
        if token.type not in {{tokenize.ENCODING, tokenize.NEWLINE, tokenize.ENDMARKER, tokenize.NL}}]
    text.seek(0)
    return name_tuples
    

with open('../inputs/real/input_day_{day}.txt', 'r') as file:
    lines = [i.rstrip("\n") for i in file.readlines()]
    encoded_lines = [BytesIO(line.encode('utf-8')) for line in lines]
    token_lines = [tokens(encoded_line) for encoded_line in encoded_lines]
    df = pd.DataFrame({{'input': lines, 'encode': encoded_lines, 'output': None}})

with open('../inputs/sample/sample_input_day_{day}.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]
    encoded_sample_lines = [BytesIO(line.encode('utf-8')) for line in sample_lines]
    token_sample_lines = [tokens(encoded_line) for encoded_line in encoded_sample_lines]
    sample_df = pd.DataFrame({{'input': sample_lines, 'encode': encoded_sample_lines, 'output': None}})




    
    
    
    
    
def process(tokens_line):
    return tokens_line


def get_result(row):
    functions = [tokens]
    result = reduce(lambda x, f: f(x), functions, row)
    return result


sample_df['output'] = sample_df['encode'].apply(get_result)
df['output'] = df['encode'].apply(get_result)
print("Sample output:", sample_df['output'].sum())
print("Answer:", df['output'].sum())

print("Sample output:", process(token_sample_lines))
print("Answer:", process(token_lines))

"""

    if not os.path.exists(f"day_{day}"):
        os.makedirs(f"day_{day}")

    if not os.path.exists(save_path):
        with open(save_path, "w") as file:
            file.write(python_file)

    if not os.path.exists(save_path_2):
        with open(save_path_2, "w") as file:
            file.write('')


if __name__ == "__main__":
    create_day(datetime.datetime.now().day)
    download_input(datetime.datetime.now().day, datetime.datetime.now().year)
