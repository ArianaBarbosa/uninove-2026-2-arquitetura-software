package br.uni9.rotasul.pedido.service;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

import org.junit.jupiter.api.Test;

import br.uni9.rotasul.pedido.domain.Pedido;

// Suíte de contrato: testa a interface PedidoService, nunca uma
// implementação específica. Cada subclasse concreta só precisa dizer qual
// implementação está sendo testada; os dois métodos abaixo rodam iguais
// para as duas. Arquivo da Aula 07, pronto no kit de hoje com um único
// ajuste: o construtor de Pedido ganhou um terceiro parâmetro obrigatório,
// regiao, no passo 1 de hoje. Sem este ajuste, as duas chamadas a
// "new Pedido(...)" abaixo deixariam de compilar, e a suíte inteira do
// fork pararia de rodar, não só os testes de hoje.
abstract class PedidoServiceContratoTest {

    protected abstract PedidoService criarServico();

    @Test
    void registraPedidoValidoEApareceNaListagem() {
        PedidoService pedidoService = criarServico();
        Pedido pedido = new Pedido("Lojista Ana", "Duas caixas de peças automotivas", "PRINCIPAL");

        pedidoService.registrar(pedido);

        assertThat(pedidoService.listar())
                .hasSize(1)
                .first()
                .satisfies(registrado -> {
                    assertThat(registrado.getId()).isNotNull();
                    assertThat(registrado.getCliente()).isEqualTo("Lojista Ana");
                });
    }

    @Test
    void recusaPedidoSemClienteInformado() {
        PedidoService pedidoService = criarServico();
        Pedido pedido = new Pedido("", "Pedido sem cliente", "PRINCIPAL");

        assertThatThrownBy(() -> pedidoService.registrar(pedido))
                .isInstanceOf(IllegalArgumentException.class)
                .hasMessage("Pedido sem cliente informado é recusado.");

        assertThat(pedidoService.listar()).isEmpty();
    }
}
