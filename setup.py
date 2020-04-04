import setuptools

setuptools.setup(
    name="dmoj-tool-dessertion",
    version="0.0.9",
    author="Desertion",
    author_email="73731354pi@gmail.com",
    description="CLI submission to DMOJ",
    scripts=['bin/dmoj-tool'],
    packages=setuptools.find_packages(),
    install_requires=['beautifulsoup4','bs4','certifi','chardet','idna','requests','soupsieve','urllib3'],
    python_requires='>=3.6'
)