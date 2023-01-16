import pytest

pytestmark = pytest.mark.django_db


class TestBlogModel:
    def test_str_return(self, blog_factory):
        blog = blog_factory(title="test-blog")
        assert blog.__str__() == "test-blog"
