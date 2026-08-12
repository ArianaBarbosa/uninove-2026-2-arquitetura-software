package br.uni9.rotasul.rastreamento.domain;

import java.time.LocalDateTime;

// Primeiro código do contexto rastreamento, reservado desde o diagrama de
// pacotes da Aula 05. O "produto" do padrão Factory Method: a hierarquia
// que OcorrenciaCreator decide qual subclasse instanciar. Sem anotação de
// framework, igual ao domínio de pedido e expedicao. Arquivo pronto no kit:
// esta hierarquia é herança simples, que a turma já domina desde a Aula 06;
// não é o padrão que a aula ensina, então escrevê-la à mão não ensinaria
// nada novo hoje. O padrão do dia, o Factory Method, está em
// OcorrenciaCreator, no passo seguinte.
public abstract class Ocorrencia {

    private final String codigoRastreio;
    private final LocalDateTime registradaEm;

    protected Ocorrencia(String codigoRastreio, LocalDateTime registradaEm) {
        this.codigoRastreio = codigoRastreio;
        this.registradaEm = registradaEm;
    }

    public String getCodigoRastreio() {
        return codigoRastreio;
    }

    public LocalDateTime getRegistradaEm() {
        return registradaEm;
    }

    public abstract String getTipo();
}
