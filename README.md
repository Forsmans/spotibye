# Spotibye

Download your Spotify playlists as MP3 files using a CSV export from Exportify.

## 🔗 Export playlists

Use Exportify to export your playlists as CSV files:
https://exportify.net/

---

## ⚙️ Requirements

* Python **3.10 or higher**
* ffmpeg

Install ffmpeg (macOS with Homebrew):

```bash
brew install ffmpeg
```

Check Python version:

```bash
python3 --version
```

---

## 🚀 Setup

Clone the repository:

```bash
git clone <your-repo>
cd Spotibye
```

Create a virtual environment with Python 3.10+:

```bash
python3.11 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📥 Export your Spotify playlists

1. Go to https://exportify.net/
2. Log in with Spotify
3. Click **Export All**
4. Download and unzip the CSV files
5. Place your desired CSV file in the project folder

---

## ▶️ Usage

Run the downloader:

```bash
python main.py --csv playlist.csv --out downloads
```

### Options

| Flag  | Default      | Description                 |
| ----- | ------------ | --------------------------- |
| --csv | playlist.csv | Path to Exportify CSV file  |
| --out | downloads    | Output folder for MP3 files |

---

## 📁 Output

* MP3 files are saved in the specified output folder
* Existing files are skipped automatically
* Failed downloads are logged in `failed.log`

---

## ⚠️ Troubleshooting

### Python version warning

If you see:

```
Support for Python 3.9 has been deprecated
```

You are using the wrong Python version. Recreate your virtual environment with Python 3.10+.

---

### Missing modules (e.g. pandas)

If you see:

```
ModuleNotFoundError: No module named 'pandas'
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### Downloads failing (HTTP 403)

This is usually caused by an outdated version of yt-dlp.

Update it:

```bash
pip install -U yt-dlp
```

---

### Process suspended (^Z)

If the script stops and shows `^Z`, it was paused.

Resume:

```bash
fg
```

---

## 📝 Notes

* Requires a working internet connection
* Download success depends on availability of tracks on YouTube
* Metadata is applied using mutagen

---
