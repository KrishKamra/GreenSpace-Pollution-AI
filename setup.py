from setuptools import setup, find_packages

setup(
    name="greenspace_pollution_ai",
    version="0.1.0",
    description="An AI-driven approach to urban air quality prediction.",
    author="Krish Kamra",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "statsmodels",
        "joblib",
        "python-dotenv",
        "requests"
    ],
    python_requires=">=3.8",
)