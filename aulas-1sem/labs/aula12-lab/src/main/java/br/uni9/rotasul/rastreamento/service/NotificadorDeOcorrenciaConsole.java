package br.uni9.rotasul.rastreamento.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import br.uni9.rotasul.rastreamento.domain.Ocorrencia;

// Implementação de dev: sem anotação nenhuma. Quem registra esta classe como
// bean é NotificacaoConfig, nunca uma anotação na própria classe.
public class NotificadorDeOcorrenciaConsole implements NotificadorDeOcorrencia {

    private static final Logger log = LoggerFactory.getLogger(NotificadorDeOcorrenciaConsole.class);

    @Override
    public void notificar(Ocorrencia ocorrencia) {
        log.info("[DEV] ocorrencia {} do tipo {} registrada",
                ocorrencia.getCodigoRastreio(), ocorrencia.getTipo());
    }
}
