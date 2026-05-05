import pandas as pd
import yt_dlp
import os
import argparse
from datetime import datetime

def load_playlist(csv_path):
    df = pd.read_csv(csv_path)
    return df

def log_failed(track_name, artist, reason, log_path):
    with open(log_path, "a") as f:
        f.write(f"{track_name} — {artist} | Reason: {reason}\n")

def get_downloaded_tracks(output_dir):
    downloaded = set()
    for fname in os.listdir(output_dir):
        if fname.endswith(".mp3"):
            downloaded.add(os.path.splitext(fname)[0].lower())
    return downloaded

def is_downloaded(track_name, artist, downloaded_set):
    first_artist = artist.split(";")[0].replace("/", "-").replace(":", "-")
    safe_track = track_name.replace("/", "-").replace(":", "-")
    expected = f"{first_artist} - {safe_track}".lower()
    return expected in downloaded_set

def search_and_download(track_name, artist, output_dir):
    query = f"ytsearch1:{track_name} {artist} official audio"

    safe_artist = artist.split(";")[0].replace("/", "-").replace(":", "-")
    safe_track = track_name.replace("/", "-").replace(":", "-")
    filename = f"{safe_artist} - {safe_track}"

    opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{output_dir}/{filename}.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "match_filter": yt_dlp.utils.match_filter_func("duration < 600"),
        "quiet": True,
        "no_warnings": True,
        "ignoreerrors": False,
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        result = ydl.download([query])
        if result != 0:
            raise Exception(f"yt-dlp returned error code {result}")

def main():
    parser = argparse.ArgumentParser(description="Download songs from a Spotify CSV export")
    parser.add_argument("--csv", default="playlist.csv", help="Path to Exportify CSV file")
    parser.add_argument("--out", default="downloads", help="Output folder for MP3s")
    args = parser.parse_args()

    os.makedirs(args.out, exist_ok=True)

    csv_name = os.path.splitext(os.path.basename(args.csv))[0]
    log_path = f"{csv_name}-failed.log"
    with open(log_path, "w") as f:
        f.write(f"Failed downloads — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 40 + "\n")

    tracks = load_playlist(args.csv)
    downloaded = get_downloaded_tracks(args.out)

    pending = [row for _, row in tracks.iterrows()
               if not is_downloaded(row["Track Name"], row["Artist Name(s)"], downloaded)]

    total = len(pending)
    skipped = len(tracks) - total
    print(f"📋 {len(tracks)} tracks in playlist — {skipped} already done, {total} to download\n")

    failed = 0
    for i, row in enumerate(pending):
        track = row["Track Name"]
        artist = row["Artist Name(s)"]
        label = f"{artist.split(';')[0]} - {track}"
        print(f"[{i+1}/{total}] Downloading: {label[:50]:<50}", end="\r", flush=True)
        try:
            search_and_download(track, artist, args.out)
            print(f"[{i+1}/{total}] ✓ {label[:50]:<50}")
        except Exception as e:
            print(f"[{i+1}/{total}] ✗ {label[:50]:<50}")
            log_failed(track, artist, str(e), log_path)
            failed += 1

    print(f"\nDone — {total - failed}/{total} downloaded.", end="")
    if failed:
        print(f" {failed} failed — see {log_path}", end="")
    print()

if __name__ == "__main__":
    main()