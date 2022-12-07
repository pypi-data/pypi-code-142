from django.urls import reverse
from admin_sync.utils import remote_reverse, unwrap


def test_get_from_remote_auth(django_app, admin_user, monkeypatch, remote):
    url = reverse("admin:auth_user_get_qs_from_remote")

    res = django_app.get(url, user=admin_user)
    assert res.status_code == 302
    assert (
        res.headers["location"]
        == "/auth/user/remote_login/?from=%2Fauth%2Fuser%2Fget_qs_from_remote%2F"
    )

    monkeypatch.setattr("admin_sync.mixin.is_logged_to_remote", lambda r: True)
    monkeypatch.setattr("admin_sync.mixin.loaddata_from_url", lambda *a: "{}")
    res = django_app.get(url, user=admin_user)
    assert res.status_code == 200
    res = res.forms[1].submit()
    assert res.status_code == 200
    assert [str(m) for m in res.context["messages"]] == ["Success"]


def test_dumpdata_qs(db, django_app, admin_user, remote):
    url = remote_reverse("admin:auth_user_dumpdata_qs")
    res = django_app.get(url, user=admin_user)
    assert res.status_code == 200
    assert unwrap(res.content)
