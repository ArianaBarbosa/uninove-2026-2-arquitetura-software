package br.uni9.rotasul.pedido.service;

import java.util.List;

import org.springframework.context.annotation.Profile;
import org.springframework.stereotype.Service;

import br.uni9.rotasul.pedido.domain.Pedido;
import br.uni9.rotasul.pedido.repository.PedidoRepository;

// Provedor padrão da interface PedidoService, ativo nos perfis "padrao",
// "dev" e "prod". É a mesma classe PedidoService da Aula 06, renomeada e
// reclassificada como implementação de um contrato, não mais o contrato em
// si. "dev" e "prod" entraram na lista na Aula 12: são perfis de ambiente,
// escolhendo o notificador de ocorrência, e não dizem nada sobre qual
// PedidoService usar; sem essa ampliação, PedidoController deixa de achar
// bean de PedidoService assim que a aplicação sobe só com "dev" ou só com
// "prod" ativo, porque nenhum dos dois batia com "padrao" nem com "risco".
@Service
@Profile({"padrao", "dev", "prod"})
public class PedidoServicePadrao implements PedidoService {

    private final PedidoRepository pedidoRepository;

    public PedidoServicePadrao(PedidoRepository pedidoRepository) {
        this.pedidoRepository = pedidoRepository;
    }

    @Override
    public Pedido registrar(Pedido pedido) {
        if (pedido.getCliente() == null || pedido.getCliente().isBlank()) {
            throw new IllegalArgumentException("Pedido sem cliente informado é recusado.");
        }
        return pedidoRepository.salvar(pedido);
    }

    @Override
    public List<Pedido> listar() {
        return pedidoRepository.listarTodos();
    }
}
