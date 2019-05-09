# Generated by Django 2.2 on 2019-05-06 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ttests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1500)),
                ('mediafile', models.ImageField(blank=True, null=True, upload_to='for_questions')),
                ('point', models.PositiveSmallIntegerField(default=1, verbose_name='балл за верный ответ')),
                ('explanation', models.TextField(blank=True, max_length=1000)),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TestTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Тег теста',
                'verbose_name_plural': 'Теги теста',
                'ordering': ('title',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('description', models.TextField(blank=True, max_length=3500, null=True)),
                ('img_description', models.ImageField(blank=True, null=True, upload_to='for_tests')),
                ('is_published', models.BooleanField(default=False, help_text='если тест опубликован, он доступен другим пользователям\t\t\t\tдля прохождения; после публикации тест нельзя изменять (только удалять)', verbose_name='опубликован')),
                ('create_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('update_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('testing_time', models.DurationField(blank=True, null=True)),
                ('show_q_number', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('is_shuffle_q', models.BooleanField(default=False)),
                ('only_fully_correct', models.BooleanField(default=False)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tests', to='ttests.User')),
                ('tags', models.ManyToManyField(related_name='tests', to='ttests.TestTag')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='QuestionTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('recommendation', models.TextField(max_length=2000)),
                ('questions', models.ManyToManyField(related_name='tags', to='ttests.Question')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions_tags', to='ttests.Test')),
            ],
            options={
                'verbose_name': 'Тег вопроса',
                'verbose_name_plural': 'Теги вопроса',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='ttests.Test'),
        ),
        migrations.CreateModel(
            name='AssociateAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('right_side', models.CharField(blank=True, max_length=300, null=True)),
                ('left_side', models.CharField(max_length=300)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ttests.Question')),
            ],
            options={
                'verbose_name': 'Ответ с сопоставлением частей',
                'verbose_name_plural': 'Ответы с сопоставлением частей',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('is_right', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ttests.Question')),
            ],
            options={
                'verbose_name': 'Одиноч. / множеств. / самост. ответ',
                'verbose_name_plural': 'Одиноx. / множеств. / самостоят. ответы',
                'managed': True,
            },
        ),
    ]
