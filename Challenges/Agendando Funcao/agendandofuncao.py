import sched
import time

def agendar_execucao(horario_do_evento, funcao, *args):
    # Instancia um agendador
    s = sched.scheduler(time.time, time.sleep)
    
    # Agendar o evento
    s.enterabs(horario_do_evento, 1, funcao, argument=args)
    
    # Mostra os detalhes do agendamento
    horario_legivel = time.asctime(time.localtime(horario_do_evento))
    print(f"Função {funcao.__name__} agendada para {horario_legivel}.")
    
    # Executa o agendamento
    s.run()

# Exemplo de função a ser agendada
def minha_mensagem(mensagem):
    print(mensagem)

# Testando o agendamento
horario_futuro = time.time() + 3  # 3 segundos no futuro
agendar_execucao(horario_futuro, minha_mensagem, "Olá, essa é uma mensagem agendada!")
