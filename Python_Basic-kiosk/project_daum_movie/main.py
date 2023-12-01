from collect.collect_daum_movie_review import review_collector
from db.movie_dao import get_last_review
def main():
    print("=" * 100)
    print("== 영화 리뷰 수집기 ver 1.0 ==")
    print("=" * 100)
    movie_code = input("== 영화코드 : ") # 169328
    print('== MSG: "매일 낮 12시 수집 한번씩 수집"')
    # last_date = DB에 저장된 마지막 리뷰 날짜

    # DB에서 데이터 조회 실패 -> None
    last_date = get_last_review()
    if last_date == None:
        last_date = 0
    else:
        last_date = int(last_date["int_regdate"])



    review_collector(movie_code, last_date)


if __name__ == "__main__":
    main()
