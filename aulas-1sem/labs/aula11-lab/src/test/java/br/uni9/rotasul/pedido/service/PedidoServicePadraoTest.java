package br.uni9.rotasul.pedido.service;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import br.uni9.rotasul.pedido.domain.Pedido;
import br.uni9.rotasul.pedido.repository.PedidoRepositoryEmMemoria;

// Teste da implementação PedidoServicePadrao, não do controlador: é no
// serviço que está a regra. Arquivo da Aula 06 (então PedidoServiceTest),
// renomeado e ajustado para PedidoServicePadraoTest já na própria Aula 07,
// quando PedidoService virou interface. Pronto no kit de hoje com um único
// ajuste novo: o terceiro argumento obrigatório, regiao, no construtor de
// Pedido. Sem ele, este arquivo não compila, e a suíte inteira do fork
// para, não só os testes de hoje.
class PedidoServicePadraoTest {

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
