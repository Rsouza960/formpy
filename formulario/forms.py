from django.forms import ModelForm
from registro.models import Solicitacao

# Create the form class.
class SolicitacaoForm(ModelForm):
     class Meta:
        model = Solicitacao
        fields = ['nome_empresa', 'cnpj_cpf', 'cep', 'logradouro', 'numerocasa', 'complemento', 'municipio', 'uf', ]