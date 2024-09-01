from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from multiselectfield import MultiSelectField
from django.contrib.auth import get_user_model

class Work(models.Model):


    TECHNOLOGY_CHOICES = [
        ('python', 'Python'),
        ('css', 'CSS'),
        ('html', 'HTML'),
        ('scss', 'SCSS'),
        ('django', 'Django'),
        ('javascript', 'Javascript'),
        ('angular', 'Angular'),
        ('docker', 'Docker'),
        ('kubernetes', 'Kubernetes'),
        ('git', 'Git'),
        ('bootstrap', 'Bootstrap'),
        ('tailwind', 'Tailwind'),
    ]

    title = models.CharField(max_length=200)
    client = models.CharField(max_length=100)
    year = models.DateField()
    credits = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    work_description = RichTextUploadingField()
    technologies_used = MultiSelectField(choices=TECHNOLOGY_CHOICES)
    work_details = RichTextUploadingField()
    photos = models.FileField(upload_to='photos/')



    class Meta:
        verbose_name = "Work"
        verbose_name_plural = "Works"

