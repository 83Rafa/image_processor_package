from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="processing_images",
    version="0.0.1",
    author="83Rafa",
    author_email="elfaramail@gmail.com",
    description="Image color processor",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/83Rafa/image-color-merger.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)