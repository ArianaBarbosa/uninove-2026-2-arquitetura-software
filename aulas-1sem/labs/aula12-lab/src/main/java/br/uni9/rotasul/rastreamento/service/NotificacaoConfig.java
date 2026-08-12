package br.uni9.rotasul.rastreamento.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;

// Configuração explícita: concentra, num único lugar, a decisão de qual
// implementação vira bean em qual perfil. As classes de implementação em si
// não têm anotação de framework; é o método @Bean que as registra. Mesmo
// padrão de CalculoDeFreteConfig (Aula 11) e ParceiroClientConfig (Aula 10).
@Configuration
public class NotificacaoConfig {

    private static final Logger log = LoggerFactory.getLogger(NotificacaoConfig.class);

    @Bean
    @Profile("dev")
    public NotificadorDeOcorrencia notificadorDeOcorrenciaDev() {
        return new NotificadorDeOcorrenciaConsole();
    }

    @Bean
    @Profile("prod")
    public NotificadorDeOcorrencia notificadorDeOcorrenciaProd(
            @Value("${rotasul.webhook.parceiro-notificacao}") String urlWebhook) {
        return new NotificadorDeOcorrenciaWebhookSimulado(urlWebhook);
    }

    // Com @Profile("dev", "prod"): roda nos dois perfis de hoje e imprime,
    // no log de subida, qual notificador o container injetou. Não pode
    // ficar sem @Profile, porque nenhum dos dois beans acima existe fora de
    // "dev" ou "prod" (o perfil "padrao", ativo por padrão desde a Aula 07,
    // não tem notificador nenhum); sem a restrição, este bean quebraria a
    // subida em qualquer outro perfil por dependência não satisfeita.
    @Bean
    @Profile({"dev", "prod"})
    public CommandLineRunner logarNotificadorAtivo(NotificadorDeOcorrencia notificador) {
        return args -> log.info("Notificador ativo: {}", notificador.getClass().getSimpleName());
    }
}
