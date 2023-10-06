# Subdesc
A simple utility module for Subtitles.

### Installation 🛠️
Subdesc requires `mkvtoolnix` and `ffmpeg` for working with mkv files. You can install them with the following commands:
```bash
brew install mkvtoolnix
brew install ffmpeg
```
Then, Just run `pip install subdesc`

## Usage 🍿
You can use Subdesc as a command line tool as follows. `subd` can be replaced with `subdesc` as well.

### Muxing Video and Subtitle
When you want to attach subtitle to your mkv file as softsub:
```bash
subd mux <video_file> <subtitle_file> <output_file>
```

### Normalizing Subtitle
When your subtitle file has weird encoding and it's not human-readable:
```bash
subd normalize <subtitle_file>
```

### Sync Subtitle
When your subtitle file is out of sync with your video file:
```bash
subd sync <source_file> <subtitle_file>
```
`source_file` could be a mkv file or another subtitle file


### Magic 🪄
When you have OCD like me and you want to apply all of the above commands at once:
```bash
subd magic <video_file> <subtitle_file>
```
This will overwrite video file with the new one.

## Caution ⚠️
Subdesc is still in development, and it's not stable yet.

It could delete your input files in case of interruption. So please take a backup and use it at your own risk.


## Contributing 🤝
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License 📄
[MIT](https://choosealicense.com/licenses/mit/)