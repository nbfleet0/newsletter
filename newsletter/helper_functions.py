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
            if geo not in word_array:
                word_array.append(geo)

    for vc in vc_list:
        if vc.lower() in article_text.lower():
            if vc not in word_array:
                word_array.append(vc)            

    for keyword in keyword_list:
        if keyword.lower() in article_text.lower():
            if keyword not in word_array:
                word_array.append(keyword)

    while "" in word_array: word_array.remove("")
    while "\n" in word_array: word_array.remove("\n")

            
    return word_array

def getCrunchbaseURL(name):
    name = name.lower().replace(" ", "-")
    return "https://www.crunchbase.com/organization/" + name


def extractName(story_object): #accepts [headline, body]
    headline = story_object[0]
    body = story_object[1]

    first = headline.split(" ")[0].replace(",", "")
    if(first == body.split(" ")[0].replace(",", "")):
        second = headline.split(" ")[1].replace(",", "")
        if(second == body.split(" ")[1].replace(",", "")):
            third = headline.split(" ")[2].replace(",", "")
            if(third == body.split(" ")[2].replace(",", "")):
                return first + " " + second + " " + third
            return first + " " + second
        return first

    first = body.split(" ")[0]
    first = first.replace(",", "")
    if first in headline:
        after = headline.split(first)[1]
        string = first
        for word in after:
            if(word[0].isupper()):
                string = string + " " + word
            else:
                return string
        return string

    else:
        trailing_verbs = ["Receives", "Scores", "Pulls", "Raises", "Announces", "Completes", "Lands", "Snags", "Procures", "Nabs", "Bags", "Closes", 
        "Attracts", "Gathers", "Inks", "Picks", "Rakes", "Takes", "Racks", "receives", "scores", "pulls", "raises", "announces", "completes", "lands", "snags", "procures", "nabs", "bags", "closes", 
        "attracts", "gathers", "inks", "picks", "rakes", "takes", "racks"]

        string = []
        for word in trailing_verbs:
            array = story_object[0].split(word)
            if(len(array) > 1):
                prefix = array[0].split(" ")
                # print(prefix)
                for word in reversed(prefix):
                    if(len(word) > 0):
                        if(word[0].isupper()):
                            string = [word] + string
                        else:
                            break
                string = " ".join(string)
                print(string)
                return string
                break

        print("haven't found anything")

        leading_verbs = ["for", "startup"]

        for word in leading_verbs:
            array = story_object[0].split(word)
            if(len(array) > 1):
                prefix = array[1].split(" ")
                # print(prefix)
                for word in reversed(prefix):
                    if(len(word) > 0):
                        if(word[0].isupper()):
                            string = [word] + string
                        else:
                            break
                string = " ".join(string)
                print(string)
                return string
                break

    return "" #worst case

