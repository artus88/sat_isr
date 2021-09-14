import matplotlib.pyplot as plt
import csv

def read(file_name):
    with open(file_name,"r",encoding="utf-8") as csvfile:
        limites=csv.DictReader(csvfile)
        limites_dic=list(limites)
    return limites_dic

def cal_isr (ingreso_grav, limites):

    for i in limites:
        if float(i["limite_i"]) < ingreso_grav < float(i["limite_s"]):
            isr_f = float(i["cuota_f"]) + ((ingreso_grav-float(i["limite_i"]))*(float(i["tasa"])/100))            
    return isr_f

def cal_isr_2 (ingreso_grav, limite_csv):

    for row in limite_csv:
        if float(row["limite_i"]) < ingreso_grav < float(row["limite_s"]):
            isr_f = float(row["cuota_f"]) + ((ingreso_grav-float(row["limite_i"]))*(float(row["tasa"])/100))            
    return isr_f

def anual_mensual(ingreso_grav):
    return (ingreso_grav*12.5)

def anual_quincenal(ingreso_grav):
    return (ingreso_grav/2)

def tasa_t (ingreso_grav, limites):
    isr_f=cal_isr(ingreso_grav,limites)
    tasa_total= (isr_f*100)/ingreso_grav
    return tasa_total

def plot_tasa(a,b):
        
    file_name_monthy= "./mensual_2021.csv"
    file_name_annual= "./anual_2021.csv"
    file_name_quincenal= "./quincenal_2021.csv"

    limites_mon = read(file_name_monthy)
    limites_anual = read (file_name_annual)
    limites_quincenal = read (file_name_quincenal)

    list_isr=[cal_isr(i,limites_mon) for i in range(a,b)]
    list_tasa_mensual=[tasa_t(i,limites_mon) for i in range(a,b) ]
    list_tasa_anual=[tasa_t(anual_mensual(i),limites_anual) for i in range(a,b) ]
    list_tasa_quincenal=[tasa_t(anual_quincenal(i),limites_quincenal) for i in range(a,b) ]

    print("Esta grafica muestra como crece el porcentaje de ISR con respecto al aumento de salario")
    plt.plot(range(a,b),list_tasa_mensual, label='Con tablas Mensuales')
    plt.plot(range(a,b),list_tasa_anual, label='Con tablas Anuales(contando 15 dias de Aguinaldo)')
    plt.legend()
    # plt.plot(range(a,b),list_tasa_quincenal)
    plt.title('Esta grafica muestra \n como crece el porcentaje de ISR retenido con respecto al aumento de salario ')
    plt.yscale('linear')
    plt.ylabel('Tasa de impuestos en mexico % ')
    plt.xlabel('Sueldo Mensual (MXN)')
    plt.grid()
    plt.show()

def plot_sueldo(a,b):

    
    file_name_monthy= "./mensual_2021.csv"
    file_name_annual= "./anual_2021.csv"
    file_name_quincenal= "./quincenal_2021.csv"

    limites_mon = read(file_name_monthy)
    limites_anual = read (file_name_annual)
    limites_quincenal = read (file_name_quincenal)

    list_isr_mensual=[cal_isr(i,limites_mon) for i in range(a,b)]
    list_isr_anual=[cal_isr(anual_mensual(i),limites_anual)/12.5 for i in range(a,b) ]


    print("Esta grafica muestra como crece la retención de ISR con respecto al aumento de salario")
    plt.plot(range(a,b),list_isr_mensual, label='Con tablas Mensuales')
    plt.plot(range(a,b),list_isr_anual, label='Con tablas Anuales(contando 15 dias de Aguinaldo)')
    plt.legend()
    # plt.plot(range(a,b),list_tasa_quincenal)
    plt.title('Esta grafica muestra \n como crece la retención de ISR con respecto al aumento de salario')
    plt.yscale('linear')
    plt.ylabel('Tasa de impuestos en mexico % ')
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
        plot_tasa(a,b)
    elif option == "b":
        plot_sueldo(a,b)



def run():
    #ingreso_grav = float(input("Cual es tu ingreso Gravable? : "))

    input_function()



if __name__ == '__main__':
    run()