def select_dates(potential_dates):

    selected_dates = []
    date_results = ""

    for potential_date in potential_dates:

        older_than_30 = False
        lives_in_berlin = False
        likes_art = False

        if int(potential_date["age"]) > 30:
            older_than_30 = True

        if potential_date["city"] == "Berlin":
            lives_in_berlin = True

        if "art" in potential_date["hobbies"]:
            likes_art = True

        if older_than_30 and lives_in_berlin and likes_art:
            selected_dates.append(potential_date["name"])

        date_results = ", ".join(selected_dates)

    return date_results

#
# potential_dates = [{"name": "Julia", "gender": "female", "age": 29,
#                     "hobbies": ["jogging", "music"], "city": "Hamburg"},
#                    {"name": "Sasha", "gender": "male", "age": 18,
#                     "hobbies": ["rock music", "art"], "city": "Berlin"},
#                    {"name": "Maria", "gender": "female", "age": 35,
#                     "hobbies": ["art"], "city": "Berlin"},
#                    {"name": "Daniel", "gender": "non-conforming", "age": 50,
#                     "hobbies": ["boxing", "reading", "art"], "city": "Berlin"},
#                    {"name": "John", "gender": "male", "age": 41,
#                     "hobbies": ["reading", "alpinism", "museums"], "city": "Munich"}]
#
# select_dates(potential_dates)
#
# #return ", ".join(dating_results)
#
# # return ", ".join()
#
