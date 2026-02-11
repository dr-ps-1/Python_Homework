from sqlalchemy import create_engine, text


class SubjectTable:

    __scripts = {
        "select": text("SELECT * FROM subject"),
        "select_by_id": text(
            "SELECT * FROM subject WHERE subject_id = :subject_id"),
        "insert": text("""
            INSERT INTO subject(subject_id, subject_title)
            VALUES (:subject_id, :subject_title)
        """),
        "get_max_id": text("SELECT COALESCE(MAX(subject_id), 0) FROM subject"),

        "update": text("""
            UPDATE subject
            SET subject_title = :subject_title
            WHERE subject_id = :subject_id
        """),
        "delete": text("DELETE FROM subject WHERE subject_id = :subject_id"),
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_all(self):
        with self.__db.connect() as conn:
            result = conn.execute(self.__scripts["select"])
            return result.mappings().all()

    def get_by_id(self, subject_id):
        with self.__db.connect() as conn:
            result = conn.execute(
                self.__scripts["select_by_id"],
                {"subject_id": subject_id}
            )
            return result.mappings().all()

    def create(self, title):
        with self.__db.connect() as conn:
            result = conn.execute(self.__scripts["get_max_id"])
            new_id = result.fetchone()[0] + 1

            conn.execute(
                self.__scripts["insert"],
                {
                    "subject_id": new_id,
                    "subject_title": title
                }
            )
            conn.commit()
            return new_id

    def update(self, subject_id, title):
        with self.__db.connect() as conn:
            conn.execute(
                self.__scripts["update"],
                {
                    "subject_id": subject_id,
                    "subject_title": title
                }
            )
            conn.commit()

    def delete(self, subject_id):
        with self.__db.connect() as conn:
            conn.execute(
                self.__scripts["delete"],
                {"subject_id": subject_id}
            )
            conn.commit()

    def get_max_id(self):
        with self.__db.connect() as conn:
            result = conn.execute(self.__scripts["get_max_id"])
            return result.fetchone()[0]
