# Generated by Django 3.2.13 on 2022-12-14 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbti', '0002_alter_mbti_mbti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mbti',
            name='board',
            field=models.CharField(choices=[('특징', '특징'), ('상대법', '상대법'), ('주의할 점', '주의할 점')], max_length=50),
        ),
        migrations.AlterField(
            model_name='mbti',
            name='mbti',
            field=models.CharField(choices=[('ISTP', 'ISTP'), ('INTP', 'INTP'), ('ESTJ', 'ESTJ'), ('ENTP', 'ENTP'), ('ISFP', 'ISFP'), ('ISFJ', 'ISFJ'), ('INFP', 'INFP'), ('ISTJ', 'ISTJ'), ('ENFP', 'ENFP'), ('ENTJ', 'ENTJ'), ('ESTP', 'ESTP'), ('ESFP', 'ESFP'), ('ESFJ', 'ESFJ'), ('ENFJ', 'ENFJ'), ('INFJ', 'INFJ'), ('INTJ', 'INTJ')], max_length=50),
        ),
    ]