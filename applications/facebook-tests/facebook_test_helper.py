import pytest
from services.friends import Friends
from services.posts import Posts
from services.user import User


class FacebookTestHelper(object):

    @pytest.mark.fixture(autouse=True)
    def setup_utils(self):
        self.posts_util = Posts()
        self.friends_util = Friends()
        self.user_util = User()
