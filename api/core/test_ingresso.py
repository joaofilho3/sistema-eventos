import pytest
from core.models import Evento, Ingresso
from datetime import date

@pytest.mark.django_db
def test_criar_ingresso():
    evento = Evento.objects.create(
        nome="Show Rock",
        descricao="Show de rock nacional",
        data=date.today(),
        local="Estádio Central"
    )
    ingresso = Ingresso.objects.create(evento=evento, preco=100.00, quantidade=50)

    assert ingresso.evento.nome == "Show Rock"
    assert ingresso.preco == 100.00
    assert ingresso.quantidade == 50
