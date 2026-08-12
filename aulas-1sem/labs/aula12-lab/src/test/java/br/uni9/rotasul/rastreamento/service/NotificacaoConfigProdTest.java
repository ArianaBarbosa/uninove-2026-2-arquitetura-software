package br.uni9.rotasul.rastreamento.service;

import static org.junit.jupiter.api.Assertions.assertInstanceOf;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.ActiveProfiles;

@SpringBootTest
@ActiveProfiles("prod")
class NotificacaoConfigProdTest {

    @Autowired
    private NotificadorDeOcorrencia notificador;

    @Test
    void perfilProdInjetaONotificadorDeWebhook() {
        assertInstanceOf(NotificadorDeOcorrenciaWebhookSimulado.class, notificador);
    }
}
