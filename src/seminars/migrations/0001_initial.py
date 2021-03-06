# Generated by Django 2.2 on 2020-04-25 17:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seminar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_time', models.IntegerField(blank=True, null=True)),
                ('end_time', models.IntegerField(blank=True, null=True)),
                ('date_time_info', models.CharField(blank=True, max_length=255)),
                ('seminar_status', models.IntegerField(choices=[(0, 'Ativo'), (1, 'Completo'), (2, 'Cancelado')], default=0)),
                ('inscription_link', models.CharField(blank=True, max_length=100)),
                ('instructors', models.ManyToManyField(blank=True, to='seminars.Instructor')),
            ],
        ),
        migrations.CreateModel(
            name='SeminarLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('street', models.CharField(blank=True, max_length=100)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('complement', models.CharField(blank=True, max_length=100)),
                ('district', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='SeminarType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=50)),
                ('modality', models.IntegerField(choices=[(0, 'ThetaHealing'), (1, 'Access Consciousness')], default=0)),
                ('image_url', models.CharField(blank=True, max_length=100)),
                ('short_description', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('early_inscription_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('inscription_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('price_parts', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('max_number_parts', models.IntegerField(blank=True, null=True)),
                ('currency', models.IntegerField(choices=[(0, 'Real'), (1, 'Dólar')], default=0)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('materials', models.ManyToManyField(blank=True, to='seminars.ClassMaterial')),
            ],
        ),
        migrations.CreateModel(
            name='SeminarTypePrerequisite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_seminartype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_seminartype', to='seminars.SeminarType')),
                ('to_seminartype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_seminartype', to='seminars.SeminarType')),
            ],
        ),
        migrations.AddField(
            model_name='seminartype',
            name='prerequisites',
            field=models.ManyToManyField(blank=True, through='seminars.SeminarTypePrerequisite', to='seminars.SeminarType'),
        ),
        migrations.CreateModel(
            name='SeminarInscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('seminar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seminars.Seminar')),
            ],
        ),
        migrations.AddField(
            model_name='seminar',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='seminars.SeminarLocation'),
        ),
        migrations.AddField(
            model_name='seminar',
            name='seminar_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seminars.SeminarType'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='seminars_teach',
            field=models.ManyToManyField(to='seminars.SeminarType'),
        ),
    ]
