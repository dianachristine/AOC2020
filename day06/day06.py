from dto import Dto


def get_yes_count_of_one_group(group_answers: str) -> int:
    counted_answers = set()
    for answer in group_answers:
        if answer.isalpha():
            counted_answers.add(answer)
    return len(counted_answers)


def is_yes_in_all_answers(question, answers):
    for answer in answers:
        if not question.isalpha() or question not in answer:
            return False
    return True


def get_all_yes_count_of_one_group(group_answers: str) -> int:
    counted_answers = set()
    answers = group_answers.split("\n")
    if answers:
        for question in answers[0]:
            if is_yes_in_all_answers(question, answers):
                counted_answers.add(question)
    return len(counted_answers)


def get_yes_count_of_all_groups(groups_answers: list, all_yes: bool) -> int:
    yes_count = 0
    for answers in groups_answers:
        yes_count += get_all_yes_count_of_one_group(answers) if all_yes else get_yes_count_of_one_group(answers)
    return yes_count


if __name__ == '__main__':
    data = Dto("data.txt", "\n\n").get_data()

    print(get_yes_count_of_all_groups(data, False))  # 6885
    print(get_yes_count_of_all_groups(data, True))  # 3550
