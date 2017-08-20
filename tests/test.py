# -*- coding: utf-8 -*-
"""
unit test code
"""

import unittest
from unittest import mock
import urllib.request
from urllib.error import HTTPError, URLError

from dockerregistry import dockerregistry

class TestDockerRegistryControl(unittest.TestCase) :
    """
    """
    def test_getImageCatalog(self) :
        """
        getImageCatalog Function Test
        """

        urlopen_path = (
            'urllib.request.urlopen'
        )

        with mock.patch(urlopen_path) as urlopen_mock:
            """ return False when raise HTTPError
            """
            urlopen_mock.side_effect = HTTPError('','','','',None)
            result = dockerregistry.getImageCatalog('http://registry.seekers.jp')
            self.assertFalse(result)
            urlopen_mock.assert_called()

        with mock.patch(urlopen_path) as urlopen_mock:
            """ return False when raise URLError
            """
            urlopen_mock.side_effect = URLError('')
            result = dockerregistry.getImageCatalog('http://registry.seekers.jp')
            self.assertFalse(result)
            urlopen_mock.assert_called()

        with mock.patch(urlopen_path) as urlopen_mock:
            """ raise exception when raise exception
            """
            urlopen_mock.side_effect = Exception()
            self.assertRaises(Exception, lambda: dockerregistry.getImageCatalog('https://registry.seekers.jp'))
            urlopen_mock.assert_called()

        """ return empty list when invalid URL
        """
        self.assertIsInstance( dockerregistry.getImageCatalog('http://registry.seekers.jp'), list )
        """ return empty list when invalid URL
        """
        self.assertIsInstance( dockerregistry.getImageCatalog('http://rgistry.seekers.jp'), list )

        """ TODO: return empty list when invalid contents.
        """

        """ return any list when valid URL
        """
        uri = 'https://registry.seekers.jp'
        result = dockerregistry.getImageCatalog(uri)
        self.assertIsInstance( result, list )

    def test_getImageTags(self):
        """
        TODO:
        """
        pass
    def test_getDigest(self):
        """
        TODO:
        """
        pass
    def test_deleteImage(self):
        """
        TODO:
        """
        pass

    def test_checkAPIVersionV2(self):
        """
        checkAPIVersionV2 Function Test
        """
        urlopen_path = (
            'urllib.request.urlopen'
        )

        with mock.patch(urlopen_path) as urlopen_mock:
            """ return False when raise HTTPError
            """
            urlopen_mock.side_effect = HTTPError('','','','',None)
            result = dockerregistry.checkAPIVersionV2('http://registry.seekers.jp')
            self.assertFalse(result)
            urlopen_mock.assert_called()

        with mock.patch(urlopen_path) as urlopen_mock:
            """ return False when raise URLError
            """
            urlopen_mock.side_effect = URLError('')
            result = dockerregistry.checkAPIVersionV2('http://registry.seekers.jp')
            self.assertFalse(result)
            urlopen_mock.assert_called()

        with mock.patch(urlopen_path) as urlopen_mock:
            """ raise exception when raise exception
            """
            urlopen_mock.side_effect = Exception()
            self.assertRaises(Exception, lambda: dockerregistry.checkAPIVersionV2('https://registry.seekers.jp'))
            urlopen_mock.assert_called()

        with mock.patch(urlopen_path) as urlopen_mock:
            """ return True when no exection raised
            """
            response_mock = urlopen_mock.return_value
            response_mock.close.return_value = None
            result = dockerregistry.checkAPIVersionV2('https://registry.seekers.jp')
            self.assertTrue(result)
            response_mock.close.assert_called_with()
            urlopen_mock.assert_called()

if __name__ == "__main__":
    unittest.main()
