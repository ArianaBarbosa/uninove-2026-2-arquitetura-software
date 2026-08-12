package br.uni9.rotasul.rastreamento.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import br.uni9.rotasul.rastreamento.domain.Ocorrencia;

// Implementação de prod: também sem anotação, também registrada só por
// NotificacaoConfig. Simulado de propósito, pela mesma razão da Aula 10: a
// aula não pode depender de um endpoint externo de verdade em qualquer sala.
public class NotificadorDeOcorrenciaWebhookSimulado implements NotificadorDeOcorrencia {

    private static final Logger log = LoggerFactory.getLogger(NotificadorDeOcorrenciaWebhookSimulado.class);

    private final String urlWebhook;

    public NotificadorDeOcorrenciaWebhookSimulado(String urlWebhook) {
        this.urlWebhook = urlWebhook;
    }

    @Override
    public void notificar(Ocorrencia ocorrencia) {
        log.info("[PROD] enviaria POST para {} com a ocorrencia {}",
                urlWebhook, ocorrencia.getCodigoRastreio());
    }
}
