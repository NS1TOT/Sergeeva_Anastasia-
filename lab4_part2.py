class SocialNetwork:
    def __init__(self, name: str, user_count: int):
        self.name = name
        self.user_count = user_count
    def post(self, content: str) -> str:
        return f"Posted on {self.name}: {content}"
    def get_user_count(self) -> int:
        return self.user_count
class VK(SocialNetwork):
    def __init__(self, name: str, user_count: int, likes: int, reposts: int):
        super().__init__(name, user_count)
        self.likes = likes
        self.reposts = reposts

    def get_user_count(self) -> int:
        return f"Total users in VK: {self.user_count}"

class Facebook(SocialNetwork):
    def __init__(self, name: str, user_count: int, comments: int):
        super().__init__(name, user_count)
        self.comments = comments

    def get_user_count(self) -> int:
        return f"Total users in Facebook: {self.user_count}"
