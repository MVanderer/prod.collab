from setuptools import find_packages, setup

# Комментарий для Дениса

with open('README.md') as fd:
    README = fd.read()

install_requires = [
    # primary packages only
    'Flask==1.1.2',
    'Flask-API==2.0',
    'Flask-Login==0.5.0',
    'PyYAML==5.3.1',
    'requests==2.22.0',
]


setup(
    name="prod.collab",
    description="Demo Project to showcase Collab practices",
    long_description=README,
    keywords='prod, collab',
    author='Vadim Flaks, Denis Egorov',
    author_email='vadim.viktorovich.flaks@gmail.com',
    url='https://github.com/MVanderer/prod.collab',
    license='GNU GENERAL PUBLIC LICENSE',
    packages=find_packages(
        where='src',
        exclude=['tests']),
    include_package_data=True,
    package_dir={
        '': 'src',
        'login': 'src/login',
        'api': 'src/api',
    },
    package_data={
        'static': ['src/api/static/*'],
        'templates': ['src/api/templates/*'],
    },
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ],
)
