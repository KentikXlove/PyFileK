from setuptools import setup, find_packages

setup(
    name="my_library",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'numpy',  # Пример зависимости
    ],
    author="Ваше Имя",
    author_email="your.email@example.com",
    description="Краткое описание библиотеки",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/my_library",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
