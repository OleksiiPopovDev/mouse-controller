from setuptools import setup, find_packages
import sys

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Base requirements
requirements = []

# Handle pyautogui dependency based on Python version and platform
if sys.platform == "darwin" and sys.version_info < (3, 9):
    # For macOS with Python < 3.9, use older pyautogui version
    requirements.append("pyautogui==0.9.53")
else:
    # For other platforms or Python >= 3.9, use latest pyautogui
    requirements.append("pyautogui>=0.9.54")

# Add other requirements
requirements.extend([
    "pytest>=7.0.0",
])

setup(
    name="mouse-controller",
    version="1.0.0",
    description="Advanced mouse cursor movement controller",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "mouse-controller=mouse_controller.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
