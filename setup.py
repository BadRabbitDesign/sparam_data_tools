import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="data_tools",
    version="0.0.1",
    author="Caspar Lucas",
    author_email="caspar@badrabbit.co.uk",
    description="Data Tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BadRabbitDesign/sparam_data_tools",
    packages=setuptools.find_packages(),
)