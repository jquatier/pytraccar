"""Setup configuration."""
import setuptools

with open("README.md", "r") as fh:
    LONG = fh.read()
setuptools.setup(
    name="pytraccar",
    version="0.2.1",
    author="Joakim Sorensen",
    author_email="ludeeus@gmail.com",
    description="",
    long_description=LONG,
    install_requires=['aiohttp', 'async_timeout'],
    long_description_content_type="text/markdown",
    url="https://github.com/ludeeus/pytraccar",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
