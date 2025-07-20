import psycopg2
from psycopg2 import sql
from psycopg2.extras import DictCursor


class FilmBaza:
    def __init__(self):
        self.ulanish = psycopg2.connect(
            dbname="film_db",
            user="postgres",
            password="1",
            host="localhost",
            port="5432"
        )
        self.kursor = self.ulanish.cursor(cursor_factory=DictCursor)
        self.jadvallarni_yarat()
        self.namuna_malumot_qosh()

    def jadvallarni_yarat(self):
        try:
            self.kursor.execute("""
                CREATE TABLE IF NOT EXISTS kategoriyalar(
                    id SERIAL PRIMARY KEY,
                    nomi VARCHAR(50) UNIQUE NOT NULL
                )""")

            self.kursor.execute("""
                CREATE TABLE IF NOT EXISTS filmlar(
                    id SERIAL PRIMARY KEY,
                    nomi VARCHAR(100) NOT NULL,
                    tavsif TEXT,
                    yil INTEGER,
                    kategoriya_id INTEGER REFERENCES kategoriyalar(id),
                    video_id TEXT
                )""")
            self.ulanish.commit()
        except Exception as e:
            print(f"Jadval yaratishda xato: {e}")

    def namuna_malumot_qosh(self):
        # Kategoriyalarni tekshirish
        self.kursor.execute("SELECT COUNT(*) FROM kategoriyalar")
        if self.kursor.fetchone()[0] == 0:
            kategoriyalar = ['Jangari', 'Komediya', 'Drama', 'Fantastik']
            for kat in kategoriyalar:
                self.kursor.execute(
                    "INSERT INTO kategoriyalar (nomi) VALUES (%s) ON CONFLICT DO NOTHING",
                    (kat,)
                )

            filmlar = [
                ('Matrix', 'Virtual haqiqat filmi', 1999, 1, None),
                ('Inception', 'Orzular dunyosi', 2010, 1, None),
                ('Forrest Gump', 'Hayot filmi', 1994, 3, None)
            ]
            for film in filmlar:
                self.kursor.execute(
                    "INSERT INTO filmlar (nomi, tavsif, yil, kategoriya_id, video_id) "
                    "VALUES (%s, %s, %s, %s, %s)",
                    film
                )
            self.ulanish.commit()

    def kategoriyalarni_ol(self):
        self.kursor.execute("SELECT id, nomi FROM kategoriyalar ORDER BY nomi")
        return self.kursor.fetchall()

    def filmlarni_ol(self, kategoriya_id):
        self.kursor.execute(
            "SELECT id, nomi, tavsif, yil, video_id FROM filmlar "
            "WHERE kategoriya_id = %s ORDER BY nomi",
            (kategoriya_id,)
        )
        return self.kursor.fetchall()

    def film_malumot(self, film_id):
        self.kursor.execute(
            "SELECT nomi, tavsif, yil, video_id FROM filmlar WHERE id = %s",
            (film_id,)
        )
        return self.kursor.fetchone()

    def __del__(self):
        self.kursor.close()
        self.ulanish.close()