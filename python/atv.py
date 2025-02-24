import tkinter as tk
import requests

def converter():
    try:
        valor_reais = float(entrada_valor.get())
        
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        resposta = requests.get(url)
        dados = resposta.json()
        
        cotacao_dolar = float(dados["USDBRL"]["bid"])
        
        valor_dolares = valor_reais / cotacao_dolar
        
        # Atualiza o rótulo com o resultado formatado
        resultado.config(text=f"USD: ${valor_dolares:.2f}")
    except ValueError:
        resultado.config(text="Por favor, insira um número válido.")
    except Exception as e:
        resultado.config(text="Erro ao acessar a API.")

# Configuração da interface Tkinter
janela = tk.Tk()
janela.title("Conversor BRL → USD")

tk.Label(janela, text="Valor em R$:", font=("Arial", 12)).pack(padx=10, pady=5)
entrada_valor = tk.Entry(janela, font=("Arial", 12))
entrada_valor.pack(padx=10, pady=5)



janela.mainloop()