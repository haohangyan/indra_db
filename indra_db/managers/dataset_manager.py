import os
import shutil
import logging
import urllib.request as urllib_request

from zipfile import ZipFile
from indra.sources.bel.api import process_jgif_file
from indra_db.util import insert_db_stmts

logger = logging.getLogger(__name__)


class DatasetManager(object):
    """This is a class to lay out the methods for updating a dataset."""
    name = NotImplemented

    def upload(self, db):
        """Upload the content for this dataset into the database."""
        dbid = self.check_reference(db)
        stmts = self._get_statements(db)
        insert_db_stmts(db, set(stmts), dbid)
        return

    def check_reference(self, db):
        """Ensure that this database has an entry in the database."""
        dbid = db.select_one(db.DBInfo.id, db.DBInfo.db_name == self.name)
        if dbid is None:
            dbid = db.insert(db.DBInfo, db_name=self.name)
        return dbid

    def _get_statements(self, db):
        raise NotImplementedError("Statement retrieval must be defined in "
                                  "each child.")


class TasManager(DatasetManager):
    """This manager handles retrieval and processing of the TAS dataset."""
    name = 'tas'

    def _get_statements(self, db):
        from indra.sources.tas import process_csv
        proc = process_csv()
        return proc.statements


class SignorManager(DatasetManager):
    name = 'signor'

    def _get_statements(self, db):
        from indra.sources.signor import process_from_web
        proc = process_from_web()
        return proc.statements


class CBNManager(object):
    """This manager handles retrieval and processing of CBN network files"""
    name = 'cbn'

    def __init__(self, tmp_archive=None, temp_extract=None, archive_url=None):
        self.tmp_archive = './temp_cbn_human.zip' if not tmp_archive else \
            tmp_archive
        self.temp_extract = './temp/' if not temp_extract else temp_extract
        self.archive_url = \
            'http://www.causalbionet.com/Content/jgf_bulk_files/Human-2.0.zip' \
            '' if not archive_url else archive_url

    def _get_statements(self):
        logger.info('Retrieving CBN network zip archive')
        response = urllib_request.urlretrieve(url=self.archive_url,
                                              filename=self.tmp_archive)
        stmts = []
        with ZipFile(self.tmp_archive) as zipf:
            logger.info(f'Extracting archive to {self.temp_extract}')
            zipf.extractall(path=self.temp_extract)
            logger.info('Processing jgif files')
            for jgif in zipf.namelist():
                if jgif.endswith('.jgf') or jgif.endswith('.jgif'):
                    logger.info(f'Processing {jgif}')
                    pbp = process_jgif_file(self.temp_extract + jgif)
                    stmts = stmts + pbp.statements

        # Cleanup
        shutil.rmtree(self.temp_extract)
        os.remove(self.tmp_archive)

        return stmts
