import setuptools
from pathlib import Path
import platform


extra_require = {}
if platform.system() == "Windows":
    extra_require["windows"] = ["pywin32"]

setuptools.setup(
    name="accesswatch",
    author="Mahdi Khoshdel",
    author_email="mahdikhoshdel47@gmail.com",
    version="1.0.3",
    description="A tool that retrieves and displays file or directory access information In Linux and Windows",
    long_description=Path("README.md").read_text(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    url="https://github.com/mahdikhoshdel/accesswatch.git",
    python_requires='>=3.6',
    extra_require=extra_require,
    license='MIT',
)