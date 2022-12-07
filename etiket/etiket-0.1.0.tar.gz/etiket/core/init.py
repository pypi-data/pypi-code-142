from sqlmodel import SQLModel, create_engine, Session, select
import os
import psycopg2
from filelock import FileLock, Timeout
import tempfile
import psutil
import time
from sqlalchemy.exc import IntegrityError, NoResultFound

from etiket.flows.secure_files import SecureFilesFlow
from etiket.app.models import User
from etiket.core.security import get_password_hash
from etiket.core.config import settings


def initialize_secure_file_flow():
    pidpath = os.path.join(settings.ETIKET_FLOW_LOCKS_PATH,"secure_file_flow_worker.pid")
    lockexists = False
    if os.path.exists(pidpath):
        with open(pidpath, 'r') as f:
            pid = int(f.readline())
        if psutil.pid_exists(pid):
            lockexists = True #running process has the lock
    lock_path = os.path.join(settings.ETIKET_FLOW_LOCKS_PATH,"secure_files_flow.lock")
    if not lockexists:
        lock = FileLock(lock_path, timeout=0.01)
        try:
            lock.acquire()
            pid = os.getpid()
            with open(pidpath, 'w') as f:
                f.write(str(pid))
            flow = SecureFilesFlow()
            flow.start()
            time.sleep(0.1) #time to hold the lock
        except Timeout:
            pass


def check_storage_dirs():
    if not os.path.exists(settings.ETIKET_FILESTORAGE_PATH):
        raise FileNotFoundError(f"{settings.ETIKET_FILESTORAGE_PATH} does not exist")
    if not os.path.exists(settings.ETIKET_UPLOADS_PATH):
        raise FileNotFoundError(f"{settings.ETIKET_UPLOADS_PATH} does not exist")
    if not os.path.exists(settings.ETIKET_FLOW_LOCKS_PATH):
        raise FileNotFoundError(f"{settings.ETIKET_FLOW_LOCKS_PATH} does not exist")


def ensure_admin_user():
    postgres_url = f"postgresql+psycopg2://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_SERVER}/{settings.POSTGRES_DB}"
    engine = create_engine(postgres_url)
    with Session(engine) as session:
        admin_username = settings.ETIKET_ADMIN_USERNAME
        admin_password = settings.ETIKET_ADMIN_PASSWORD
        admin_email = settings.ETIKET_ADMIN_EMAIL
        user = session.exec(select(User).where(User.username == admin_username)).first()
        if not user:
            try:
                adminuser = User(
                    username=admin_username,
                    hashed_password=get_password_hash(admin_password),
                    active=True,
                    admin=True,
                    firstname="admin",
                    lastname="etiket",
                    email=admin_email,
                )
                session.add(adminuser)
                session.commit()
            except IntegrityError as e:
                session.rollback()
                #user probably already exists?
