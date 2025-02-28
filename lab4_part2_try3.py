class SocialNetwork:
    def __init__(self, name: str, user_count: int):
        """
        инициализатор объекта социальной сети
        :param name: наименование социальной сети
        :param user_count: количество товарищей в социальной сети
        """
        self.name = name
        self.user_count = user_count

    def post(self, content: str) -> str:
        """
        Разрешенный к размещению контент
        :param content: То что будет опубликовано
        :return: Уведомление подтверждающее публикацию
        """
        return f"Posted on {self.name}: {content}"

    def get_user_count(self) -> int:
        """
        Общее число товарищей в социальной сети
        :return: Общее число товарищей
        """
        return self.user_count


class VK(SocialNetwork):
    def __init__(self, name: str, user_count: int, likes: int, reposts: int):
        """
        получаем объект VK.
        :param name: наименование социальной сети (VK)
        :param user_count: количество товарищей в  VK
        :param likes: количество лайков в VK
        :param reposts: количество поделившихся людей в  VK
        """
        super().__init__(name, user_count)
        self.likes = likes
        self.reposts = reposts

    def get_user_count(self) -> int:
        """
        Общее количество товарищей в  VK.
        :return: Уведомление с общим количеством товарищей в VK
        """
        return self.user_count


class Facebook(SocialNetwork):
    def __init__(self, name: str, user_count: int, comments: int):
        """
        получаем объект Facebook.
        :param name: наименование социальной сети (Facebook)
        :param user_count: количество товарищей в Facebook
        :param comments: количество комментариев в Facebook
        """
        super().__init__(name, user_count)
        self.comments = comments

    def get_user_count(self) -> int:
        """
        Общее количество товарищей в Facebook.

        :return: Уведомление с общим количеством товарищей в Facebook
        """
        return self.user_count


if __name__ == "__main__":
    vk = VK("VK", 1000000, 5000, 2000)
    facebook = Facebook("Facebook", 1500000, 3000)

    print(vk.post("Привет, ФСБ!"))
    print(vk.get_user_count())

    print(facebook.post("Привет, Цукерберг!"))
    print(facebook.get_user_count())
