import time


def test_add_new(db, unique_subject_title):
    before = len(db.get_all())
    new_id = db.create(unique_subject_title)
    after = len(db.get_all())
    subjects = db.get_all()
    db.delete(new_id)

    assert after - before == 1
    assert any(s["subject_title"] == unique_subject_title for s in subjects)


def test_edit(db):
    old_title = f"Старое {int(time.time() * 1000)}"
    new_id = db.create(old_title)
    new_title = f"Новое {int(time.time() * 1000)}"
    db.update(new_id, new_title)
    subject = db.get_by_id(new_id)
    db.delete(new_id)

    assert len(subject) == 1
    assert subject[0]["subject_title"] == new_title


def test_delete(db):
    title = f"Удалить {int(time.time() * 1000)}"
    new_id = db.create(title)
    before = db.get_by_id(new_id)
    db.delete(new_id)
    after = db.get_by_id(new_id)

    assert len(before) == 1
    assert len(after) == 0
