import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

class MarketingAssistant:
    def __init__(self):
        # Tenta pegar a chave da variável de ambiente
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("A chave GROQ_API_KEY não foi encontrada. Verifique o arquivo .env")
        
        # Inicializa o modelo (Llama 3 é ótimo para português)
        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            api_key=api_key
        )

    def generate_post(self, topic: str, platform: str, tone: str) -> str:
        """
        Gera um post de marketing baseado nos parâmetros fornecidos.
        """
        template = """
        Você é um especialista em Marketing Digital e Social Media Copywriting.
        Sua tarefa é criar um post altamente engajador para a rede social: {platform}.
        
        DETALHES DO PEDIDO:
        - Tópico Principal: {topic}
        - Tom de Voz desejado: {tone}
        - Idioma: Português do Brasil (pt-BR)
        
        ESTRUTURA OBRIGATÓRIA DO POST:
        1. Headline (Título): Impactante e curto (use emojis se a plataforma permitir).
        2. Corpo do Texto: Use técnicas de storytelling ou AIDA (Atenção, Interesse, Desejo, Ação).
        3. Call to Action (CTA): Uma chamada clara para o leitor interagir.
        4. Hashtags: 3 a 5 hashtags relevantes de alto volume.
        
        Gere apenas o conteúdo do post, sem explicações extras.
        """
        
        prompt = PromptTemplate.from_template(template)
        chain = prompt | self.llm | StrOutputParser()
        
        try:
            response = chain.invoke({
                "topic": topic,
                "platform": platform,
                "tone": tone
            })
            return response
        except Exception as e:
            return f"Erro ao gerar o post: {str(e)}"