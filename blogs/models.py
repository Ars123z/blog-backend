from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Blog(models.Model):

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published')
    ]
    TOPIC_CHOICES = [
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
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    status= models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    topic = models.CharField(max_length=100, choices=TOPIC_CHOICES)
    content = RichTextUploadingField()
    updated_on = models.DateField(auto_now=True)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Blog by {self.author} on {self.created_on}"

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['created_on']),
        ]

class Comment(models.Model):
    commenter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.commenter} on {self.blog}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        indexes = [
            models.Index(fields=['created_on']),
        ]

class Like(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'blog')

    def __str__(self):
        return f"Like by {self.user} on {self.blog}"



