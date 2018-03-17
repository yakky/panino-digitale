from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Panino(models.Model):
    nome = models.CharField(verbose_name=_('nome'), max_length=200)
    descrizione = models.TextField(verbose_name=_('descrizione'))
    prezzo = models.DecimalField(verbose_name=_('prezzo'), max_digits=4, decimal_places=2)
    inserimento = models.DateTimeField(verbose_name=_('giorno inserimento'), auto_now_add=True, null=True)
    disponibilita = models.DateTimeField(verbose_name=_('giorno disponibilità'), null=True)

    class Meta:
        verbose_name = _('panino')
        verbose_name_plural = _('panini')

    def __str__(self):
        return self.nome
