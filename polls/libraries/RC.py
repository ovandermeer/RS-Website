import ast
from copy import deepcopy

test_input = ast.literal_eval("{'csrfmiddlewaretoken': ['Fkb5qYMZt8LLD1g2tAGJx75TUS6vadOP03slAfTpeNh8m7OVk0x2tZfKt1j3F2WH'], 'name': ['hy3h3gh3h'], 'q1': ['1'], 'q2': ['1'], 'q3': ['1'], 'q4': ['1', '7'], 'q5': ['1'], 'q6': ['1'], 'q7': ['1'], 'q8': ['1'], 'q9': ['1'], 'q10': ['1'], 'q11': ['1']}")
{'csrfmiddlewaretoken': ['KlCJuH5iXZc9pv8oazVoOBMEQj6vLwdCgyj3vN4ijZgWPUkkW5iCli0ec71wd8J2'], 'name': ['bob'], 'q1': ['1'], 'q2': ['1'], 'q3': ['3'], 'q4': ['2', '5'], 'q5': ['1'], 'q6': ['3'], 'q7': ['2'], 'q8': ['1'], 'q9': ['1'], 'q10': ['1'], 'q11': ['1']}

global final_information
final_information = {}


religions = ["Basedism", "Hinduism", "Buddhism", "Sikhism", "Christianity", "Islam", "Judaism"]

global religion_pro_cons

religion_pro_cons = {
    "Basedism" : {
        "pro" : [],
        "con" : []
    },
    "Hinduism" : {
        "pro" : [],
        "con" : []
    },
    "Buddhism" : {
        "pro" : [],
        "con" : []
    },
    "Sikhism" : {
        "pro" : [],
        "con" : []
    },
    "Christianity" : {
        "pro" : [],
        "con" : []
    },
    "Islam" : {
        "pro" : [],
        "con" : []
    },
    "Judaism" : {
        "pro" : [],
        "con" : []
    }
}

def reset():
    global final_information
    final_information = {}
    global religion_pro_cons
    religion_pro_cons = {
        "Basedism" : {
            "pro" : [],
            "con" : []
        },
        "Hinduism" : {
            "pro" : [],
            "con" : []
        },
        "Buddhism" : {
            "pro" : [],
            "con" : []
        },
        "Sikhism" : {
            "pro" : [],
            "con" : []
        },
        "Christianity" : {
            "pro" : [],
            "con" : []
        },
        "Islam" : {
            "pro" : [],
            "con" : []
        },
        "Judaism" : {
            "pro" : [],
            "con" : []
        }
    }

questions = [
    "What happens after death?",
    "How many deities are there?",
    "Types and amount of prayer?",
    "What kind of restrictions are you alright with?",
    "Do you want to travel/go on a pilgrimage?",
    "Preferred type of meeting place for your religious gatherings",
    "Does sitting with people of the opposite sex distract you from the service?",
    "Do you want your place of worship to open during non-service times for personal prayer?",
    "Preferred method of joining a religion",
    "How do you think the world/universe was created?",
    "Do you wish to attain spiritual enlightenment through you or religious authorities?"
]


quiz = {
    1 : ["Reincarnation", "Go to a holy place", "Nothing"],
    2 : ["One (Monotheistic)", "More than one God (Polytheistic)", "More than one aspect of one God", "None"],
    3 : ["Regimented prayer schedule", "Recommended prayer", "Meditation", "Group prayer"],
    4 : ["Eating And Drinking Restrictions", "Manditory fasting", "Restrictions on who you can marry", "No pre-marital sex", "Restrictions on Gender Identity/Sexuality", "Restrictions on cutting hair", "None of the above"],
    5 : ["Yes", "No"],
    6 : ["Worships in a building of religious significance of a specific week day each week", "Often happens in a building of religious significance but sometimes happens in an informal setting, on a specific day of the week", "Worship is not on a specific day, or no common gathering place"],
    7 : ["Yes", "No"],
    8 : ["Yes", "No"],
    9 : ["Start showing up", "Specific ritual", "Through birth or a special council"],
    10 : ["No specific way", "The heavens and earth were created in six days, and on the seventh day, God rested.", "The God(s) created it and it is just an extension of the God(s)"],
    11 : ["Through the clergy", "Personal Relationship"]
}

