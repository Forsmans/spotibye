# Spotibye

Download your Spotify playlists as MP3s using a CSV export from Exportify.

https://exportify.net/

---

## Requirements

- Python 3.10+
- [ffmpeg](https://ffmpeg.org/) — install via Homebrew:
  ```bash
  brew install ffmpeg
  ```

---

## Setup

```bash
git clone <your-repo>
cd Spotiq
python3 -m venv .venv
source .venv/bin/activate
pip install yt-dlp pandas mutagen
```

---

## Export your Spotify playlists

1. Go to [exportify.net](https://exportify.net)
2. Log in with Spotify
3. Click **Export All** to download a zip of all your playlists as CSV files
4. Place the CSV file you want to download into the `Spotiq` folder

---

## Usage

```bash
python main.py --csv playlist.csv --out downloads
```

| Flag | Default | Description |
|------|---------|-------------|
| `--csv` | `playlist.csv` | Path to your Exportify CSV file |
| `--out` | `downloads` | Folder where MP3s will be saved | 

---

## Output

- MP3 files are saved to the `--out` folder
- Any failed downloads are listed in `failed.log` after each run
- Songs already in the output folder are skipped automatically
# spotibye
