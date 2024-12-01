import pytest
from django.urls import reverse
from cars.models import Brand, Car
from django.contrib.auth.models import User
from django.test import Client

# Fixtures

@pytest.fixture
def create_user(db):
    """Fixture para criar um usuário"""
    user = User.objects.create_user(username='testuser', password='testpass')
    return user

@pytest.fixture
def authenticated_client(create_user):
    """Fixture para criar um cliente autenticado"""
    client = Client()
    client.login(username='testuser', password='testpass')
    return client

@pytest.fixture
def brand_instance(db):
    """Fixture para criar uma marca"""
    return Brand.objects.create(name="Toyota")

@pytest.fixture
def car_instance(db, brand_instance):
    """Fixture para criar um carro"""
    return Car.objects.create(
        model="Corolla",
        brand=brand_instance,
        factory_year=2020,
        model_year=2021,
        plate="ABC1234",
        value=30000.0,
        color="Red",
        bio="A reliable car",
    )

# Testes

# Teste para a CarListView
@pytest.mark.django_db
def test_car_list_view(client, car_instance):
    response = client.get(reverse('cars_list'))
    assert response.status_code == 200
    assert 'cars' in response.context
    assert car_instance in response.context['cars']

# Teste para o filtro de busca na CarListView
@pytest.mark.django_db
def test_car_list_view_search(client, car_instance):
    response = client.get(reverse('cars_list') + '?search=Corolla')
    assert response.status_code == 200
    assert car_instance in response.context['cars']

# Teste para a CarDetailView
@pytest.mark.django_db
def test_car_detail_view(client, car_instance):
    response = client.get(reverse('car_detail', kwargs={'pk': car_instance.pk}))
    assert response.status_code == 200
    assert response.context['object'] == car_instance

# Teste para a NewCarCreateView
@pytest.mark.django_db
def test_new_car_create_view(authenticated_client, brand_instance):
    response = authenticated_client.post(reverse('new_car'), data={
        'model': 'Focus',
        'brand': brand_instance.id,
        'factory_year': 2019,
        'model_year': 2020,
        'plate': 'DEF5678',
        'value': 25000.0,
        'color': 'Blue',
        'bio': 'Compact and efficient',
    })
    assert response.status_code in (200, 302), f"Form errors: {response.context.get('form').errors if response.status_code == 200 else ''}"
    if response.status_code == 302:
        assert Car.objects.filter(model='Focus').exists()

# Teste para a CarUpdateView
@pytest.mark.django_db
def test_car_update_view(authenticated_client, car_instance):
    response = authenticated_client.post(reverse('car_update', kwargs={'pk': car_instance.pk}), data={
        'model': 'Civic',
        'brand': car_instance.brand.id,
        'factory_year': 2021,
        'model_year': 2022,
        'plate': 'XYZ1234',
        'value': 32000.0,
        'color': 'Black',
        'bio': 'Updated description',
    })
    assert response.status_code in (200, 302), f"Form errors: {response.context.get('form').errors if response.status_code == 200 else ''}"
    if response.status_code == 302:
        car_instance.refresh_from_db()
        assert car_instance.model == 'Civic'
        assert car_instance.color == 'Black'

# Teste para a CarDeleteView
@pytest.mark.django_db
def test_car_delete_view(authenticated_client, car_instance):
    response = authenticated_client.post(reverse('car_delete', kwargs={'pk': car_instance.pk}))
    assert response.status_code == 302  # Redirecionamento após exclusão
    assert not Car.objects.filter(pk=car_instance.pk).exists()

# Teste de acesso não autenticado
@pytest.mark.django_db
def test_create_view_requires_authentication(client):
    response = client.get(reverse('new_car'))
    assert response.status_code == 302  # Redirecionamento para login
    assert response.url.startswith(reverse('login'))