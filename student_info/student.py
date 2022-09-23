class Student:

    __chat_id = 0
    __direction = ""
    __course = 0
    __group = ""
    __path_to_hw = ""

    def __init__(self, chat_id, direction, course, group):
        self.__chat_id = chat_id
        self.__direction = direction
        self.__course = course
        self.__group = group

    def __init__(self):
        pass

    def set_chat_id(self, chat_id):
        self.__chat_id = chat_id

    def set_direction(self, direction):
        self.__direction = direction

    def set_course(self, course):
        self.__course = course

    def set_group(self, group):
        self.__group = group

    def set_path_to_hw(self, path_to_hw):
        self.__path_to_hw = path_to_hw

    def get_chat_id(self):
        return self.__chat_id

    def get_direction(self):
        return self.__direction

    def get_course(self):
        return self.__course

    def get_group(self):
        return self.__group
