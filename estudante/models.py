from django.db import models
from django.db.models.functions import Now
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils import timezone
import random
from pessoa.models import Pessoa, Documento, Endereco
from django.contrib.auth.models import User

def generar_matricula():
    matricula = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    while Matricula.objects.filter(numero_matricula=matricula).exists():
        matricula = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    return matricula

class Turma(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    data_inclusao = models.DateTimeField(default=timezone.now, null=True, blank=True)
    data_inicio = models.DateField(blank=True, null= True)
    data_fim = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    codigo = models.CharField(blank=True, null=True)
    carga_horaria_aula = models.DurationField(blank=True, null =True)
    data_inclusao = models.DateTimeField(default=timezone.now, null=True, blank=True)
    def __str__(self):
        return self.nome

class Empresa(models.Model):
    nome_fantasia = models.CharField(max_length=255)
    razao_social = models.CharField(max_length=255)
    pessoa_responsavel = models.ForeignKey(Pessoa, on_delete= models.CASCADE, null=True)
    documento = models.ManyToManyField(Documento,  related_name='empresas', blank=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nome_fantasia

class Cbo(models.Model):
    descricao = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255)
    def __str__(self):
        return self.descricao
    
class CBOAssociado(models.Model):
    cbo = models.ForeignKey(Cbo, related_name='associados', on_delete=models.CASCADE)
    associado = models.ForeignKey(Cbo, related_name='associado_de', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('cbo', 'associado')
        verbose_name = 'Associação de CBO'
        verbose_name_plural = 'Associações de CBOs'

    def __str__(self):
        return f"{self.cbo} associado a {self.associado}"

class Escolaridade(models.Model):
    descricao = models.CharField(max_length=255)
    def __str__(self):
        return self.descricao

class DiaSemana(models.Model):
    DIA_CHOICES = [
        ('Segunda-feira', 'Segunda-feira'),
        ('Terça-feira', 'Terça-feira'),
        ('Quarta-feira', 'Quarta-feira'),
        ('Quinta-feira', 'Quinta-feira'),
        ('Sexta-feira', 'Sexta-feira'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ]
    dia = models.CharField(max_length=20, choices=DIA_CHOICES, unique=True)

    def __str__(self):
        return self.get_dia_display()

class Psa(models.Model):
    data_inicio = models.DateField()
    data_fim = models.DateField()
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.data} - {self.descricao}"

class Matricula(models.Model):
    numero_matricula = models.CharField(max_length=6, unique=True, default=generar_matricula)
    data_inclusao = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=True)
    data_inativacao = models.DateTimeField(null=True, blank=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True)
    escolaridade = models.ForeignKey(Escolaridade, on_delete=models.DO_NOTHING, null=True, blank=True)
    salario = models.CharField(null=True, blank=True)
    data_inicio_contrato = models.DateField(null=True, blank=True)
    data_terminio_contrato = models.DateField(null=True, blank=True)
    quantidade_meses_contrato = models.IntegerField(null=True, blank=True)
    data_inicio_empresa = models.DateField(null=True, blank=True)
    data_terminio_empresa = models.DateField(null=True, blank=True)
    hora_inicio_expediente = models.CharField(max_length=10, null=True, blank=True)
    hora_fim_expediente = models.CharField(max_length=10, null=True, blank=True)
    dias_da_semana_empresa = models.ManyToManyField(DiaSemana, related_name='matriculas_empresa', null=True, blank=True)
    dias_da_semana_curso = models.ManyToManyField(DiaSemana, related_name='matriculas_curso', null=True, blank=True)
    turma = models.ForeignKey(Turma, on_delete= models.DO_NOTHING, null=True)
    curso = models.ForeignKey(Curso, on_delete= models.DO_NOTHING, null=True)
    empresa = models.ForeignKey(Empresa, on_delete= models.DO_NOTHING, null=True)
    cbo = models.ForeignKey(Cbo, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        nome = self.pessoa.nome if self.pessoa and self.pessoa.nome else 'Nome não disponível'
        numero_matricula = self.numero_matricula if self.numero_matricula else 'Matrícula não disponível'
        return nome + ' | ' + numero_matricula

    
class Desligamento_matricula(models.Model):
    matricula = models.ForeignKey(Matricula, on_delete=models.DO_NOTHING)
    motivo = models.CharField(null=True, blank=True)
    data_desligamento = models.DateField(null=True, blank=True)
    usuario_inclui = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.matricula.pessoa.nome

class Atividade_teorica(models.Model):
    matricula = models.ForeignKey(Matricula, on_delete=models.DO_NOTHING)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    dias_da_semana = models.ManyToManyField(DiaSemana)
    hora_inicio = models.CharField(max_length=10, null=True, blank=True)
    hora_termino = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.matricula.pessoa.nome

class Modulo(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    curso = models.ForeignKey(Curso, on_delete= models.DO_NOTHING,null=True)
    def __str__(self):
        return self.nome

class Aula(models.Model):
    tema = models.CharField(max_length=250)
    conteudo = models.CharField(null=True, blank=True)
    ocorrencias = models.TextField(null=True, blank=True)
    data_aula = models.DateField(null=True, blank=True)
    turma = models.ForeignKey(Turma, on_delete= models.DO_NOTHING, null=True)
    educador = models.ForeignKey(Pessoa, on_delete= models.DO_NOTHING, null=True, blank=True)
    modulo = models.ForeignKey(Modulo, on_delete= models.DO_NOTHING, null=True, blank=True)
    def __str__(self):
        return self.tema + ' | ' + self.turma.nome

class Tipo_presenca(models.Model):
    codigo = models.CharField(null=True, blank=True)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Profissional interno'
        verbose_name_plural = 'Tipos de profissionais internos'
        
    def __str__(self):
        return self.descricao
    
class Presenca(models.Model):
    matricula = models.ForeignKey(Matricula, on_delete= models.DO_NOTHING, null=True)
    tipo_presenca = models.ForeignKey(Tipo_presenca, on_delete= models.DO_NOTHING, null=True, blank=True)
    aula_id = models.ForeignKey(Aula, on_delete= models.DO_NOTHING)
    data_presenca = models.DateField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Registro de presença'
        verbose_name_plural = 'Presenças'
        
    def __str__(self):
        return self.matricula.pessoa.nome + ' | ' + self.tipo_presenca.codigo
    
@receiver(pre_save, sender=Matricula)
def update_data_inativacao(sender, instance, **kwargs):
    if instance.pk:
        original_instance = sender.objects.get(pk=instance.pk)
        if original_instance.ativo != instance.ativo:
            if instance.ativo:
                instance.data_inativacao = timezone.now()
            else:
                instance.data_inativacao = None
    elif instance.ativo:
        instance.data_inativacao = timezone.now()
