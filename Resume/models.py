from django.db import models
import uuid

class ResumeData(models.Model):
    uid			 = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name         = models.CharField(max_length=255, blank=True)
    file_path    = models.CharField(max_length=255, blank=True)
    experience   = models.TextField(blank=True)
    projects     = models.TextField(blank=True)
    # exp_period   = models.CharField(max_length=50, default=None, blank=True)

    class Meta:
        verbose_name_plural = 'ResumeData'


        
