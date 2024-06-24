def test(funcion):
    def wrapper():
        print("인사가 시작되었습니다.")
        funcion()
        print("인사가 종료되엇습니다.")
    return wrapper

@test
def hello():
    print("hello")

hello()
