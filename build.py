import os
from setuptools_cpp import CMakeExtension, ExtensionBuilder
from typing import Any, Dict


def build(setup_kwargs: Dict[str, Any]) -> None:
    ext_modules = [
        CMakeExtension("llamacpp.llamacpp", sourcedir="."),
    ]

    setup_kwargs.update(
        {
            "ext_modules": ext_modules,
            "cmdclass": dict(build_ext=ExtensionBuilder),
            "zip_safe": False,
            "options": {
                'bdist_wheel': {
                    'plat_name': os.getenv('PP_PYTHON_TARGET', 'any')
                },
                'egg_info': {
                    'egg_base': './build/'
                }
            }
        }
    )
