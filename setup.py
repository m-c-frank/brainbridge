from setuptools import setup, find_packages

setup(
    name="brainbridge",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'neuralapi @ git+https://github.com/m-c-frank/neuralapi.git#egg=neuralapi'
    ],
    entry_points={
        'console_scripts': [
            'brainbridge=brainbridge.brainbridge:main',
        ],
    },
    author="Martin Christoph Frank",
    author_email="martin7.frank7@gmail.com",
    description="A CLI tool to interact with neural models directly from the command line",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourgithubusername/brainbridge",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
