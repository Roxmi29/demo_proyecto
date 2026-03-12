TSS = 0.0591      
BONIFICACION = 0.10 

def calcular_isr(sueldo_anual):
    if sueldo_anual <= 416220:
        return 0
    elif sueldo_anual <= 624329:
        return (sueldo_anual - 416220) * 0.15
    elif sueldo_anual <= 867123:
        return 31216 + (sueldo_anual - 624329) * 0.20
    else:
        return 79484 + (sueldo_anual - 867123) * 0.25

sueldo_bruto = float(input("Ingrese el sueldo bruto mensual: "))
otros_descuentos = float(input("Ingrese otros descuentos: "))
aplica_bonificacion = input("¿Aplica bonificación? (s/n): ").lower() == "s"

if sueldo_bruto <= 0:
    print("Error: El sueldo bruto debe ser mayor que cero.")
else:
    desc_tss = sueldo_bruto * TSS
    isr_mensual = calcular_isr(sueldo_bruto * 12) / 12
    bonificacion = sueldo_bruto * BONIFICACION if aplica_bonificacion else 0
    sueldo_neto = sueldo_bruto - desc_tss - isr_mensual - otros_descuentos + bonificacion

    print("\n--- Resultados del cálculo ---")
    print(f"Sueldo Bruto: RD${sueldo_bruto:.2f}")
    print(f"Descuento TSS: RD${desc_tss:.2f}")
    print(f"ISR: RD${isr_mensual:.2f}")
    print(f"Otros Descuentos: RD${otros_descuentos:.2f}")
    print(f"Bonificación: RD${bonificacion:.2f}")
    print(f"Sueldo Neto: RD${sueldo_neto:.2f}")
