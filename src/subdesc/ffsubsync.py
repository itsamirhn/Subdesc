import subprocess
from pathlib import Path


class FFSubSync:
    def __init__(self, command: str = "ffsubsync"):
        self.command = command

    def _run_command(self, args):
        """
        Run a command asynchronously.
        """
        cmd = [self.command] + args
        subprocess.run(cmd, check=True)

    def sync(self, source_path: Path, subtitle_path: Path, output_path: Path):
        """
        Sync a video and a subtitle file into a new subtitle file.
        """
        args = [
            str(source_path),
            *self._subtitle_file_args(subtitle_path),
            *self._output_file_args(output_path),
        ]
        return self._run_command(args)

    @staticmethod
    def _subtitle_file_args(subtitle_path: Path):
        return ["-i", str(subtitle_path)]

    @staticmethod
    def _output_file_args(output_path: Path):
        return ["-o", str(output_path)]
