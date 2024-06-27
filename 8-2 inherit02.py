class CustomException(Exception):
    def __init__(self):
        super().__init__()
        print("#### 내가 만든 오류가 생성되었어요 ####")

raise CustomException
