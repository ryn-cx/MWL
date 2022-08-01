from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.db.models.query import QuerySet
    from typing_extensions import Self

from django.db import models

from common.model_helper import GetOrNew
from common.model_templates import ModelWithIdAndTimestamp

from .functions import lazy_db_table, lazy_fk, lazy_unique

# Media
if True:

    class Media(ModelWithIdAndTimestamp, GetOrNew):  # type: ignore - Composing abstract models always throws type errors
        class Meta:  # type: ignore - Meta class always throws type errors
            abstract = True

        id = models.PositiveSmallIntegerField(primary_key=True)
        title = models.CharField(max_length=255)
        main_picture_medium = models.CharField(max_length=255)
        main_picture_large = models.CharField(max_length=255)
        start_date = models.DateField(null=True)
        end_date = models.DateField(null=True)
        synopsis = models.TextField()
        mean = models.FloatField(null=True)
        rank = models.PositiveSmallIntegerField(null=True)
        popularity = models.PositiveSmallIntegerField()
        num_list_users = models.PositiveSmallIntegerField()
        num_scoring_users = models.PositiveSmallIntegerField()
        nsfw = models.CharField(max_length=255)
        created_at = models.DateTimeField()
        updated_at = models.DateTimeField()
        media_type = models.CharField(max_length=255)
        status = models.CharField(max_length=255)
        background = models.TextField()
        sparse = models.BooleanField()

        def __str__(self) -> str:
            return self.title

    class Anime(Media):
        objects: QuerySet[Self]

        class Meta:  # type: ignore - Meta always throws type errors
            db_table = lazy_db_table()

        num_episodes = models.PositiveSmallIntegerField()
        start_season_year = models.PositiveSmallIntegerField(null=True)
        start_season_season = models.CharField(max_length=255)
        broadcast_day_of_the_week = models.CharField(max_length=255)
        broadcast_start_time = models.TimeField(null=True)
        source = models.CharField(max_length=255)
        average_episode_duration = models.PositiveSmallIntegerField()
        rating = models.CharField(max_length=255)

    class Manga(Media):
        objects: QuerySet[Self]

        class Meta:  # type: ignore - Meta always throws type errors
            db_table = lazy_db_table()

        alternative_titles_en_title = models.CharField(max_length=255)
        alternative_titles_ja_title = models.CharField(max_length=255)
        num_volumes = models.PositiveSmallIntegerField()
        num_chapters = models.PositiveSmallIntegerField()


# Alternative Title
if True:

    class AnimeAlternativeTitles(models.Model):
        objects: QuerySet[Self]

        class Meta:  # type: ignore - Meta always throws type errors
            db_table = lazy_db_table()

        anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
        title = models.CharField(max_length=255)

    class MangaAlternativeTitles(models.Model):
        objects: QuerySet[Self]

        class Meta:  # type: ignore - Meta always throws type errors
            db_table = lazy_db_table()

        anime = models.ForeignKey(Manga, on_delete=models.CASCADE)
        title = models.CharField(max_length=255)


# Related entries
if True:

    class RelatedMedia(models.Model):
        class Meta:  # type: ignore - Meta class always throws type errors
            abstract = True

        id = models.AutoField(primary_key=True)
        relationship = models.CharField(max_length=255)

        # Abstract attributes to avoid function type errors errors
        media: models.ForeignKey[Anime | Manga]
        related_media: models.ForeignKey[Anime | Manga]

        def __str__(self) -> str:
            return f"{self.media} {self.related_media} {self.relationship}"

    class AnimeRelatedAnime(RelatedMedia):
        objects: QuerySet[Self]

        class Meta:  # type: ignore - Meta class always throws type errors
            db_table = lazy_db_table()
            constraints = lazy_unique("media", "related_media", "relationship")

        media = lazy_fk(Anime)
        related_media = lazy_fk(Anime)

    class AnimeRelatedManga(RelatedMedia):
        objects: QuerySet[Self]

        class Meta:  # type: ignore - Meta class always throws type errors
            db_table = lazy_db_table()
            constraints = lazy_unique("media", "related_media", "relationship")

        id = models.AutoField(primary_key=True)
        media = lazy_fk(Anime)
        related_media = lazy_fk(Manga)
        relationship = models.CharField(max_length=255)

    class MangaRelatedAnime(RelatedMedia):
        objects: QuerySet[Self]

        class Meta:  # type: ignore - Meta class always throws type errors
            db_table = lazy_db_table()
            constraints = lazy_unique("media", "related_media", "relationship")

        media = lazy_fk(Manga)
        related_media = lazy_fk(Anime)

    class MangaRelatedManga(RelatedMedia):
        objects: QuerySet[Self]

        class Meta:  # type: ignore - Meta class always throws type errors
            db_table = lazy_db_table()
            constraints = lazy_unique("media", "related_media", "relationship")

        media = lazy_fk(Manga)
        related_media = lazy_fk(Manga)


