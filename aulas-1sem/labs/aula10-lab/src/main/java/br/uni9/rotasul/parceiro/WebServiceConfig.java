package br.uni9.rotasul.parceiro;

import org.springframework.boot.web.servlet.ServletRegistrationBean;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.ClassPathResource;
import org.springframework.ws.config.annotation.EnableWs;
import org.springframework.ws.config.annotation.WsConfigurerAdapter;
import org.springframework.ws.transport.http.MessageDispatcherServlet;
import org.springframework.ws.wsdl.wsdl11.DefaultWsdl11Definition;
import org.springframework.xml.xsd.SimpleXsdSchema;
import org.springframework.xml.xsd.XsdSchema;

// Classe de configuração pronta no kit: publica o MessageDispatcherServlet
// em /ws/* e expõe o WSDL gerado a partir do parceiro.xsd, sem que o aluno
// precise escrever nenhuma linha destes três beans.
@EnableWs
@Configuration
public class WebServiceConfig extends WsConfigurerAdapter {

    @Bean
    public ServletRegistrationBean<MessageDispatcherServlet> messageDispatcherServlet(ApplicationContext applicationContext) {
        MessageDispatcherServlet servlet = new MessageDispatcherServlet();
        servlet.setApplicationContext(applicationContext);
        servlet.setTransformWsdlLocations(true);
        return new ServletRegistrationBean<>(servlet, "/ws/*");
    }

    @Bean(name = "parceiro")
    public DefaultWsdl11Definition defaultWsdl11Definition(XsdSchema parceiroSchema) {
        DefaultWsdl11Definition wsdl11Definition = new DefaultWsdl11Definition();
        wsdl11Definition.setPortTypeName("ParceiroPort");
        wsdl11Definition.setLocationUri("/ws");
        wsdl11Definition.setTargetNamespace("http://rotasul.uni9.br/parceiro");
        wsdl11Definition.setSchema(parceiroSchema);
        return wsdl11Definition;
    }

    @Bean
    public XsdSchema parceiroSchema() {
        return new SimpleXsdSchema(new ClassPathResource("parceiro.xsd"));
    }
}
