import os
import setuptools

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(
    os.path.join(here, "opendatalab", "__version__.py"), "r", encoding="utf-8"
) as f:
    exec(f.read(), about)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    version=about["__version__"],
    project_urls={
        "Bug Tracker": "https://gitlab.shlab.tech/dps/opendatalab-python-sdk/-/tree/dev-datahub/-/issues",
    },
    install_requires=["requests", "oss2", "Click", "tqdm"],
)
