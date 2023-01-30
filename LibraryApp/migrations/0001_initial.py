# Generated by Django 4.1.4 on 2023-01-18 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_Name', models.CharField(max_length=40)),
                ('Author_Name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_Name', models.CharField(max_length=40)),
                ('S_Password', models.CharField(max_length=40)),
                ('S_Phno', models.BigIntegerField()),
                ('S_Semester', models.IntegerField()),
                ('S_Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryApp.course')),
            ],
        ),
        migrations.CreateModel(
            name='Issue_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Start_Date', models.DateField()),
                ('End_Date', models.DateField()),
                ('Book_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryApp.book')),
                ('Stud_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryApp.student')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='Course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryApp.course'),
        ),
    ]
