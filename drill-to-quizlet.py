import json


def json_to_dict(file_name):
    with open(file_name, 'r') as f:
        questions_dict = json.load(f)
    return questions_dict


def save_file(file_name, contents):
    f = open(file_name, "w+")
    f.write(contents)
    f.close()


def parse_drill_dict(questions_dict):
    result = ""
    for question in questions_dict:
        right = ""
        curr_char = "a"
        result += "*" + question['name'] + "*\n"
        for answer in question['answers']:
            curr_answer = curr_char + ") " + answer['body']
            result += curr_answer + "\n"
            if answer['right']:
                right = curr_answer
            curr_char = chr(ord(curr_char) + 1)
        result += ";;;" + right + "\n\n\n"
    return result


if __name__ == "__main__":
    file_name = "questions_PB151.json"
    json_dict = json_to_dict(file_name)
    parsed_drill = parse_drill_dict(json_dict)
    try:
        new_name = file_name.split(".")[0]
    except IndexError:
        new_name = file_name
    save_file(new_name + "-quizlet.txt", parsed_drill)
