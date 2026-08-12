package br.uni9.rotasul.rastreamento.domain;

import java.time.LocalDateTime;

// Arquivo pronto no kit, junto com Ocorrencia e OcorrenciaAtraso: veja o
// comentário de Ocorrencia sobre por que a hierarquia de produto não é
// digitada hoje.
public class OcorrenciaExtravio extends Ocorrencia {

    private final String ultimaLocalizacaoConhecida;

    public OcorrenciaExtravio(String codigoRastreio, LocalDateTime registradaEm, String ultimaLocalizacaoConhecida) {
        super(codigoRastreio, registradaEm);
        this.ultimaLocalizacaoConhecida = ultimaLocalizacaoConhecida;
    }

    public String getUltimaLocalizacaoConhecida() {
        return ultimaLocalizacaoConhecida;
    }

    @Override
    public String getTipo() {
        return "EXTRAVIO";
    }
}
