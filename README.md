# Docker Registry V2 Adminiratoin Helper Script

Private Docker Registry V2 Administration Helper

## Feature

- display contain images
- delete contain images

this script only delete image:tag manifests  
need delete blob objects, exec garbage-collect on registry  
e.g.

```
docker exec -it docker-registry bin/registry garbage-collect /etc/docker/registry/config.yml
```

## License

This software is released under the MIT License, see LICENSE.txt

## build

### build requirement

- wheel
- pypandoc


### test

```
python setup.py test
```

### build and create wheel package

```
python setup.py bdist_wheel

```


## install

```
pip install dist/*.whl
```


## uninstall

```
pip unistall dockerregistry
```

## usage

```
<CLI> [-h] {images, tags, delete} ...
```

`<CLI>` is
- `python -m dockerregistry.main` (when no installed.)
- `dockerregistry` (when installed.)

### print all images

```
<CLI> images <private docker registry url>
```

### print tags in image

```
<CLI> tags <private docker registry url> <image>
```

### delete image

```
<CLI> delete <private docker registry url> <image:tag>

dry-run:
<CLI> delete --dry-run <private docker registry uri> <image:tag>
```

### delete all tags in image

```
<CLI> delete <private docker registry uri> <image:*>

dry-run:
<CLI> delete --dry-run <private docker registry uri> <image:*>
```
