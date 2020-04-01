import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="foo-bar-pkg-test", # Replace with your own username
    version="0.0.4",
    author="Jacques Beukes",
    author_email="jpbeukes01@gmail.com",
    description="A small foo bar package for testing Python packaging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JPBeukes/foo_bar_pkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)