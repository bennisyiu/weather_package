from setuptools import setup

setup(
    name='checkweather',  # Your package will have this name
    packages=['checkweather'],  # Name the package again
    version='1.0.0',  # To be increased every time you change your library
    license='MIT',  # Type of license. More here: https://help.github.com/articles/licensing-a-repository
    description='Weather forecast data',  # Short description of your library
    author='Bennis Yiu',  # Your name
    author_email='bennisyiu@gmail.com',  # Your email
    # Homepage of your library (e.g. github or your website)
    url='https://example.com',
    # Keywords users can search on pypi.org
    keywords=['weather', 'forecast', 'openweather'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        # Choose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',  # Who is the audience for your library?
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Type a license again
        # Python versions that your library supports
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