ans_key = {
    1 : [[0,1,2,3], [4,5,6], []],
    2 : [[3,4,5,6], [0], [1], [2]],
    3 : [[5], [6,4], [0,2,1], [0]],
    4 : [[5,6], [5,4], [5,6], [4,5,6], [1,2,3,4,5,6], [3], [0]],
    5 : [[0,1,4,5,6], [2,3]],
    6 : [[4,5,6], [0,2], [1,3]],
    7 : [[1,3,5], [0,2,4,6]],
    8 : [[0,1,2,3], [4,5,6]],
    9 : [[0,1,2], [3,4,5], [6]],
    10 : [[2], [4,5,6], [0,1,3]],
    11 : [[4], [0,1,2,3,5,6]]
}

def translate_to_stupid(fin):
    final = []
    for i in fin:
        if "q" in i:
            select_ans = [int(item) for item in fin[i]]
            question_num = int(i[1:])
            pos_ans = list(range(1,len(ans_key[int(question_num)]) + 1))
            final.append([select_ans, {question_num : pos_ans}])
    return final


def get_rel(num):
    return religions[num]

def add_answer(question : dict) -> None:
    (ans_num, query) = question
    for i in query.keys():
        query_num = i
        break
    new_info = []
    for i in query.values():
        for j in i:
            for k in query.keys():
                key = k
                break
            new_info.append(j in ans_num)
    final_information[query_num] = new_info



def make_pro_con_dict() -> None:
    for index, j in enumerate(final_information.values()):
        key = index + 1
        for ind, i in enumerate(ans_key[key]):
            try:
                if j[ind]:
                    for rel in i:
                        religion = get_rel(rel)
                        religion_pro_cons[religion]["pro"].append([key,ind])

                else:
                    for rel in i:
                        religion = get_rel(rel)
                        religion_pro_cons[religion]["con"].append([key, ind])
            except IndexError:
                pass

def get_pro_con_ans(coord):
    (question,ans) = coord
    answer = quiz[question][ans]
    title = questions[question - 1]
    return_value = {title : answer}
    return return_value

def make_under(word: str) -> str:
    return ""

def order_religions():
    new_dict = deepcopy(religion_pro_cons)
    final = []
    while new_dict:
        new_top = get_top(new_dict)
        final.append(new_top)
        new_dict.pop(new_top)
    return final

def get_result(sorted_reli) -> str:
    result = ""
    for i in sorted_reli:
        result += f"<religion>{i}</religion>\n{make_under(i)}\n<pros>Pros</pros>\n<survey_ans>"
        prev_key = ""
        for j in religion_pro_cons[i]["pro"]:
            pro_dict = get_pro_con_ans(j)
            key = list(pro_dict.keys())[0]
            val = pro_dict[key]
            if prev_key == key:
                result = result[:-1]
                result += f"""
    -<answers>{val}</answers>\n"""
            else:
                result += f"""  <questions>{key}</questions>
    -<answers>{val}</answers>\n"""
            prev_key = key
        result += f"<cons>Cons</cons>\n"
        prev_key = ""
        for j in religion_pro_cons[i]["con"]:
            con_dict = get_pro_con_ans(j)
            key = list(con_dict.keys())[0]
            val = con_dict[key]
            if prev_key == key:
                result = result[:-1]
                result += f"""
    -<answers>{val}</answers>\n"""
            else:
                result += f"""  <questions>{key}</questions>
    -<answers>{val}</answers>\n"""
            prev_key = key
            
        result += "</survey_ans> \n"
    return result[:-2]

def add_answers(answers: list) -> None:
    for i in answers:
        add_answer(i)

def make_answers(fin : dict) -> list:
    return translate_to_stupid(fin)

def get_top(reli: dict) -> list:
    count = 0
    top = []
    for i in reli:
        cur_count = len(reli[i]["pro"])
        if cur_count > count:
            count = cur_count
            top = [i]
        elif cur_count == count:
            top.append(i)
    if len(top) > 1:
        lowest_con = 100
        best = []
        for i in top:
            cur_count = len(reli[i]["con"])
            if cur_count < lowest_con:
                lowest_con = cur_count
                best = [i]
            if cur_count == lowest_con:
                best.append(i)
        top = list(best)
    return top [0]
    
        

def exec(form_input: dict) -> None:
    reset()
    answers = make_answers(form_input)
    add_answers(answers)
    make_pro_con_dict()
    new_order = order_religions()
    return [get_result(new_order), get_top(religion_pro_cons)]
    

if __name__ == "__main__":
    for i in range(1):
        print(exec(test_input)[0])