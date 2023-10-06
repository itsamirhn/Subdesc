import subprocess
from pathlib import Path


class MKVMerge:
    def __init__(self, command: str = "mkvmerge"):
        self.command = command

    def mux(
        self,
        video_path: Path,
        subtitle_path: Path,
        output_path: Path,
        language="eng",
        sub_char="utf-8",
    ):
        """
        Merge a Video and an SRT subtitle file into a new MKV file.
        """
        args = [
            *self._output_file_args(output_path),
            str(video_path),
            *self._language_arg(language),
            *self._sub_char_arg(sub_char),
            str(subtitle_path),
        ]
        return self._run_command(args)

    def _run_command(self, args):
        """
        Run a command asynchronously.
        """
        cmd = [self.command] + args
        subprocess.run(cmd, check=True)

    @staticmethod
    def _output_file_args(output_path: Path):
        return ["-o", str(output_path)]

    @staticmethod
    def _language_arg(language):
        return ["--language", "0:{}".format(language)]

    @staticmethod
    def _sub_char_arg(charset):
        return ["--sub-charset", "0:{}".format(charset)]
