from setuptools import setup


requires = ["aiohttp>=3.5.4"]


setup(
    name='HimazinAPI',
    version='0.1',
    description='暇人きずき氏が運営する「新・暇人が運営する暇人のためのBot」のAPIモジュールです',
    url='https://github.com/nekok500/HimazinAPI',
    author='ねこかわいい',
    author_email='nekokawaii500.1@gmail.com',
    license='MIT',
    keywords='Himazin',
    packages=[
        "HimazinAPI"
    ],
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
)
