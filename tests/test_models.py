import pytest
from cars.models import Brand, Car, CarInventory

@pytest.mark.django_db
def test_brand_creation():
    brand = Brand.objects.create(name="Toyota")
    assert brand.name == "Toyota"
    assert str(brand) == "Toyota"

@pytest.mark.django_db
def test_car_creation():
    brand = Brand.objects.create(name="Tesla")
    car = Car.objects.create(
        model="Model 3",
        brand=brand,
        factory_year=2022,
        model_year=2023,
        plate="ABC1234",
        value=35000.00,
        color="Red",
        bio="Electric car with autopilot."
    )
    assert car.model == "Model 3"
    assert car.brand == brand
    assert car.factory_year == 2022
    assert car.model_year == 2023
    assert car.plate == "ABC1234"
    assert car.value == 35000.00
    assert car.color == "Red"
    assert car.bio == "Electric car with autopilot."
    assert str(car) == "Model 3"

@pytest.mark.django_db
def test_car_inventory_creation():
    inventory = CarInventory.objects.create(
        cars_count=5,
        cars_value=150000.00
    )
    assert inventory.cars_count == 5
    assert inventory.cars_value == 150000.00
    assert str(inventory) == "5 - 150000.0"

@pytest.mark.django_db
def test_relationship_car_brand():
    brand = Brand.objects.create(name="Ford")
    car = Car.objects.create(
        model="Mustang",
        brand=brand,
        factory_year=2020,
        value=50000.00
    )
    assert car.brand.name == "Ford"
    assert brand.car_brand.count() == 1  
    assert brand.car_brand.first() == car