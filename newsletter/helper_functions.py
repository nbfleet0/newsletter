def checkInterestLvl(article_text):
    interest_lvl = 0
    word_array = []

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

    for geo in geo_list:
        if geo.lower() in article_text.lower():
            word_array.append(geo)

    for vc in vc_list:
        if vc.lower() in article_text.lower():
            word_array.append(vc)            

    for keyword in keyword_list:
        if keyword.lower() in article_text.lower():
            word_array.append(keyword)

    while "" in word_array: word_array.remove("")
    while "\n" in word_array: word_array.remove("\n")

    # for element in word_array: #sanatize
    #     element.strip()
    #     if element == "":
    #         word_array.remove(element)
    #     if element == "\n":
    #         print("removing new line")
    #         word_array.remove(element)
            
    return word_array
