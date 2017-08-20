# -*- coding: utf-8 -*-

"""
Docker Regsitry Adminiration Helper Script entrypoint
"""

import sys
import argparse
from . import dockerregistry

def command_images(args):
    """
    execute images command.
    """
    uri = args.uri
    if False == dockerregistry.checkAPIVersionV2(uri):
        return 'invalid registry server'

    result = dockerregistry.getImageCatalog(uri)
    for item in result:
        tags = dockerregistry.getImageTags(uri, item)
        for tag in tags:
            print('{0}:{1}'.format(item, tag))

    return 0

def command_tags(args):
    """
    execute tags command.
    """
    if False == dockerregistry.checkAPIVersionV2(args.uri):
        return 'invalid registry server'

    tags = dockerregistry.getImageTags(args.uri, args.image)
    for tag in tags:
        print('{0}:{1}'.format(args.image, tag))

    return 0

def command_delete(args):
    """
    execute delete command.
    """
    if False == dockerregistry.checkAPIVersionV2(args.uri):
        return 'invalid registry server'

    image = args.image.split(':',1)

    if len(image) == 2 :
        if image[1] == '*':
            tags = dockerregistry.getImageTags(args.uri, image[0])
            for tag in tags:
                digest = dockerregistry.getDigest(args.uri, image[0], tag)
                if digest == '':
                    print('{0}:{1} digest not found.'.format(image[0], tag))
                    continue
                print('{0}:{1} digest:{2}'.format(image[0], tag, digest))
                if False == args.dry_run:
                    dockerregistry.deleteImage(args.uri, image[0], digest)
        else:
            tag = image[1]
            digest = dockerregistry.getDigest(args.uri, image[0], tag)
            if digest == '':
                return ('{0}:{1} digest not found.'.format(image[0], tag))
            print('{0}:{1} digest:{2}'.format(image[0], tag, digest))
            if False == args.dry_run:
                dockerregistry.deleteImage(args.uri, image[0], digest)
    else:
        return 'image format error.'

    return 0

def main():
    """
    entrypoint
    """
    parser = argparse.ArgumentParser(description='Docker Registry V2 Administration Helper Script')
    subparsers = parser.add_subparsers()

    parser_images = subparsers.add_parser('images', help='see `images -h`')
    parser_images.add_argument('uri', help='target docker registry URL')
    parser_images.set_defaults(handler=command_images)

    parser_tags = subparsers.add_parser('tags', help='see `tags -h`')
    parser_tags.add_argument('uri', help='target docker registry URL')
    parser_tags.add_argument('image', help='target image')
    parser_tags.set_defaults(handler=command_tags)

    parser_delete = subparsers.add_parser('delete', help='see `delete -h`')
    parser_delete.add_argument('--dry-run', action='store_true', help='dry run')
    parser_delete.add_argument('uri', help='target docker registry URL')
    parser_delete.add_argument('image', help='target image')
    parser_delete.set_defaults(handler=command_delete)

    args = parser.parse_args()
    if hasattr(args, 'handler'):
        return args.handler(args)
    else:
        parser.print_help()
        return 1

if __name__ == "__main__":
    sys.exit( main() )
