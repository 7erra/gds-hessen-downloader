# GDS Hessen Downloader

This project is a Python tool that automatically downloads all DGM1 (Digital
Terrain Model, 1m resolution) data from the [Geodatenportal Hessen](gds.hessen.de).

## Installation

```bash
git clone https://github.com/7erra/gds-hessen-downloader.git
cd gds-hessen-downloader

python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python3 src/gds_hessen_downloader.py <directory>
```

Options:

- `<directory>`: Path to which the downloaded files should be saved

Example:

```bash
python3 src/gds_hessen_downloader.py ./download
```

## License

MIT
