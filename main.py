# -*- coding: utf-8 -*-
import json


def jsonconvert(filename1, filename2):
    with open(filename1, 'r', encoding='utf8')as fp:
        json_data = json.load(fp, strict=False)

    subjects = []
    for subject in json_data["subjects"]:
        chapters = []

        for chapter in subject["chapters"]:
            sections = []
            topictitle = chapter["name"]
            for segment in chapter["segments"]:
                section = {"topicTitle": topictitle,
                           "guid": segment["guid"],
                           "text": segment["text"],
                           "elaborate": segment["elaborate"],
                           "srcUrl": segment["srcUrl"],
                           "imgUrl": segment["imgUrl"],
                           "sampleQuestions": segment["sampleQuestions"],
                           "continue": segment["continue"],
                           "type": segment["type"],
                           "action": segment["action"],
                           "htmlTag": "",
                           "pipeline": segment["pipeline"],
                           "internal_path": segment["internal_path"],
                           }
                sections.append(section)

            chapters.append({"name": chapter["name"],
                             "sections": sections
                             })

        subjects.append({"fileName": subject["id"],
                         "name": subject["name"],
                         "chapters": chapters,
                         "isStartUpSubject": subject["isStartUpSubject"],
                         "path": subject["fileUrl"].split("/")
                         })

    output_data = {"subjects": subjects,
                   "synonymsList": [],
                   "guid": "597c0f44-b3ab-49b5-9866-e653dec058a6",
                   "companyId": json_data["workspaceId"],
                   "productId": ""}
    output_str = json.dumps(output_data, ensure_ascii=False, indent=1)
    output_str = output_str.replace('<', '\\u003c')
    output_str = output_str.replace('>', '\\u003e')
    output_str = output_str.replace('&', '\\u0026')
    with open(filename2, 'w', encoding='utf8')as fp:
        fp.write(output_str)


if __name__ == '__main__':
    jsonconvert('format1.json', 'format2.json')
