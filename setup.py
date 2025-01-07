from setuptools import setup, find_packages

setup(
    name="ServerFolder",
    version="1.0.0",
    description="Uno script Python per generare cartelle di sistema in modo interattivo.",
    author="Tuo Nome",
    author_email="tuo.email@example.com",
    url="https://github.com/TuoUsername/ServerFolder",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "serverfolder=main:main",
        ],
    },
    install_requires=[],  # Aggiungi le dipendenze qui, se necessario
)
