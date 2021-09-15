import matplotlib.pyplot as plt
import csv


class salary_range():
    def __init__(self,a,b):
        self.a=a
        self.b=b

class isr_object ():
    def __init__(self, year, rango):
        self.year = year
        self.rango = rango
        self._limits_m = self.limits(period="mensual")
        self._limits_a = self.limits(period="anual")
        self._range_list = self.range_list()

    # @property
    # def limits(self):
    #     return self._limits
    
    # @limits.setter
    def limits(self, period):
        file_name="./"+period+"_"+self.year+".csv"
        with open(file_name,"r",encoding="utf-8") as csvfile:
            limites=csv.DictReader(csvfile)
            limites_dic=list(limites)
        return limites_dic

    
    # @property
    # def range_list(self):
    #     return self._range_list
    
    # @limits.setter
    def range_list(self):
        list1=[i for i in range(self.rango.a,self.rango.b)]
        return list1
        
        

    def cal_isr (self, ingreso_grav, limites):
        for i in limites:
            if float(i["limite_i"]) < ingreso_grav < float(i["limite_s"]):
                isr_f = float(i["cuota_f"]) + ((ingreso_grav-float(i["limite_i"]))*(float(i["tasa"])/100))            
        return isr_f


    def anual_mensual(self,ingreso_grav):
        return (ingreso_grav*12.5)

    def anual_quincenal(ingreso_grav):
        return (ingreso_grav/2)

    def tasa_t (self, ingreso_grav, limites):
        isr_f=self.cal_isr(ingreso_grav,limites)
        tasa_total= (isr_f*100)/ingreso_grav
        return tasa_total

    def plot_tasa(self):
        
        list_tasa_mensual=[self.tasa_t(i,self._limits_m) for i in self._range_list ]
        list_tasa_anual=[self.tasa_t(self.anual_mensual(i),self._limits_a) for i in self._range_list ]
        print("Esta grafica muestra como crece el porcentaje de ISR con respecto al aumento de salario")
        plt.plot(self._range_list,list_tasa_mensual, label='Con tablas Mensuales')
        plt.plot(self._range_list,list_tasa_anual, label='Con tablas Anuales(contando 15 dias de Aguinaldo)')
        plt.legend()
        plt.title('Crecimiento de la tasa de ISR retenido con respecto al aumento de salario ')
        plt.yscale('linear')
        plt.ylabel('Tasa de impuestos en mexico % ')
        plt.xlabel('Sueldo Mensual (MXN)')
        plt.grid()
        plt.show()
    
    def plot_isr(self):
        
        list_tasa_mensual=[self.cal_isr(i,self._limits_m) for i in self._range_list ]
        list_tasa_anual=[self.cal_isr(self.anual_mensual(i),self._limits_a)/12.5 for i in self._range_list ]
        print("Esta grafica muestra como crece la retención de ISR con respecto al aumento de salario")
        plt.plot(self._range_list,list_tasa_mensual, label='Con tablas Mensuales')
        plt.plot(self._range_list,list_tasa_anual, label='Con tablas Mensuales')
        plt.legend()
        plt.title('Crecimiento de la retención de ISR con respecto al aumento de salario')
        plt.yscale('linear')
        plt.ylabel('Impuesto retenido por el SAT (MXN) ')
        plt.xlabel('Sueldo Mensual (MXN)')
        plt.grid()
        plt.show()

def input_function():

    print("    ISR Mexico  " )    
    print("    a) Graficar tasas  de ISR en un rango de sueldos " )
    print("    b) Graficar retenciones de ISR en un rango de sueldos " )
    option = input("Elige una Opcion: ")
    assert option.isdigit and len(option)>0 and option in ['a','b'], "Opcion no valida, elige a o b"
    a = input("Escribe el sueldo en MXN inferior (Mayor a 0 y que sea numerico) : ")
    assert a.isnumeric  and int(a) > 0 , "Opciones nos validas"
    a=int(a)
    b = input("Escribe el sueldo en MXN superior (Mayor al inferior y que sea numerico) : ")
    assert b.isnumeric  and int(b) > int(a), "Opciones nos validas"
    b = int(b)
    if option == "a":
        salary_range1=salary_range(a,b)
        isr_mexico=isr_object('2021',salary_range1)
        isr_mexico.plot_tasa()

    elif option == "b":
        salary_range1=salary_range(a,b)
        isr_mexico=isr_object('2021',salary_range1)
        isr_mexico.plot_isr()

def run():
    input_function()

if __name__ == '__main__':
    run()