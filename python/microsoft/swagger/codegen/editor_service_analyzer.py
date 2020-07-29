from python.microsoft.swagger.codegen.editorservice import editor_service
from python.microsoft.swagger.codegen.editorservice.models import check_request_v1
from python.microsoft.swagger.codegen.editorservice.models import critique_type_option
from python.microsoft.swagger.codegen.editorservice.models import editor_service_response
from python.microsoft.swagger.codegen.editorservice.models.constants import *


class CheckText:
    textToCheck = ""
    listIncludedCritique = []
    listCritiqueWeight = []
    listDes = []
    language = ""
    profileId = ""
    text_unit = ""
    appId = ""
    weight = 0

    def __init__(self, text, weight):
        self.textToCheck = text
        self.listDes = listDes
        self.listIncludedCrit = listIncludedCrit
        self.listCritWeight = listCritWeight
        self.language = language
        self.profileId = profileId
        self.text_unit = text_unit
        self.appId = appId
        self.weight = weight

    def call_service(self):
        req1 = check_request_v1.CheckRequestV1(self.appId, self.language, self.textToCheck, None, self.listDes,
                                               self.language, self.profileId, self.text_unit)
        service = editor_service.EditorService()
        res = service.post_check(req1)

        return res

    def get_config(self):
        config_req = check_request_v1.CheckRequestV1(self.appId, self.language, self.textToCheck, None, self.listDes,
                                                     self.language)
        service = editor_service.EditorService()
        res = service.config_v1(config_req)

        return res

    def valid_critique_groups(self):
        config = self.get_config()
        valid_group = []
        valid_group_parent = []

        for groups in config.profiles[0].critique_category_info_list:
            critique_temp_group = critique_type_option.CritiqueTypeOption(groups.id, 1, self.language, groups.name)

            if critique_temp_group.name not in self.listIncludedCrit:
                continue

            valid_group.append(critique_temp_group.name)
            valid_group_parent.append(critique_temp_group.name)

            for subGroup in groups.critique_type_info_list:
                valid_group.append(subGroup.name)
                valid_group_parent.append(critique_temp_group.name)

        return valid_group, valid_group_parent

    def get_scores(self):
        res = self.call_service()
        scores = {}
        marks = 0
        errors = 0

        valid_group, valid_group_parent = self.valid_critique_groups()

        for critique in res.critiques:
            if critique.category_title in valid_group:
                i = valid_group.index(critique.category_title)
                if valid_group_parent[i] not in scores:
                    scores[valid_group_parent[i]] = self.listCritWeight[self.listIncludedCrit.index(valid_group_parent[i])]
                else:
                    scores[valid_group_parent[i]] = scores.get(valid_group_parent[i]) + self.listCritWeight[
                        self.listIncludedCrit.index(valid_group_parent[i])]

                marks += scores.get(valid_group_parent[i])
                errors += 1
        marks = round((100 - ((marks * 100) / len(self.textToCheck))) * 2) / 2

        return marks, errors


def main():
    text = "For years I have been drving an old used car with a lot of mileage, and I hate it. It gets me where I need to go, but I’m tired of fixing leaks and broken parts all the time. Its annoying that I hav to take it to mechanic every times. Even when they take care of everything, I know in a week I’ll just end up going back there. I have finally decided that I am not going to do it anymore. I have decided to buy a new car! Unfortunately, I have a problem. I have no idea what car to get. Do I want something fast? Do I want something big? Do I want something stylish? Something economical? I have so many choices that I don’t even know where to begin. I am not sure if I will be able to make the decision on my own. I don't have a lot of money either, so I probably don't have many option. After I did some research, I knew that I would need some expert advice. Eventually, I went to a local dealership to check out some new models. I talked to the saleswoman and listened at she carefully. Her honesty and professionalism were really impressive. She had a lot of vary helpful suggestions and showed myself some safe affordable choices. After a long discussion I finally decided which one I wanted. She not only helped me with the paperwork and finished the sale, but also the insurance. I was expecting this purchase to be a serious hassle, but the experience was almost painless. Everything went smoothly, and now I have a brand new car! I was so excited when I pulled out of the lot that the first thing I did was change lanes right in front of other car. “That wasn't very nice,” I thought to myself. I needed to relax. I didn’t realize what a serious mistake I had made however. I hadn’t just cut off any other car, I had cut off a police car! It took a few seconds to realize what was happening when I saw the flashing lights in my rearview mirror. By the time I had managed to pull over, my heart was racing. I gathered all the paperwork as he approached my window. “You forgot to signal back there” said Officer Johnson, according to his nametag. “Yes, well, it’s a new car so I guess I was a bit unfamiliar with the controls,” I stammered. He looked at me skeptically. “I’m pretty sure the controls for the turn signal are in the same place on every car."
    checker = CheckText(text,2)
    marks, errors = checker.get_scores()
    print(editor_service_response.EditorServiceResponse("editor_critique", marks, errors))


if __name__ == "__main__":
    main()
