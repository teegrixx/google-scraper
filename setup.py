from setuptools import setup, find_packages

setup(
    name='google-scraper',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
    'console_scripts': [
        'scrape=google_scraper.scraper:main'
    ]
},
    install_requires=[
        'requests',
        'beautifulsoup4'
    ],
    author='TEEGRIXC',
    author_email='teegrixx01@gmail.com',
    description='A simple Google search scraper',
    url='https://github.com/teegrixx/google-scraper',
)
254-750-963901
