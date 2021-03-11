# -*- coding: utf-8 -*-

# Este exemplo demonstra a manipulação de intents de uma habilidade do Alexa usando o Alexa Skills Kit SDK para Python.
# Visite https://alexa.design/cookbook para obter exemplos adicionais sobre a implementação de slots, gerenciamento de diálogo,
# persistência de sessão, chamadas de API e muito mais.
# Este exemplo é construído usando a abordagem de classes de manipulador no construtor de habilidades.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler para iniciar a Skill."""
    def can_handle(self, handler_input):
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        speak_output = "Olá, você conhece o canal Sobrinho de T I ? Diga sim ou não."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class SimIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("SimIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Que legal, espero que já esteja inscrito no canal."

        return (
            handler_input.response_builder
                .speak(speak_output)
                #.ask("adicione um novo prompt se quiser manter a sessão aberta para o usuário responder")
                .response
        )

class NaoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("NaoIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Que pena, não perde tempo e se inscreve. Vai ter vídeos novos toda semana."

        return (
            handler_input.response_builder
                .speak(speak_output)
                #.ask("adicione um novo prompt se quiser manter a sessão aberta para o usuário responder")
                .response
        )

class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Tratamento de erro genérico para capturar qualquer tipo de erro."""
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        logger.error(exception, exc_info=True)

        speak_output = "Desculpe, eu não entendi o que você disse. Poderia repetir ?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# O objeto SkillBuilder atua como o ponto de entrada para sua skill, 
# roteando todas as cargas úteis de solicitação e resposta para os manipuladores acima. 
# Certifique-se de que quaisquer novos manipuladores ou interceptores que você definiu estejam incluídos abaixo. 
# A ordem é importante - eles são processados de cima para baixo.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(SimIntentHandler())
sb.add_request_handler(NaoIntentHandler())

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
