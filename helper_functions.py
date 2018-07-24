def generateLists(): #called once in main
    text_file = open("vclist.txt", "r")
    vc_list = text_file.read().split(',')
    text_file.close()
    # geographies
    text_file = open("geographies.txt", "r")
    geo_list = text_file.read().split(',')
    text_file.close()
    # keywords
    text_file = open("keywords.txt", "r")
    keyword_list = text_file.read().split(',')
    text_file.close()


def checkInterestLvl(article_text):
    interest_lvl = 0

    for geo in geo_list:
        if geo.lower() in article_text.lower():
            geo_match += (geo + ", ")
            interest_lvl += 1

    for vc in vc_list:
        if vc.lower() in article_text.lower():
            vc_match += (vc + ", ")
            interest_lvl += 1

    for keyword in keyword_list:
        if keyword.lower() in article_text.lower():
            keyword_match += (keyword + ", ")
            interest_lvl += 1

    return interest_lvl
