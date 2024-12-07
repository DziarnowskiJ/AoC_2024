import requests
import datetime
import os
from decouple import config


def get_code_position(text):
    start_tag = '<pre><code>'
    end_tag = '</code></pre>'
    start = text.rfind(start_tag) + len(start_tag)
    end = text.rfind(end_tag)

    return start, end


def get_title(day, year):
    base_url = f"https://adventofcode.com/{year}/day/{day}"
    response = requests.get(base_url)
    text = response.text

    start_tag = '<h2>'
    end_tag = '</h2>'
    start = text.rfind(start_tag) + len(start_tag)
    end = text.rfind(end_tag)

    title = text[start + 4:end - 4]

    return title


def download_input(day, year):
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

    if end == -1:
        raise Exception(f"Failed to download sample input for Day {day}. Sample code not found")
    else:
        save_path = f"inputs/sample/sample_input_day_{day}.txt"
        with open(save_path, "w") as file:
            file.write(response.text[start:end-1])
        print(f"Sample input file for Day {day} saved as {save_path}")


def create_day(day, year):
    save_path = f"day_{day}/part_1.py"
    save_path_2 = f"day_{day}/part_2.py"
    readme_path = 'README.md'

    python_file = f"""
with open('../inputs/real/input_day_{day}.txt', 'r') as file:
    input_lines = [i.rstrip("\\n") for i in file.readlines()]

with open('../inputs/sample/sample_input_day_{day}.txt', 'r') as file:
    sample_lines = [i.rstrip("\\n") for i in file.readlines()]
  
  
  
    
def process(lines):
    return lines

print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

"""

    readme = f"""\n## [{get_title(day, year)}](https://adventofcode.com/{year}/day/{day})

```
Part 1:

Part 2:
```
"""

    if not os.path.exists(f"day_{day}"):
        os.makedirs(f"day_{day}")

    if not os.path.exists(save_path):
        with open(save_path, "w") as file:
            file.write(python_file)

    if not os.path.exists(save_path_2):
        with open(save_path_2, "w") as file:
            file.write('')

    with open(readme_path, 'a') as file:
        file.write(readme)


if __name__ == "__main__":
    day = datetime.datetime.now().day
    year = datetime.datetime.now().year
    create_day(day, year)
    download_input(day, year)
