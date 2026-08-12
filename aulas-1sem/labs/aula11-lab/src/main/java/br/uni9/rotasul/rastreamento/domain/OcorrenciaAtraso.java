package br.uni9.rotasul.rastreamento.domain;

import java.time.LocalDateTime;

// Arquivo pronto no kit, junto com Ocorrencia e OcorrenciaExtravio: veja o
// comentário de Ocorrencia sobre por que a hierarquia de produto não é
// digitada hoje.
public class OcorrenciaAtraso extends Ocorrencia {

    private final int horasDeAtraso;

    public OcorrenciaAtraso(String codigoRastreio, LocalDateTime registradaEm, int horasDeAtraso) {
        super(codigoRastreio, registradaEm);
        this.horasDeAtraso = horasDeAtraso;
    }

    public int getHorasDeAtraso() {
        return horasDeAtraso;
    }

    @Override
    public String getTipo() {
        return "ATRASO";
    }
}
