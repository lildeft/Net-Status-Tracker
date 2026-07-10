import subprocess
import platform
import datetime
import time

def ping_server(host):
    """Dispara um pacote ICMP (ping) para o servidor e retorna True se responder."""
    # O Windows usa '-n' para o número de pacotes, enquanto sistemas baseados em Unix usam '-c'
    parametro = '-n' if platform.system().lower() == 'windows' else '-c'
    comando = ['ping', parametro, '1', host]
    
    # Executa o comando de rede direto no sistema operacional de forma invisível
    resultado = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return resultado.returncode == 0

def iniciar_monitoramento():
    """Inicia o loop de monitoramento de rotas e gravação de logs."""
    # Lista de alvos críticos para testar a rota de internet
    # Lista de alvos críticos para testar a rota de internet
    servidores = {
        "Google DNS": "8.8.8.8",
        "Cloudflare DNS": "1.1.1.1",
        "Gateway Padrão": "192.168.X.X" # <-- Substitua pelo IP do seu roteador local
    }
    
    arquivo_log = "network_log.txt"
    
    print("=== 🌐 Monitor de Conectividade e Rotas ===")
    print(f"Log sendo gravado em: {arquivo_log}")
    print("Pressione [Ctrl+C] no terminal para encerrar o monitoramento.\n")
    
    try:
        while True:
            agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            linha_log = f"[{agora}]\n"
            
            for nome, ip in servidores.items():
                status = "ONLINE 🟢" if ping_server(ip) else "OFFLINE 🔴"
                linha_log += f" - {nome} ({ip}): {status}\n"
                print(f"[{agora}] {nome} -> {status}")
            
            linha_log += "-"*40 + "\n"
            
            # Abre o arquivo em modo 'a' (append) para adicionar o log sem apagar o histórico
            with open(arquivo_log, "a", encoding="utf-8") as f:
                f.write(linha_log)
            
            print("⏳ Aguardando 10 segundos para o próximo ciclo de testes...\n")
            time.sleep(10) # Intervalo entre os pings para não sobrecarregar a rede
            
    except KeyboardInterrupt:
        print("\n🛑 Monitoramento encerrado pelo usuário com sucesso.")

if __name__ == "__main__":
    iniciar_monitoramento()