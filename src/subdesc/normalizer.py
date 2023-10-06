from pathlib import Path

import charset_normalizer
import srt


class SubtitleNormalizer:
    REPLACE_CHARS = {
        "ي": "ی",
        "ك": "ک",
    }

    def normalize(self, subtitle_path: Path, output_path: Path):
        result = charset_normalizer.from_path(str(subtitle_path)).best()
        result = self.sanitize(result.output())
        with open(output_path, "wb") as file:
            file.write(result)

    def sanitize(self, subtitle_data: bytes) -> bytes:
        subs = srt.parse(subtitle_data.decode(), ignore_errors=True)
        fixed_subs = []
        for sub in subs:
            for key, value in self.REPLACE_CHARS.items():
                sub.content = sub.content.replace(key, value)
            fixed_subs.append(sub)
        return srt.compose(fixed_subs).encode()
