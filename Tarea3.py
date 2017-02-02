#!/usr/bin/env python
# -*- coding: utf-8 -*-
class BilleteraElectronica:
	def __init__(self,nombres,apellidos,ci,pin):
		self.nombres = nombres
		self.apellidos = apellidos
		self.ci = ci
		self.pin = pin
		self.saldo = 0
		self.recargas = []
		self.consumos = []
	
	def recargar(self,monto,fecha_r,id_er):
		self.recargas.append(Recarga(monto,fecha_r,id_er))
		self.saldo = self.saldo + monto
		
	def consumir(self,monto,fecha_c,id_ec,pin_billetera):
		if (self.pin == pin_billetera):
			if (self.saldo >= monto):
				self.saldo = self.saldo - monto
				self.consumos.append(Consumo(monto,fecha_c,id_ec))
			else:
				print "No cuenta con suficiente balance para este consumo"
		else:
			print "PIN incorrecto"
		
	def miSaldo(self):
		return self.saldo
		
	def mostrar_recargas(self):
		i = 0
		print "MONTO -   FECHA   - ID"
		while (i < len(self.recargas)):
			print "["+str(self.recargas[i].monto)+" - "+self.recargas[i].fecha_r+" - "+str(self.recargas[i].id_er)+"]"
			i = i + 1

	def mostrar_consumos(self):
		i = 0
		print "MONTO -   FECHA   - ID"
		while (i < len(self.consumos)):
			print "["+str(self.consumos[i].monto)+" - "+self.consumos[i].fecha_c+" - "+str(self.consumos[i].id_ec)+"]"
			i = i + 1
			
class Recarga:
	def __init__(self,monto,fecha_r,id_er):
		self.monto = monto
		self.fecha_r = fecha_r
		self.id_er = id_er

class Consumo:
	def __init__(self,monto,fecha_c,id_ec):
		self.monto = monto
		self.fecha_c = fecha_c
		self.id_ec = id_ec
