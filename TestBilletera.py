from Tarea3 import *
import unittest

class TestRecarga(unittest.TestCase):
    def testRecarga(self):
        monto = 2000
        fecha = "02/02/2001"
        id_er = 4321
        recarga = Recarga(monto,fecha,id_er)
        self.assertEqual(monto, recarga.monto)
        self.assertEqual(id_er, recarga.id_er)
        self.assertEqual(fecha, recarga.fecha_r)

class TestConsumo(unittest.TestCase):
    def tesConsumo(self):
        monto = 2000
        fecha = "02/02/2001"
        id_er = 4321
        consumo = Consumo(monto,fecha,id_er)
        self.assertEqual(monto, consumo.monto)
        self.assertEqual(id_er, consumo.id_ec)
        self.assertEqual(fecha, consumo.fecha_c)

class TestBilletera(unittest.TestCase):
    def testInit(self):
        nombre = "Juan Carlos"
        apellido = "Rodrigas Suares"
        ci = 11111111
        pin = 0000
        billetera = BilleteraElectronica(nombre,apellido,ci,pin)
        self.assertEqual(nombre, billetera.nombres)
        self.assertEqual(apellido, billetera.apellidos)
        self.assertEqual(ci, billetera.ci)
        self.assertEqual(pin, billetera.pin)
        
    def testRecargarMonto(self):
        recarga = Recarga(123213,"20/20/2002",123)
        billetera = BilleteraElectronica("a","b",123456789,0000)
        billetera.recargar(recarga.monto,recarga.fecha_r,recarga.id_er)
        self.assertEqual(billetera.recargas.pop().monto,123213)
        self.assertEqual(billetera.miSaldo(), 123213)
        
    def testRecargarFecha(self):
        recarga = Recarga(123213,"20/20/2002",123)
        billetera = BilleteraElectronica("a","b",123456789,0000)
        billetera.recargar(recarga.monto,recarga.fecha_r,recarga.id_er)
        self.assertEqual(billetera.recargas.pop().fecha_r,"20/20/2002")
        
    def testRecargarID(self):
        recarga = Recarga(123213,"20/20/2002",123)
        billetera = BilleteraElectronica("a","b",123456789,0000)
        billetera.recargar(recarga.monto,recarga.fecha_r,recarga.id_er)
        self.assertEqual(billetera.recargas.pop().id_er,123)
        
    def testRecargaNegativa(self):
        billetera = BilleteraElectronica("a","b",123456789,0000)
        billetera.recargar(-123213,"20/20/2002",123)
        self.assertGreaterEqual(billetera.recargas.pop().monto,0)
        self.assertEqual(billetera.miSaldo(), 123213)
        
    def testRecargaCero(self):
        billetera = BilleteraElectronica("a","b",123456789,0000)
        billetera.recargar(0,"20/20/2002",123)
        self.assertEqual(billetera.recargas.pop().monto,0)
        self.assertEqual(billetera.miSaldo(), 0)
        
    def testConsumoID(self):
        billetera = BilleteraElectronica("a","b",123456789,0000)
        billetera.recargar(1100,"20/20/2002",123)
        billetera.consumir(100,"20/20/2012",1,0000)
        self.assertEqual(billetera.consumos.pop().id_ec,1)
        
    def testConsumoNormal(self):
        billetera = BilleteraElectronica("a","b",123456789,0000)
        billetera.recargar(1100,"20/20/2002",123)
        billetera.consumir(100,"20/20/2012",1,0000)
        self.assertEqual(billetera.miSaldo(),1000)    
    
    def ConsumoIgualRecarga(self):
        billetera = BilleteraElectronica("a","b",123456789,0000)
        billetera.recargar(110,"20/20/2002",123)
        billetera.consumir(110,"20/20/2012",1,0000)
        self.assertEqual(billetera.miSaldo(),0)
        
    def ConsumoPinInvalido(self):
        billetera = BilleteraElectronica("a","b",123456789,0000)
        billetera.recargar(110,"20/20/2002",123)
        billetera.consumir(110,"20/20/2012",1,4)
        self.assertEqual(billetera.miSaldo(),110)
        
    def ConsumoNegativo(self):
        billetera = BilleteraElectronica("a","b",123456789,0000)
        billetera.recargar(110,"20/20/2002",123)
        billetera.consumir(-110,"20/20/2012",1,0000)
        self.assertEqual(billetera.miSaldo(),0)
        
    def testConsumoMayorARecarga(self):
        billetera = BilleteraElectronica("a","b",123456789,0000)
        billetera.recargar(11,"20/20/2002",123)
        billetera.consumir(100,"20/20/2012",1,0000)
        self.assertEqual(billetera.miSaldo(),11)
        
    def RecargaDecimal(self):
        billetera = BilleteraElectronica("a","b",123456789,0000)
        billetera.recargar(0.00000000000001,"20/20/2002",123)
        self.assertEqual(billetera.miSaldo(), 0.00000000000001)
        
    def testConsumoDecimal(self):
        billetera = BilleteraElectronica("a","b",123456789,0000)
        billetera.recargar(10.11,"20/20/2002",123)
        billetera.consumir(1.1,"20/20/2012",1,0000)
        self.assertEqual(billetera.miSaldo(),9.01)
        
    def testConsumoCero(self):
        billetera = BilleteraElectronica("a","b",123456789,0000)
        billetera.recargar(10.11,"20/20/2002",123)
        billetera.consumir(0,"20/20/2012",1,0000)
        self.assertEqual(billetera.miSaldo(),10.11)