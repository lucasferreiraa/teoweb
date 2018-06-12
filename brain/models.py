from django.db import models

class Clinica(models.Model):
	cnpj = models.CharField(max_length = 45, primary_key = True)
	nome = models.CharField(max_length = 45)
	endereco = models.CharField(max_length = 45)
	contato = models.CharField(max_length = 45)

	def __str__(self):
    	return self.nome

class Admin(models.Model):
	cpf = models.CharField(max_length = 45,primary_key = True)
	nome = models.CharField(max_length = 45)
	contato = models.CharField(max_length = 45)
	cnpj_clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)

class Paciente(models.Model):
	cpf = models.CharField(max_length = 45, primary_key = True)
	nome = models.CharField(max_length = 45)
	historico = models.CharField(max_length = 45)
<<<<<<< HEAD
=======

	def __str__(self):
    	return self.nome

>>>>>>> 5c0300663a2ac1e6ad29f5c4ec88488634264a57
class Profissional(models.Model):
	cpf = models.CharField(max_length = 45, primary_key = True)
	nome = models.CharField(max_length = 45)
	contato = models.CharField(max_length = 45)
	especialidade = models.CharField(max_length = 45)
	cnpj_clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)

<<<<<<< HEAD
=======
	def __str__(self):
    	return self.nome
>>>>>>> 5c0300663a2ac1e6ad29f5c4ec88488634264a57

class Trabalha_Em(models.Model):
	funcao = models.CharField(max_length = 45)
	cnpj_clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)
	cpf_profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)