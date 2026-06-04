"""
AllAtomic - Setup Script
Dev: @GhostMarshal | Channel: @ComputeCode
(૨๑•̀ㅁ•́ฅा) Purple Anime Theme (#9A8CFF)
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="AllAtomic",
    version="2.0.0",
    author="GhostMarshal",
    author_email="ghostmarshal@example.com",
    description="Your Ultimate Telegram Userbot (✿◠‿◠)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/corruptcrew/AllAtomic",
    project_urls={
        "Bug Tracker": "https://github.com/corruptcrew/AllAtomic/issues",
        "Documentation": "https://github.com/corruptcrew/AllAtomic#readme",
        "Source Code": "https://github.com/corruptcrew/AllAtomic",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Topic :: Communications :: Chat",
        "Topic :: Internet :: WWW/HTTP",
    ],
    python_requires=">=3.11",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "allatomic=AllAtomic.__main__:main",
        ],
    },
    keywords=["telegram", "userbot", "pyrogram", "bot", "anime"],
)
