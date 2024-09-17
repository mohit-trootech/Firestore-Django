from django.db import models
from firestore.utils.firestore_config import db, store
from django_extensions.db.models import TitleDescriptionModel, TimeStampedModel
from firestore.utils.constants import ModelsConstants, DESCENDING


class BaseModel(models.Model):
    db = db
    bucket = store
    id = models.AutoField(primary_key=True)

    class Meta:
        abstract = True


class Article(BaseModel, TitleDescriptionModel):

    class Meta:
        db_table = ModelsConstants.TABLE_NAME.value

    def __str__(self):
        return self.title

    def _get_fields(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
        }

    def _id_autoincrement(self):
        def get_fast_id():
            docs = (
                self._get_ref_col().order_by("id", direction=DESCENDING).limit(1).get()
            )
            return int(docs[0].id) if docs else None

        db_pk = get_fast_id()
        return str(db_pk + 1 if db_pk else 1)

    def _get_ref_col(self):
        db_table = self._get_ref_table()
        return self.db.collection(db_table)

    def _get_ref_table(self):
        return self._meta.db_table
