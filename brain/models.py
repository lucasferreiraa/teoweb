from django.db import models

class Clinica(models.Model):
	cnpj = models.CharField(max_length = 45, primary_key = True)
	nome = models.CharField(max_length = 45)
	endereco = models.CharField(max_length = 45)
	contato = models.CharField(max_length = 45)

class Admin(models.Model):
	cpf = models.CharField(max_length = 45,primary_key = True)
	nome = models.CharField(max_length = 45)
	contato = models.CharField(max_length = 45)
	cnpj_clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)

class Paciente(models.Model):
	cpf = models.CharField(max_length = 45, primary_key = True)
	nome = models.CharField(max_length = 45)
	historico = models.CharField(max_length = 45)

class Profissional(models.Model):
	cpf = models.CharField(max_length = 45, primary_key = True)
	nome = models.CharField(max_length = 45)
	contato = models.CharField(max_length = 45)
	cnpj_clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)

class Trabalha_Em(models.Model):
	cnpj_clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)
	cpf_profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
