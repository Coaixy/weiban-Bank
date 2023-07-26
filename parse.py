import json

textData = 0

with open("data.json", "r", encoding="utf-8") as file:
    textData = file.read()
jsonData = json.loads(textData)["data"]["questions"]
qc = list()
result = dict()
couter = 0
for i in jsonData:
    if not (i["title"] in qc):
        text = ""
        for j in i["optionList"]:
            if j["isCorrect"] == 1:
                text = text + j["content"] + "--"
        result[i["title"]] = text
        qc.append(i["title"])
        couter = couter + 1
print(couter)
data = json.dumps(result, ensure_ascii=False)
with open("result.json", "w", encoding="utf-8") as file:
    file.write(data)
