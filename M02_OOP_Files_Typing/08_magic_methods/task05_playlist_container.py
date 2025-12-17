from __future__ import annotations

from typing import Iterator, Union, overload


class InvalidTitlePlaylist(Exception):
    """Ошибка. Выбрасывается, если название плейлиста не строка."""

    pass


class InvalidTitleSong(Exception):
    """Ошибка. Выбрасывается, ели название песни не строка."""

    pass


class PlayList:
    def __init__(self, playlist_name: str, song_titles: list[str]) -> None:
        # Валидация названия плейлиста
        if not isinstance(playlist_name, str) or not playlist_name:
            raise InvalidTitlePlaylist(
                f'Название для плейлиста "{playlist_name}". не валидное. '
                f"\nОжидается строковое название плейлиста."
            )

        # Валидация названий песен
        for title in song_titles:
            if not isinstance(title, str):
                raise InvalidTitleSong(
                    f'Название песни "{title}" не валидное. '
                    f"\nОжидается сроковое название песни."
                )

        self._song_titles = song_titles
        self._playlist_name = playlist_name

    def __len__(self) -> int:
        return len(self._song_titles)

    def __iter__(self) -> Iterator[str]:
        return iter(self._song_titles)

    @overload
    def __getitem__(self, index: int) -> str: ...

    @overload
    def __getitem__(self, index: slice) -> PlayList: ...

    def __getitem__(self, index: Union[int, slice]) -> Union[str, PlayList]:
        if isinstance(index, slice):
            return PlayList(self.playlist_name, self._song_titles[index])
        return self.song_titles[index]

    @property
    def playlist_name(self) -> str:
        return self._playlist_name

    @playlist_name.setter
    def playlist_name(self, value: str) -> None:
        if not isinstance(value, str) or not value:
            raise InvalidTitlePlaylist(
                f'Название для плейлиста "{value}". не валидное. '
                f"\nОжидается строковое название плейлиста."
            )
        self._playlist_name = value

    @property
    def song_titles(self) -> tuple[str, ...]:
        return tuple(self._song_titles)

    def add_title(self, title: str) -> None:
        if not isinstance(title, str):
            raise InvalidTitleSong(
                f'Название песни "{title}" невалидное. ' f"\nОжидается троковое название песни."
            )
        self._song_titles.append(title)


def main() -> None:
    songs = [
        "Arctic Monkeys — Do I Wanna Know?",
        "Radiohead — No Surprises",
        "Daft Punk — Instant Crush",
        "Tame Impala — The Less I Know the Better",
        "Linkin Park — Shadow of the Day",
        "Coldplay — Adventure of a Lifetime",
        "Lana Del Rey — West Coast",
        "Red Hot Chili Peppers — Californication",
        "Imagine Dragons — Demons",
    ]

    playlist = PlayList("My playlist", songs)

    print(f"> Playlist size - {len(playlist)} songs")

    print(f"\nПлейлитс: {playlist.playlist_name}")

    for index, title in enumerate(playlist.song_titles, 1):
        print(f"> Song {index}: {title}")

    short_playlist = playlist[3:5]

    print(f"\nПлейлитс: {short_playlist.playlist_name}")

    for index, title in enumerate(short_playlist.song_titles, 1):
        print(f"> Song {index}: {title}")


if __name__ == "__main__":
    main()
