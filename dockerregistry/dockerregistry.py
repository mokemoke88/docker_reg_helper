# -*- coding: utf-8 -*-

""" Docker Registry V2 Administration Helper Script
"""

__author__ = 'Katsuhiko Shibata <kshibata@seekers.jp>'
__version__ = '0.0.1'
__date__ = '2017-08-19'

import urllib.request
from urllib.error import HTTPError, URLError
import json

def checkAPIVersionV2(uri):
    """
    Check Enable Docker Reigstry API V2
    """
    request = urllib.request.Request('{0}/v2/'.format(uri))
    response = None
    try:
        response = urllib.request.urlopen(request)
        return True
    except HTTPError as e:
        pass
    except URLError as e:
        pass
    finally:
        if response:
            response.close()
    return False

def getImageCatalog(uri):
    """
    get Image Catalogs
    """
    request = urllib.request.Request('{0}/v2/_catalog'.format(uri))
    response = None
    try:
        response = urllib.request.urlopen(request)
        contents = response.read().decode('utf-8')
        json_dict = json.loads(contents)
        if 'repositories' in json_dict and isinstance(json_dict['repositories'], list):
            return json_dict['repositories']
    except HTTPError as e:
        pass
    except URLError as e:
        pass
    finally:
        if response:
            response.close()
    return []

def getImageTags(uri, image):
    """
    Get Tags in image
    """
    request = urllib.request.Request('{0}/v2/{1}/tags/list'.format(uri, image))
    response = None
    try:
        response = urllib.request.urlopen(request)
        contents = response.read().decode('utf-8')
        json_dict = json.loads(contents)
        if 'tags' in json_dict and isinstance(json_dict['tags'], list):
            return json_dict['tags']
    except HTTPError as e:
        pass
    except URLError as e:
        pass
    finally:
        if response:
            response.close()
    return []

def getDigest(uri, image, tag) :
    """
    Get Digest by image:tag
    """
    request = urllib.request.Request('{0}/v2/{1}/manifests/{2}'.format(uri, image, tag))
    request.add_header('Accept', 'application/vnd.docker.distribution.manifest.v2+json')
    request.get_method = lambda: 'HEAD'
    response = None
    try:
        response = urllib.request.urlopen(request)
        return response.info().get('Docker-Content-Digest')
    except HTTPError as e:
        pass
    except URLError as e:
        pass
    finally:
        if response:
            response.close()
    return ''

def deleteImage(uri, image, digest) :
    """
    Delete Image using Digest
    """
    request = urllib.request.Request('{0}/v2/{1}/manifests/{2}'.format(uri, image, digest))
    request.add_header('Accept', 'application/vnd.docker.distribution.manifest.v2+json')
    request.get_method = lambda: 'DELETE'
    response = None
    try:
        response = urllib.request.urlopen( request )
        return True
    except HTTPError as e:
        # TODO: code handling 404 or
        pass
    except URLError as e:
        pass
    finally:
        if response:
            response.close()
    return False
