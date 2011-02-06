from tests import FlexGetBase
from nose.plugins.attrib import attr


class TestTmdbLookup(FlexGetBase):

    __yaml__ = """
        feeds:
          invalid url:
            mock:
              - {title: '[Group] Taken 720p', imdb_url: 'http://www.imdb.com/title/tt0936501/'}
              - {title: 'The Matrix'}
            tmdb_lookup: yes
    """

    @attr(online=True)
    def test_invalid_url(self):
        self.execute_feed('invalid url')
        # check that these were created
        assert self.feed.find_entry(tmdb_name='Taken', tmdb_year=2008), 'Didn\'t populate tmdb info for Taken'
        assert self.feed.find_entry(tmdb_name='The Matrix', tmdb_year=1999), \
                'Didn\'t populate tmdb info for The Matrix'
