import pandas as pd
import json
import os


input_folder = "base"  
output_folder = "conversiones"

# Crear la carpeta de salida si no existe
os.makedirs(output_folder, exist_ok=True)

# Obtener la lista de archivos en la carpeta base
files = [f for f in os.listdir(input_folder) if f.endswith('.xlsx')]

if not files:
    print("No se encontraron archivos .xlsx en la carpeta 'base'.")
else:
    for file in files:
        input_path = os.path.join(input_folder, file)  
        output_filename = file.replace('.xlsx', '.csv')
        output_path = os.path.join(output_folder, output_filename)

        # Cargar el archivo Excel
        df = pd.read_excel(input_path, sheet_name='Reporte')

        # Convertir los datos a formato JSON
        data = df.to_dict(orient='records')
        json_data = json.dumps(data, indent=4, ensure_ascii=False)  

        # Guardar el código en un archivo CSV
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(json_data)

        print(f"Archivo convertido y guardado en: {output_path}")

print("Proceso finalizado.")
