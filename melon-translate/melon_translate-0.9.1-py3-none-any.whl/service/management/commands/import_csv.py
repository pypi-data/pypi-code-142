import csv
from pathlib import Path

from django.conf.locale import LANG_INFO
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand

from translate.core.utils.logging import log
from translate.service.models import Language, Translation, TranslationKey


class Command(BaseCommand):
    """
    Updates translations in database from CSV file. It does not create new Translation objs, nor TranslationKey objs.
    Languages need to be created before usage of the command.
    Following format of CSV file is accepted:  language, key, context, translation, translation_plural
    """

    help = "Updates database with translations from CSV file"

    def add_arguments(self, parser):
        """Attach argument for import_translations command."""

        parser.add_argument(
            "file_name",
            type=str,
            nargs=1,
            default="translations_de.csv",
        )

    @staticmethod
    def get_language_code(file_name):
        """Get language code from file name"""
        i = file_name.rfind(".")
        if 0 < i < len(file_name) - 1:
            name = file_name[:i]
        else:
            name = file_name
        parts = name.split("_")
        language_code = parts[-1]

        return language_code

    @staticmethod
    def import_csv(language: Language, file_name):
        """Import translations from CSV file to database."""

        file_name = Path(file_name)
        log.info(f"Importing translations from {file_name.absolute()}")

        with file_name.open() as csvfile:
            reader_dict = csv.DictReader(csvfile)

            for record in reader_dict:
                try:
                    key = TranslationKey.objects.get(snake_name=record.get("key"))
                except ObjectDoesNotExist:
                    log.info(f"This key {record.get('key')} does not exists in database...")
                    log.info("Have you created keys with import_translations management command?")
                    continue

                translation, _ = Translation.objects.update_or_create(
                    language=language,
                    key=key,
                    translation=record.get("translation"),
                    translation_plural=record.get("translation_plural"),
                )
                log.info(f"Writing record {key.snake_name}")

    def handle(self, *args, **options):
        """Handle command."""
        file_name = options.get("file_name")[0]
        language_code = Command.get_language_code(file_name)

        if language_code not in LANG_INFO:
            raise RuntimeError(f"Language {language_code} not found.")
        try:
            language = Language.objects.get(lang_info=language_code)
            self.import_csv(language, file_name)
        except ObjectDoesNotExist:
            log.error(f"Language {language} not found in database.")

        log.info("Done!")
