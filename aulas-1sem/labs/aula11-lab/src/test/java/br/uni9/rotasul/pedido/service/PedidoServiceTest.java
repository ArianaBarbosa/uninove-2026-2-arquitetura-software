package br.uni9.rotasul.pedido.service;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import br.uni9.rotasul.pedido.domain.Pedido;
import br.uni9.rotasul.pedido.repository.PedidoRepositoryEmMemoria;

// Teste do serviço, não do controlador: é no serviço que está a regra.
// Arquivo da Aula 06, pronto no kit de hoje com dois ajustes acumulados,
// nenhum dos dois novo: o primeiro, da própria Aula 07, troca o tipo
// concreto PedidoService (que virou interface naquela aula) pelo
// PedidoServicePadrao que a substituiu; o segundo, de hoje, acrescenta o
// terceiro argumento obrigatório, regiao, ao construtor de Pedido. Sem os
// dois, este arquivo não compila, e a suíte inteira do fork para, não só os
// testes de hoje.
class PedidoServiceTest {

    private PedidoService pedidoService;

    @BeforeEach
    void configurar() {
        pedidoService = new PedidoServicePadrao(new PedidoRepositoryEmMemoria());
    }

    @Test
    void registraPedidoValidoEApareceNaListagem() {
        Pedido pedido = new Pedido("Lojista Ana", "Duas caixas de peças automotivas", "PRINCIPAL");

        pedidoService.registrar(pedido);

        assertThat(pedidoService.listar())
                .hasSize(1)
                .first()
                .satisfies(registrado -> {
                    assertThat(registrado.getId()).isNotNull();
                    assertThat(registrado.getCliente()).isEqualTo("Lojista Ana");
                    assertThat(registrado.getSituacao()).isEqualTo("RECEBIDO");
                });
    }

    @Test
    void recusaPedidoSemClienteInformado() {
        Pedido pedido = new Pedido("", "Pedido sem cliente", "PRINCIPAL");

        assertThatThrownBy(() -> pedidoService.registrar(pedido))
                .isInstanceOf(IllegalArgumentException.class)
                .hasMessage("Pedido sem cliente informado é recusado.");

        assertThat(pedidoService.listar()).isEmpty();
    }
}
