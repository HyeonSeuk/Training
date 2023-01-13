import requests
from pprint import pprint

def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    BASE_URL = 'https://api.themoviedb.org/3' 
    path = '/movie/popular' 
    params = {
        'api_key': '1a135b877970744bf1fc70c0b71ef5c6', 
        'language': 'ko-KR'
    }
    response = requests.get(BASE_URL+path, params=params).json() 
    n = 0
    for i in response.get('results'): 
        n += 1 
    return n
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
