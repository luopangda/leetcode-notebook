"""
获取官网上的加锁题目
"""
from tools.all_kinds_of_types_data_to_csv import nested_list_to_csv
from tools.get_data import get_data_by_link
from urllib.parse import quote

url = "https://leetcode.com/api/problems/all/"
raw_data = get_data_by_link(url)
stat_status_pairs = raw_data["stat_status_pairs"]
locked_questions = []

for item in stat_status_pairs:
    if item["paid_only"]:
        # 判断是否能在“九章算法平台上找到并且不用付费的”
        frontend_question_id = item["stat"]["frontend_question_id"]
        question__title = item["stat"]["question__title"]
        url = "https://www.jiuzhang.com/api/solution/?search={search}"
        url = url.format(search=quote(question__title))
        data = get_data_by_link(url)
        print(data)
        question__title_joined = question__title.replace(" ", "-").replace("---", "-").lower()
        website_a_company = "http://206.81.6.248:12306/leetcode/" + question__title_joined + "/description"
        if data["results"]:
            for child in data["results"]:
                is_private = child["is_private"]
                cn_title = child["cn_title"]
                description = child["description"]
                cn_description = child["cn_description"]
                if "unique_name" in child:
                    website_jiuzhang = "https://www.jiuzhang.com/solution/" + child["unique_name"]
                else:
                    website_jiuzhang = "https://www.jiuzhang.com/solution/" + question__title_joined
                if is_private:
                    locked_question_info = {"id": frontend_question_id, "title": question__title,
                                            "cn_title": cn_title, "description": description,
                                            "can_find_answer": 0, "accessible_website_jiuzhang": "-",
                                            "accessible_website_a_company": website_a_company}
                    locked_questions.append(locked_question_info)
                else:
                    locked_question_info = {"id": frontend_question_id, "title": question__title,
                                            "cn_title": cn_title, "description": description,
                                            "can_find_answer": 1, "accessible_website_jiuzhang": website_jiuzhang,
                                            "accessible_website_a_company": website_a_company}
                    locked_questions.append(locked_question_info)
        else:
            locked_question_info = {"id": frontend_question_id, "title": question__title,
                                    "cn_title": "-", "description": "-",
                                    "can_find_answer": 0, "accessible_website_jiuzhang": "-",
                                    "accessible_website_a_company": website_a_company}
            locked_questions.append(locked_question_info)

nested_list_to_csv(locked_questions, "locked_questions_3.csv")
print("目前有" + str(len(locked_questions)) + "加锁的题目")
