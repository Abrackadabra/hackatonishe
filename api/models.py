from django.db import models


class Key(models.Model):
    key = models.TextField()


class Pony(models.Model):
    key = models.ForeignKey(Key)


class Torrent(models.Model):
    pony = models.ForeignKey(Pony)

    link = models.TextField()
    text = models.TextField()


class Entryashka(models.Model):
    active_pony = models.ForeignKey(Pony, related_name='entryashki_as_active')
    passive_pony = models.ForeignKey(Pony, related_name='entryashki_as_passive')

    torrent = models.ForeignKey(Torrent)


class Chat(models.Model):
    entryashka = models.ForeignKey(Entryashka)

    link = models.TextField()
