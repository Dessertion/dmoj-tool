import setuptools

setuptools.setup(
    name="dmoj-tool-dessertion",
    version="0.1.7",
    author="Desertion",
    author_email="73731354pi@gmail.com",
    description="CLI submission to DMOJ",
    # scripts=['bin/dmoj-tool'],
    packages=['dmoj_tool'],
    package_dir={'dmoj-tool':'dmoj_tool'},
    entry_points={
        'console_scripts':[
            'dmoj-tool = dmoj_tool.cli:main',
        ]
    },
    include_package_data=True,
    install_requires=['beautifulsoup4','bs4','certifi','chardet','idna','requests','soupsieve','urllib3'],
    python_requires='>=3.6'
)