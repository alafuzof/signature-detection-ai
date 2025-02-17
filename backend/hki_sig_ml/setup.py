import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hki_sig_ml-alafuzof",
    version="0.1.0",
    author="Aleksander Alafuzoff",
    author_email="aleksander.alafuzoff@siili.com",
    description="Helsinki PDF signature detection model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)