package br.uni9.rotasul.pedido.domain;

// Classe de domínio. Sem anotação de framework nenhuma: o domínio não
// depende de Spring, e essa independência vai importar na Aula 12, quando
// a injeção de dependência explícita entrar em pauta. Primeira mudança
// desde que a classe nasceu na Aula 06: o atributo regiao, que o Strategy
// de hoje usa para decidir qual estratégia de frete aplicar. Arquivo pronto
// no kit: o construtor ganha um terceiro parâmetro obrigatório, o que
// quebraria, sem ajuste, qualquer chamada com dois argumentos que já
// existisse no fork.
public class Pedido {

    private Long id;
    private final String cliente;
    private final String descricao;
    private String situacao;
    private final String regiao;

    public Pedido(String cliente, String descricao, String regiao) {
        this.cliente = cliente;
        this.descricao = descricao;
        this.situacao = "RECEBIDO";
        this.regiao = regiao;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getCliente() {
        return cliente;
    }

    public String getDescricao() {
        return descricao;
    }

    public String getSituacao() {
        return situacao;
    }

    public void setSituacao(String situacao) {
        this.situacao = situacao;
    }

    public String getRegiao() {
        return regiao;
    }
}
