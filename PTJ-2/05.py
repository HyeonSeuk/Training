import requests
from pprint import pprint


def recommendation(title):
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
        # 무비아이디는 입력한 값으로 검색한 영화 정보들 중 첫 번째 영화의 아이디.
        path1 = '/movie/'+str(movie_id)+'/recommendations'
        response1 = requests.get(BASE_URL+path1, params=params1).json()
        # response1는 무비아이디로 검색한 추천 영화들의 리스트.
        list = []
        for i in range(len(response1.get('results'))): # 제목들만 나오게
            list.append(response1.get('results')[i].get('title'))
        return list
    except:
        return None

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
    