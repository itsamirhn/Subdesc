import pathlib

import click

from subdesc.ffsubsync import FFSubSync
from subdesc.mkvmerge import MKVMerge
from subdesc.normalizer import SubtitleNormalizer


class Tools:
    ffsubsync: FFSubSync
    mkvmerge: MKVMerge
    normalizer: SubtitleNormalizer


class PathPath(click.Path):
    """A Click path argument that returns a pathlib Path, not a string"""

    def convert(self, value, param, ctx):
        return pathlib.Path(super().convert(value, param, ctx))


@click.group()
@click.option("--debug/--no-debug", default=False)
@click.option("--mkvmerge-bin", default="mkvmerge")
@click.option("--ffsubsync-bin", default="ffsubsync")
@click.pass_context
def cli(ctx, debug, mkvmerge_bin, ffsubsync_bin):
    ctx.ensure_object(Tools)
    ctx.obj.ffsubsync = FFSubSync(ffsubsync_bin)
    ctx.obj.mkvmerge = MKVMerge(mkvmerge_bin)
    ctx.obj.normalizer = SubtitleNormalizer()
    click.echo(click.style(f"Debug mode is {'on' if debug else 'off'}", fg="yellow"))


@cli.command()
@click.argument("video_path", type=PathPath(exists=True))
@click.argument("subtitle_path", type=PathPath(exists=True))
@click.argument("output_path", type=PathPath())
@click.argument("language", default="eng")
@click.pass_context
def mux(ctx, video_path, subtitle_path, output_path, language):
    ctx.obj.mkvmerge.mux(video_path, subtitle_path, output_path, language)
    click.echo(click.style(f"Muxing finished Successfully: {output_path}", fg="green"))


@cli.command()
@click.argument("source_path", type=PathPath(exists=True))
@click.argument("subtitle_path", type=PathPath(exists=True))
@click.pass_context
def sync(ctx, source_path, subtitle_path):
    ctx.obj.ffsubsync.sync(source_path, subtitle_path, subtitle_path)
    click.echo(click.style(f"Syncing finished Successfully: {subtitle_path}", fg="green"))


@cli.command()
@click.argument("subtitle_path", type=PathPath(exists=True))
@click.pass_context
def normalize(ctx, subtitle_path):
    ctx.obj.normalizer.normalize(subtitle_path, subtitle_path)
    click.echo(click.style(f"Normalizing finished Successfully: {subtitle_path}", fg="green"))


@cli.command()
@click.argument("video_path", type=PathPath(exists=True))
@click.argument("subtitle_path", type=PathPath(exists=True))
@click.argument("language", default="eng")
@click.pass_context
def magic(ctx, video_path, subtitle_path, language):
    normalized_subtitle_path: pathlib.Path = subtitle_path.with_suffix(".normalized")
    output_path: pathlib.Path = video_path.with_suffix(".merged.mkv")
    ctx.obj.normalizer.normalize(subtitle_path, normalized_subtitle_path)
    ctx.obj.ffsubsync.sync(video_path, normalized_subtitle_path, subtitle_path)
    ctx.obj.mkvmerge.mux(video_path, normalized_subtitle_path, output_path, language)
    click.echo(click.style(f"Magic finished Successfully: {output_path}", fg="green"))
    click.echo(click.style("Replacing original video with muxed video", fg="yellow"))
    video_path.unlink()
    normalized_subtitle_path.unlink()
    output_path = output_path.rename(video_path.with_suffix(".mkv"))
    click.echo(
        click.style(
            f"Original video replaced with muxed video: {output_path}",
            fg="green",
        )
    )


if __name__ == "__main__":
    cli(obj=Tools())
