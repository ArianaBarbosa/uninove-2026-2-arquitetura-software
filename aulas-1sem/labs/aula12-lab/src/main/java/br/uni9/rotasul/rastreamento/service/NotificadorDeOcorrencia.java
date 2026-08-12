package br.uni9.rotasul.rastreamento.service;

import br.uni9.rotasul.rastreamento.domain.Ocorrencia;

// O contrato de notificação. Sem anotação de framework: como toda interface
// de contrato do semestre, ela não sabe que o Spring existe.
public interface NotificadorDeOcorrencia {

    void notificar(Ocorrencia ocorrencia);
}
