'''
모노 스테이트 패턴
'''


class GitFetcher:
    __current_tag = None
    
    def __init__(self, tag):
        self.current_tag = tag

    
    @property
    def current_tag(self):
        if not self.__current_tag:
            raise AttributeError("tag가 초화ㅣ지 않음")
        return self.__current_tag
    

    @current_tag.setter
    def current_tag(self, new_tag):
        self.__class__.__current_tag = new_tag

    
    def pull(self):
        print(f'{self.__class__}에서 pull')
        return self.current_tag
    
f1 = GitFetcher(0.1)
f2 = GitFetcher(0.2)
f1.current_tag = 0.3
print(f2.pull(), f1.pull())


# class SharedAttribute:
#     def __init__(self, initial_value=None):
#         self.value = initial_value
#         self.__name = None
    

#     def __get__(self, instance, owner):
#         if instance in None:
#             return self
#         if self.value is None:
#             raise AttributeError(f"{self.__name} was never set")
#         return self.value
    
    
#     def __set__(self, instance, new_value):
#         self.value = new_value

    
#     def __set_name__(self, owner, name):
#         self.__name = name


# class GitFetcher:
#     current_tag = SharedAttribute()
#     current_branch = SharedAttribute()

#     def __init__(self, tag, branch=None) -> None:
#         self.current_tag = tag
#         self.current_branch = branch


#     def pull(sself):
#         print(f'{sself.current_tag}에서 pull')
#         return sself.current_tag
    

# f1 = GitFetcher(SharedAttribute(0.1))
# f2 = GitFetcher(SharedAttribute(0.2))

# print(f2.pull(), f1.pull())
