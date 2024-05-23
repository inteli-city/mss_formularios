from src.shared.helpers.errors.base_error import BaseError


class MissingParameters(BaseError):
    def __init__(self, message: str):
        super().__init__(f'Parâmetro ausente: {message}')
class WrongTypeParameter(BaseError):
    def __init__(self, fieldName: str, fieldTypeExpected: str, fieldTypeReceived: str):
        super().__init__(f'Campo {fieldName} deveria ser do tipo {fieldTypeExpected}, mas foi recebido um campo do tipo {fieldTypeReceived}')