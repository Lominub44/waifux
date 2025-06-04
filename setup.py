from setuptools import setup, find_packages

setup(
    name="WaifuX",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click"
    ],
    entry_points={
        'console_scripts': [
            'waifux=waifux.cli:main',
        ],
    },
    author="Lomi",
    description="CLI tool for showing random waifu ASCII art",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "Topic :: Artistic Software",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
)
