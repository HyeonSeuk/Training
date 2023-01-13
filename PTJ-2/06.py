import requests
from pprint import pprint


def credits(title):
    pass
    # 여기에 코드를 작성합니다.
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': '1a135b877970744bf1fc70c0b71ef5c6',
        'language': 'ko-KR',
        'query' : title
    }
    params1 = {
        'api_key': '1a135b877970744bf1fc70c0b71ef5c6',
        'language': 'ko-KR'
    }
    try:
        response = requests.get(BASE_URL+path, params=params).json()
        movie_id = response.get('results')[0].get('id') 
        path1 = '/movie/'+str(movie_id)+'/credits'
        response1 = requests.get(BASE_URL+path1, params=params1).json()
        cast1 = response1.get('cast')
        crew1 = response1.get('crew')
        cast = []
        crew = []
        ac = {'cast': cast, 'crew': crew}
        for i in cast1:
            if i.get('cast_id') < 10:
                cast.append(i.get('name'))
        for i in crew1:
            if i.get('department') == 'Directing':
                crew.append(i.get('name'))
        return ac
    except:
        return None
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록 반환
    영화 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
