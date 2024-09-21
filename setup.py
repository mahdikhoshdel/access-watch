import setuptools
from pathlib import Path

setuptools.setup(
    name="accesswatch",
    version=1.0,
    description="A tool that retrieves and displays file or directory access information In Linux and Windows",
    long_description=Path("README.md").read_text(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages()
)