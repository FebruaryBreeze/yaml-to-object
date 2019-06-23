from pathlib import Path

import yaml_to_object

if yaml_to_object.generate(Path(__file__).parent / 'example.yml', suffix='config'):
    from .build import *  # noqa: F403
