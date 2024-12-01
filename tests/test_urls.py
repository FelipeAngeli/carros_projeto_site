import pytest
from django.test import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.views import logout_view
from django.contrib.messages import get_messages


@pytest.mark.django_db
def test_logout_view():
    """
    Testa o comportamento da view de logout para usuários autenticados.
    """
    # Configura o RequestFactory
    factory = RequestFactory()
    request = factory.get(reverse('logout'))

    # Adiciona o usuário autenticado
    request.user = User.objects.create_user(username="testuser", password="testpass")
    print(f"Usuário criado: {request.user}")

    # Adiciona o middleware de sessão manualmente ao request
    session_middleware = SessionMiddleware(lambda req: None)
    session_middleware.process_request(request)
    request.session.save()
    print("Middleware de sessão configurado com sucesso.")

    # Adiciona o middleware de mensagens manualmente ao request
    message_middleware = MessageMiddleware(lambda req: None)
    message_middleware.process_request(request)
    print("Middleware de mensagens configurado com sucesso.")

    # Chama a view de logout
    response = logout_view(request)
    print("View logout chamada com sucesso.")

    # Verifica o redirecionamento
    assert response.status_code == 302, "Logout não está redirecionando corretamente."
    assert response.url == reverse('login'), "Logout não redireciona para a página de login."

    # Verifica se a mensagem de sucesso foi adicionada
    messages = [msg.message for msg in get_messages(request)]
    print(f"Mensagens capturadas: {messages}")
    assert "Você foi desconectado com sucesso." in messages, "Mensagem de logout não foi adicionada."
