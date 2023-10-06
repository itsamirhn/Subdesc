# Subdesc
A simple utility module for Subtitles

### Requirements
Subdesc requires `mkvtoolnix` and `ffmpeg` for working with mkv files. You can install them with the following commands:
```bash
brew install mkvtoolnix
brew install ffmpeg
```

### Installation
Just run `pip install subdesc`

## Usage
You can use Subdesc as a command line tool as follows:
### Muxing Video and Subtitle
When you want to attach subtitle to your mkv file as softsub:
```bash
subdesc mux <video_file> <subtitle_file> <output_file>
```

### Normalizing Subtitle
When your subtitle file has weird encoding and it's not human-readable:
```bash
subdesc normalize <subtitle_file>
```

### Sync Subtitle
When your subtitle file is out of sync with your video file:
```bash
subdesc sync <source_file> <subtitle_file>
```
`source_file` could be a mkv file or another subtitle file

## Caution!
Subdesc is still in development, and it's not stable yet.

It could delete your input files in case of interruption. So please take a backup and use it at your own risk.
