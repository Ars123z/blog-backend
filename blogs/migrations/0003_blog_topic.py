# Generated by Django 4.2 on 2024-09-01 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='topic',
            field=models.CharField(choices=[('python', 'Python'), ('css', 'CSS'), ('html', 'HTML'), ('scss', 'SCSS'), ('django', 'Django'), ('javascript', 'Javascript'), ('angular', 'Angular'), ('docker', 'Docker'), ('kubernetes', 'Kubernetes'), ('git', 'Git')], default='python', max_length=100),
            preserve_default=False,
        ),
    ]
