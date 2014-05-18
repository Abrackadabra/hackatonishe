from django.db import models


class Pony(models.Model):
    key = models.TextField()

    def __str__(self):
        return str(self.key)


class Torrent(models.Model):
    pony = models.ForeignKey(Pony)

    link = models.TextField()
    text = models.TextField()

    def as_dict(self):
        return {
            'user': self.pony.key,
            'link': self.link,
            'text': self.text
        }

#
# class Entryashka(models.Model):
#     active_pony = models.ForeignKey(Pony, related_name='entryashki_as_active')
#     passive_pony = models.ForeignKey(Pony, related_name='entryashki_as_passive')
#
#     torrent = models.ForeignKey(Torrent)
#
#
# class Chat(models.Model):
#     entryashka = models.ForeignKey(Entryashka)
#
#     link = models.TextField()
