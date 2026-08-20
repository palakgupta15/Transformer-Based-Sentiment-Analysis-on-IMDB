from pathlib import Path
from urllib.request import urlretrieve
import tarfile

URL = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
ROOT = Path(__file__).resolve().parent
ARCHIVE = ROOT / "aclImdb_v1.tar.gz"
DATASET = ROOT / "aclImdb"

if DATASET.exists():
    print(f"Dataset already exists at: {DATASET}")
else:
    if not ARCHIVE.exists():
        print("Downloading the IMDB Large Movie Review Dataset...")
        urlretrieve(URL, ARCHIVE)
        print(f"Downloaded: {ARCHIVE.name}")
    print("Extracting dataset...")
    with tarfile.open(ARCHIVE, "r:gz") as tar:
        tar.extractall(ROOT)
    print(f"Done. Dataset is available at: {DATASET}")
