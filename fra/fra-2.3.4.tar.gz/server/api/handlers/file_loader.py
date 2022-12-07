import os
from uuid import UUID

import flask_rebar
from flask import request
from flask_rebar import errors
from werkzeug.utils import secure_filename

from motor.models import FileMapModel
from motor.models import RawFileModel
from server.config import basedir
from server.database import db
from server.rebar import registry
from server.schemas.file_data import FileMapResponseSchema
from server.schemas.file_data import FileMapSchema


ALLOWED_EXTENSIONS = {"txt", "csv"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@registry.handles(
    rule="/organization/<uuid:organization_id>/dataset/add",
    method="POST",
    mimetype="multipart/form-data",
)
def file_upload(organization_id: UUID):
    """
    Upload files for train the model.
    """
    file = request.files["file"]
    file_name = file.filename
    if file_name == "":
        return {"msg": "empty filename"}, 400

    file_type = request.form.get("file_type")

    if file and file_name and allowed_file(file_name):
        filename = secure_filename(file_name)  # noqa
        file.save(os.path.join(basedir + f"/uploads/{organization_id}", filename))
        upload = RawFileModel(
            filename=filename, organization_id=organization_id, file_type=file_type
        )
        db.session.add(upload)
        db.session.commit()
        return {"file_id": upload.id}, 201


@registry.handles(
    rule="/organization/<uuid:organization_id>/dataset/map",
    method="POST",
    request_body_schema=FileMapSchema(),
    response_body_schema={201: FileMapResponseSchema()},
)
def file_mapping(organization_id: UUID):
    """
    Set meta data for an specific file, so it could be converted on data the model can use for get recommendations
    """
    body = flask_rebar.get_validated_body()
    # validate dataset for organization
    file = RawFileModel.query.filter_by(
        organization_id=organization_id, id=body["file_id"]
    ).first()
    if file is None:
        raise errors.BadRequest(msg="Dataset not found in organization")
    file_map = FileMapModel(**body)
    db.session.add(file_map)
    db.session.commit()
    return file_map, 201
