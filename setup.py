from setuptools import setup


setup(
    name="sigma",
    version="0.2.1a0",
    packages=["sigma"],
    install_requires=["sigma.core", "sigma.standard"],
    extras_require={},
    zip_safe=True,
    package_data={
        "": ["*.txt", "*.rst", "*.md"]
    },
    author="Suzuki Shunsuke",
    author_email="suzuki.shunsuke.1989@gmail.com",
    description="Validation framework(namespace package).",
    license="MIT",
    keywords="validation",
    url="https://github.com/pysigma/namespace",
)
