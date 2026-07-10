# Net Status Tracker 🌐

Um script de automação focado em infraestrutura de redes, desenvolvido em **Python**. 

## 🎯 Objetivo do Projeto
Diagnosticar instabilidades de rede é uma das tarefas mais críticas no nível de Suporte e Operações. Este projeto foi criado para automatizar disparos de pacotes ICMP (Ping) contra servidores vitais (DNS e Gateways Locais) e registrar a disponibilidade das rotas em um arquivo de log contínuo. É uma ferramenta útil para homologar a estabilidade de conexão de ISPs (Provedores de Internet) e detectar quedas de pacotes temporárias.

## ⚙️ Funcionalidades
- **Teste de Conectividade ICMP:** Interação direta com o prompt de comando do sistema operacional via módulo `subprocess`.
- **Cross-Platform:** O código identifica o SO rodando na máquina hospedeira (Windows ou Unix) e adapta os parâmetros do ping automaticamente.
- **Geração de Logs (I/O de Arquivos):** Escrita contínua em arquivo `.txt` mantendo o histórico de horário e status sem sobrescrever dados anteriores (modo Append).
- **Graceful Shutdown:** Tratamento da interrupção do teclado (`Ctrl+C`) para um encerramento limpo da execução.

## 🚀 Como utilizar
Nenhuma biblioteca externa é necessária.
1. Abra o terminal na pasta do projeto.
2. Execute o comando:
   ```bash
   python net_monitor.py
