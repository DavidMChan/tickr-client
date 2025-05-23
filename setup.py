from setuptools import setup, find_packages

setup(
    name="tickr-client",
    version="0.1.0",
    description="Python client for the Tickr API (counters service)",
    author="Your Name",
    packages=find_packages(),
    install_requires=["requests>=2.25.1"],
    python_requires=">=3.7",
)
