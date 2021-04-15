# تكليفات الدروس من الدرس 060 إلى 064
# -----------------------------------------------

# Task_1


def get_score(**myScore):      # Type of myScore is dictionary
    for key, value in myScore.items():      # <class 'dict'>
        print(f"{key} => {value}")


get_score(Math=90, Science=80, Language=70)
get_score(Logic=70, Problems=60)


# Task_2


def get_people_scores(name="", **skills_with_progress):
    if len(skills_with_progress) > 0:
        if len(name) > 0:
            print(f"\"Hello {name} This Is Your Score Table:\"")

        for skill, value in skills_with_progress.items():
            print(f"{skill} => {value}")
    else:
        print(f"Hello {name} You Have No Scores To Show")


get_people_scores("Osama", Math=90, Science=80, Language=70)

get_people_scores("Mahmoud", Logic=70, Problems=60)

get_people_scores(Logic=70, Problems=60)

get_people_scores("Ahmed")


# Task_3

scores_list = {
    "Math": "90",
    "Science": "80",
    "Language": "70"
}


def get_the_scores(name="", **scoresList):
    if len(scoresList) > 0:
        if len(name) > 0:
            print(f"\"Hello {name} This Is Your Score Table:\"")

        for skill, value in scoresList.items():
            print(f"{skill} => {value}")
    else:
        print(f"\"Hello {name} You Have No Scores To Show\"")


get_the_scores("Osama", **scores_list)
get_the_scores("Osama")
get_the_scores(**scores_list)


