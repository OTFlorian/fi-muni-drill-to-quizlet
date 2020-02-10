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
    TERM_DELIMITER = ";;;"
    CARD_DELIMITER = "\n\n\n"
    
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
        result += TERM_DELIMITER + right + CARD_DELIMITER
    return result


def drill_to_quizlet_file(file_name):
    json_dict = json_to_dict(file_name)
    parsed_drill = parse_drill_dict(json_dict)
    try:
        new_name = file_name.split(".")[0]
    except IndexError:
        new_name = file_name
    save_file(new_name + "-quizlet.txt", parsed_drill)


if __name__ == "__main__":
    drill_to_quizlet_file("questions_PB151.json")
