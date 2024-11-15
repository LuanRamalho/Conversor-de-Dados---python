import tkinter as tk
from tkinter import ttk

# Função para conversão de dados
def converter():
    try:
        # Dicionário com fatores de conversão
        conversion_factors = {
            "bit": 1,
            "byte": 8,
            "kilobyte": 8 * 1024,
            "megabyte": 8 * 1024**2,
            "gigabyte": 8 * 1024**3,
            "terabyte": 8 * 1024**4,
            "petabyte": 8 * 1024**5,
        }

        # Coletar valores de entrada
        entrada = combo_entrada.get()
        saida = combo_saida.get()
        quantidade = float(entry_quantidade.get())

        # Calcular resultado
        valor_bits = quantidade * conversion_factors[entrada]
        resultado = valor_bits / conversion_factors[saida]

        # Exibir o resultado
        lbl_resultado.config(text=f"Resultado: {resultado:.10f} {saida}(s)")
    except Exception as e:
        lbl_resultado.config(text=f"Erro: {str(e)}")

# Janela principal
app = tk.Tk()
app.title("Conversor de Dados")
app.geometry("400x300")
app.configure(bg="lime")

# Widgets
lbl_titulo = tk.Label(app, text="Conversor de Dados", font=("Arial", 18, "bold"), bg="lime", fg="darkslateblue")
lbl_titulo.pack(pady=10)

frame_entrada = tk.Frame(app, bg="lime")
frame_entrada.pack(pady=5)

lbl_quantidade = tk.Label(frame_entrada, text="Quantidade:", bg="lime", font=("Arial",12))
lbl_quantidade.grid(row=0, column=0, padx=5, pady=5)
entry_quantidade = tk.Entry(frame_entrada, width=15, font=("Arial",12))
entry_quantidade.grid(row=0, column=1, padx=5, pady=5)

lbl_de = tk.Label(frame_entrada, text="De:", bg="lime", font=("Arial",12))
lbl_de.grid(row=1, column=0, padx=5, pady=5)
combo_entrada = ttk.Combobox(frame_entrada, values=["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte"], font=("Arial",12))
combo_entrada.grid(row=1, column=1, padx=5, pady=5)
combo_entrada.set("bit")

lbl_para = tk.Label(frame_entrada, text="Para:", bg="lime", font=("Arial",12))
lbl_para.grid(row=2, column=0, padx=5, pady=5)
combo_saida = ttk.Combobox(frame_entrada, values=["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte"], font=("Arial",12))
combo_saida.grid(row=2, column=1, padx=5, pady=5)
combo_saida.set("byte")

btn_converter = tk.Button(app, text="Converter", command=converter, font=("Arial", 15, "bold"), bg="darkmagenta", fg="honeydew")
btn_converter.pack(pady=10)

lbl_resultado = tk.Label(app, text="Resultado: ", font=("Arial", 15, "bold"), bg="lime", fg="indigo")
lbl_resultado.pack(pady=10)

# Iniciar o programa
app.mainloop()
