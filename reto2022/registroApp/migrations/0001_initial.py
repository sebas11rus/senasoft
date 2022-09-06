# Generated by Django 4.1.1 on 2022-09-06 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudadano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_doc', models.CharField(max_length=3)),
                ('n_doc', models.IntegerField()),
                ('nom', models.CharField(max_length=30)),
                ('ape', models.CharField(max_length=50)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'femenino')], max_length=15)),
                ('cel', models.CharField(max_length=20)),
                ('tel', models.IntegerField()),
                ('mun', models.CharField(max_length=30)),
                ('dire', models.CharField(max_length=30)),
                ('barrio', models.CharField(max_length=30)),
                ('fecha_nac', models.DateField()),
                ('etnia', models.CharField(max_length=30)),
                ('disc', models.CharField(max_length=30)),
                ('estrato', models.IntegerField()),
                ('accs_tec', models.CharField(max_length=30)),
                ('cuales', models.CharField(max_length=50)),
                ('con_int', models.BooleanField()),
                ('reg', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Condicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brr', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('grupo_p', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sondeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=25)),
                ('fecha_p', models.DateField()),
                ('hora_p', models.TimeField()),
                ('visible', models.BooleanField(default=True)),
                ('tematica', models.CharField(max_length=25)),
                ('fecha_c', models.DateField()),
                ('hora_c', models.TimeField()),
                ('img', models.ImageField(upload_to='sondeo/')),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('id_ciudadano', models.ManyToManyField(to='registroApp.ciudadano')),
                ('id_condicion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registroApp.condicion')),
                ('id_pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registroApp.pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_gen', models.DateTimeField(auto_now_add=True)),
                ('id_sondeo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registroApp.sondeo')),
            ],
        ),
    ]