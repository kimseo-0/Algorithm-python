import re

def solution(word, pages):
    dic = []
    score = {}
    urls = []

    for page in pages:
        url = re.search('<meta property="og:url" content="(.*)"/>', page, re.DOTALL).group(1)
        links = re.findall('<a href="(.*)">', page, re.DOTALL)
        body = re.search('<body>(.*)</body>', page, re.DOTALL).group(1)
        body = re.sub("<a(.*)</a>", "", str(body))
        body = re.sub("[^a-zA-Z]", " ", str(body))
        # body = re.sub("[0-9]", " ", str(body))
        # body = body.replace("\n", " ")
        # body = body.replace("\t", " ")
        basic_score = len(re.findall(' ' + word + ' ', str(body), re.I))
        dic.append({'url': url, 'links': links, 'body': body, 'basic_score': basic_score})

        score[url] = basic_score
        urls.append(url)

    # print(dic)
    for page in dic:
        for link in page['links']:
            if link in score:
                score[link] += page['basic_score'] / len(page['links'])

    # print(score)
    # print(urls)

    answer = 0
    for i in range(len(urls)):
        if score[urls[i]] > score[urls[answer]]:
            answer = i

    # print(answer)
    return answer


# solution(	"blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"])
solution("Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
                  "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"])