# Recs
if True:

    class AnimeRecs(models.Model):
        objects: QuerySet[Self]

        class Meta:  # type: ignore - Meta class always throws type errors
            db_table = lazy_db_table()
            constraints = lazy_unique("media", "recommended_media")

        id = models.AutoField(primary_key=True)
        media = lazy_fk(Anime)
        recommended_media = lazy_fk(Anime)
        recommendations = models.PositiveSmallIntegerField()

    class MangaRecs(models.Model):
        objects: QuerySet[Self]

        class Meta:  # type: ignore - Meta class always throws type errors
            db_table = lazy_db_table()
            constraints = lazy_unique("media", "recommended_media")

        id = models.AutoField(primary_key=True)
        media = lazy_fk(Manga)
        recommended_media = lazy_fk(Manga)
        recommendations = models.PositiveSmallIntegerField()


# Genres
if True:
    # This is sharedb etween anime and manga
    class Genres(models.Model):
        objects: QuerySet[Self]

        class Meta:  # type: ignore - Meta always throws type errors
            db_table = lazy_db_table()

        id = models.PositiveSmallIntegerField(primary_key=True)
        name = models.CharField(max_length=255)

    class AnimeGenres(models.Model):
        objects: QuerySet[Self]

        class Meta:  # type: ignore - Meta always throws type errors
            db_table = lazy_db_table()

        media = models.ForeignKey(Anime, on_delete=models.CASCADE)
        genre = models.ForeignKey(Genres, on_delete=models.CASCADE)

    class MangaGenres(models.Model):
        objects: QuerySet[Self]

        class Meta:  # type: ignore - Meta always throws type errors
            db_table = lazy_db_table()

        media = models.ForeignKey(Manga, on_delete=models.CASCADE)
        genre = models.ForeignKey(Genres, on_delete=models.CASCADE)


# User
if True:

    class User(ModelWithIdAndTimestamp, GetOrNew):  # type: ignore - Composing abstract models always throws type errors
        objects: QuerySet[Self]

        class Meta:  # type: ignore - Meta always throws type errors
            db_table = lazy_db_table()

        id = models.AutoField(primary_key=True)
        alternative_titles_en = models.CharField(max_length=255)
        alternative_titles_ja = models.CharField(max_length=255)
        name = models.CharField(max_length=255, unique=True)
        anime_count = models.PositiveSmallIntegerField(null=True)
        manga_count = models.PositiveSmallIntegerField(null=True)
        average_anime_score = models.FloatField(null=True)
        average_manga_score = models.FloatField(null=True)
        anime_list_private = models.BooleanField()
        manga_list_private = models.BooleanField()
        last_successful_anime_list_import = models.DateTimeField(null=True)
        last_successful_manga_list_import = models.DateTimeField(null=True)

        def user_anime(self) -> QuerySet[UserAnime]:
            return UserAnime.objects.filter(user=self, media__sparse=False)

        def user_manga(self) -> QuerySet[UserManga]:
            return UserManga.objects.filter(user=self, media__sparse=False)

    class UserMedia(GetOrNew):
        class Meta:  # type: ignore - Meta class always throws type errors
            abstract = True

        objects: QuerySet[Self]
        id = models.AutoField(primary_key=True)
        status = models.PositiveSmallIntegerField()
        score = models.PositiveSmallIntegerField()
        updated_at = models.DateTimeField()
        finish_date = models.DateField(null=True)

    class UserAnime(UserMedia):
        objects: QuerySet[Self]

        class Meta:  # type: ignore - Meta class always throws type errors
            db_table = lazy_db_table()
            constraints = lazy_unique("user", "media")

        user = lazy_fk(User)
        media = lazy_fk(Anime)
        num_episodes_watched = models.PositiveSmallIntegerField(null=True)
        is_rewatching = models.BooleanField()

    class UserManga(UserMedia):
        objects: QuerySet[Self]

        class Meta:  # type: ignore - Meta class always throws type errors
            db_table = lazy_db_table()
            constraints = lazy_unique("user", "media")

        user = lazy_fk(User)
        media = lazy_fk(Manga)
        is_rereading = models.BooleanField()
        num_volumes_read = models.PositiveSmallIntegerField()
        num_chapters_read = models.PositiveSmallIntegerField()


class ImportQue(models.Model):
    objects: QuerySet[Self]

    class Meta:  # type: ignore - Meta class always throws type errors
        db_table = lazy_db_table()
        constraints = lazy_unique("type", "key")

    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255, null=False)
    key = models.CharField(max_length=255, null=False)
    priority = models.PositiveSmallIntegerField()
    minimum_info_timestamp = models.DateTimeField(null=True)
    minimum_modified_timestamp = models.DateTimeField(null=True)
